"""Independent verifier: replays lane-240 certificates from committed weights only.

Reads results.json (in same dir), rechecks with INDEPENDENT code paths:
 V0 reflexivity (ai | Q) and normalized volume.
 V1 brute-force box enumeration L(k) for k=1,2,3 vs stored tallies.
    Box: vertices are e_i and -a, so kP has -k*a_i <= x_i <= k (tight).
    Membership by the 7 facet inequalities (independent of slice formula).
 V2 Vandermonde interpolation from k=0..6 predicts k=7,8,9; vol check.
 V3 age histogram == stored h*; palindromicity; unimodality verdict.
 V4 parallelepiped reps: cone membership at claimed height.
 V5/V6 full 2P table replay: each stored row's summand (or failure) rechecked
    against brute-force S1/S2; witness in 2P with no P+P split.
"""
import json
import os
from fractions import Fraction

BASE = os.path.dirname(os.path.abspath(__file__))
DIM = 6

def avec(t):
    return (1, 1, 2, 2, 2, t)

def in_kP(a, k, x):
    Q = 1 + sum(a)
    if sum(x) > k:
        return False
    s = sum(x)
    for i in range(DIM):
        ai = a[i]
        if ai * (s - x[i]) - (Q - ai) * x[i] > k * ai:
            return False
    return True

def box_enum(a, k):
    ranges = [range(-k * a[i], k + 1) for i in range(DIM)]
    pts = []
    def gen(i, cur, s):
        if i == DIM:
            if s <= k and in_kP(a, k, tuple(cur)):
                pts.append(tuple(cur))
            return
        for v in ranges[i]:
            cur.append(v)
            gen(i + 1, cur, s + v)
            cur.pop()
    gen(0, [], 0)
    return pts

def age_hist(a):
    Q = 1 + sum(a)
    hist = [0] * 7
    for b in range(Q):
        assert (b + sum((b * ai) % Q for ai in a)) % Q == 0
        hist[(b + sum((b * ai) % Q for ai in a)) // Q] += 1
    return hist

def main():
    R = json.load(open(os.path.join(BASE, "results.json")))
    for ts, m in R["members"].items():
        t = int(ts)
        a = avec(t)
        Q = m["Q"]
        assert Q == 1 + sum(a) and all(Q % ai == 0 for ai in a), (t, "reflexive")
        L = m["L_0_9"]
        assert L[0] == 1
        # V1
        for k in (1, 2, 3):
            pts = box_enum(a, k)
            assert len(pts) == L[k], (t, k, len(pts), L[k])
        # V2
        M = [[Fraction(k ** j) for j in range(7)] for k in range(7)]
        b = [Fraction(L[k]) for k in range(7)]
        for col in range(7):
            piv = next(r for r in range(col, 7) if M[r][col])
            M[col], M[piv] = M[piv], M[col]
            b[col], b[piv] = b[piv], b[col]
            d = M[col][col]
            M[col] = [v / d for v in M[col]]
            b[col] /= d
            for r in range(7):
                if r != col and M[r][col]:
                    f = M[r][col]
                    M[r] = [u - f * v for u, v in zip(M[r], M[col])]
                    b[r] -= f * b[col]
        assert [str(v) for v in b] == m["ehrhart_coeffs"], (t, "coeffs")
        for k in (7, 8, 9):
            assert sum(b[j] * k ** j for j in range(7)) == L[k], (t, k)
        assert 720 * b[6] == Q
        # V3
        h = age_hist(a)
        assert h == m["hstar"] and h == h[::-1], (t, h)
        assert m["unimodal"] == all(h[j] <= h[j + 1] for j in range(3))
        # V4
        reps = m["parallelepiped_table"]
        assert len(reps) == Q
        for bs, e in reps.items():
            bb = int(bs)
            x = tuple(e["x"])
            hh = e["height"]
            mu = hh - sum(x)
            assert mu >= 0, (t, bb, "height")
            lam = [x[i] + mu * a[i] for i in range(DIM)]
            assert all(v >= 0 for v in lam), (t, bb, "cone")
            assert (bb + sum((bb * ai) % Q for ai in a)) // Q == hh
        # V5+V6
        S1 = box_enum(a, 1)
        S2 = box_enum(a, 2)
        assert len(S1) == m["L1"] and len(S2) == m["L2"], (t, "sizes")
        S1s = set(S1)
        assert len(m["twoP_rows"]) == len(S2)
        for row in m["twoP_rows"]:
            z = tuple(row["z"])
            assert in_kP(a, 2, z), (t, z, "not in 2P")
            s = row["summand"]
            if s is None:
                assert all(tuple(z[i] - p[i] for i in range(DIM)) not in S1s for p in S1), (t, z)
            else:
                assert tuple(s) in S1s and tuple(z[i] - s[i] for i in range(DIM)) in S1s, (t, z)
        w = tuple(m["twoP_fail"])
        assert in_kP(a, 2, w)
        assert all(tuple(w[i] - p[i] for i in range(DIM)) not in S1s for p in S1), (t, "witness splits!")
        assert m["IDP"] is False
        print(f"t={t}: VERIFY_OK  L1={len(S1)} L2={len(S2)} h*={h} witness={list(w)}", flush=True)
    print("ALL VERIFY_OK", flush=True)

if __name__ == "__main__":
    main()
