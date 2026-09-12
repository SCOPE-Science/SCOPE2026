"""Exact QQ check of the L2 (E02 vanishing) base case at n=3.
Builds the lifted d02 matrix L (2 nbc pairs) and the E21 sliding-relation
matrix R over QQ; checks rank_Q([L;R]) - rank_Q(R) == 2 == dim E02(K3).
"""
import sys
import sympy as sp
from explore_dims import build_H, cup, pairs_list

n = 3
mons, _, _ = build_H(n)
H1, H2 = mons[1], mons[2]
h2idx = {m: k for k, m in enumerate(H2)}
pairs = pairs_list(n)
ng = len(pairs)
Delta = sp.zeros(ng, len(H2))
for k, (i, j) in enumerate(pairs):
    Delta[k, h2idx[tuple(sorted([2*i, 2*j+1]))]] += 1
    Delta[k, h2idx[tuple(sorted([2*i+1, 2*j]))]] -= 1
F = len(H2)*ng


def f21(c, k):
    return c*ng + k


Rrows = []
for k, (i, j) in enumerate(pairs):
    for h in H1:
        for mu in H1:
            vec = [0]*F
            for (pt, sgn) in [(i, 1), (j, -1)]:
                g = 2*pt + (h[0] % 2)
                r = cup((g,), mu, None, n)
                if r is None:
                    continue
                _, m2v, s = r
                vec[f21(h2idx[m2v], k)] += sgn*s
            if any(vec):
                Rrows.append(vec)
R = sp.Matrix(Rrows)
L = sp.zeros(2, F)
for q, (u, v) in enumerate([(0, 1), (0, 2)]):
    for c in range(len(H2)):
        L[q, f21(c, v)] += Delta[u, c]
        L[q, f21(c, u)] -= Delta[v, c]
print("rankQ(R) =", R.rank(),
      " rankQ([L;R])-rankQ(R) =", sp.Matrix.vstack(L, R).rank() - R.rank(),
      "(need 2)")
assert sp.Matrix.vstack(L, R).rank() - R.rank() == 2
print("L2 base case verified over QQ")
