"""Lane 240: Ehrhart + h* + IDP decision for pre-committed 6D family.

Family (pre-committed BEFORE counting, see WORKLOG):
  P_t = conv{e1..e6, -a(t)}, a(t) = (1,1,2,2,2,t), t in {1,3,9}.
  Q(t) = 1+sum(a) = 9+t in {10,12,18}. Reflexive since each ai | Q.
Weights q = (1,a1..a6) (q0=1 plus a(t)).

Methods (exact integer arithmetic throughout):
  E1 slice stars-and-bars Ehrhart counts L(k), k=0..9.
  E2 Vandermonde interpolation (QQ) on k=0..6, prediction check k=7,8,9.
  E3 h* two routes: Ehrhart-series triangular solve AND age histogram.
  E4 IDP full simplicial-cone parallelepiped criterion + exhaustive 2P table.
"""
import json
import os
from fractions import Fraction
from math import comb

BASE = os.path.dirname(os.path.abspath(__file__))

DIM = 6
MEMBERS = [1, 3, 9]

def avec(t):
    return (1, 1, 2, 2, 2, t)

def Qof(a):
    return 1 + sum(a)

def check_reflexive(a):
    Q = Qof(a)
    return all(Q % ai == 0 for ai in a)

def ehrhart_count(a, k):
    """Exact L(k) by S-slice stars-and-bars (proved in DRAFT)."""
    Q = Qof(a)
    total = 0
    for r in range(k * Q + 1):
        s = k - r
        T = s + sum((r * ai) // Q for ai in a)  # s - sum(ceil(-r ai/Q))
        if T >= 0:
            total += comb(T + DIM - 1, DIM - 1)
    return total

def explicit_points(a, k):
    """Explicit lattice points of kP via per-slice compositions (k<=2 used)."""
    Q = Qof(a)
    pts = []
    for r in range(k * Q + 1):
        s = k - r
        m = [-(r * ai // Q) for ai in a]
        T = s - sum(m)
        if T < 0:
            continue
        # compositions of T into DIM parts
        def gen(i, rem, cur):
            if i == DIM - 1:
                yield cur + [rem]
                return
            for v in range(rem + 1):
                yield from gen(i + 1, rem - v, cur + [v])
        for y in gen(0, T, []):
            pts.append(tuple(y[i] + m[i] for i in range(DIM)))
    return pts

def in_kP(a, k, x):
    Q = Qof(a)
    if sum(x) > k:
        return False
    for i in range(DIM):
        ai = a[i]
        if ai * (sum(x) - x[i]) - (Q - ai) * x[i] > k * ai:
            return False
    return True

def interpolate(vals):
    """vals[k], k=0..6 -> coeffs c_j (QQ) with L(k)=sum c_j k^j."""
    n = 7
    M = [[Fraction(k ** j) for j in range(n)] for k in range(n)]
    b = [Fraction(vals[k]) for k in range(n)]
    # Gauss-Jordan
    for col in range(n):
        piv = next(r for r in range(col, n) if M[r][col] != 0)
        M[col], M[piv] = M[piv], M[col]
        b[col], b[piv] = b[piv], b[col]
        d = M[col][col]
        M[col] = [v / d for v in M[col]]
        b[col] = b[col] / d
        for r in range(n):
            if r != col and M[r][col] != 0:
                f = M[r][col]
                M[r] = [u - f * v for u, v in zip(M[r], M[col])]
                b[r] = b[r] - f * b[col]
    return b  # c_0..c_6

def hstar_from_ehrhart(L):
    """L[0..6] -> h* via L(k)=sum_{j<=k} h_j C(k-j+6,6)."""
    h = []
    for k in range(7):
        s = L[k] - sum(h[j] * comb(k - j + 6, 6) for j in range(k))
        h.append(s)
    return h

def age_histogram(a):
    Q = Qof(a)
    q = (1,) + tuple(a)
    hist = [0] * 7
    ages = {}
    for b in range(Q):
        age = (b + sum((b * qi) % Q for qi in q[1:])) // Q + (0 if b == 0 else 0)
        # careful: frac(b*1/Q) = b/Q since 0<=b<Q -> contributes b; total:
        age = (b + sum((b * qi) % Q for qi in a)) // Q
        assert (b + sum((b * qi) % Q for qi in a)) % Q == 0
        hist[age] += 1
        ages[b] = age
    return hist, ages

def parallelepiped_reps(a):
    """Rep_b = (-floor(b ai/Q)), height = age(b). Proved in DRAFT."""
    Q = Qof(a)
    reps = {}
    for b in range(Q):
        x = tuple(-((b * ai) // Q) for ai in a)
        h = (b + sum((b * ai) % Q for ai in a)) // Q
        reps[b] = (x, h)
    return reps

def idp_check(a, S1):
    """Full IDP verdict via parallelepiped reps + fold-sumset DP."""
    reps = parallelepiped_reps(a)
    S1set = set(S1)
    maxh = max(h for _, h in reps.values())
    reach = {1: set(S1set)}
    for h in range(2, maxh + 1):
        prev = reach[h - 1]
        out = set()
        for p in prev:
            for q in S1set:
                out.add(tuple(p[i] + q[i] for i in range(DIM)))
        reach[h] = out
    table = {}
    ok = True
    for b in range(Qof(a)):
        x, h = reps[b]
        if h <= 1:
            dec, good = ([x] if h == 1 else []), True
        else:
            good = x in reach[h]
            dec = None
        table[b] = {"x": list(x), "height": h, "decomposable": good}
        if not good:
            ok = False
    return ok, table

def twoP_table(a, S1, S2):
    S1set = set(S1)
    rows = []
    fail = None
    for z in S2:
        wit = None
        for p in S1set:
            if tuple(z[i] - p[i] for i in range(DIM)) in S1set:
                wit = list(p)
                break
        rows.append({"z": list(z), "summand": wit})
        if wit is None and fail is None:
            fail = list(z)
    return rows, fail

def main():
    out = {"family": "a(t)=(1,1,2,2,2,t)", "dim": DIM, "members": {}}
    for t in MEMBERS:
        a = avec(t)
        Q = Qof(a)
        assert check_reflexive(a), "reflexivity failed"
        L = [ehrhart_count(a, k) for k in range(10)]  # k=0..9
        c = interpolate(L[:7])
        pred = {k: sum(c[j] * Fraction(k ** j) for j in range(7)) for k in (7, 8, 9)}
        assert all(pred[k] == L[k] for k in (7, 8, 9)), "interpolation replay failed"
        volcheck = 720 * c[6]
        assert volcheck == Q, "volume != Q"
        hE = hstar_from_ehrhart(L[:7])
        hA, ages = age_histogram(a)
        assert hE == hA, "h* routes disagree"
        assert hE == hE[::-1], "h* not palindromic"
        unim = all(hE[j] <= hE[j + 1] for j in range(3))
        S1 = explicit_points(a, 1)
        S2 = explicit_points(a, 2)
        assert len(S1) == L[1] and len(S2) == L[2]
        assert all(in_kP(a, 1, p) for p in S1) and all(in_kP(a, 2, p) for p in S2)
        idp_ok, idptab = idp_check(a, S1)
        rows2, fail2 = twoP_table(a, S1, S2)
        out["members"][str(t)] = {
            "a": list(a), "Q": Q,
            "L_0_9": L,
            "ehrhart_coeffs": [str(v) for v in c],
            "volume_check": str(volcheck),
            "hstar": hE,
            "unimodal": unim,
            "L1": len(S1), "L2": len(S2),
            "IDP": idp_ok,
            "parallelepiped_table": {str(b): v for b, v in idptab.items()},
            "twoP_rows": rows2,
            "twoP_fail": fail2,
        }
        print(f"t={t} Q={Q} L1={len(S1)} L2={len(S2)} h*={hE} "
              f"unimodal={unim} IDP={idp_ok} twoP_fail={fail2}", flush=True)
    with open(os.path.join(BASE, "results.json"), "w") as f:
        json.dump(out, f)
    print("WROTE results.json", flush=True)

if __name__ == "__main__":
    main()
