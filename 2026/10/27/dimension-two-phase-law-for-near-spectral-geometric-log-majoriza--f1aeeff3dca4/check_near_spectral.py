#!/usr/bin/env python3
"""Exact finite checks for near-spectral versus spectral geometric curves.

Uses rational positive 2-by-2 test matrices and higher-dimensional
commutator-energy identities. These checks do not replace the proof for
arbitrary matrices and real parameters.
"""
from fractions import Fraction as F
from itertools import product
from math import asinh, acosh, cosh, sinh


def identity(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def diagonal(values):
    return [[v if i == j else F(0) for j in range(len(values))]
            for i, v in enumerate(values)]


def transpose(a):
    return [list(row) for row in zip(*a)]


def mult(a, b):
    assert len(a[0]) == len(b)
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def add(a, b):
    return [[x + y for x, y in zip(r, s)] for r, s in zip(a, b)]


def trace(a):
    return sum((a[i][i] for i in range(len(a))), F(0))


def det2(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def rotation(p, q):
    # Rational Pythagorean rotation, p^2+q^2=1.
    return [[p, -q], [q, p]]


checks = 0
# The exact trace commutator identity holds for every positive diagonal A
# and every self-adjoint C; test many symmetric rational C in dimensions 2-4.
for n in (2, 3, 4):
    for base in (F(2), F(3, 2), F(5, 3), F(4)):
        eig = [base ** (i - n // 2) for i in range(n)]
        a = diagonal(eig)
        ai = diagonal([1 / v for v in eig])
        for z in (F(0), F(1, 7), F(2, 9), F(-1, 11)):
            c = [[F(3 + i) if i == j else z / (i + j + 1)
                  for j in range(n)] for i in range(n)]
            lhs = trace(mult(mult(mult(ai, c), a), c)) - trace(mult(c, c))
            norm_sq = sum(((eig[i] - eig[j]) ** 2 / (eig[i] * eig[j]))
                          * c[i][j] ** 2 for i in range(n) for j in range(n))
            assert lhs == norm_sq / 2
            assert lhs >= 0
            checks += 2

# Positive definite det-one 2x2 examples; square roots chosen rational.
rots = [(F(1), F(0)), (F(0), F(1)), (F(3, 5), F(4, 5)),
        (F(5, 13), F(12, 13)), (F(15, 17), F(8, 17))]
for a0, b0, (p, q) in product((F(1), F(2), F(3, 2), F(5, 3), F(4)),
                                (F(1), F(2), F(4, 3), F(3)), rots):
    a = diagonal([a0 * a0, 1 / (a0 * a0)])
    ai = diagonal([1 / (a0 * a0), a0 * a0])
    ahinv = diagonal([1 / a0, a0])
    r = rotation(p, q)
    c = mult(mult(r, diagonal([b0, 1 / b0])), transpose(r))
    b = mult(c, c)
    d = mult(mult(mult(mult(ahinv, c), a), c), ahinv)
    k2 = F(2) + trace(mult(a, b))
    m_num = add(ai, b)
    n_num = add(ai, d)
    assert det2(a) == det2(b) == det2(d) == 1
    assert det2(m_num) == det2(n_num) == k2
    assert trace(mult(a, m_num)) == trace(mult(a, n_num)) == k2
    defect = trace(d) - trace(b)
    assert defect == ((a[0][0] - a[1][1]) ** 2 /
                      (a[0][0] * a[1][1])) * c[0][1] ** 2
    assert defect >= 0
    # At t=1/2 the traces are identical, at t=1 the comparison reverses.
    x = mult(mult(n_num, a), n_num)
    y = mult(mult(m_num, a), m_num)
    assert trace(x) >= trace(y)
    # Quantitative exact 2x2 commutator identity using B, not B^{1/2}.
    comm = add(mult(a, b), [[-v for v in row] for row in mult(b, a)])
    norm2 = sum((v * v for row in comm for v in row), F(0))
    denom = 2 * det2(a) * (trace(b) + 2)  # det(B)=1
    assert defect == norm2 / denom
    checks += 8

print(f"PASS: {checks} exact rational identities and inequalities")
