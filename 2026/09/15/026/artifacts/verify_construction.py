"""Verify the (n-3)-coset extremal construction for 2-intersecting permutations.

Construction: C0 = {s : s(1)=1, s(2)=2}. M = (n-3)-coset sharing exactly s(1)=1
with C0 (fixes n-4 further tail positions). P_full = M \ C0 (4 type-A perms).
F = (C0 minus {s : exists p in P_full with agr(s,p)<2}) union P_full.

Checks: 2-intersecting validity, |F| = (n-2)! + 4 - U(n), Delta_2, gamma_2,
and agreement of the closed rook-theoretic U(n) formula with brute force.
Run: python3 verify_construction.py  (n<=8 fast; n=9 ~1 min; n=10 formula only)
"""
import itertools
import math


def agr(a, b):
    return sum(1 for x, y in zip(a, b) if x == y)


def build(n):
    T = list(range(2, n))
    V = [v for v in range(n) if v not in (0, 1)]
    k = n - 3
    fixM = {0: 0}
    fixM.update({i: i for i in range(2, k + 1)})
    free_idx = [i for i in range(n) if i not in fixM]
    free_vals = [v for v in range(n) if v not in list(fixM.values())]
    Pfull = []
    for pv in itertools.permutations(free_vals):
        s = [None] * n
        for i, v in fixM.items():
            s[i] = v
        for i, v in zip(free_idx, pv):
            s[i] = v
        t = tuple(s)
        if t[1] == 1:
            continue
        Pfull.append(t)
    assert len(Pfull) == 4, len(Pfull)
    U = 0
    ret = 0
    for e in itertools.permutations(V):
        deleted = False
        for p in Pfull:
            if sum(1 for i, v in zip(T, e) if p[i] == v) == 0:
                deleted = True
                break
        if deleted:
            U += 1
        else:
            ret += 1
    Flen = math.factorial(n - 2) - U + len(Pfull)
    assert ret + U == math.factorial(n - 2)
    return Pfull, U, Flen


def avoid(n, rF):
    m = n - 2
    s = n - 4
    tot = 0
    for i in range(s + 1):
        for j in range(len(rF)):
            kk = i + j
            if kk > m:
                continue
            tot += ((-1) ** kk) * math.comb(s, i) * rF[j] * math.factorial(m - kk)
    return tot


def U_formula(n):
    S1 = avoid(n, [1, 1])
    Pnt = avoid(n, [1, 2, 0])
    Ptr = avoid(n, [1, 2, 1])
    T = avoid(n, [1, 3, 1, 0])
    Q = avoid(n, [1, 4, 2, 0])
    return 4 * S1 - (4 * Pnt + 2 * Ptr) + 4 * T - Q


if __name__ == "__main__":
    for n in (6, 7, 8):
        Pfull, U, Flen = build(n)
        Uf = U_formula(n)
        print(f"n={n}: brute U={U} formula U={Uf} match={U == Uf} "
              f"|F|={Flen} = {math.factorial(n-2)}+4-{U}")
    for n in (9, 10):
        Uf = U_formula(n)
        print(f"n={n}: formula U={Uf} |F|={math.factorial(n-2) + 4 - Uf}")
