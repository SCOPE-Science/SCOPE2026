#!/usr/bin/env python3
"""Exact arithmetic checks for a prime-support obstruction in the square-totient divisibility problem.

Only finite arithmetic identities are checked here; the theorem for unbounded integers is proved separately.
"""
from fractions import Fraction
from math import prod, gcd, isqrt

ODD_FIRST_8 = (3, 5, 7, 11, 13, 17, 19, 23)
ODD_EXCLUDING_3_FIRST_8 = (5, 7, 11, 13, 17, 19, 23, 29)


def fraction_for(primes):
    value = Fraction(1)
    for p in primes:
        value *= Fraction(p, p + 1)
    return value


def spf_table(limit):
    spf = list(range(limit + 1))
    for i in range(2, isqrt(limit) + 1):
        if spf[i] == i:
            for j in range(i * i, limit + 1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf


def beta_from_spf(n, spf):
    out = 1
    while n > 1:
        p = spf[n]
        a = 0
        while n % p == 0:
            n //= p
            a += 1
        numerator = p ** (a + 1) + (-1) ** a
        assert numerator % (p + 1) == 0
        out *= numerator // (p + 1)
    return out


def beta_from_square_gcd(n):
    return sum(isqrt(gcd(n, j)) ** 2 == gcd(n, j) for j in range(1, n + 1))


def main():
    r8 = fraction_for(ODD_FIRST_8)
    s8 = fraction_for(ODD_EXCLUDING_3_FIRST_8)
    assert r8 == Fraction(1062347, 2654208)
    assert s8 == Fraction(30808063, 59719680)
    assert r8 > Fraction(2, 5)
    assert s8 > Fraction(1, 2)
    assert fraction_for(ODD_FIRST_8 + (29,)) < Fraction(2, 5)
    assert fraction_for(ODD_EXCLUDING_3_FIRST_8 + (31,)) < Fraction(1, 2)
    print('CERTIFICATES_OK', r8, s8)

    limit = 500000
    spf = spf_table(limit)
    even_witnesses = []
    for n in range(2, limit + 1):
        b = beta_from_spf(n, spf)
        assert b > 0
        if n <= 150:
            assert b == beta_from_square_gcd(n), (n, b)
        if n % 2 == 0 and (n - 1) % b == 0:
            even_witnesses.append(n)
    assert even_witnesses == [2, 4], even_witnesses
    print('EVEN_CENSUS_OK', limit, even_witnesses)

    # Test the unbounded factorization and the modular rejection mechanism on
    # large exact integers assembled from prime powers.
    for a in range(1, 16):
        for t in (1, 3, 5, 7, 3 * 5, 5 * 7 * 11, prod(ODD_FIRST_8), prod(ODD_EXCLUDING_3_FIRST_8)):
            n = (2 ** a) * t * t
            b = ((2 ** (a + 1) + (-1) ** a) // 3)
            m = t
            for p in (3, 5, 7, 11, 13, 17, 19, 23, 29):
                e = 0
                while m % p == 0:
                    e += 1
                    m //= p
                if e:
                    b *= (p ** (2 * e + 1) + 1) // (p + 1)
            assert m == 1
            assert (n - 1) % b != 0 or n in (2, 4), (a, t, n)
    print('STRUCTURAL_SAMPLES_OK', 15 * 8)
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
