#!/usr/bin/env python3
"""Exact face/normal-cone certificate for the 19-basis matroid polytope.

Requires only Python's standard library. Run: python verify_matroid19.py
No floating-point computations, approximate hulls, or external data.
"""
from itertools import combinations
from collections import Counter
from fractions import Fraction
from math import gcd
from functools import lru_cache

N = 6
H = frozenset((0, 1, 2))
C = frozenset((3, 4, 5))
BASES = tuple(frozenset(B) for B in combinations(range(N), 3) if set(B) != H)
VERTICES = tuple(tuple(int(i in B) for i in range(N)) for B in BASES)

# Each facet is the tight set for a primitive outward normal a and bound b.
INEQUALITIES = []
for i in range(N):
    INEQUALITIES.append((tuple(int(j == i) for j in range(N)), 1, 'upper' + str(i)))
    INEQUALITIES.append((tuple(-int(j == i) for j in range(N)), 0, 'lower' + str(i)))
INEQUALITIES.append((tuple(int(i in H) for i in range(N)), 2, 'circuit'))

def rank_integer(rows):
    if not rows:
        return 0
    A = [list(map(Fraction, row)) for row in rows]
    m, n = len(A), len(A[0])
    r = 0
    for j in range(n):
        pivot = next((i for i in range(r, m) if A[i][j]), None)
        if pivot is None:
            continue
        A[r], A[pivot] = A[pivot], A[r]
        val = A[r][j]
        A[r] = [v / val for v in A[r]]
        for i in range(m):
            if i != r and A[i][j]:
                val = A[i][j]
                A[i] = [x - val*y for x, y in zip(A[i], A[r])]
        r += 1
        if r == m:
            break
    return r

def determinant(A):
    n = len(A)
    if n == 0:
        return 1
    M = [list(map(Fraction, row)) for row in A]
    factor = Fraction(1)
    for j in range(n):
        pivot = next((i for i in range(j, n) if M[i][j]), None)
        if pivot is None:
            return 0
        if pivot != j:
            M[j], M[pivot] = M[pivot], M[j]
            factor *= -1
        v = M[j][j]
        factor *= v
        for i in range(j + 1, n):
            q = M[i][j] / v
            for t in range(j + 1, n):
                M[i][t] -= q*M[j][t]
            M[i][j] = 0
    assert factor.denominator == 1
    return int(factor)

@lru_cache(None)
def face_dimension(V):
    if len(V) <= 1:
        return 0
    ref = VERTICES[next(iter(V))]
    return rank_integer(tuple(tuple(VERTICES[j][i] - ref[i] for i in range(N - 1)) for j in V))

TIGHT = tuple(frozenset(j for j, p in enumerate(VERTICES)
                        if sum(x*y for x, y in zip(a, p)) == bound)
              for a, bound, name in INEQUALITIES)
ALL = frozenset(range(len(BASES)))
assert len(BASES) == 19 and len(TIGHT) == 13
assert all(face_dimension(F) == 4 for F in TIGHT)

# Exhaust all possible nonempty intersections of facet supporting sets.
FACES = {ALL}
for tight in TIGHT:
    FACES |= {F & tight for F in tuple(FACES) if F & tight}
assert frozenset() not in FACES
assert len(FACES) == 285
assert Counter(face_dimension(F) for F in FACES) == {0: 19, 1: 81, 2: 111, 3: 60, 4: 13, 5: 1}

# The dual lattice N = Z^6 / Z(1,...,1) is represented in the basis
# dual to e_0-e_5,...,e_4-e_5.  The 13 normal rays are primitive.
RAYS = tuple(tuple(a[i]-a[5] for i in range(N - 1)) for a, _, _ in INEQUALITIES)

def gcd_maximal_minors(rows):
    r = len(rows)
    if r == 0:
        return 1
    g = 0
    for cols in combinations(range(N - 1), r):
        g = gcd(g, abs(determinant([[row[j] for j in cols] for row in rows])))
    return g

def active(F):
    return tuple(i for i, V in enumerate(TIGHT) if F <= V)

def smooth(F):
    rays = [RAYS[i] for i in active(F)]
    codim = N - 1 - face_dimension(F)
    assert rank_integer(rays) == codim
    return len(rays) == codim and gcd_maximal_minors(rays) == 1

# The two ruling systems of triangles in the new Δ2 × Δ2 facet.
TRIANGLES = []
for deleted in H:
    TRIANGLES.append(frozenset(j for j, B in enumerate(BASES) if B & H == H-{deleted}))
for new in C:
    TRIANGLES.append(frozenset(j for j, B in enumerate(BASES) if new in B and len(B & H) == 2))
assert len(TRIANGLES) == 6 and len(set(TRIANGLES)) == 6
assert all(F in FACES and len(F) == 3 and face_dimension(F) == 2 for F in TRIANGLES)
assert sum(bool(F & G) for F, G in combinations(TRIANGLES, 2)) == 9
assert all(len(F & G) <= 1 for F, G in combinations(TRIANGLES, 2))
ISOLATED = {frozenset((j,)) for j, B in enumerate(BASES) if len(B & H) <= 1}
assert len(ISOLATED) == 10
SINGULAR = {F for F in FACES if not smooth(F)}
PREDICTED = {F for F in FACES if any(F <= T for T in TRIANGLES) or F in ISOLATED}
assert SINGULAR == PREDICTED
assert Counter(face_dimension(F) for F in SINGULAR) == {0: 19, 1: 18, 2: 6}
assert len(SINGULAR) == 43
assert all(len(active(T)) == 4 for T in TRIANGLES)

# Each triangular component has a rank-three cone with four primitive
# rays, all triples saturated and one primitive 2-versus-2 relation.
for T in TRIANGLES:
    A = [RAYS[i] for i in active(T)]
    assert rank_integer(A) == 3
    for triple in combinations(A, 3):
        assert gcd_maximal_minors(triple) == 1
    assert any(tuple(A[i][c]+A[j][c] for c in range(N-1)) ==
               tuple(A[k][c]+A[l][c] for c in range(N-1))
               for i, j in combinations(range(4), 2)
               for k, l in [tuple(sorted(set(range(4))-{i,j}))])

# At exactly ten remaining fixed points the local cone is the same as
# for Δ(3,6): six coordinate rays, with a 3-to-3 primitive relation.
for F in ISOLATED:
    a = active(F)
    assert len(a) == 6 and 12 not in a
    pos = [RAYS[i] for i in a if i % 2 == 0]
    neg = [RAYS[i] for i in a if i % 2 == 1]
    assert len(pos) == len(neg) == 3
    assert tuple(map(sum, zip(*pos))) == tuple(map(sum, zip(*neg)))

print('VERIFY_OK')
print('BASES=19 FACETS=13 FACES=285 F_VECTOR=(19,81,111,60,13,1)')
print('SINGULAR_ORBITS_BY_DIMENSION=(19,18,6) TOTAL=43')
print('MAXIMAL_SINGULAR_FACES=6_TRIANGLES_PLUS_10_POINTS')
print('TRANSVERSE_CONIFOLD_CONES=6 ISOLATED_SEGRE_3x3_CONES=10')
