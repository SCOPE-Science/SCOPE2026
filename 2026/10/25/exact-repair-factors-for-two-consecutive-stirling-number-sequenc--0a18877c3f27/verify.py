#!/usr/bin/env python3
"""Reproduce finite congruence certificates for two Stirling repair factors.

Python 3 standard library only. Exact modular arithmetic, no finite-prefix
extrapolation: the accompanying proof reduces all indices to these tests.
"""
from math import comb, factorial, gcd

M = 13860
EXCEPTIONAL = ((2, 8, 256, 11), (3, 3, 54, 6), (5, 1, 20, 4))


def stirling_second(n, k):
    row = [0] * (k + 1)
    row[0] = 1
    for _ in range(n):
        nr = [0] * (k + 1)
        for j in range(1, k + 1):
            nr[j] = j * row[j] + row[j - 1]
        row = nr
    return row[k]


def mobius(n):
    x = n
    sign = 1
    d = 2
    while d * d <= x:
        if x % d == 0:
            x //= d
            if x % d == 0:
                return 0
            sign = -sign
            while x % d == 0:
                x //= d
        d += 1
    if x > 1:
        sign = -sign
    return sign


def delta(k, n):
    return sum(mobius(n // d) * stirling_second(d + k - 1, k)
               for d in range(1, n + 1) if n % d == 0)


def valuation(n, p):
    v = 0
    while n % p == 0:
        v += 1
        n //= p
    return v


def check():
    assert factorial(12) % M == 0
    assert factorial(13) % M == 0
    for k in (12, 13):
        weights = [(-1) ** (k - j) * comb(k, j) * j ** (k - 1)
                   for j in range(1, k + 1)]
        for p, h, period, maximum_r in EXCEPTIONAL:
            assert valuation(factorial(k), p) - valuation(M, p) == h
            assert period == (p - 1) * p ** h
            assert maximum_r == h + 3
            for r in range(1, maximum_r + 1):
                pr, previous = p ** r, p ** (r - 1)
                modulus = p ** (r + h)
                for t in range(1, 2 * period + 1):
                    if t % p == 0:
                        continue
                    s = 0
                    for j, c in enumerate(weights, start=1):
                        numerator = (pow(j, pr * t, modulus)
                                     - pow(j, previous * t, modulus)) % modulus
                        assert numerator % pr == 0
                        s += c * (numerator // pr)
                    assert s % (p ** h) == 0, (k, p, r, t)
            print('PASS finite p-adic certificate', k, p, h,
                  period, maximum_r)
        witnesses = ((8, 4), (9, 9), (5, 5), (7, 7), (11, 11)) if k == 12 else (
            (4, 4), (9, 9), (5, 5), (7, 7), (11, 11))
        for n, required in witnesses:
            numerator = delta(k, n)
            denominator = n // gcd(n, numerator)
            assert denominator == required, (k, n, denominator, required)
        print('PASS exact minimality witnesses', k, witnesses)
    print('ALL CERTIFICATES PASS')


if __name__ == '__main__':
    check()
