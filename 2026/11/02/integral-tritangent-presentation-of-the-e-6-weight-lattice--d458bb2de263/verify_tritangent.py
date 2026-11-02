#!/usr/bin/env python3
"""Exact integer checks for the 27-line/45-tritangent lattice presentation.
No third-party dependencies; all coordinates are integral or exact fractions.
"""
from fractions import Fraction
from itertools import combinations

def matchings(vertices):
    if not vertices:
        yield ()
        return
    a = vertices[0]
    for b in vertices[1:]:
        remaining = tuple(x for x in vertices if x != a and x != b)
        for m in matchings(remaining):
            yield ((a, b),) + m

E = [('E', i) for i in range(1, 7)]
L = [('L', i, j) for i in range(1, 7) for j in range(i + 1, 7)]
Q = [('Q', i) for i in range(1, 7)]
lines = E + L + Q
assert len(lines) == 27
T = {('T', i, j): (('E', i), ('L', min(i, j), max(i, j)), ('Q', j))
     for i in range(1, 7) for j in range(1, 7) if i != j}
U = {}
for matching in matchings(tuple(range(1, 7))):
    key = ('U',) + tuple(matching)
    U[key] = tuple(('L', i, j) for i, j in matching)
columns = {**T, **U}
assert len(columns) == 45 and len(U) == 15
chosen_keys = ([('T', i, j) for i in range(1, 7) for j in range(i+1, 7)]
               + [('T', j, 1) for j in range(2, 7)]
               + [('U', (1, 2), (3, 4), (5, 6))])
assert len(chosen_keys) == 21
chosen_rows = L + [('Q', i) for i in range(2, 7)] + [('E', 6)]
assert len(chosen_rows) == 21

def vector(triple):
    return [sum(int(name == t) for t in triple) for name in lines]

matrix = [vector(columns[key]) for key in columns]
B = [vector(columns[key]) for key in chosen_keys]
row_index = [lines.index(row) for row in chosen_rows]
D = [[B[col][row] for col in range(21)] for row in row_index]

def inverse_with_det(mat):
    n = len(mat)
    aug = [[Fraction(v) for v in row] + [Fraction(int(i == j)) for j in range(n)]
           for i, row in enumerate(mat)]
    determinant = Fraction(1)
    for i in range(n):
        pivot = next((j for j in range(i, n) if aug[j][i]), None)
        if pivot is None:
            raise AssertionError('selected minor singular')
        if pivot != i:
            aug[i], aug[pivot] = aug[pivot], aug[i]
            determinant *= -1
        a = aug[i][i]
        determinant *= a
        aug[i] = [x / a for x in aug[i]]
        for j in range(n):
            if j == i:
                continue
            b = aug[j][i]
            if b:
                aug[j] = [x - b * y for x, y in zip(aug[j], aug[i])]
    return determinant, [row[n:] for row in aug]

det, inv = inverse_with_det(D)
assert abs(det) == 1, det
assert all(x.denominator == 1 for row in inv for x in row)
for full_column in matrix:
    restricted = [full_column[i] for i in row_index]
    coeff = [sum(inv[i][j] * restricted[j] for j in range(21)) for i in range(21)]
    assert all(c.denominator == 1 for c in coeff)
    recovered = [sum(coeff[i] * B[i][r] for i in range(21)) for r in range(27)]
    assert recovered == full_column
print('INCIDENCE_OK: 27 lines, 45 tritangent triples; selected 21x21 minor det',det)
print('LATTICE_OK: chosen 21 tritangent columns form a Z-basis of the entire incidence image')

def pic_class(line):
    out = [0] * 7  # H,E_1,...,E_6
    kind = line[0]
    if kind == 'E':
        out[line[1]] = 1
    elif kind == 'L':
        out[0] = 1
        out[line[1]] = out[line[2]] = -1
    elif kind == 'Q':
        out[0] = 2
        for i in range(1, 7):
            if i != line[1]:
                out[i] = -1
    return out
kappa = [3] + [-1] * 6
for triple in columns.values():
    assert [sum(pic_class(t)[i] for t in triple) for i in range(7)] == kappa
print('GEOMETRY_OK: all 45 triples have class -K = 3H-sum(E_i)')
print('SMITH_OK: 21 unit invariant factors and six zero rows; quotient free of rank six')
