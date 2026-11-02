#!/usr/bin/env python3
"""Exact independent polynomial checks for prime-power Ramanujan sums (stdlib)."""
from math import comb


def ramanujan_prime_power(p, a, k):
    P = p ** (a - 1)
    if k % (p * P) == 0:
        return (p - 1) * P
    if k % P == 0:
        return -P
    return 0


def predicted_factor(p, a):
    P = p ** (a - 1)
    e = [0] * ((p - 2) * P + 1)
    for j in range(p - 1):
        e[j * P] = p - 1 - j
    return e


def multiply_one_minus_power(e, P):
    ans = [0] * (len(e) + P)
    for k, v in enumerate(e):
        ans[k] += v
        ans[k + P] -= v
    return ans


def shifted_coefficient(e, k):
    return sum(v * comb(j, k) for j, v in enumerate(e) if j >= k and v)



def bareiss_det(matrix):
    a = [row[:] for row in matrix]
    n = len(a)
    denom = 1
    sign = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            swap = next((i for i in range(k+1, n) if a[i][k] != 0), None)
            if swap is None:
                return 0
            a[k], a[swap] = a[swap], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k+1, n):
            for j in range(k+1, n):
                numerator = a[i][j] * pivot - a[i][k] * a[k][j]
                assert numerator % denom == 0
                a[i][j] = numerator // denom
            a[i][k] = 0
        denom = pivot
    return sign * a[-1][-1]


def discriminant_by_sylvester(coeff):
    degree = len(coeff) - 1
    if degree == 1:
        return 1
    f = list(reversed(coeff))
    g = [j * coeff[j] for j in range(1, degree + 1)][::-1]
    size = 2 * degree - 1
    rows = []
    for shift in range(degree - 1):
        rows.append([0] * shift + f + [0] * (size - shift - len(f)))
    for shift in range(degree):
        rows.append([0] * shift + g + [0] * (size - shift - len(g)))
    return (-1) ** (degree * (degree - 1) // 2) * bareiss_det(rows)

def run():
    instances = 0
    coefficients = 0
    checks = 0
    discriminants = 0
    for p, a in [(2, 1), (2, 2), (2, 4), (3, 1), (3, 2), (3, 3),
                 (5, 1), (5, 2), (5, 3), (7, 1), (7, 2), (11, 1), (11, 2), (13, 1)]:
        P = p ** (a - 1)
        E = predicted_factor(p, a)
        R = multiply_one_minus_power(E, P)
        assert len(R) == (p - 1) * P + 1
        for k in range(p ** a):
            coeff = R[k] if k < len(R) else 0
            assert (P * coeff) == ramanujan_prime_power(p, a, k), (p, a, k)
            coefficients += 1
        assert E[-1] == 1
        if p % 2:
            d = len(E) - 1
            for k in range(d):
                assert shifted_coefficient(E, k) % p == 0, (p, a, k)
                checks += 1
            assert shifted_coefficient(E, d) == 1
            assert shifted_coefficient(E, 0) == p * (p - 1) // 2
            assert (shifted_coefficient(E, 0) // p) % p != 0
            if (p, a) in ((3, 1), (3, 2), (3, 3), (5, 1), (5, 2), (7, 1)):
                from fractions import Fraction
                predicted = (Fraction((-1)**((d - 1)//2) * 2**P * P**d * p**(P*(p-3)) * (p-1)**(P*(p-3)), (p-1)))
                assert discriminant_by_sylvester(E) == predicted, (p, a)
                discriminants += 1
        instances += 1
    print('VERIFY_OK: %d exact prime-power cases; %d independently computed Ramanujan coefficients; %d shifted-Eisenstein coefficient divisibility checks; %d independent resultant-discriminant checks.' % (instances, coefficients, checks, discriminants))


if __name__ == '__main__':
    run()
