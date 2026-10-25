#!/usr/bin/env python3
"""Exact chains and a mod-five cup product for the column-cyclic 4-by-5 chessboard quotient.

Requires Python 3 and SymPy. No external data. Every face is generated from its
row and column coordinates; the quotient retains multiplicities of cells.
"""
from itertools import combinations, permutations
from sympy import Matrix, zeros
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

NROWS, NCOLS = 4, 5

def shift(face, amount):
    return tuple(sorted((r, (c + amount) % NCOLS) for r, c in face))

def all_faces(size):
    return [tuple(zip(rr, cc)) for rr in combinations(range(NROWS), size)
            for cc in permutations(range(NCOLS), size)]

representatives = []
orbit_index = []
for size in range(1, NROWS + 1):
    every_face = all_faces(size)
    reps = sorted({min(shift(f, a) for a in range(NCOLS)) for f in every_face})
    lookup = {shift(f, a): index
              for index, f in enumerate(reps) for a in range(NCOLS)}
    assert len(reps) * NCOLS == len(every_face) == len(lookup)
    representatives.append(reps)
    orbit_index.append(lookup)
assert list(map(len, representatives)) == [4, 24, 48, 24]

boundary = []
for size in range(2, NROWS + 1):
    lower = representatives[size - 2]
    upper = representatives[size - 1]
    matrix = zeros(len(lower), len(upper))
    for j, face in enumerate(upper):
        for k in range(size):
            subface = face[:k] + face[k + 1:]
            matrix[orbit_index[size - 2][subface], j] += (-1)**k
    boundary.append(matrix)
assert boundary[0] * boundary[1] == zeros(4, 48)
assert boundary[1] * boundary[2] == zeros(24, 24)

expected_nonzero_smith = [[1]*3, [1]*20+[5], [1]*23]
for d, expected in zip(boundary, expected_nonzero_smith):
    diag = [abs(int(v)) for v in smith_normal_form(d, domain=ZZ).diagonal() if v]
    assert sorted(diag) == sorted(expected), (d.shape, diag)

# A preferred orientation on the top cells: append the missing column and
# take the sign of that permutation of [0,1,2,3,4].
def permutation_sign(values):
    return (-1)**sum(values[i] > values[j] for i in range(len(values))
                        for j in range(i+1, len(values)))

def top_coefficient(face):
    used = [col for _, col in face]
    missing = next(col for col in range(NCOLS) if col not in used)
    return permutation_sign(used + [missing])

top = Matrix([top_coefficient(f) for f in representatives[3]])
assert boundary[2] * top == zeros(48, 1)
assert set(int(a) for a in top) == {-1, 1}

# Column difference defines a Z/5 1-cocycle on the quotient: its integer lift
# takes values in {0,1,2,3,4}. Delta(lift)/5 is an integral 2-cocycle.
def lift_u(edge):
    return (edge[1][1] - edge[0][1]) % NCOLS

def beta_u(triple):
    a, b, c = triple
    numerator = lift_u((b, c)) - lift_u((a, c)) + lift_u((a, b))
    assert numerator % NCOLS == 0
    return numerator // NCOLS

# The cocycle and Bockstein respect the column-translation equivalence.
for edge in representatives[1]:
    for a in range(NCOLS):
        assert lift_u(edge) == lift_u(shift(edge, a))
for triangle in representatives[2]:
    for a in range(NCOLS):
        assert beta_u(triangle) == beta_u(shift(triangle, a))
for tetra in representatives[3]:
    assert (beta_u(tetra[1:]) - beta_u(tetra[:1]+tetra[2:])
            + beta_u(tetra[:2]+tetra[3:]) - beta_u(tetra[:3])) == 0

# Alexander-Whitney product u cup reduction(beta_u) on every 3-cell.
product_evaluation = sum(int(top[j]) * lift_u(face[:2]) * beta_u(face[1:])
                         for j, face in enumerate(representatives[3]))
assert product_evaluation % NCOLS == 2, product_evaluation

print('CELL COUNTS 4,24,48,24')
print('SMITH d1=(1^3); d2=(1^20,5); d3=(1^23)')
print('H0=Z; H1=Z/5; H2=Z^4; H3=Z')
print('integral top-cycle coefficients are +/-1; all boundaries verified')
print('mod-5 evaluation <u cup beta(u),[Y]> =', product_evaluation % NCOLS)
print('PASS')
