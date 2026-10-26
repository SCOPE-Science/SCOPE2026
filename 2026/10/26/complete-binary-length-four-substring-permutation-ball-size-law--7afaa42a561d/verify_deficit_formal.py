#!/usr/bin/env python3
"""Exact all-length coefficient certificate for a four-state deficit transfer law.

Polynomials use integer coefficients in commuting indeterminates s,z.
No symbolic-algebra dependencies are required.
"""
from itertools import permutations

ZERO = {}
ONE = {(0, 0): 1}
S = {(1, 0): 1}
Z = {(0, 1): 1}


def constant(c):
    return {(0, 0): c} if c else {}


def add(a, b):
    r = dict(a)
    for m, c in b.items():
        r[m] = r.get(m, 0) + c
        if not r[m]: del r[m]
    return r


def neg(a):
    return {m: -c for m, c in a.items()}


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    r = {}
    for (i, j), c in a.items():
        for (k, l), d in b.items():
            m = (i+k, j+l)
            r[m] = r.get(m, 0) + c*d
    return {m: c for m, c in r.items() if c}


def power(a, n):
    r = ONE
    for _ in range(n): r = mul(r, a)
    return r


def determinant(mat):
    n = len(mat)
    total = ZERO
    for perm in permutations(range(n)):
        inv = sum(perm[i] > perm[j] for i in range(n) for j in range(i+1, n))
        term = ONE
        for i, j in enumerate(perm):
            term = mul(term, mat[i][j])
            if not term: break
        total = add(total, neg(term) if inv % 2 else term)
    return total


def trim_z(poly, degree=5):
    return {k: v for k, v in poly.items() if k[1] <= degree}


def main():
    z2 = power(Z, 2)
    z3 = power(Z, 3)
    A = [
        [z3, z2, ZERO, ZERO],
        [ZERO, ZERO, z2, ONE],
        [ZERO, ZERO, ONE, z2],
        [ONE, ONE, ZERO, ZERO],
    ]
    b = [z2, ONE, ONE, ONE]
    B = [[sub(ONE if i == j else ZERO, mul(S, A[i][j]))
          for j in range(4)] for i in range(4)]
    # The 5x5 block determinant equals det(B) * 2*1^T*A*B^{-1}*b.
    u = [mul(constant(-2), sum_polys(A[i][j] for i in range(4))) for j in range(4)]
    enlarged = [B[i] + [b[i]] for i in range(4)] + [u + [ZERO]]
    D = determinant(B)
    N = determinant(enlarged)
    one_minus_s = sub(ONE, S)
    expected_numerator = add(add(
        mul(constant(6), power(one_minus_s, 2)),
        mul(mul(sub(constant(8), mul(constant(2), S)), one_minus_s), z2)),
        add(mul(mul(constant(6), S), power(Z, 4)),
            mul(mul(constant(2), one_minus_s), power(Z, 5))))
    lhs = trim_z(mul(D, expected_numerator))
    rhs = trim_z(mul(power(one_minus_s, 3), N))
    assert lhs == rhs, (sub(lhs, rhs))
    assert D.get((0, 0)) == 1
    print('FORMAL_COEFFICIENTS_OK')
    print('transfer_det_terms=', len(D), 'block_numerator_terms=', len(N))
    print('deficit coefficient 0: 6/(1-s)')
    print('deficit coefficient 1: 0')
    print('deficit coefficient 2: (8-2s)/(1-s)^2')
    print('deficit coefficient 3: 0')
    print('deficit coefficient 4: 6s/(1-s)^3')
    print('deficit coefficient 5: 2/(1-s)^2')


def sum_polys(items):
    r = ZERO
    for x in items: r = add(r, x)
    return r


if __name__ == '__main__':
    main()
