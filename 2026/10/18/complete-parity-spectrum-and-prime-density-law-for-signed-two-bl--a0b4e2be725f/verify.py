#!/usr/bin/env python3
"""Recompute finite cases of a signed two-block partition parity theorem.

Uses only the Python standard library. Finite checks supplement the proof.
"""
from math import isqrt, log, pi


def arithmetic_coefficients(bound):
    sigma = [0] * (bound + 1)
    lam = [0] * (bound + 1)
    for d in range(1, bound + 1):
        chi = 1 if d % 4 == 1 else (-1 if d % 4 == 3 else 0)
        for n in range(d, bound + 1, d):
            sigma[n] += d
            lam[n] += chi
    a = [0] * (bound + 1)
    for n in range(1, bound + 1):
        numerator = sigma[n] - lam[n]
        numerator -= 2 * sigma[n // 2] if n % 2 == 0 else 0
        numerator += 4 * sigma[n // 4] if n % 4 == 0 else 0
        assert numerator % 4 == 0
        a[n] = numerator // 4
    return a, sigma, lam


def naive_signed_count(n):
    count = 0
    for x in range(1, n):
        for alpha in range(1, n // x + 1, 2):
            rem = n - alpha * x
            if rem <= x:
                continue
            for y in range(x + 1, rem + 1):
                if rem % y == 0 and (rem // y) % 2 == 1:
                    beta = rem // y
                    count += (-1) ** ((alpha - 1) // 2 + (beta - 1) // 2)
    return count


def smallest_prime_factors(bound):
    spf = list(range(bound + 1))
    for d in range(2, isqrt(bound) + 1):
        if spf[d] == d:
            for n in range(d * d, bound + 1, d):
                if spf[n] == n:
                    spf[n] = d
    return spf


def expected_odd(n, spf):
    k = 0
    m = n
    while m % 2 == 0:
        k += 1
        m //= 2
    odd_exponents = []
    t = m
    while t > 1:
        p = spf[t]
        e = 0
        while t % p == 0:
            t //= p
            e += 1
        if e & 1:
            odd_exponents.append((p, e))
    if not odd_exponents:
        s = isqrt(m)
        assert s * s == m
        return s % 8 in ((3, 5) if k <= 1 else (1, 7))
    return (len(odd_exponents) == 1
            and odd_exponents[0][0] % 8 in (3, 5)
            and odd_exponents[0][1] % 4 == 1)


def main():
    BOUND = 200000
    a, sigma, lam = arithmetic_coefficients(BOUND)
    spf = smallest_prime_factors(BOUND)
    for n in range(1, 110):
        direct = naive_signed_count(n)
        assert a[n] == direct, (n, a[n], direct)
    odd_count = 0
    for n in range(1, BOUND + 1):
        assert bool(a[n] & 1) == expected_odd(n, spf), (n, a[n])
        if a[n] & 1:
            odd_count += 1
        m = n
        while m % 2 == 0:
            m //= 2
        if m % 4 == 3:
            assert (a[n] & 1) == ((sigma[m] // 4) & 1)
    print('DIRECT_SIGNED_COUNTS=109')
    print('EXACT_PARITY_TESTS=', BOUND)
    print('ODD_COEFFICIENT_COUNT=', odd_count)
    print('NORMALIZED_RATIO_AT_BOUND=', round(odd_count * log(BOUND) / BOUND, 12))
    print('LIMIT_PREDICTION=', round(pi ** 2 / 8, 12))
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
