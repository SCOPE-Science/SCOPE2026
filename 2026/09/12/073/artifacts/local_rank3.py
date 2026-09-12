"""Exact QQ verification of the three n=3 local lemmas (sympy rationals).
(a) rank_Q(f: F11 -> H^3) == 4.
(b) coker local traces: id -> 4, transposition -> -4, 3-cycle -> +4
    (hence coker_T = 4 copies of the sign representation of S_3).
Uses the same integral Totaro matrices as the main computation.
"""
import sys
import sympy as sp
from explore_dims import build_H, cup, pairs_list

n = 3
mons, _, _ = build_H(n)
H1, H2 = mons[1], mons[2]
H3 = mons.get(3, [])
h2idx = {m: k for k, m in enumerate(H2)}
h3idx = {m: k for k, m in enumerate(H3)}
pairs = pairs_list(n)
ng = len(pairs)
Delta = sp.zeros(ng, len(H2))
for k, (i, j) in enumerate(pairs):
    Delta[k, h2idx[tuple(sorted([2*i, 2*j+1]))]] += 1
    Delta[k, h2idx[tuple(sorted([2*i+1, 2*j]))]] -= 1
F = len(H1)*ng
fmat = sp.zeros(F, len(H3))
for hi, h in enumerate(H1):
    for k in range(ng):
        for c, m2 in enumerate(H2):
            coef = int(Delta[k, c])
            if coef == 0:
                continue
            r = cup(h, m2, None, n)
            if r is None:
                continue
            _, m3, s = r
            fmat[hi*ng+k, h3idx[m3]] += coef*s
print("(a) rank_Q(f) =", fmat.rank(), "(need 4)")
assert fmat.rank() == 4


def S_H3_exact(sigma):
    d = len(H3)
    S = sp.zeros(d, d)
    for j, m in enumerate(H3):
        imgs = [2*sigma[g//2] + (g % 2) for g in m]
        inv = sum(1 for a in range(len(imgs)) for b in range(a+1, len(imgs))
                  if imgs[a] > imgs[b])
        S[H3.index(tuple(sorted(imgs))), j] = -1 if inv % 2 else 1
    return S


def S_F_exact(sigma):
    SH1 = sp.zeros(len(H1), len(H1))
    for j, m in enumerate(H1):
        g = m[0]
        SH1[H1.index((2*sigma[g//2] + (g % 2),)), j] = 1
    SG = sp.zeros(ng, ng)
    for j, (i, jj) in enumerate(pairs):
        SG[pairs.index(tuple(sorted([sigma[i], sigma[jj]]))), j] = 1
    return sp.ImmutableMatrix(sp.Matrix(sp.kronecker_product(SH1, SG)))


A = fmat.T
for name, sg in [("id", [0, 1, 2]), ("tau", [1, 0, 2]), ("3cyc", [1, 2, 0])]:
    SV = S_F_exact(sg)
    SW = S_H3_exact(sg)
    assert (A*SV - SW*A).is_zero_matrix
    ker = A.nullspace()
    N = sp.Matrix.hstack(*ker).T
    trker = sp.simplify(((N*SV*N.T)*(N*N.T).inv()).trace())
    trH3 = SW.trace()
    trcoker = sp.simplify(trH3 - (SV.trace() - trker))
    print(f"(b) {name}: trQ(ker)={trker}, trQ(H3)={trH3}, trQ(coker)={trcoker}")
print("local lemmas verified over QQ")
