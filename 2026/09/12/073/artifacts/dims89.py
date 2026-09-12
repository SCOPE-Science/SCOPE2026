"""Dimension + spot-character probe at n=8,9 to test persistence of P2."""
import sys
sys.path.insert(0, 'output/artifacts')
import numpy as np
from explore_dims import build_H, cup, pairs_list, rank_mod
from math import comb

P = 1000003

def dims(n):
    mons, _, _ = build_H(n)
    H1 = mons.get(1, []); H2 = mons.get(2, []); H3 = mons.get(3, [])
    d1, d2, d3 = len(H1), len(H2), len(H3)
    pairs = pairs_list(n); ng = len(pairs)
    h2idx = {m: k for k, m in enumerate(H2)}
    Delta = np.zeros((ng, d2), dtype=np.int64)
    for k, (i, j) in enumerate(pairs):
        Delta[k, h2idx[tuple(sorted([2*i, 2*j+1]))]] += 1
        Delta[k, h2idx[tuple(sorted([2*i+1, 2*j]))]] -= 1
    r01 = rank_mod(Delta % P, P)
    e20 = d2 - r01
    h1idx = {m: k for k, m in enumerate(H1)}
    F = d1*ng
    def f11(hi, gi):
        return hi*ng + gi
    R = np.zeros((2*ng, F), dtype=np.int64)
    for k, (i, j) in enumerate(pairs):
        R[2*k, f11(h1idx[(2*i,)], k)] += 1
        R[2*k, f11(h1idx[(2*j,)], k)] -= 1
        R[2*k+1, f11(h1idx[(2*i+1,)], k)] += 1
        R[2*k+1, f11(h1idx[(2*j+1,)], k)] -= 1
    rR = rank_mod(R % P, P)
    h3idx = {m: k for k, m in enumerate(H3)}
    fmat = np.zeros((F, d3), dtype=np.int64)
    for hi, h in enumerate(H1):
        for k in range(ng):
            row = f11(hi, k)
            for c, m2 in enumerate(H2):
                coef = int(Delta[k, c])
                if coef == 0:
                    continue
                r = cup(h, m2, None, n)
                if r is None:
                    continue
                _, m3, s = r
                fmat[row, h3idx[m3]] = (fmat[row, h3idx[m3]] + coef*s)
    rf = rank_mod(fmat % P, P)
    e11 = (F - rf) - rR
    pred = 2*comb(n, 3) + 5*comb(n, 2)
    print(f"n={n}: E20={e20} (pred {3*comb(n,2)}), E11={e11} (pred {2*comb(n,3)+2*comb(n,2)}), TOT={e20+e11} pred={pred} {'OK' if e20+e11==pred else 'DEVIATION'}",
          flush=True)

for n in [8, 9]:
    dims(n)
