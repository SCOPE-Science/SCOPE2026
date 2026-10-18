#!/usr/bin/env python3
"""Exact finite checks for the four-interval squarefree divisor-sum theorem.

The infinite-prime step uses the published prime-in-short-interval theorem of
Nagura (1952), not a finite computation; see the mathematical proof.
"""
from fractions import Fraction
from math import isqrt, pi


def primes_through(n):
    sieve = bytearray([1]) * (n + 1)
    sieve[:2] = b'\x00\x00'
    for d in range(2, isqrt(n) + 1):
        if sieve[d]:
            sieve[d * d : n + 1 : d] = b'\x00' * ((n - d * d) // d + 1)
    return [j for j, is_prime in enumerate(sieve) if is_prime]


def finite_prime_tail_checks():
    endpoints = {5: 19, 7: 23, 11: 17, 13: 19,
                 17: 23, 19: 29, 23: 31}
    primes = primes_through(31)
    results = []
    for p, cutoff in endpoints.items():
        witnesses = [q for q in primes if p < q <= cutoff]
        product = Fraction(1)
        for q in witnesses:
            product *= 1 + Fraction(1, q * q)
        difference = product - (1 + Fraction(1, p * p))
        assert difference > 0, (p, witnesses, difference)
        results.append((p, witnesses, str(difference)))
    return results


def archimedes_endpoint_checks():
    # The classical rational bounds 223/71 < pi < 22/7 are inputs.
    lower_pi2 = Fraction(223, 71) ** 2
    upper_pi2 = Fraction(22, 7) ** 2
    assert lower_pi2 > Fraction(243, 25)  # implies T < 10/9.
    assert upper_pi2 < Fraction(54, 5)   # implies T > 1.
    # The complete interval-separation conditions reduce to T < 10/9.
    assert Fraction(10, 9) < Fraction(9, 8)
    # The prime-gap bound gives 25/[11(p^2+1)] > 1/p^2.
    # The comparison is algebraically the positive quantity 14p^2-11.
    assert all(14 * p * p - 11 > 0 for p in (29, 31, 101, 1009))


def finite_squarefree_samples(limit=30000):
    least_prime = [0] * (limit + 1)
    for p in range(2, limit + 1):
        if least_prime[p] == 0:
            for m in range(p, limit + 1, p):
                if least_prime[m] == 0:
                    least_prime[m] = p
    tail = 54 / (5 * pi * pi)
    scales = [1, 10 / 9, 5 / 4, 25 / 18]
    count = 0
    for n in range(1, limit + 1):
        m, value, squarefree = n, Fraction(1), True
        while m > 1:
            p = least_prime[m]
            m //= p
            if m % p == 0:
                squarefree = False
                break
            value *= 1 + Fraction(1, p * p)
        if squarefree:
            x = float(value)
            assert any(scale - 1e-12 <= x <= scale * tail + 1e-12
                       for scale in scales), (n, x)
            count += 1
    return count


if __name__ == '__main__':
    exact = finite_prime_tail_checks()
    archimedes_endpoint_checks()
    sampled = finite_squarefree_samples()
    for p, primes, surplus in exact:
        print('EXACT_TAIL', p, primes, 'surplus=', surplus)
    print('ARCHIMEDES_INEQUALITIES PASS')
    print('SQUAREFREE_SAMPLES', sampled)
    print('ALL_CHECKS_PASSED')
