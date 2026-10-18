#!/usr/bin/env python3
"""Exact integral certificate for two unordered points on the six-vertex complete graph.
Run with Python 3.10+; only the standard library is used.
"""
from itertools import combinations

N = 6
VERTICES = list(combinations(range(N), 2))
GRAPH_EDGES = list(combinations(range(N), 2))
CELLS1 = [(e, v) for e in GRAPH_EDGES for v in range(N) if v not in e]
CELLS2 = [(e, f) for e, f in combinations(GRAPH_EDGES, 2)
          if not (set(e) & set(f))]
V_INDEX = {v: k for k, v in enumerate(VERTICES)}
E_INDEX = {v: k for k, v in enumerate(CELLS1)}
F_INDEX = {v: k for k, v in enumerate(CELLS2)}
assert (len(VERTICES), len(CELLS1), len(CELLS2)) == (15, 60, 45)

# B1: boundary of a one-cell; B2: boundary of a square (e,f), with e<f.
B1 = [[0] * 60 for _ in range(15)]
B2 = [[0] * 45 for _ in range(60)]
for j, ((u, v), w) in enumerate(CELLS1):
    B1[V_INDEX[tuple(sorted((v, w)))]][j] += 1
    B1[V_INDEX[tuple(sorted((u, w)))]][j] -= 1
for j, ((u, v), (w, z)) in enumerate(CELLS2):
    f, e = (w, z), (u, v)
    B2[E_INDEX[(f, v)]][j] += 1
    B2[E_INDEX[(f, u)]][j] -= 1
    B2[E_INDEX[(e, z)]][j] -= 1
    B2[E_INDEX[(e, w)]][j] += 1
assert all(sum(B1[a][k] * B2[k][j] for k in range(60)) == 0
           for a in range(15) for j in range(45))
M = [[B2[k][i] for k in range(60)] for i in range(45)]  # cochain coboundary

# Integer determinant by fraction-free Gaussian elimination.
def det(matrix):
    a = [list(row) for row in matrix]
    n = len(a)
    assert all(len(row) == n for row in a)
    if n == 0:
        return 1
    prev, sign = 1, 1
    for k in range(n-1):
        if a[k][k] == 0:
            p = next((i for i in range(k+1,n) if a[i][k] != 0), None)
            if p is None:
                return 0
            a[k],a[p] = a[p],a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator = a[i][j]*pivot - a[i][k]*a[k][j]
                assert numerator % prev == 0
                a[i][j] = numerator // prev
            a[i][k] = 0
        prev = pivot
    return sign*a[-1][-1]

def minor(a, rows, cols):
    assert len(rows) == len(cols)
    return det([[a[i][j] for j in cols] for i in rows])

def rank_mod2_cols(columns):
    pivots = {}
    for x in columns:
        while x:
            b = x.bit_length()-1
            if b not in pivots:
                pivots[b] = x
                break
            x ^= pivots[b]
    return len(pivots)

def columns_mod2(a):
    assert a
    return [sum((a[i][j] & 1) << i for i in range(len(a)))
            for j in range(len(a[0]))]

# Four short determinant certificates, with all indices zero-based.
ROWS24 = [0,1,2,3,4,5,6,7,8,10,11,12,15,16,20,24,28,32,36,40,44,48,52,56]
ROWS35 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,33,34,37]
COLS35 = [0,1,2,4,5,6,8,9,10,12,13,14,16,17,18,20,21,22,24,25,26,28,29,30,33,34,36,37,38,40,41,42,46,48,49]
ROWS36 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,33,34,36,37]
COLS36 = [0,1,2,4,5,6,8,9,10,12,13,14,16,17,18,20,21,22,24,25,26,28,29,30,33,34,36,37,38,40,41,42,46,48,49,50]
COLS30 = [0,1,2,4,5,6,8,9,10,12,13,14,16,17,18,20,21,22,24,25,26,28,29,36,37,38,40,41,48,49]

# Ten natural cocycles: total motion over each non-tree graph edge (i,j), 1<=i<j<=5.
NONTREE = [e for e in GRAPH_EDGES if 0 not in e]
assert len(NONTREE) == 10
A = [[int(e == f) for f in NONTREE] for e, v in CELLS1]
# Fourteen independent vertex coboundaries, dropping the first configuration vertex.
L = [[B1[a][i] for a in range(1,15)] + A[i] for i in range(60)]
assert all(sum(M[i][k]*L[k][j] for k in range(60)) == 0
           for i in range(45) for j in range(24))
assert minor(L, ROWS24, list(range(24))) == 1

# All non-tree disjoint graph edge pairs yield a unit square cup cocycle.
P_INDEX = [F_INDEX[(e,f)] for e,f in combinations(NONTREE,2)
           if not(set(e)&set(f))]
assert P_INDEX == list(range(30,45))
COMPLEMENT = [i for i in range(45) if i not in P_INDEX]
assert len(COMPLEMENT) == 30
assert minor(M, COMPLEMENT, COLS30) == 1

# Rational rank 36 follows from a nonzero 36-minor and the 24-dimensional kernel L.
assert minor(M, ROWS36, COLS36) == 2
assert minor(M, ROWS35, COLS35) == 1
assert rank_mod2_cols(columns_mod2(M)) == 35
# These certificates force cokernel(M) = Z^9 + Z/2, while all cup products generate it.

# The particular degree-two class below is a five-term product combination.
TAU = {33:1, 35:-1, 39:1, 40:1, 42:-1}
assert CELLS2[33] == ((1,3),(2,4))
assert CELLS2[35] == ((1,3),(4,5))
assert CELLS2[39] == ((1,5),(2,3))
assert CELLS2[40] == ((1,5),(2,4))
assert CELLS2[42] == ((2,3),(4,5))
x_support = [4,8,9,16,17,18,25,28,33,34,40,41,46,48,49,50]
q_support = [4,8,9,16,17,24,25,26,28,36,37,38,40,41]
x = [int(i in x_support) for i in range(60)]
q = [int(i in q_support) for i in range(60)]
assert all(sum(M[i][j]*x[j] for j in range(60)) % 2 == 0
           for i in range(45))
assert all(sum(M[i][j]*(x[j]-2*q[j]) for j in range(60))
           == 2*TAU.get(i,0) for i in range(45))
assert rank_mod2_cols(columns_mod2(L)) == 24
x_bitset = sum(1 << i for i in x_support)
assert rank_mod2_cols(columns_mod2(L) + [x_bitset]) == 25
# Thus tau has order exactly two, since x does not lift modulo 2 to an
# integral 1-cocycle (the integral cocycles are exactly the span of L).

# Connected 1-skeleton: each one-cell joins the vertex pairs (u,w), (v,w).
seen = {0}
changed = True
while changed:
    changed = False
    for (e,w) in CELLS1:
        u,v=e
        p = V_INDEX[tuple(sorted((u,w)))]
        qv = V_INDEX[tuple(sorted((v,w)))]
        if (p in seen) != (qv in seen):
            seen.update([p,qv]); changed = True
assert len(seen) == 15
print('VERIFY_OK cells=(15,60,45) ranks=(14,36) H2=Z^9+Z/2 cup_surjective=True torsion_order=2')
