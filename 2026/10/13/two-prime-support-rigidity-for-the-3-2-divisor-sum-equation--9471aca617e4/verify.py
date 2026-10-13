#!/usr/bin/env python3
"""Exact finite corroboration of a two-prime divisor-sum classification.

Usage: python verify.py [upper_bound]
The unrestricted argument is in the accompanying mathematical proof.
"""
from array import array
from math import isqrt
import sys


def is_prime_trial(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    for d in range(3, isqrt(n) + 1, 2):
        if n % d == 0:
            return False
    return True


def sigma_and_omega_sieves(limit):
    sigma = array('Q', [0]) * (limit + 1)
    omega = array('B', [0]) * (limit + 1)
    is_composite = bytearray(limit + 1)
    for d in range(1, limit + 1):
        for multiple in range(d, limit + 1, d):
            sigma[multiple] += d
    for p in range(2, limit + 1):
        if is_composite[p] == 0:
            for multiple in range(p, limit + 1, p):
                is_composite[multiple] = 1
                omega[multiple] += 1
    return sigma, omega


def main():
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 1_000_000
    assert 10 <= limit <= 10_000_000
    sigma, omega = sigma_and_omega_sieves(limit)
    observed = [m for m in range(1, limit + 1)
                if omega[m] <= 2 and 2 * sigma[m] == 3 * (m + 1)]
    expected = []
    a = 1
    while True:
        q = 3 ** (a + 1) - 4
        m = 3 ** a * q
        if m > limit:
            break
        if is_prime_trial(q):
            expected.append(m)
        a += 1
    assert observed == expected, (observed, expected)
    # An unbounded exponent witness does not require assuming the neighboring
    # integer is prime. The following instance has a composite neighbor.
    a = 20
    q = 3 ** (a + 1) - 4
    m = 3 ** a * q
    assert q == 10460353199 and is_prime_trial(q)
    assert (3 ** (a + 1) - 1) * (q + 1) == 3 * (m + 1)
    assert ((m - 1) // 2) % 102461 == 0
    print('VERIFY_OK', 'upper_bound=', limit,
          'checked_omega_le_two=', sum(1 for j in range(1, limit+1) if omega[j] <= 2),
          'observed=', observed, 'expected=', expected,
          'large_witness=', m, 'large_q=', q, 'composite_neighbor_factor=102461')


if __name__ == '__main__':
    main()
