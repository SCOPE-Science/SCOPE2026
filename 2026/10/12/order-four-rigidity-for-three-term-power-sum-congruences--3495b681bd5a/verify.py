#!/usr/bin/env python3
"""Finite regression checks for three-term sums of fourth-order units."""
from collections import Counter
from itertools import combinations_with_replacement
from math import gcd


def minimum_at_most_three(orbit, modulus):
    for length in (1, 2, 3):
        if any(sum(v) % modulus == 0 for v in
               combinations_with_replacement(orbit, length)):
            return length
    return None


def run(limit=3000):
    counts = Counter()
    exceptional = []
    for modulus in range(2, limit + 1):
        for residue in range(1, modulus):
            if gcd(modulus, residue) != 1:
                continue
            if pow(residue, 4, modulus) != 1 or pow(residue, 2, modulus) == 1:
                continue
            orbit = [pow(residue, j, modulus) for j in range(4)]
            observed = minimum_at_most_three(orbit, modulus)
            expected = (2 if pow(residue, 2, modulus) == modulus - 1 else
                        3 if modulus == 15 and residue in (7, 13) else None)
            assert observed == expected, (modulus, residue, observed, expected)
            counts[observed] += 1
            if observed == 3:
                exceptional.append((modulus, residue))

    assert exceptional == [(15, 7), (15, 13)]
    assert minimum_at_most_three([1, 7, 4, 13], 15) == 3
    assert minimum_at_most_three([1, 2, 4, 8], 15) is None
    assert all(not any(sum(v) % 30 == 0 for v in
                       combinations_with_replacement([1, 7, 19, 13], length))
               for length in range(1, 6))
    assert any(sum(v) % 30 == 0 for v in
               combinations_with_replacement([1, 7, 19, 13], 6))
    for q in range(2, 50):
        assert (q * q + 2) * (q * q - 2) - (q**4 - 1) == -3
        assert ((2 * q)**4 - 1) - 16 * (q**4 - 1) == 15
        assert (q**4 - 1) - q * (q**3 - 1) == q - 1
    print('VERIFY_OK')
    print('modulus_limit=', limit)
    print('order_four_pairs=', sum(counts.values()))
    print('minimum_length_2=', counts[2])
    print('minimum_length_3=', counts[3])
    print('no_zero_sum_of_length_at_most_3=', counts[None])
    print('unique_length_3_classes=', exceptional)
    print('boundary_order_four_length_6_case=PASS')
    print('finite_regression_only=True')


if __name__ == '__main__':
    run()
