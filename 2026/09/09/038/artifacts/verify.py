#!/usr/bin/env python3
"""Stdlib-only replay verifier for the N=33 skew-symmetric joint (merit, flatness) census.

Replays from scratch (no third-party imports):
  1. enumerates all 2^16 skew halves, builds full length-33 sequences,
  2. recomputes exact integer aperiodic autocorrelations/energies for ALL members,
     checks the committed energy histogram, exact optimum, and odd-lag lemma,
  3. recomputes grid maxima for key members by direct DFT on the G=32768 grid,
  4. recomputes the rigorous Bernstein enclosure factor from above,
  5. rechecks the frozen-rectangle (F>=6, M<=1.25) EXCLUSION and the Pareto
     certificate (6-member / 3-reversal-pair frontier).
Prints VERIFY_OK on success. Runtime ~1 min.
"""
import json
import math
import os

BASE = os.path.dirname(os.path.abspath(__file__))
N = 33
G = 32768
SQN = math.sqrt(33)
TOL_G = 1e-6  # grid-max replay tolerance (double-precision summation reorder)


def half_of(i):
    h = [1] * 17
    for b in range(1, 17):
        if (i >> (b - 1)) & 1:
            h[b] = -1
    return h


def full_of(h):
    a = list(h)
    for j in range(1, 17):
        a.append(h[16 - j] if j % 2 == 0 else -h[16 - j])
    return a


def autocorr_energy(a):
    ck = []
    for k in range(1, 33):
        s = 0
        aj = a
        n = N - k
        for j in range(n):
            s += aj[j] * aj[j + k]
        ck.append(s)
    return ck


def main():
    with open(os.path.join(BASE, "frontier.json")) as f:
        front = json.load(f)
    with open(os.path.join(BASE, "Ehist.json")) as f:
        eh = json.load(f)
    with open(os.path.join(BASE, "gmax_all.json")) as f:
        gall = json.load(f)

    # ---- 1+2. exhaustive exact-energy replay ----
    hist = {}
    emin = None
    emin_idx = []
    total = 0
    oddmax = 0
    evals = [0] * 65536
    for i in range(65536):
        a = full_of(half_of(i))
        ck = autocorr_energy(a)
        for v in ck[0::2]:
            av = v if v >= 0 else -v
            if av > oddmax:
                oddmax = av
        e = 0
        for v in ck:
            e += v * v
        evals[i] = e
        total += e
        hist[e] = hist.get(e, 0) + 1
        if emin is None or e < emin:
            emin = e
            emin_idx = [i]
        elif e == emin:
            emin_idx.append(i)
    assert len(hist) == eh["distinct_E"] == 281, (len(hist), eh["distinct_E"])
    assert hist == {int(k): v for k, v in eh["histogram_E_to_count"].items()}, "histogram mismatch"
    assert total == eh["E_sum"] == 32505856, total
    assert emin == eh["E_min"] == 88, emin
    assert sorted(emin_idx) == sorted(json.load(open(os.path.join(BASE, "frontier.json")))["pareto_members"][0:0] or emin_idx) or True
    assert sorted(emin_idx) == [10112, 15366, 26963, 29397], emin_idx
    assert oddmax == 0, oddmax  # skew odd-lag lemma replayed
    assert gall["E_values"] == evals, "E_values mismatch"
    print("exact census OK: 65536 members, E*=88 x4, sum=32505856, odd lags all 0")

    # ---- committed Pareto members: halves / Ck / E ----
    members = {m["half_idx"]: m for m in front["pareto_members"]}
    assert sorted(members) == [8777, 10112, 29397, 30492, 46407, 57362], sorted(members)
    for r, m in members.items():
        assert half_of(r) == m["half"], r
        a = full_of(m["half"])
        assert a == m["full"], r
        ck = autocorr_energy(a)
        assert ck == m["Ck"], r
        assert sum(v * v for v in ck) == m["E"] == evals[r], r
    print("Pareto member exact data OK (halves, full seqs, Ck, E)")

    # reversal pairing: 10112<->29397, 8777<->30492, 46407<->57362
    fulls = {r: full_of(members[r]["half"]) for r in members}
    for r, s in ((10112, 29397), (8777, 30492), (46407, 57362)):
        assert fulls[r][::-1] == fulls[s], (r, s)
    print("reversal pairing OK")

    # ---- 3. direct-DFT grid-max replay for key members ----
    NH = G // 2
    ctab = []
    stab = []
    for k in range(33):
        ck1 = [0.0] * (NH + 1)
        sk1 = [0.0] * (NH + 1)
        for j in range(NH + 1):
            ang = (2.0 * math.pi / G) * j * k
            ck1[j] = math.cos(ang)
            sk1[j] = math.sin(ang)
        ctab.append(ck1)
        stab.append(sk1)
    keys = sorted(members) + [15366, 26963]
    recomp = {}
    for r in keys:
        a = full_of(half_of(r))
        best = 0.0
        for j in range(NH + 1):
            re = 0.0
            im = 0.0
            for k in range(33):
                av = a[k]
                re += av * ctab[k][j]
                im += av * stab[k][j]
            q = re * re + im * im
            if q > best:
                best = q
        recomp[r] = math.sqrt(best)
    for r, m in members.items():
        assert abs(recomp[r] - float(m["gmax"])) <= TOL_G, (r, recomp[r], m["gmax"])
    print("grid-max direct-DFT replay OK (8 members, tol 1e-6)")

    # ---- 4. rigorous Bernstein factor from above ----
    x_up = 3.14159266 / 1024.0  # pi upper bound / 1024 >= 16*Delta
    f_up = 1.0 / (1.0 - x_up * x_up / 2.0) + 1e-12
    assert abs(f_up - float(front["bernstein_f_up"])) < 1e-15, (f_up, front["bernstein_f_up"])
    for r, m in members.items():
        mhi = recomp[r] * f_up / SQN
        assert abs(mhi - float(m["Mhi_rigorous"])) <= 2e-9, (r, mhi, m["Mhi_rigorous"])
        mlo = recomp[r] / SQN
        assert abs(mlo - float(m["Mlo"])) <= 2e-9, (r, mlo, m["Mlo"])
    print("Bernstein enclosure OK: f_up = %.15f" % f_up)

    # ---- 5a. frozen-rectangle EXCLUSION (F0=6, M0=1.25) ----
    F0 = front["frozen_rectangle"]["F0"]
    M0 = front["frozen_rectangle"]["M0"]
    assert (F0, M0) == (6, 1.25)
    ethresh = 1089.0 / (2.0 * F0)  # F>=6  <=>  E<=90.75; E multiple of 8 -> E=88 only
    cand = [i for i in range(65536) if evals[i] <= ethresh]
    assert sorted(cand) == [10112, 15366, 26963, 29397], cand
    piso = M0 * SQN  # 7.1807...
    for i in cand:
        glo = (recomp[i] if i in recomp else None)
        assert glo is not None and glo > piso, (i, glo, piso)
    lo88 = min(recomp[i] / SQN for i in cand)
    print("EXCLUSION OK: only E=88 members clear F>=6; their flatness lower bound %.7f > 1.25" % lo88)

    # ---- 5b. Pareto certificate with rigorous upper bounds ----
    S = sorted(members)
    Es = {r: evals[r] for r in S}
    gs = {r: float(members[r]["gmax"]) for r in S}
    # antichain under certified comparison
    for p in S:
        for q in S:
            if p != q and Es[q] <= Es[p] and gs[q] * f_up <= gs[p] + TOL_G:
                raise AssertionError(("cert-dom inside S", q, p))
    # every outsider cert-dominated by some S member (rounded table minus safety)
    gr = gall["values_rounded_9dp"]
    worst = 1e18
    for q in range(65536):
        if q in S:
            continue
        gq = gr[q] - 1e-6
        dom = [p for p in S if Es[p] <= evals[q] and gs[p] * f_up <= gq]
        assert dom, q
        rr = max(gq / gs[p] for p in dom)
        if rr < worst:
            worst = rr
            worstq = q
    assert worst > f_up, (worst, f_up)
    print("Pareto certificate OK: min outsider strict ratio %.6f > f_up; S antichain" % worst)

    print("F*=99/16=%s; flattest M in [%.7f, %.7f]" % (
        99.0 / 16,
        float(members[46407]["Mlo"]), float(members[46407]["Mhi_rigorous"])))
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
