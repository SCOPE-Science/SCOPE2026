#!/usr/bin/env python3
"""Pure-integer certified bounds for an iterated divisor-sum constant.

All numerical claims in RESULT.md are checked with integer arithmetic.
A complete run needs under approximately 150 MiB of memory.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import isqrt

LIMIT = 100_000_000
SMALL = 1_000
DEGREE = 4
Q = 10 ** 40
PRUNE = Q // 10 ** 18
EXPONENT_CUTOFF = 10 ** 22


def primes_upto(limit):
    if limit < 2:
        return
    size = (limit + 1) // 2
    sieve = bytearray(b'\x01') * size
    sieve[0] = 0
    for i in range(1, isqrt(limit) // 2 + 1):
        p = 2 * i + 1
        if sieve[i]:
            start = (p * p) // 2
            sieve[start::p] = b'\x00' * ((size - 1 - start) // p + 1)
    yield 2
    for i in range(1, size):
        if sieve[i]:
            yield 2 * i + 1


def oddpart(n):
    while n % 2 == 0:
        n //= 2
    return n


def tau(n):
    assert n >= 1
    out = 1
    d = 2
    while d * d <= n:
        if n % d == 0:
            exponent = 0
            while n % d == 0:
                exponent += 1
                n //= d
            out *= exponent + 1
        d = 3 if d == 2 else d + 2
    if n > 1:
        out *= 2
    return out


def small_prime_distribution():
    """Return lower fixed-point probabilities for odd parts of e_p+1."""
    states = {1: Q}
    for p in primes_upto(SMALL):
        power = p
        count = 0
        while power < EXPONENT_CUTOFF:
            power *= p
            count += 1
        outcomes = [(oddpart(e + 1), p ** (e + 1)) for e in range(count)]
        updated = defaultdict(int)
        for v, q in states.items():
            for factor, denominator in outcomes:
                weight = (q * (p - 1)) // denominator
                if weight:
                    updated[v * factor] += weight
        states = {v: q for v, q in updated.items() if q >= PRUNE}
    assert 0 < sum(states.values()) <= Q
    return states


def large_prime_distribution():
    """Bounded Bernoulli generating polynomial for p in (SMALL,LIMIT]."""
    coeff = [Q] + [0] * DEGREE
    prime_count = 0
    for p in primes_upto(LIMIT):
        if p <= SMALL:
            continue
        prime_count += 1
        den = p * p * p
        numerator = p - 1
        updated = [0] * (DEGREE + 1)
        for k, q in enumerate(coeff):
            updated[k] += (q * (den - numerator)) // den
            if k < DEGREE:
                updated[k + 1] += (q * numerator) // den
        coeff = updated
    assert 0 < sum(coeff) <= Q
    return coeff, prime_count


def interval():
    small = small_prime_distribution()
    large, count = large_prime_distribution()
    total_rep = 0
    contribution = 0
    ceiling_contribution = 0
    for v, q in small.items():
        for k, r in enumerate(large):
            weight = (q * r) // Q
            total_rep += weight
            divisor = tau(v * (3 ** k))
            contribution += weight // divisor
            ceiling_contribution += (weight + divisor - 1) // divisor
    assert 0 < contribution <= ceiling_contribution <= total_rep <= Q
    # For p>SMALL, replacing oddpart(e_p+1) by 3 if e_p=2,
    # by 1 otherwise, can only increase 1/tau(V).
    # The two models differ only if some SMALL<p<=LIMIT has e_p>=4,
    # or a p>LIMIT has e_p>=2. The union bound is below:
    delta = Fraction(1, 3 * SMALL ** 3) + Fraction(1, LIMIT)
    low = Fraction(contribution, Q) - delta
    high = Fraction(ceiling_contribution + Q - total_rep, Q)
    assert 0 < low < high < 1
    return low, high, contribution, ceiling_contribution, total_rep, len(small), count


def exact_tiny_check():
    """Independent rational check of finite exponent product probabilities."""
    ps = (2, 3, 5)
    Es = (5, 3, 2)
    enumerated = {}
    for es in product(*(range(e + 1) for e in Es)):
        v = 1
        mass = Fraction(1)
        for p, e in zip(ps, es):
            v *= oddpart(e + 1)
            mass *= Fraction(p - 1, p ** (e + 1))
        enumerated[v] = enumerated.get(v, Fraction(0)) + mass
    # An independent convolution via exact rational arithmetic.
    states = {1: Fraction(1)}
    for p, E in zip(ps, Es):
        updated = defaultdict(Fraction)
        for v, q in states.items():
            for e in range(E + 1):
                updated[v * oddpart(e + 1)] += q * Fraction(p - 1, p ** (e + 1))
        states = dict(updated)
    assert states == enumerated
    assert sum(states.values()) == Fraction(1, 1) - Fraction(1, 2 ** 6) - Fraction(1, 3 ** 4) - Fraction(1, 5 ** 3) + Fraction(1, 2 ** 6 * 3 ** 4) + Fraction(1, 2 ** 6 * 5 ** 3) + Fraction(1, 3 ** 4 * 5 ** 3) - Fraction(1, 2 ** 6 * 3 ** 4 * 5 ** 3)
    return len(states)


def main():
    sanity_states = exact_tiny_check()
    lo, hi, numerator, ceil_numerator, represented, state_count, prime_count = interval()
    # Claim a strict rational enclosure, not a rounded floating-point claim.
    assert lo > Fraction(83670132, 100000000)
    assert hi < Fraction(83670134, 100000000)
    scale = 10 ** 13
    lower_floor = (lo.numerator * scale) // lo.denominator
    upper_ceil = -((-hi.numerator * scale) // hi.denominator)
    assert lo > Fraction(lower_floor, scale)
    assert hi < Fraction(upper_ceil, scale)
    print('CERTIFIED_LOWER_FLOOR_13', lower_floor)
    print('CERTIFIED_UPPER_CEIL_13', upper_ceil)
    print('CONTRIBUTION', numerator)
    print('CEILING_CONTRIBUTION', ceil_numerator)
    print('REPRESENTED_MASS', represented)
    print('SMALL_STATES', state_count)
    print('LARGE_PRIMES', prime_count)
    print('SANITY_RATIONAL_STATES', sanity_states)
    print('VERIFY_OK rational_tiny=PASS exact_integer_interval=PASS prime_tail=PASS')


if __name__ == '__main__':
    main()
