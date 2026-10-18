#!/usr/bin/env python3
"""Standalone exact integer certificate for the K6 two-point torus presentation.
Requires Python 3 standard library only. All graph, cell, and cycle data regenerated.
"""
from itertools import combinations, permutations

V = tuple(range(6))
E = list(combinations(V, 2))
EI = {e: i for i, e in enumerate(E)}
F = [(i, j) for i, j in combinations(range(15), 2)
     if set(E[i]).isdisjoint(E[j])]
FI = {f: j for j, f in enumerate(F)}
C1 = [(e, v) for e in range(15) for v in V if v not in E[e]]
CI = {x: i for i, x in enumerate(C1)}
assert len(F) == 45 and len(C1) == 60

# Matrix with rows indexed (fixed edge, free vertex) and columns disjoint edge pairs.
B = [[0] * 45 for _ in range(60)]
for j, (e, f) in enumerate(F):
    a, b = E[e]
    c, d = E[f]
    for i, s in [(CI[(f, b)], 1), (CI[(f, a)], -1),
                 (CI[(e, d)], -1), (CI[(e, c)], 1)]:
        B[i][j] += s

P = [(A, tuple(x for x in V if x not in A))
     for A in combinations(V, 3) if 0 in A]
assert len(P) == 10

def par(seq):
    return (-1) ** sum(seq[i] > seq[j]
                       for i in range(len(seq)) for j in range(i+1, len(seq)))

def triangle(A):
    a,b,c = A
    z = [(a,b),(b,c),(c,a)]
    return [(EI[tuple(sorted((x,y)))], 1 if x < y else -1) for x,y in z]

T = [[0] * 10 for _ in range(45)]
for j, (A, C) in enumerate(P):
    for e, se in triangle(A):
        for f, sf in triangle(C):
            pair = tuple(sorted((e, f)))
            T[FI[pair]][j] += se * sf * (1 if e < f else -1)
sgn = [par(A + C) for A,C in P]
N = [[T[i][j]*sgn[j] for j in range(10)] for i in range(45)]

# Pure exact integral determinant algorithm (Bareiss fraction-free elimination).
def determinant(arr):
    a = [list(row) for row in arr]
    n = len(a)
    if n == 0: return 1
    assert all(len(row) == n for row in a)
    old = 1
    sign = 1
    for k in range(n-1):
        pivot = next((i for i in range(k,n) if a[i][k]), None)
        if pivot is None: return 0
        if pivot != k:
            a[k],a[pivot] = a[pivot],a[k]
            sign = -sign
        z = a[k][k]
        for i in range(k+1,n):
            x = a[i][k]
            for j in range(k+1,n):
                numerator = a[i][j]*z - x*a[k][j]
                assert numerator % old == 0
                a[i][j] = numerator // old
            a[i][k]=0
        old=z
    return sign*a[-1][-1]

# Exact two-particle chain condition and single primitive relation.
assert all(sum(B[i][k]*T[k][j] for k in range(45)) == 0
           for i in range(60) for j in range(10))
assert all(sum(N[i]) == 0 for i in range(45))

# Two short, entirely explicit integer-minor certificates.
R9 = (0,1,3,6,7,9,12,13,18)
M9 = [[T[i][j] for j in range(9)] for i in R9]
d9 = determinant(M9)
assert abs(d9) == 1, d9
R36 = (0,1,2,4,5,6,8,9,10,12,13,14,16,17,18,20,21,22,
       24,25,26,28,29,30,33,34,36,37,38,40,41,42,46,48,49,50)
C36 = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,
       18,19,20,21,22,23,24,25,26,27,28,29,30,31,33,34,36,37)
d36 = determinant([[B[i][j] for j in C36] for i in R36])
assert d36 != 0, d36

# Every element of S6 acts on oriented squares. Check the claimed
# sign-twisted *integral* permutation module, not merely its character.
pset = {frozenset((frozenset(A),frozenset(C))):j for j,(A,C) in enumerate(P)}
for q in permutations(V):
    sign_q = par(q)
    eact = []
    for a,b in E:
        x,y = q[a],q[b]
        eact.append((EI[tuple(sorted((x,y)))], 1 if x < y else -1))
    fact = []
    for e,f in F:
        j,s = eact[e]
        k,t = eact[f]
        fact.append((FI[tuple(sorted((j,k)))],s*t*(1 if j<k else -1)))
    for j,(A,C) in enumerate(P):
        pj = pset[frozenset((frozenset(q[v] for v in A),
                             frozenset(q[v] for v in C)))]
        lhs = [0]*45
        for i,(v,si) in enumerate(fact):
            lhs[v] += N[i][j]*si
        assert all(lhs[i] == sign_q*N[i][pj] for i in range(45)),(q,j)
print('VERIFY_OK_K6_UNORDERED_TWO_POINT_TORUS_LATTICE')
print('CELLS_C0_15_C1_60_C2_45')
print('EXACT_BOUNDARY_TEN_CYCLES_ZERO; NORMALIZED_SUM_ZERO')
print('NINE_TORUS_UNIMODULAR_MINOR',d9,'R9',R9)
print('THIRTYSIX_BOUNDARY_NONZERO_MINOR',d36,'R36',R36,'C36',C36)
print('TEN_CARRIERS_UNIQUE_RELATION_SIGNS',sgn)
print('ALL_720_S6_PERMUTATIONS_SIGN_TWIST_ACTION_VERIFIED')
print('CONCLUSION_H2_Z9_ANY_NINE_INTEGRAL_BASIS')
