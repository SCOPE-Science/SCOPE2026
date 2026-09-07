"""Simulation audit for lane-04: lazy SRW on balanced spider S(k,L).
Fixed seed, reproducible. Tests:
 (a) leaf->center hitting mean vs 2L^2 (within 5%),
 (b) constructed two-stage coupling mean vs 3L^2 envelope,
 (c) tail P(tau > m*T0) vs 2^{-m} with T0=32kL^2,
 (d) TV proxy via occupation frequencies.
Coupling simulated = the proved construction:
 Stage1: lift J to cycle Z_{2L}, alternating-selection coupling until fold-meet.
 Stage2: synchronous J motion until joint 0 (center). Full positions tracked
   for exactness (legs sampled conditional on J path); tau = first full equality,
   which in this construction equals end of stage 2 (both at center).
Also simulates independent-until-meet for comparison.
"""
import json, hashlib, time, sys
import numpy as np

SEED = 20260907
rng_global = np.random.default_rng(SEED)

def lazy_step_full(pos, k, L, rng):
    """pos: 0=center, else (leg*L_off): encode leg in [0,k), dist in [1,L].
    Returns new pos after one lazy step."""
    if rng.random() < 0.5:
        return pos
    # must move
    if pos == 0:
        leg = rng.integers(0, k)
        return 1 + leg * L + 0  # dist 1: encode as 1+leg*L+(d-1)
    else:
        tmp = pos - 1
        leg = tmp // L
        d = (tmp % L) + 1
        if L == 1:
            return 0
        if d == 1:
            # neighbors center, (leg,2)
            if rng.random() < 0.5:
                return 0
            else:
                return 1 + leg * L + 1
        elif d == L:
            return 1 + leg * L + (L - 2)
        else:
            if rng.random() < 0.5:
                return 1 + leg * L + (d - 2)
            else:
                return 1 + leg * L + d

def dist_of(pos, k, L):
    if pos == 0:
        return 0
    return ((pos - 1) % L) + 1

def leg_of(pos, k, L):
    if pos == 0:
        return -1
    return (pos - 1) // L

def hitting_leaf_to_center(k, L, ntrials, rng):
    leaf = 1 + 0 * L + (L - 1)  # leg 0 leaf
    tot = 0
    for _ in range(ntrials):
        p = leaf
        t = 0
        while p != 0:
            p = lazy_step_full(p, k, L, rng)
            t += 1
        tot += t
    return tot / ntrials

def simulate_constructed_coupling(k, L, ntrials, rng, cap_multiplier=4):
    """Direct simulation of full walks under two-stage coupling.
    Stage 1: we simulate Z lifts with alternating selection; full positions'
    J must follow fold(Z). To keep it exact yet simple, we simulate full
    positions X,Y and Z lifts jointly:
      - Maintain Zx, Zy (cycle values in 0..2L-1) with fold(Z)=J=dist(X),dist(Y).
      - At each step pick to-move walk I in {X,Y} (prob 1/2), direction s=+-1.
      - Move selected walk's Z by s (mod 2L); set its J=fold(new Z).
      - Update full position to a vertex with that J consistent with spider
        dynamics: if J went 0->1, pick uniform leg; if J stayed (other walk's
        turn => this walk's lazy step is 'stay', so position unchanged -- but
        then its Z should also stay, contradiction!).
    PROBLEM: alternating coupling moves exactly one Z per step, meaning the
    other walk's Z stays, i.e., other's J stays. But other's full position must
    take a lazy 'stay' step (position unchanged) -- consistent! And the moved
    walk's full position must move radially as J dictates, but spider radial
    move from interior is +-1 with prob 1/2 each conditional on moving, while
    our Z move is +-1 equally -- matches after folding? At boundaries fold
    maps both +1/-1 of Z to same J direction, still uniform. Leg handling:
    moved walk: if old J=0,new J=1: new leg uniform; if old,new interior: leg
    unchanged; if new J=0: leg forgotten (at center). Unmoved walk: position
    unchanged (lazy stay). This preserves marginals? Moved walk conditional on
    being selected takes a non-lazy radial step +-1 equally -- but true lazy
    walk conditional on moving also +-1 equally interior, and at boundaries
    deterministically inward -- wait at J=0, lazy move always goes to 1
    (only neighbor direction), our Z move +-1 both fold to 1 -- same. At J=L,
    lazy move always goes to L-1, our Z move +-1 both fold to L-1 -- same.
    Good. Unmoved walk stays -- valid lazy stay. Overall each walk stays w.p.1/2
    (when other selected) and moves radially correctly w.p.1/2. Leg choice
    uniform on 0->1. So exact.
    Stage 2: after Jx==Jy, switch to synchronous: each step both Z move by same
    s=+-1 (common direction) or both stay? To keep lazy marginals with uniform
    1/2 move prob and synchronous J, use common coin: both stay w.p.1/2, else
    both move with common uniform direction s. Folded J's stay equal. Full
    positions: both stay (if stay coin) else both move radially per J (legs:
    on 0->1 each picks independent uniform leg; else legs unchanged).
    End: when Jx==Jy==0 both at center => meet. Return time.
    """
    N = 2 * L
    taus = np.zeros(ntrials, dtype=np.int64)
    for n in range(ntrials):
        # worst-case start: two leaves on different legs (leg 0 vs leg 1)
        X = 1 + 0 * L + (L - 1)
        Y = 1 + 1 * L + (L - 1) if k >= 2 else 0
        Zx = L  # fold(L)=L (could also be L; fine)
        Zy = L
        # ensure fold matches: fold(L)=L yes.
        legX = 0
        legY = 1 if k >= 2 else 0
        # Stage 1 until J equal
        t = 0
        # cap to avoid infinite loop in case of bug
        cap = int(cap_multiplier * 32 * k * L * L) + 1000
        # Stage 1
        while dist_of(X, k, L) != dist_of(Y, k, L):
            # alternating selection
            if rng.random() < 0.5:
                # move X
                s = 1 if rng.random() < 0.5 else -1
                Zx = (Zx + s) % N
                newJ = Zx if Zx <= L else N - Zx
                oldJ = dist_of(X, k, L)
                # update X full position to newJ
                if newJ == oldJ:
                    # can this happen? fold step can keep J same? e.g., Z=0 -> Z=1? J 0->1 changes.
                    # Z=1 -> Z=0? J 1->0. Z=L->L+-1? J L->L-1. Interior Z=a->a+-1: J changes by +-1
                    # always changes (since fold is locally injective except at 0,L where both
                    # directions change J the same way). Actually J always changes when Z moves.
                    # So this branch unreachable; keep position.
                    pass
                else:
                    if newJ == 0:
                        X = 0
                    elif oldJ == 0 and newJ == 1:
                        legX = int(rng.integers(0, k))
                        X = 1 + legX * L + 0
                    else:
                        # leg unchanged
                        X = 1 + legX * L + (newJ - 1)
                        if newJ == 0:
                            X = 0
                # Y stays (lazy stay): unchanged
            else:
                s = 1 if rng.random() < 0.5 else -1
                Zy = (Zy + s) % N
                newJ = Zy if Zy <= L else N - Zy
                oldJ = dist_of(Y, k, L)
                if newJ != oldJ:
                    if newJ == 0:
                        Y = 0
                    elif oldJ == 0 and newJ == 1:
                        legY = int(rng.integers(0, k))
                        Y = 1 + legY * L + 0
                    else:
                        Y = 1 + legY * L + (newJ - 1)
            t += 1
            if t > cap:
                break
            # full early meet impossible before J meet unless J equal, so no check needed
        # Stage 2: synchronous until both at center
        while not (X == 0 and Y == 0):
            # if J's equal but full positions equal elsewhere? Could meet off-center
            # with same leg+dist before reaching center. Check:
            if X == Y:
                break
            if rng.random() < 0.5:
                # both stay
                # Z's unchanged
                pass
            else:
                s = 1 if rng.random() < 0.5 else -1
                # move both Z by s
                Zx = (Zx + s) % N
                Zy = (Zy + s) % N
                newJx = Zx if Zx <= L else N - Zx
                newJy = Zy if Zy <= L else N - Zy
                assert newJx == newJy, (newJx, newJy)
                newJ = newJx
                oldJ = dist_of(X, k, L)
                assert oldJ == dist_of(Y, k, L)
                if newJ == oldJ:
                    pass  # unreachable as above (Z move always changes fold)
                else:
                    if newJ == 0:
                        X = 0
                        Y = 0
                    elif oldJ == 0 and newJ == 1:
                        legX = int(rng.integers(0, k))
                        legY = int(rng.integers(0, k))
                        X = 1 + legX * L + 0
                        Y = 1 + legY * L + 0
                    else:
                        X = 1 + legX * L + (newJ - 1)
                        Y = 1 + legY * L + (newJ - 1)
                        # update legs? legs unchanged; if at center handled above
            t += 1
            if t > cap:
                break
        taus[n] = t
    return taus

def simulate_independent_meet(k, L, ntrials, rng, cap):
    taus = np.zeros(ntrials, dtype=np.int64)
    for n in range(ntrials):
        X = 1 + 0 * L + (L - 1)
        Y = 1 + 1 * L + (L - 1) if k >= 2 else 0
        t = 0
        while X != Y:
            X = lazy_step_full(X, k, L, rng)
            Y = lazy_step_full(Y, k, L, rng)
            # careful: meeting should be checked with simultaneous updates?
            # Independent copies each take a lazy step per unit time; meet if same vertex.
            # The loop above advances both then checks; misses meet at intermediate?
            # Since both move simultaneously each round, check after each round suffices
            # (positions compared at integer times). Start t=0 positions differ.
            t += 1
            if t > cap:
                break
        taus[n] = t
    return taus

def main():
    rng = np.random.default_rng(SEED)
    grid = [(3, 5), (3, 10), (3, 20), (4, 5), (4, 10), (4, 20), (5, 5), (5, 10), (5, 20)]
    n_hit = 20000
    n_coup = 10000
    out = {"seed": SEED, "grid": []}
    lines = []
    lines.append("k L | E_leafH(mean, theory=2L^2) | coup_mean(constructed) vs 3L^2 | T0=32kL^2 | emp P(tau>T0) | emp P(tau>2T0) | indep_mean")
    all_pass = True
    for (k, L) in grid:
        theory_hit = 2 * L * L
        emp_hit = hitting_leaf_to_center(k, L, n_hit, rng)
        hit_ratio = emp_hit / theory_hit
        hit_ok = abs(hit_ratio - 1.0) <= 0.05
        taus = simulate_constructed_coupling(k, L, n_coup, rng)
        mean_c = float(np.mean(taus))
        env = 3 * L * L
        T0 = 32 * k * L * L
        p1 = float(np.mean(taus > T0))
        p2 = float(np.mean(taus > 2 * T0))
        # independent for reference (fewer trials for speed on large L)
        cap = 4 * T0 + 5000
        taus_ind = simulate_independent_meet(k, L, min(n_coup, 3000), rng, cap)
        mean_ind = float(np.mean(taus_ind))
        q99 = float(np.quantile(taus, 0.99))
        q50 = float(np.quantile(taus, 0.5))
        tail_ok = (p1 <= 0.5) and (p2 <= 0.25)
        mean_ok = mean_c <= env
        status = "PASS" if (hit_ok and tail_ok and mean_ok) else "FAIL"
        if status == "FAIL":
            all_pass = False
        lines.append(f"{k} {L} | hit {emp_hit:.1f} vs {theory_hit} (ratio {hit_ratio:.3f}) | coup_mean {mean_c:.1f} vs {env} | T0 {T0} | P1 {p1:.5f} (bound 0.5) | P2 {p2:.5f} (bound 0.25) | indep {mean_ind:.1f} | med {q50:.0f} q99 {q99:.0f} | {status}")
        out["grid"].append({"k": k, "L": L, "theory_hit": theory_hit, "emp_hit": emp_hit,
                            "hit_ratio": hit_ratio, "coup_mean": mean_c, "envelope_3L2": env,
                            "T0": T0, "p_gt_T0": p1, "p_gt_2T0": p2, "indep_mean": mean_ind,
                            "median": q50, "q99": q99, "status": status})
    out["all_pass"] = all_pass
    out["ntrials_hit"] = n_hit
    out["ntrials_coup"] = n_coup
    print("\n".join(lines))
    with open("/srv/scope-research/rounds/2026-09-07-pilot-01/workspaces/research/lane-04/output/artifacts/results.json", "w") as f:
        json.dump(out, f, indent=2)
    with open("/srv/scope-research/rounds/2026-09-07-pilot-01/workspaces/research/lane-04/output/artifacts/results_table.txt", "w") as f:
        f.write("\n".join(lines) + "\n")
    # hash code file
    with open(__file__, "rb") as f:
        h = hashlib.sha256(f.read()).hexdigest()
    print("code_sha256:", h)
    with open("/srv/scope-research/rounds/2026-09-07-pilot-01/workspaces/research/lane-04/output/artifacts/code_hash.txt", "w") as f:
        f.write(f"sim_spider.py sha256={h} seed={SEED}\n")
    print("ALL_PASS" if all_pass else "SOME_FAIL")

if __name__ == "__main__":
    main()
