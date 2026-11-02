#!/usr/bin/env python3
"""Exact finite checks for a congruence of two partition generating series.

The program does not replace a proof for all degrees and all primes.
"""
from math import isqrt


def sigma_one(limit):
    result = [0] * (limit + 1)
    for d in range(1, limit + 1):
        for n in range(d, limit + 1, d):
            result[n] += d
    return result


def euler_power(exponent, limit):
    # E(q)^exponent, from q(E^e)'/(E^e)=-e sum_{k>=1} sigma_1(k)q^k.
    sigma = sigma_one(limit)
    coefficients = [1] + [0] * limit
    for n in range(1, limit + 1):
        numerator = -exponent * sum(
            sigma[k] * coefficients[n - k] for k in range(1, n + 1)
        )
        assert numerator % n == 0
        coefficients[n] = numerator // n
    return coefficients


def multiply(first, second, limit):
    result = [0] * (limit + 1)
    for j, x in enumerate(first[:limit + 1]):
        if x:
            for k, y in enumerate(second[:limit + 1 - j]):
                result[j + k] += x * y
    return result


def reciprocal(series, limit):
    assert series[0] == 1
    inv = [1] + [0] * limit
    for n in range(1, limit + 1):
        inv[n] = -sum(series[k] * inv[n - k] for k in range(1, n + 1))
    return inv


def first_order_correction(p, a, limit):
    """Predicted normalized difference (F-C)/p^(a+1) mod p, before C factor."""
    shift = p ** (a - 1)
    h = [0] * (limit + 1)
    if p == 2:
        for r in range(1, isqrt(limit // shift) + 1):
            for multiplier in (shift, 2 * shift):
                pos = multiplier * r * r
                if pos <= limit:
                    h[pos] += 1
    else:
        for n in range(1, limit // shift + 1):
            h[shift * n] = -sum(pow(d, -1, p)
                                  for d in range(1, n + 1)
                                  if n % d == 0 and d % p != 0)
    return [value % p for value in h]


def verify(p, a, limit):
    t = p ** a
    f = euler_power(t * t - 1, limit)
    e = euler_power(1, limit)
    upper_small = euler_power(t, limit // t)
    upper = [0] * (limit + 1)
    for j, value in enumerate(upper_small):
        upper[t * j] = value
    c = multiply(upper, reciprocal(e, limit), limit)
    difference = [x - y for x, y in zip(f, c)]
    modulus = p ** (a + 1)
    assert all(value % modulus == 0 for value in difference), (p, a, 'modulus')
    first = next((n for n, value in enumerate(difference)
                  if value % (p * modulus) != 0), None)
    assert first == p ** (a - 1), (p, a, first)
    assert difference[first] // modulus % p == p - 1
    prediction = multiply([x % p for x in c],
                          first_order_correction(p, a, limit), limit)
    for n, value in enumerate(difference):
        assert value // modulus % p == prediction[n] % p, (p, a, n)
    return first


if __name__ == '__main__':
    examples = [(2, 1, 120), (2, 2, 120), (2, 3, 120), (2, 4, 120),
                (3, 1, 120), (3, 2, 120), (3, 3, 120),
                (5, 1, 120), (5, 2, 120), (7, 1, 100), (7, 2, 100),
                (11, 1, 100)]
    for p, a, limit in examples:
        verify(p, a, limit)
    print('VERIFY_OK cases=%d full_coefficient_checks=%d dyadic_cases=4'
          % (len(examples), sum(limit + 1 for _, _, limit in examples)))
