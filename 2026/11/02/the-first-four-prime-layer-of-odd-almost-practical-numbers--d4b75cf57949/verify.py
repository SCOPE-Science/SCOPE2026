#!/usr/bin/env python3
"""Exact finite checks for the first four-prime almost-practical exponent layers."""
from math import isqrt


def divisors(n):
    out = []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
    return sorted(out)


def bitset_sums(values):
    bits = 1
    for d in values:
        bits |= bits << d
    return bits


def boolean_sums(values):
    total = sum(values)
    reached = bytearray(total + 1)
    reached[0] = 1
    running = 0
    for d in values:
        for k in range(running, -1, -1):
            if reached[k]:
                reached[k + d] = 1
        running += d
    return reached


def almost_complete(values):
    total = sum(values)
    bits = bitset_sums(values)
    required = ((1 << (total - 2)) - 1) ^ 7  # exactly indices 3,...,total-3
    return (bits & required) == required


def is_prime(n):
    return n > 1 and all(n % d for d in range(2, isqrt(n) + 1))


def main():
    bases = (105, 315, 525, 735)
    bits = {}
    for b in bases:
        ds = divisors(b)
        bb = bitset_sums(ds)
        independent = boolean_sums(ds)
        assert len(independent) == sum(ds) + 1
        assert all(((bb >> j) & 1) == independent[j] for j in range(len(independent)))
        bits[b] = bb
    S = sum(divisors(315))
    assert S == 624
    holes = [x for x in range(S + 1) if not (bits[315] >> x) & 1]
    assert holes == [2, 307, 310, 311, 312, 313, 314, 317, 622]
    assert sum(divisors(105)) == 192
    for x in [2, 190, *range(88,105)]:
        assert not (bits[105] >> x) & 1
    for b in (525,735):
        assert not (bits[b] >> 14) & 1

    # Independent computational check of the complete two-block interval lemma.
    a315 = [j for j in range(625) if (bits[315] >> j) & 1]
    for t in range(1,105):
        represented = 0
        for b in a315:
            represented |= bits[315] << (t * b)
        required = ((1 << (624 * (t + 1) - 2)) - 1) ^ 7
        assert ((represented & required) == required) == (t <= 103)
    assert not (represented >> (309 * 104 + 622)) & 1

    for b,p,exponent,expected in [
        (105,11,1,False),(105,13,1,False),
        (315,11,1,True),(315,103,1,True),(315,107,1,False),
        (525,11,1,True),(525,13,1,True),(525,17,1,False),
        (735,11,1,True),(735,13,1,True),(735,17,1,False),
        (105,11,2,True),(105,13,2,False),(105,17,2,False)]:
        n = b * p**exponent
        ds = divisors(n)
        answer = almost_complete(ds)
        assert answer == expected, (b,p,exponent,answer)
        if expected:
            first = bitset_sums(ds)
            second = boolean_sums(ds)
            assert all(((first >> j) & 1) == second[j] for j in range(len(second)))

    # Independent full divisor-prefix certificate for the five exceptional bases.
    for n in (525*11, 525*13, 735*11, 735*13, 105*11**2):
        ds = divisors(n)
        assert ds[:3] == [1,3,5] and len(ds) == 24
        prefix = sum(ds[:3])
        for d in ds[3:]:
            slack = prefix - 2 - d
            assert slack >= 0 and slack != 2, (n,d,slack)
            prefix += d

    # Explicit obstructions for the three nontrivial exclusion patterns.
    assert not (bitset_sums(divisors(105*11)) >> (87*11+190)) & 1
    assert not (bitset_sums(divisors(105*13)) >> (87*13+190)) & 1
    assert not (bitset_sums(divisors(105*13**2)) >> 17389) & 1

    primes = [p for p in range(11,104) if is_prime(p)]
    assert len(primes) == 23 and primes[-1] == 103 and is_prime(107)
    solutions = sorted([315*p for p in primes] + [525*11,525*13,735*11,735*13,105*11**2])
    assert len(solutions) == 28 and len(set(solutions)) == 28
    assert solutions[0] == 3465 and solutions[-1] == 315*103
    assert all(almost_complete(divisors(n)) for n in solutions)
    print('VERIFY_OK bases=4 base_holes315=9 two_block_t=1..104 boundary=103 positives=28 min=3465 max=32445')
    print('PRIMES',','.join(map(str,primes)))
    print('SOLUTIONS',','.join(map(str,solutions)))


if __name__ == '__main__':
    main()
