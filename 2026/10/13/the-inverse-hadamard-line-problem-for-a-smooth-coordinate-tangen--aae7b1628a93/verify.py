#!/usr/bin/env python3
"""Exact illustrative matrix checks for a smooth coordinate-tangent Hadamard quadric.
This finite instance supplements, but does not replace, the general geometric proof.
Only Python's standard library is required.
"""
from itertools import permutations


def det(a):
    n = len(a)
    total = 0
    for p in permutations(range(n)):
        inv = sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n))
        term = (-1 if inv % 2 else 1)
        for i in range(n):
            term *= a[i][p[i]]
        total += term
    return total


def transpose(a):
    return [list(row) for row in zip(*a)]


def mul(a, b):
    bt = transpose(b)
    return [[sum(x * y for x, y in zip(row, col)) for col in bt] for row in a]


# For each i: the product of L_i = a_i*s+b_i*t and R_i = c_i*u+d_i*v.
L = [[1, 0], [0, 1], [1, 1], [1, 2]]
R = [[1, 0], [0, 1], [1, 3], [1, 5]]
T = [[a*c, a*d, b*c, b*d] for (a, b), (c, d) in zip(L, R)]
assert T == [[1, 0, 0, 0], [0, 0, 0, 1], [1, 3, 1, 3], [1, 5, 2, 10]]
assert det(T) == 1
Tinv = [[1, 0, 0, 0], [-1, 4, 2, -1], [2, -15, -5, 3], [0, 1, 0, 0]]
identity = [[int(i == j) for j in range(4)] for i in range(4)]
assert mul(T, Tinv) == identity and mul(Tinv, T) == identity
print('Segre_coordinate_change_determinant=1')

# The standard Segre equation is z0*z3-z1*z2=0.
# H0/2 is its symmetric coefficient matrix; dual quadric matrix is T*H0*T^t.
H0 = [[0, 0, 0, 1], [0, 0, -1, 0],
      [0, -1, 0, 0], [1, 0, 0, 0]]
D = mul(mul(T, H0), transpose(T))
assert det(D) != 0
assert [D[i][i] for i in range(4)] == [0, 0, 0, 0]
print('nonsingular_quadric_and_four_coordinate_tangencies=ok')

for a, b in zip(L, R):
    assert len(a) == len(b) == 2
    # The 2x2 bilinear matrix of the i-th coordinate has determinant zero.
    C = [[a[0]*b[0], a[0]*b[1]], [a[1]*b[0], a[1]*b[1]]]
    assert det(C) == 0 and any(C[i][j] for i in range(2) for j in range(2))
print('four_nonzero_rank_one_bilinear_sections=ok')

# Matrix identity Tinv*T=I proves the polynomial identity for all s,t,u,v.
# Verify its intended monomial order with independent integer checks.
for s, t, u, v in [(-3, 2, 7, 1), (1, 0, 0, 1), (4, 9, 5, -2)]:
    z = [s*u, s*v, t*u, t*v]
    x = [sum(T[i][j]*z[j] for j in range(4)) for i in range(4)]
    y = [sum(Tinv[i][j]*x[j] for j in range(4)) for i in range(4)]
    assert y == z and y[0]*y[3] == y[1]*y[2]
print('example_polynomial_identity=ok')
print('VERIFY_OK')
