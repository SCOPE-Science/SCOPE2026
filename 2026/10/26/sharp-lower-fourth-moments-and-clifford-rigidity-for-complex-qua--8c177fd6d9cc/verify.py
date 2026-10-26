#!/usr/bin/env python3
"""Independent exact arithmetic checks of a spherical quartic identity.

Run: python3 verify.py. Requires only the Python standard library.
"""
from fractions import Fraction
import random


def add(z, w):
    return z[0] + w[0], z[1] + w[1]


def mul(z, w):
    return z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0]


def conj(z):
    return z[0], -z[1]


def matrix_mul(a, b):
    n = len(a)
    return [[sum_pairs(mul(a[i][k], b[k][j]) for k in range(n))
             for j in range(n)] for i in range(n)]


def sum_pairs(pairs):
    z = (0, 0)
    for w in pairs:
        z = add(z, w)
    return z


def trace(a):
    return sum_pairs(a[i][i] for i in range(len(a)))


def conjugate(a):
    return [[conj(z) for z in row] for row in a]


def polynomial_product(p, q):
    result = {}
    for e, z in p.items():
        for f, w in q.items():
            k = tuple(x + y for x, y in zip(e, f))
            result[k] = add(result.get(k, (0, 0)), mul(z, w))
    return result


def odd_double_factorial(k):
    result = 1
    for j in range(k, 0, -2):
        result *= j
    return result


def spherical_wick_numerator(p):
    # For total degree eight the common denominator is
    # n(n+2)(n+4)(n+6). This sum computes its exact numerator.
    answer = (0, 0)
    for exponents, coefficient in p.items():
        if any(e % 2 for e in exponents):
            continue
        weight = 1
        for e in exponents:
            weight *= odd_double_factorial(e-1)
        answer = add(answer, (weight*coefficient[0], weight*coefficient[1]))
    return answer


def check_pair(b, c):
    n = len(b)
    a = [[(b[i][j], c[i][j]) for j in range(n)] for i in range(n)]
    ac = conjugate(a)
    a2 = matrix_mul(a, a)
    aa = matrix_mul(a, ac)
    q = trace(a2)
    t = trace(aa)
    r = trace(matrix_mul(a2, conjugate(a2)))
    s = trace(matrix_mul(aa, aa))
    assert t[1] == r[1] == s[1] == 0
    t, r, s = t[0], r[0], s[0]
    q2 = q[0]**2+q[1]**2

    x = [[sum(b[i][k]*b[k][j]+c[i][k]*c[k][j]
              for k in range(n)) for j in range(n)] for i in range(n)]
    x2 = sum(x[i][j]*x[j][i] for i in range(n) for j in range(n))
    assert r+s == 2*x2

    poly = {}
    for i in range(n):
        for j in range(n):
            exponents = tuple(int(k==i)+int(k==j) for k in range(n))
            poly[exponents] = add(poly.get(exponents, (0, 0)), a[i][j])
    poly_conj = {e: conj(z) for e, z in poly.items()}
    quartic = polynomial_product(polynomial_product(poly, poly),
                                  polynomial_product(poly_conj, poly_conj))
    numerator = spherical_wick_numerator(quartic)
    assert numerator[1] == 0
    asserted_numerator = 4*q2 + 8*t*t + 32*r + 16*s
    assert numerator[0] == asserted_numerator

    denominator = n*(n+2)*(n+4)*(n+6)
    second_moment = Fraction(2*t, n*(n+2))
    fourth_moment = Fraction(numerator[0], denominator)
    deficit = fourth_moment - Fraction(2*(n+2), n+6)*second_moment**2
    sos = (Fraction(4*q2+16*r, denominator)
           + Fraction(32, denominator)*(Fraction(x2)-Fraction(t*t,n)))
    assert deficit == sos >= 0
    return deficit


def random_tracefree_symmetric(n, rng):
    a = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            a[i][j] = a[j][i] = rng.randint(-2, 2)
    a[n-1][n-1] = -sum(a[i][i] for i in range(n-1))
    return a


def canonical_clifford(n):
    assert n%2 == 0
    m = n//2
    b = [[0]*n for _ in range(n)]
    c = [[0]*n for _ in range(n)]
    for i in range(m):
        b[i][i] = 1
        b[i+m][i+m] = -1
        c[i][i+m] = c[i+m][i] = 1
    return b, c


def main():
    rng = random.Random(20260920)
    count = 0
    for n in (2, 3, 4, 5, 6):
        for _ in range(16):
            b = random_tracefree_symmetric(n, rng)
            c = random_tracefree_symmetric(n, rng)
            check_pair(b, c)
            count += 1
    for n in (2, 4, 6, 8):
        assert check_pair(*canonical_clifford(n)) == 0
        count += 1
    print(f'PASS: {count} complete exact polynomial-moment/deficit comparisons')
    print('PASS: Clifford equality matrices in dimensions 2, 4, 6, 8')


if __name__ == '__main__':
    main()
