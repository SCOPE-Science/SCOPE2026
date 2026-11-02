#!/usr/bin/env python3
"""Exact finite-field and integral coefficient checks for Fermat cubic plane reduction.

Uses only the Python standard library. All enumerations are exhaustive within
specified finite coordinate sets; the accompanying geometric proof supplies the
arguments over algebraic closures and complete discrete valuation rings.
"""
import collections
import itertools

M = ((0, 0, 0, 0), (0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2))
INV = (0, 1, 3, 2)
SQ = (0, 1, 3, 2)


def rref(rows):
    a = [list(row) for row in rows]
    p = 0
    for col in range(6):
        pivot = next((i for i in range(p, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[p], a[pivot] = a[pivot], a[p]
        v = INV[a[p][col]]
        a[p] = [M[v][x] for x in a[p]]
        for i in range(len(a)):
            if i != p and a[i][col]:
                c = a[i][col]
                a[i] = [x ^ M[c][y] for x, y in zip(a[i], a[p])]
        p += 1
        if p == len(a):
            break
    return tuple(tuple(row) for row in a[:p])


def rank(rows):
    if not rows:
        return 0
    a = [list(row) for row in rows]
    p = 0
    for j in range(len(a[0])):
        piv = next((i for i in range(p, len(a)) if a[i][j]), None)
        if piv is None:
            continue
        a[p], a[piv] = a[piv], a[p]
        iv = INV[a[p][j]]
        for i in range(p + 1, len(a)):
            if a[i][j]:
                c = M[a[i][j]][iv]
                for l in range(j + 1, len(a[0])):
                    a[i][l] ^= M[c][a[p][l]]
                a[i][j] = 0
        p += 1
        if p == len(a):
            break
    return p


def matchings(elements):
    if not elements:
        yield ()
        return
    a = elements[0]
    for i in range(1, len(elements)):
        b = elements[i]
        for rest in matchings(elements[1:i] + elements[i + 1:]):
            yield ((a, b),) + rest


def hermitian(a, b):
    v = 0
    for x, y in zip(a, b):
        v ^= M[SQ[x]][y]
    return v


def isotropic(rows):
    return all(hermitian(a, b) == 0 for a in rows for b in rows)


# The two orbit constructions are explicit and independent of the 891 count.
paired = set()
for pairing in matchings(list(range(6))):
    for coefficients in itertools.product((1, 2, 3), repeat=3):
        rows = []
        for (a, b), c in zip(pairing, coefficients):
            row = [0] * 6
            row[a] = 1
            row[b] = c
            rows.append(row)
        paired.add(rref(rows))
assert len(paired) == 405

seed = ((1, 0, 0, 1, 1, 1),
        (0, 1, 0, 1, 2, 3),
        (0, 0, 1, 1, 3, 2))
hexacode = set()
for permutation in itertools.permutations(range(6)):
    permuted = [[row[permutation[j]] for j in range(6)] for row in seed]
    for scalings in itertools.product((1, 2, 3), repeat=5):
        diagonal = (1,) + scalings
        hexacode.add(rref([[M[diagonal[j]][row[j]] for j in range(6)]
                            for row in permuted]))
assert len(hexacode) == 486
assert paired.isdisjoint(hexacode)
assert len(paired | hexacode) == 891
assert all(isotropic(rows) and len(rows) == 3 for rows in paired | hexacode)
for rows in hexacode:
    for a, b, c in itertools.product(range(4), repeat=3):
        if a == b == c == 0:
            continue
        word = [M[a][rows[0][i]] ^ M[b][rows[1][i]] ^
                M[c][rows[2][i]] for i in range(6)]
        assert sum(x != 0 for x in word) in (4, 6)
# Every special plane has a bipartition into independent triples. This is
# the chart condition ensuring its differential has rank 9 in the proof.
for rows in paired | hexacode:
    assert any(rank([[row[j] for j in choice] for row in rows]) == 3 and
               rank([[row[j] for j in range(6) if j not in choice] for row in rows]) == 3
               for choice in itertools.combinations(range(6), 3))


def intersections(reference, group):
    return dict(sorted(collections.Counter(6 - rank(reference + other)
                                           for other in group).items()))

for reference, other, expected in (
    (next(iter(paired)), paired, {0: 224, 1: 156, 2: 24, 3: 1}),
    (next(iter(paired)), hexacode, {0: 288, 1: 180, 2: 18}),
    (next(iter(hexacode)), paired, {0: 240, 1: 150, 2: 15}),
    (next(iter(hexacode)), hexacode, {0: 272, 1: 186, 2: 27, 3: 1}),
):
    assert intersections(reference, other) == expected

# Characteristic-two tangent map at representative paired/hexacode planes.
MONOMIALS = list(itertools.combinations_with_replacement(range(3), 3))
assert len(MONOMIALS) == 10

def tangent_rank(rows):
    assert rank([row[:3] for row in rows]) == 3
    # Both seed examples are in the normalized [I_3 | A] chart.
    assert [tuple(row[:3]) for row in rows] == [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    columns = []
    for j in range(3, 6):
        linear = [rows[i][j] for i in range(3)]
        for k in range(3):
            vec = [0] * len(MONOMIALS)
            for i in range(3):
                entry = tuple(sorted((i, i, k)))
                vec[MONOMIALS.index(entry)] ^= SQ[linear[i]]
            columns.append(vec)
    matrix = list(map(list, zip(*columns)))
    return rank(matrix)

paired_seed = ((1,0,0,1,0,0),(0,1,0,0,1,0),(0,0,1,0,0,1))
assert tangent_rank(paired_seed) == 9
assert tangent_rank(seed) == 9

# Exact coefficients in Z[zeta]/(zeta^2+zeta+1).
def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def mul(a, b):
    u, v = a
    x, y = b
    return (u*x-v*y, u*y+v*x-v*y)

Z = (0, 0)
ONE = (1, 0)
OMEGA = (0, 1)
OMEGA2 = (-1, -1)
linear_forms = [
    (ONE,Z,Z), (Z,ONE,Z), (Z,Z,ONE),
    (ONE,ONE,ONE), (ONE,OMEGA,OMEGA2), (ONE,OMEGA2,OMEGA),
]
monomials = collections.defaultdict(lambda: Z)
for linear in linear_forms:
    for i in range(3):
        for j in range(3):
            for k in range(3):
                degree = (int(i==0)+int(j==0)+int(k==0),
                          int(i==1)+int(j==1)+int(k==1),
                          int(i==2)+int(j==2)+int(k==2))
                monomials[degree] = add(monomials[degree],
                                        mul(mul(linear[i], linear[j]), linear[k]))
for degree, coefficient in monomials.items():
    expected = (18, 0) if degree == (1,1,1) else \
               ((4, 0) if degree in ((3,0,0),(0,3,0),(0,0,3)) else (0,0))
    assert coefficient == expected, (degree, coefficient, expected)

# Independent exact Hermitian point count (six and four coordinates).
def isotropic_points(n):
    return sum(1 for a in itertools.product(range(4), repeat=n)
               if any(a) and sum(x != 0 for x in a) % 2 == 0) // 3
assert isotropic_points(6) == 693
assert isotropic_points(4) == 45
assert (693 * 45 // 5) * 3 // 21 == 891
print('FERMAT_CUBIC_FOURFOLD_HEXACODE_405_486_MOD4_AND_INCIDENCE_EXACT_PASS')
