#!/usr/bin/env python3
"""Exact arithmetic checks for finite-ring polynomial root-count moments."""
from fractions import Fraction
from itertools import product


def closed_third(p, k):
    assert p >= 2 and k >= 1
    if k % 2:
        m = (k - 1) // 2
        numer = 5 * (p + 1) * p ** (m + 1) - (3 * k + 8) * p + (3 * k - 1)
    else:
        m = k // 2
        numer = p ** m * (p * p + 8 * p + 1) - (3 * k + 8) * p + (3 * k - 1)
    return Fraction(numer, p * p)


def valuation(z, p, k):
    if z == 0:
        return k
    t = 0
    while t < k and z % p == 0:
        z //= p
        t += 1
    return t


def triple_vandermonde(p, k):
    q = p ** k
    total = 0
    for u in range(q):
        for v in range(q):
            a = valuation(u, p, k)
            b = valuation(v, p, k)
            c = valuation(u - v, p, k)
            t = min(a, b, c)
            if t == k:
                weight = p ** (2 * k)
            else:
                second = min(k, a + b + c - t)
                weight = p ** (t + second)
            total += weight
    return Fraction(total, q * q)


def grouped(p, k):
    m = (k + 1) // 2
    first = sum(p ** t * (p + 1 + 3 * (p - 1) * (k - 2 * t))
                for t in range(m))
    second = sum(p ** (k - t) for t in range(m, k))
    return (Fraction(1) + Fraction(p - 1, p * p) * first
            + Fraction(p * p - 1, p * p) * second)


def brute(p, k, d):
    q = p ** k
    total = 0
    for a in product(range(q), repeat=d):
        root_count = 0
        for x in range(q):
            value = 1
            for coefficient in reversed(a):
                value = (value * x + coefficient) % q
            if value == 0:
                root_count += 1
        total += root_count ** 3
    return Fraction(total, q ** d)


def run():
    cases = [(2, 1), (2, 2), (2, 3), (2, 4), (2, 5),
             (3, 1), (3, 2), (3, 3), (5, 1), (5, 2), (7, 1)]
    for p, k in cases:
        expect = closed_third(p, k)
        assert grouped(p, k) == expect, ('grouped', p, k)
        assert triple_vandermonde(p, k) == expect, ('triple', p, k)
        assert brute(p, k, 3) == expect, ('cubic', p, k)
    for p in (2, 3, 5, 7, 11):
        for k in range(1, 21):
            assert grouped(p, k) == closed_third(p, k)
    quartic_cases = [(2, 2), (2, 3), (3, 2)]
    for p, k in quartic_cases:
        assert brute(p, k, 4) == closed_third(p, k)
    print(f'VERIFY_OK cubic_full_enumerations={len(cases)} '
          f'quartic_full_enumerations={len(quartic_cases)} '
          'smith_triple_checks=11 symbolic_group_checks=100 exact_arithmetic=yes')


if __name__ == '__main__':
    run()
