#!/usr/bin/env python3
"""Finite exact-arithmetic checks for parity of two-block odd partitions.

Run with Python 3, no third-party dependencies. The infinite assertions rest on
separate mathematical arguments, not on these bounded computations.
"""
from math import isqrt, pi, log

LIMIT = 300000
DIRECT = 220


def smallest_prime_factors(limit):
    spf = list(range(limit + 1))
    for p in range(2, isqrt(limit) + 1):
        if spf[p] == p:
            for n in range(p * p, limit + 1, p):
                if spf[n] == n:
                    spf[n] = p
    return spf


def divisor_sums(limit):
    sigma = [0] * (limit + 1)
    lam = [0] * (limit + 1)
    for d in range(1, limit + 1):
        c = 1 if d % 4 == 1 else (-1 if d % 4 == 3 else 0)
        for n in range(d, limit + 1, d):
            sigma[n] += d
            lam[n] += c
    return sigma, lam


def predicted_odd(n, spf):
    t = 0
    while not n % 2:
        n //= 2
        t += 1
    odd_exponents = []
    square_root_character = 1
    while n > 1:
        p = spf[n]
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        if e % 2:
            odd_exponents.append((p, e))
        if p % 8 in (3, 5) and (e // 2) % 2:
            square_root_character *= -1
    if not odd_exponents:
        return square_root_character == (-1 if t < 2 else 1)
    return (len(odd_exponents) == 1
            and odd_exponents[0][0] % 8 in (3, 5)
            and odd_exponents[0][1] % 4 == 1)


def direct_two_block(limit):
    a = [0] * (limit + 1)
    for x in range(1, limit):
        for y in range(x + 1, limit - x + 1):
            for r in range((limit - x - y) // (2 * x) + 1):
                first = (2 * r + 1) * x + y
                for s in range((limit - first) // (2 * y) + 1):
                    a[first + 2 * s * y] += -1 if (r + s) % 2 else 1
    return a


def verify():
    spf = smallest_prime_factors(LIMIT)
    sigma, lam = divisor_sums(LIMIT)
    direct = direct_two_block(DIRECT)
    counted = 0
    samples = {}
    for n in range(1, LIMIT + 1):
        s_half = sigma[n // 2] if n % 2 == 0 else 0
        s_quarter = sigma[n // 4] if n % 4 == 0 else 0
        numerator = sigma[n] - lam[n] - 2 * s_half + 4 * s_quarter
        assert numerator % 4 == 0, ('integrality', n, numerator)
        coefficient = numerator // 4
        if n <= DIRECT:
            assert direct[n] == coefficient, ('direct signed partitions', n, direct[n], coefficient)
        prediction = predicted_odd(n, spf)
        assert coefficient % 2 == prediction, ('parity', n, coefficient, prediction)
        counted += prediction
        if n in (1000, 10000, 100000, 300000):
            samples[n] = (counted, round(counted * log(n) / n, 6))
    local_cases = 0
    for p in range(3, 400):
        if spf[p] != p:
            continue
        for exponent in range(0, 16):
            s = sum(pow(p, j) for j in range(exponent + 1))
            lam_p = exponent + 1 if p % 4 == 1 else (1 if exponent % 2 == 0 else 0)
            predicted = 4 * ((exponent + 1) // 2) if p % 8 in (3, 5) else 0
            assert (s - lam_p - predicted) % 8 == 0, ('local lemma', p, exponent)
            local_cases += 1
    print('VERIFY_OK direct_signed=', DIRECT,
          'coefficient_parity=', LIMIT,
          'local_mod8=', local_cases,
          'samples=', samples,
          'asymptotic_constant=', round(pi * pi / 8, 9))


if __name__ == '__main__':
    verify()
