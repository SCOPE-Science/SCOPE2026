#!/usr/bin/env python3
"""Exact finite corroboration of co-generated denumerant formulas; no dependencies."""
from math import gcd


def test_pair(a, b):
    cutoff = 3 * a * b + a + b
    ways = [0] * (cutoff + 1)
    ways[0] = 1
    for coin in (a, b, a + b):
        for n in range(coin, cutoff + 1):
            ways[n] += ways[n - coin]
    for n, observed in enumerate(ways):
        u = (n * pow(a, -1, b)) % b
        v = (n * pow(b, -1, a)) % a
        assert (n - a * u - b * v) % (a * b) == 0
        t = (n - a * u - b * v) // (a * b)
        predicted = sum(1 + min(u + b * j, v + a * (t - j)) for j in range(max(0, t + 1)))
        assert observed == predicted, (a, b, n, observed, predicted)
    genus = (a - 1) * (b - 1) // 2
    assert ways.count(0) == genus
    assert max(n for n, value in enumerate(ways) if value == 0) == a * b - a - b
    for k in range(1, a + 2):
        observed_exact = sum(value == k for value in ways)
        observed_atmost = sum(value <= k for value in ways)
        observed_max = max(n for n, value in enumerate(ways) if value <= k)
        expected_exact = (a + b - k) if k <= a else a
        expected_atmost = genus + k * (a + b) - k * (k + 1) // 2 if k <= a else genus + a * (a + b) - a * (a + 1) // 2 + a
        expected_max = a * b - a - b + b * k if k <= a else b * (2 * a - 1)
        assert (observed_exact, observed_atmost, observed_max) == (expected_exact, expected_atmost, expected_max), (
            a, b, k, (observed_exact, observed_atmost, observed_max),
            (expected_exact, expected_atmost, expected_max))
    return cutoff + 1


def main():
    pairs = 0
    integer_values = 0
    for a in range(2, 41):
        for b in range(a + 1, 46):
            if gcd(a, b) == 1:
                integer_values += test_pair(a, b)
                pairs += 1
    assert pairs > 500
    print(f'CERTIFICATE_OK pairs={pairs} exact_denumerant_values={integer_values}')


if __name__ == '__main__':
    main()
