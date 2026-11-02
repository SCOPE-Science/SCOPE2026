#!/usr/bin/env python3
"""Exact finite checks for the critical additive Cantor-type sumset formulas.

This program verifies finite instances; the infinite conclusions require the
mathematical proof, not the enumerations performed here.
"""
from fractions import Fraction
from itertools import product
from collections import Counter
from math import comb


def base_valuation(n, base):
    r = 0
    while n % base == 0:
        n //= base
        r += 1
    return r


def eval_digits(m, weights, base):
    s = 0
    for w in weights:
        s += (m % base) * w
        m //= base
    assert m == 0
    return s


def digit_increments(weights, base):
    return [weights[j] - (base - 1) * sum(weights[:j])
            for j in range(len(weights))]


def test():
    configurations = 0
    gap_comparisons = 0
    completeness_checks = 0
    representation_checks = 0
    for base in range(2, 7):
        for alpha in [Fraction(11, 10), Fraction(3, 2), Fraction(7, 4), Fraction(19, 10)]:
            assert 1 < alpha < 2
            weights = [(alpha.numerator * base ** j) // alpha.denominator
                       for j in range(6)]
            increments = digit_increments(weights, base)
            assert all(d >= 1 for d in increments)
            for j in range(1, 6):
                digit = weights[j] - base * weights[j-1]
                assert 0 <= digit < base
                assert increments[j] == increments[j-1] + digit
            n = base ** 5
            f = [eval_digits(i, weights[:5], base) for i in range(n)]
            assert sorted(set(f)) == f
            for i in range(n-1):
                assert f[i+1] - f[i] == increments[base_valuation(i+1, base)]
                gap_comparisons += 1
            represented = sorted(sum(c * w for c, w in zip(coeffs, weights[:5]))
                                 for coeffs in product(range(base), repeat=5))
            assert represented == f
            for i, val in enumerate(f):
                assert 0 <= alpha * i - val < (base-1) * 5 + 1
            # Unaggregated ordered critical representations, tested independently.
            critical_order = base - 1
            short_c = [sum(bit * weight for bit, weight in zip(bits, weights[:3]))
                       for bits in product((0, 1), repeat=3)]
            fibers = Counter(map(sum, product(short_c, repeat=critical_order)))
            assert len(fibers) == base ** 3
            for target_index in range(base ** 3):
                digits = []
                value = target_index
                for _ in range(3):
                    digits.append(value % base)
                    value //= base
                weight = eval_digits(target_index, weights[:3], base)
                predicted = 1
                for digit in digits:
                    predicted *= comb(critical_order, digit)
                assert fibers[weight] == predicted
                representation_checks += 1
            assert sum(v * v for v in fibers.values()) == comb(2 * critical_order, critical_order) ** 3
            h = max(base, weights[1]-1)
            sums = {0}
            for w in weights[:4]:
                sums = {s + c * w for s in sums for c in range(h+1)}
            assert len(sums) == h * sum(weights[:4]) + 1
            assert min(sums) == 0 and max(sums) == h * sum(weights[:4])
            completeness_checks += 1
            assert h == max(base, (alpha.numerator * base) // alpha.denominator - 1)
            configurations += 1
    print(f"VERIFY_OK configurations={configurations} ",
          f"consecutive_gap_checks={gap_comparisons} ",
          f"complete_finite_prefix_checks={completeness_checks} ",
          f"ordered_representation_checks={representation_checks}", sep="")


if __name__ == '__main__':
    test()
