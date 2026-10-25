#!/usr/bin/env python3
"""Exact exhaustive certificate for degree-six generalized Ramanujan root locations.

No non-standard libraries, floating arithmetic, stored character tables, or
unverified primality assumptions are required.
"""
from fractions import Fraction
from math import gcd


def all_real_nonprincipal(n):
    """Generate each nontrivial homomorphism (Z/nZ)^* -> {1,-1} once."""
    units = [a for a in range(1, n) if gcd(a, n) == 1]
    squares = {a * a % n for a in units}
    def coset(a):
        return min((a * s) % n for s in squares)
    labels = {a: coset(a) for a in units}
    groups = sorted(set(labels.values()))
    coords = {coset(1): 0}
    rank = 0
    for q in groups:
        if q in coords:
            continue
        new = {labels[q * b % n]: bit | (1 << rank)
               for b, bit in tuple(coords.items())}
        assert not (set(new) & set(coords))
        coords.update(new)
        rank += 1
    assert len(coords) == len(groups) == 1 << rank
    for mask in range(1, 1 << rank):
        values = {a: 1 - 2 * ((coords[labels[a]] & mask).bit_count() % 2)
                  for a in units}
        yield mask, values


def odd_B135(n, values):
    sums = [sum(sign * a ** j for a, sign in values.items())
            for j in range(1, 6)]
    s1, s2, s3, s4, s5 = sums
    B1 = Fraction(s1, n)
    B3 = Fraction(s3, n) - Fraction(3 * s2, 2) + Fraction(n * s1, 2)
    B5 = (Fraction(s5, n) - Fraction(5 * s4, 2)
          + Fraction(5 * n * s3, 3) - Fraction(n ** 3 * s1, 6))
    return B1, B3, B5


def even_B24(n, values):
    sums = [sum(sign * a ** j for a, sign in values.items())
            for j in range(1, 5)]
    s1, s2, s3, s4 = sums
    return Fraction(s2, n) - s1, Fraction(s4, n) - 2 * s3 + n * s2


def verify():
    total = odd = even = nonzero_odd = degenerate_odd = 0
    closest = (Fraction(-1), None)
    failures = []
    for n in range(2, 164):
        units = [a for a in range(1, n) if gcd(a, n) == 1]
        for mask, ch in all_real_nonprincipal(n):
            total += 1
            assert sum(ch.values()) == 0
            # Checks that the generated sign map is genuinely multiplicative.
            for a in units:
                for b in units:
                    assert ch[a] * ch[b] == ch[a * b % n]
            if ch[n - 1] == 1:
                even += 1
                B2, B4 = even_B24(n, ch)
                assert B2 and B4  # S_6 is proportional to X^3 + X.
                continue
            odd += 1
            B1, B3, B5 = odd_B135(n, ch)
            assert B3
            if B1 == 0:
                degenerate_odd += 1
                # S_6 is a nonzero multiple of X^2, with no nonzero roots.
                continue
            nonzero_odd += 1
            assert B1 * B5 > 0
            ratio = Fraction(5 * B3 * B3, 3 * B1 * B5)
            if n <= 162 and ratio > closest[0]:
                closest = (ratio, (n, mask, B1, B3, B5))
            if ratio > 1:
                failures.append((n, mask, B1, B3, B5, ratio))
            # Verify that the character at each boundary example is Legendre.
            if n in (67, 163):
                assert all(ch[a] == (1 if pow(a, (n-1)//2, n) == 1 else -1)
                           for a in units)
    assert (total, even, odd, degenerate_odd, nonzero_odd) == (433, 173, 260, 85, 175)
    assert closest == (Fraction(378006, 390241),
                       (67, 1, Fraction(-1), Fraction(1506), Fraction(-3902410)))
    assert failures == [(163, 1, Fraction(-1), Fraction(13890),
                         Fraction(-213225610), Fraction(32155350, 21322561))]
    print('CERTIFICATE_OK moduli=2..163 nonprincipal_real=433 even=173 odd=260')
    print('ODD_CASES B1_zero=85 B1_nonzero=175')
    print('SHARP_PREFAIL_MAX modulus=67 ratio=378006/390241 unique_character')
    print('FIRST_FAILURE modulus=163 ratio=32155350/21322561 unique_character')
    print('EXACT_163_BERNOULLI B1=-1 B3=13890 B5=-213225610')

if __name__ == '__main__':
    verify()
