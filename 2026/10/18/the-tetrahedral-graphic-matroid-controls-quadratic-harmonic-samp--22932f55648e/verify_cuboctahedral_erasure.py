#!/usr/bin/env python3
"""Exact rational check of cuboctahedral degree-two spherical sampling ranks.

The coordinate rows are unnormalized by a common sqrt(2): this only rescales
nonconstant harmonic columns and does not change any sampling rank.
"""
from collections import Counter
from itertools import combinations, permutations
from fractions import Fraction

POINTS = sorted({p for a in (-1, 1) for b in (-1, 1)
                 for p in permutations((0, a, b))})
assert len(POINTS) == 12

EDGE_REPS = {
    (1, 2): (-1, 1, 0),
    (1, 3): (1, 0, 1),
    (1, 4): (0, -1, -1),
    (2, 3): (0, 1, -1),
    (2, 4): (-1, 0, 1),
    (3, 4): (1, 1, 0),
}
POTENTIALS = {1: (0, 1, 1), 2: (-1, 0, 0),
              3: (0, 0, 1), 4: (0, 0, 0)}

def harmonic_row(p):
    x, y, z = p
    return (1, x, y, z, x*x-y*y, x*x+y*y-2*z*z, x*y, x*z, y*z)

def matrix_rank(rows):
    if not rows:
        return 0
    a = [[Fraction(v) for v in row] for row in rows]
    m, n = len(a), len(a[0]); pivot_row = 0
    for j in range(n):
        piv = next((i for i in range(pivot_row, m) if a[i][j]), None)
        if piv is None:
            continue
        a[pivot_row], a[piv] = a[piv], a[pivot_row]
        t = a[pivot_row][j]
        a[pivot_row] = [v/t for v in a[pivot_row]]
        for i in range(pivot_row+1, m):
            if a[i][j]:
                t = a[i][j]
                a[i] = [u-t*v for u, v in zip(a[i], a[pivot_row])]
        pivot_row += 1
        if pivot_row == m:
            break
    return pivot_row

def minus(p):
    return tuple(-x for x in p)

EDGE_OF = {}
B_ROW = {}
for edge, rep in EDGE_REPS.items():
    a, b = edge
    inc = tuple(POTENTIALS[a][i]-POTENTIALS[b][i] for i in range(3))
    for sign, point in ((1,rep),(-1,minus(rep))):
        assert point not in EDGE_OF
        EDGE_OF[point] = edge
        B_ROW[point] = tuple(sign*x for x in inc)
assert set(EDGE_OF) == set(POINTS)
E = [harmonic_row(p) for p in POINTS]
B = [B_ROW[p] for p in POINTS]
assert matrix_rank(E) == 9
assert matrix_rank(B) == 3
assert all(sum(B[i][j] * E[i][k] for i in range(12)) == 0
           for j in range(3) for k in range(9))

def components(edge_set):
    parent = list(range(5))
    def root(x):
        while x != parent[x]:
            x = parent[x]
        return x
    for a, b in edge_set:
        parent[root(a)] = root(b)
    return len({root(i) for i in range(1, 5)})

COUNTS = Counter()
for mask in range(1 << 12):
    deleted = {p for i,p in enumerate(POINTS) if (mask >> i) & 1}
    kept = [harmonic_row(p) for p in POINTS if p not in deleted]
    H = {EDGE_OF[p] for p in deleted}
    predicted_rank = 13 - len(deleted) - components(H)
    actual_rank = matrix_rank(kept)
    assert actual_rank == predicted_rank, (mask,actual_rank,predicted_rank)
    COUNTS[len(deleted), actual_rank] += 1

EXPECTED = {
0:{9:1},1:{9:12},2:{8:6,9:60},3:{8:92,9:128},
4:{7:63,8:432},5:{6:24,7:768},6:{5:4,6:920},
7:{5:792},8:{4:495},9:{3:220},10:{2:66},11:{1:12},12:{0:1}
}
for n, ranks in EXPECTED.items():
    assert {r:COUNTS[n,r] for r in ranks} == ranks
    assert sum(v for (n2,r),v in COUNTS.items() if n2 == n) == sum(ranks.values())
assert sum(COUNTS.values()) == 4096
print('PASS: rank(E)=9, rank(B)=3, B^T E=0 (integer)')
print('PASS: all 4096 erasure patterns (rational Gaussian elimination)')
print('PASS: all 13 exact rank distributions')
for n in sorted(EXPECTED):
    print('erased',n,'ranks',EXPECTED[n])
