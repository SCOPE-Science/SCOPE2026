#!/usr/bin/env python3
"""Verifier for lane-175: N(A0)=P^2 for A0=Q[x,y,z]/(x^3,y^3,z^3,xyz).
Stdlib only (fractions, itertools). Replays:
 (1) monomial bases, Hilbert function (1,3,6,6,3), socle;
 (2) det M_2(a,b,c) == 0 identically via permutation expansion (2 cancelling terms);
 (3) all 36 five-by-five minors of M_2 nonzero (monomials);
 (4) single-L (1,1,1) ranks incl. kernel witness; (5) Jordan partition [5,4,4,2,2,1,1].
"""
from itertools import product, permutations, combinations
from fractions import Fraction
from collections import defaultdict

def killed(m):
    return any(e >= 3 for e in m) or all(e >= 1 for e in m)

bases = {}
for d in range(7):
    bases[d] = sorted([m for m in product(range(d+1), repeat=3)
                       if sum(m) == d and not killed(m)],
                      key=lambda m: (m[2], m[1], m[0]))
hf = [len(bases[d]) for d in range(6)]
assert hf == [1, 3, 6, 6, 3, 0], hf
assert sum(hf) == 19
print("Hilbert function:", hf, "total dim 19: OK")

# socle
soc = {d: [m for m in bases[d]
           if killed((m[0]+1, m[1], m[2])) and killed((m[0], m[1]+1, m[2]))
           and killed((m[0], m[1], m[2]+1))] for d in range(5)}
assert soc[4] == bases[4] and all(not soc[d] for d in range(4)), soc
print("socle = all of deg 4 (type 3, level): OK")

# M_2 as variable-name table (rows deg3, cols deg2)
E = [['b','a',None,None,None,None],
     [None,'b','a',None,None,None],
     ['c',None,None,'a',None,None],
     [None,None,'c',None,'b',None],
     [None,None,None,'c',None,'a'],
     [None,None,None,None,'c','b']]
def det_terms(rows, cols):
    k = len(rows); out = defaultdict(int); nz = []
    for p in permutations(cols):
        inv = sum(1 for i in range(k) for j in range(i+1, k) if p[i] > p[j])
        t = [E[rows[i]][p[i]] for i in range(k)]
        if any(x is None for x in t):
            continue
        nz.append((p, inv, tuple(t)))
        out[tuple(sorted(t))] += 1 if inv % 2 == 0 else -1
    return {k: v for k, v in out.items() if v != 0}, nz

d6, nz6 = det_terms(list(range(6)), list(range(6)))
assert len(nz6) == 2, nz6
assert d6 == {}, d6
print("det M_2 = a^2b^2c^2 - a^2b^2c^2 = 0 identically (2 nonzero perm terms): OK")

n5 = sum(1 for r in combinations(range(6), 5) for c in combinations(range(6), 5)
         if det_terms(list(r), list(c))[0])
assert n5 == 36, n5
print("all 36 5x5 minors of M_2 nonzero monomials: OK")

# numeric ranks
idx = {d: {m: i for i, m in enumerate(bases[d])} for d in bases}
def nummat(i, L):
    R, C = len(bases[i+1]), len(bases[i])
    M = [[Fraction(0)]*C for _ in range(R)]
    for j, m in enumerate(bases[i]):
        for s, cf in [((1,0,0),L[0]),((0,1,0),L[1]),((0,0,1),L[2])]:
            t = (m[0]+s[0], m[1]+s[1], m[2]+s[2])
            if not killed(t):
                M[idx[i+1][t]][j] += cf
    return M
def rank(M):
    M = [r[:] for r in M]; R, C = len(M), len(M[0]); piv = 0
    for c in range(C):
        p = next((i for i in range(piv, R) if M[i][c] != 0), None)
        if p is None:
            continue
        M[piv], M[p] = M[p], M[piv]
        for i in range(R):
            if i != piv and M[i][c] != 0:
                f = M[i][c]/M[piv][c]
                for k in range(c, C):
                    M[i][k] -= f*M[piv][k]
        piv += 1
    return piv
O = Fraction(1)
r = [rank(nummat(i, (O, O, O))) for i in range(4)]
assert r == [1, 3, 5, 3], r
print("ranks at L=x+y+z (deg 0..3):", r, "-> WLP FAIL at 2->3: OK")
M2 = nummat(2, (O, O, O))
w = [sum(M2[i][j]*v for j, v in
     enumerate([Fraction(1),Fraction(-1),Fraction(1),Fraction(-1),Fraction(-1),Fraction(1)]))
     for i in range(6)]
assert all(x == 0 for x in w)
print("kernel witness x^2-xy+y^2-xz-yz+z^2: OK")

# Jordan partition
allm = [m for d in range(5) for m in bases[d]]; pos = {m: i for i, m in enumerate(allm)}
N = len(allm)
ML = [[Fraction(0)]*N for _ in range(N)]
for j, m in enumerate(allm):
    for s in [(1,0,0),(0,1,0),(0,0,1)]:
        t = (m[0]+s[0], m[1]+s[1], m[2]+s[2])
        if not killed(t):
            ML[pos[t]][j] += Fraction(1)
def matmul(A, B):
    n = len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
def nullity(M):
    M = [row[:] for row in M]; n = len(M); piv = 0
    for c in range(n):
        p = next((i for i in range(piv, n) if M[i][c] != 0), None)
        if p is None:
            continue
        M[piv], M[p] = M[p], M[piv]
        for i in range(n):
            if i != piv and M[i][c] != 0:
                f = M[i][c]/M[piv][c]
                for k in range(c, n):
                    M[i][k] -= f*M[piv][k]
        piv += 1
    return n - piv
P = [[Fraction(int(i == j)) for j in range(N)] for i in range(N)]
nulls = []
for _ in range(6):
    P = matmul(ML, P)
    nulls.append(nullity(P))
assert nulls[:5] == [7, 12, 15, 18, 19], nulls
n = [0] + nulls
cnt = [n[k]-n[k-1] for k in range(1, len(n))]
blocks = []
for k in range(1, len(cnt)):
    blocks += [k]*(cnt[k-1] - (cnt[k] if k < len(cnt) else 0))
assert sorted(blocks, reverse=True) == [5, 4, 4, 2, 2, 1, 1], blocks
print("Jordan partition of xL:", sorted(blocks, reverse=True), ": OK")
print("ALL CHECKS PASSED")
