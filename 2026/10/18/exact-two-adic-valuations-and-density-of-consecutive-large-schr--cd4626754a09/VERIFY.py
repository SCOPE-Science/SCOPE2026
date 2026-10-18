#!/usr/bin/env python3
"""Exact finite consistency checks of a theorem on Schröder-number differences.
These tests do not constitute an exhaustive proof of the infinite statements.
"""
from math import comb


def v2(x):
    assert x != 0
    z = abs(x)
    return (z & -z).bit_length() - 1


def large_schroder(limit):
    a = [1, 2]
    for n in range(2, limit + 1):
        numerator = 3 * (2 * n - 1) * a[-1] - (n - 2) * a[-2]
        assert numerator % (n + 1) == 0
        a.append(numerator // (n + 1))
    return a


def binom_integer(x, k):
    prod = 1
    for j in range(k):
        prod *= x - j
    return prod // __import__('math').factorial(k)


def interpolated_mod(x, precision):
    modulus = 1 << precision
    total = 0
    # Terms k>=3*precision vanish modulo 2^precision, since
    # k-v2(k)>=precision on that tail.
    for k in range(1, 3 * precision):
        two_val = k - v2(k)
        if two_val >= precision:
            continue
        odd_divisor = k >> v2(k)
        factor = (1 << two_val) * pow(odd_divisor, -1, modulus)
        term = (factor * binom_integer(x - 1, k - 1)
                * binom_integer(x, k - 1)) % modulus
        total = (total + term) % modulus
    return total


def verify():
    a = large_schroder(2300)
    assert a[:8] == [1, 2, 6, 22, 90, 394, 1806, 8558]
    d = [a[n + 1] - a[n] for n in range(0, 2300)]
    assert d[0] == 1  # Explicitly outside the theorem's n>=1 domain.
    for n in range(1, 2031):
        claimed = 2 if n % 2 else 1 + v2(n * (n + 2))
        assert v2(d[n]) == claimed, (n, v2(d[n]), claimed)
    for alpha in range(1, 9):
        modulus = 1 << (alpha + 3) if alpha >= 2 else 16
        for n in range(1, 96):
            delta = a[n + (1 << alpha)] - a[n]
            rhs = (((-1) ** ((n - 1) // 2)) * (1 << (alpha + 1))
                   if alpha >= 2 else 4)
            assert (delta - rhs) % modulus == 0
            if alpha >= 2 and n % 2 == 0:
                delta_d = d[n + (1 << alpha)] - d[n]
                assert (delta_d - (1 << (alpha + 2))) % modulus == 0
    for j in range(4, 11):
        modulus = 1 << (j - 1)
        expected = {1 << (j - 2), ((1 << (j - 2)) - 2) % modulus}
        seen = {n % modulus for n in range(1, 1 << 11)
                if v2(d[n]) == j}
        assert seen == expected, (j, seen, expected)
    for precision in (8, 12, 16, 20):
        modulus = 1 << precision
        assert interpolated_mod(0, precision) == 2
        assert interpolated_mod(1, precision) == 2
        assert interpolated_mod(-1, precision) == (-2) % modulus
        assert interpolated_mod(-2, precision) == (-2) % modulus
        assert (interpolated_mod(1, precision)
                - interpolated_mod(0, precision)) % modulus == 0
        assert (interpolated_mod(-1, precision)
                - interpolated_mod(-2, precision)) % modulus == 0
    print('VERIFY_OK: valuations, shift congruences, residue fibres, and 2-adic zeros')


if __name__ == '__main__':
    verify()
