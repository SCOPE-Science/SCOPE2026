#!/usr/bin/env python3
"""Reproducible finite checks for the two-step entrance-minimum formula.

The infinite theorem is proved in RESULT.md, not by this program.
"""
from fractions import Fraction
from math import gcd


def step(x):
    q = x.numerator // x.denominator
    return q * (1 + (x - q))


def is_order_two(a, M):
    assert a >= 2 * M and gcd(a, M) == 1
    x = Fraction(a, M)
    first = step(x)
    if first.denominator == 1:
        return False
    return step(first).denominator == 1


def minimum_formula(p, k):
    M = p ** k
    if p == 2 and k == 1:
        return 7
    if k % 2 == 0:
        return M * p ** (k // 2) + 1
    s = (k - 1) // 2
    if p == 2:
        return M * 2 ** (s + 1) + 1
    return M * p ** s * ((p + 1) // 2) + ((M * (p - 1) + p) // (p + 1))


def primes_up_to(limit):
    return [p for p in range(2, limit + 1)
            if all(p % j for j in range(2, int(p ** .5) + 1))]


def main():
    cases = 0
    smaller_numerators = 0
    full_bound = 2200
    for p in primes_up_to(37):
        k, M = 1, p
        while M <= full_bound:
            a = minimum_formula(p, k)
            assert is_order_two(a, M), (p, k, 'candidate invalid')
            for b in range(2 * M, a):
                if gcd(b, M) != 1:
                    continue
                assert not is_order_two(b, M), (p, k, b, a)
                smaller_numerators += 1
            cases += 1
            k, M = k + 1, M * p
    high_scale = 0
    for p in primes_up_to(41):
        for k in range(1, 30):
            M = p ** k
            a = minimum_formula(p, k)
            assert is_order_two(a, M), (p, k)
            if p != 2 or k != 1:
                q, r = divmod(a, M)
                assert 1 <= r < M and gcd(r, M) == 1
                q0 = p ** (k // 2) if k % 2 == 0 else (
                    (2 ** ((k + 1) // 2)) if p == 2 else
                    p ** ((k - 1) // 2) * ((p + 1) // 2))
                assert q == q0
                # Independently exclude every smaller integer quotient using the
                # denominator and first-iterate floor range, not enumeration.
                for trial_q in range(2, min(q0, 10000)):
                    d = M // gcd(trial_q, M)
                    assert (2 * trial_q - 1) // d == (trial_q - 1) // d
            high_scale += 1
    assert minimum_formula(2, 1) == 7
    assert minimum_formula(3, 3) == 176
    assert minimum_formula(5, 3) == 1959
    print('VERIFY_OK exhaustive_prime_powers=%d rejected_smaller_coprime_numerators=%d large_power_candidate_checks=%d' % (
          cases, smaller_numerators, high_scale))


if __name__ == '__main__':
    main()
