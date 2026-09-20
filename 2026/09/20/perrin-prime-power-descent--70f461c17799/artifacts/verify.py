#!/usr/bin/env python3
"""Exact modular checks for Perrin prime-power lifting statements."""


def mat_mul(A, B, m):
    d = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(d)) % m
             for j in range(d)] for i in range(d)]


def mat_pow(A, n, m):
    d = len(A)
    R = [[int(i == j) for j in range(d)] for i in range(d)]
    A = [[x % m for x in row] for row in A]
    while n:
        if n & 1:
            R = mat_mul(R, A, m)
        A = mat_mul(A, A, m)
        n //= 2
    return R


def trace(A, m):
    return sum(A[i][i] for i in range(len(A))) % m


# Polynomial arithmetic in (Z/mZ)[x]/(x^3-x-1), where x^3=x+1.
def poly_mul(a, b, m):
    t = [0] * 5
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            t[i + j] = (t[i + j] + x * y) % m
    for deg in (4, 3):
        c = t[deg] % m
        if c:
            t[deg] = 0
            t[deg - 3] = (t[deg - 3] + c) % m
            t[deg - 2] = (t[deg - 2] + c) % m
    return t[:3]


def poly_pow(a, n, m):
    r = [1, 0, 0]
    while n:
        if n & 1:
            r = poly_mul(r, a, m)
        a = poly_mul(a, a, m)
        n //= 2
    return r


def perrin_poly(n, m):
    # trace(1,x,x^2)=(3,0,2), and x^{-1}=x^2-1.
    base = [0, 1, 0] if n >= 0 else [-1, 0, 1]
    a = poly_pow(base, abs(n), m)
    return (3 * a[0] + 2 * a[2]) % m


M = [[0, 1, 0], [0, 0, 1], [1, 1, 0]]
Mi = [[-1, 0, 1], [1, 0, 0], [0, 1, 0]]


def perrin_matrix(n, m):
    return trace(mat_pow(M if n >= 0 else Mi, abs(n), m), m)


# The first three entries currently listed in OEIS A173656.
for p in (521, 190699, 36944128783):
    m2, m3 = p * p, p ** 3
    vals = {}
    for n, label in [(p, 'P_p'), (-p, 'P_-p'),
                     (p * p, 'P_p2'), (-p * p, 'P_-p2')]:
        a = perrin_matrix(n, m3)
        b = perrin_poly(n, m3)
        assert a == b, (p, n, a, b)
        vals[label] = a

    assert vals['P_p'] % m2 == 0
    assert vals['P_p2'] % m2 == 0
    assert vals['P_p2'] % m3 != 0
    assert vals['P_-p'] % m2 != m2 - 1
    assert vals['P_-p2'] % m2 == vals['P_-p'] % m2

    print(f'p={p}')
    print(f'  p^2 = {m2}')
    print(f'  P(p) mod p^2 = {vals["P_p"] % m2}')
    print(f'  P(-p) mod p^2 = {vals["P_-p"] % m2}; target = {m2 - 1}')
    print(f'  (P(-p)+1)/p mod p = {((vals["P_-p"] % m2) + 1) // p}')
    print(f'  P(p^2) mod p^3 = {vals["P_p2"]}; '
          f'quotient by p^2 mod p = {(vals["P_p2"] // m2) % p}')

# The even prime does not start a prime-power chain.
assert perrin_matrix(2, 4) == 2
assert perrin_matrix(4, 4) == 2
print('p=2: P(2) mod 4 = 2, so 4 is not an unrestricted Perrin pseudoprime')
print('matrix/polynomial agreement: PASS')
