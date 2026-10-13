#!/usr/bin/env python3
"""Exact finite symbolic checks for a quaternionic model of hollow SO(4).

This file tests algebraic identities and combinatorial counts. The general
formal-local theorem is proved in RESULT.md rather than inferred from tests.
"""
from itertools import combinations

# Products i*j=k, j*k=i, k*i=j with reversed products negative.
unit_products = {
    (0, 0): (1, 0),
    (1, 1): (-1, 0), (2, 2): (-1, 0), (3, 3): (-1, 0),
    (0, 1): (1, 1), (1, 0): (1, 1),
    (0, 2): (1, 2), (2, 0): (1, 2),
    (0, 3): (1, 3), (3, 0): (1, 3),
    (1, 2): (1, 3), (2, 1): (-1, 3),
    (2, 3): (1, 1), (3, 2): (-1, 1),
    (3, 1): (1, 2), (1, 3): (-1, 2),
}


def diagonal_coefficient(i, middle, j):
    # Coefficient of e_middle in e_i * e_middle * conjugate(e_j).
    sm, k = unit_products[i, middle]
    sb, out = unit_products[k, j]
    return sm * sb * (-1 if j else 1) if out == middle else 0


H = tuple(tuple(diagonal_coefficient(i, col, i) for i in range(4))
          for col in range(4))
# The off-diagonal monomials must have identically zero coefficient in each diagonal.
for middle in range(4):
    for i in range(4):
        for j in range(4):
            v = diagonal_coefficient(i, middle, j)
            if i != j:
                assert v == 0, (middle, i, j, v)
assert H == (
    (1, 1, 1, 1),
    (1, 1, -1, -1),
    (1, -1, 1, -1),
    (1, -1, -1, 1),
), H
assert all(sum(H[i][j]*H[k][j] for j in range(4)) == (4 if i == k else 0)
           for i in range(4) for k in range(4))

# At a point with disjoint nonempty coordinate supports A,B, the zero-support
# count is r=4-|A|-|B|. Count r=2 closed vertices and r=1 curve families.
labels = set(range(4))
patterns = []
for s in range(1, 4):
    for A0 in combinations(range(4), s):
        A = set(A0)
        for t in range(1, 5-s):
            for B0 in combinations(sorted(labels-A), t):
                B = set(B0)
                patterns.append((frozenset(A), frozenset(B), 4-s-t))
assert sum(r == 2 for _, _, r in patterns) == 12
assert sum(r == 1 for _, _, r in patterns) == 24
assert sum(r == 0 for _, _, r in patterns) == 14
assert 2 * sum(r == 2 for _, _, r in patterns) == 24  # quotient sign pairs

# For (xy,zw) the 2x2 Jacobian minors generate the four cross-products;
# adjoining the two original equations gives all six squarefree pair products.
vars4 = tuple(range(4))
derivative_row_1 = [(1,), (0,), (), ()]  # y, x, 0, 0
# Instead check the exact monomial exponent vectors of the Jacobian minors.
grad1 = [(0, 1, 0, 0), (1, 0, 0, 0), None, None]
grad2 = [None, None, (0, 0, 0, 1), (0, 0, 1, 0)]
def mult(u, v):
    return tuple(x + y for x, y in zip(u, v))
minors = {mult(grad1[i], grad2[j]) for i in [0, 1] for j in [2, 3]}
orig = {(1, 1, 0, 0), (0, 0, 1, 1)}
all_squarefree_pairs = {
    tuple(int(k in pair) for k in vars4) for pair in combinations(vars4, 2)
}
assert minors | orig == all_squarefree_pairs
# This is the radical ideal of the union of four coordinate axes.
assert all(sum(m) == 2 and all(x in (0, 1) for x in m) for m in minors | orig)
print('HSO4_EXACT_CHECK_OK: Hadamard identities, 24 vertices, 24 curve families, reduced four-axis Jacobian germ')
