#!/usr/bin/env python3
"""Check the two-heavy-layer reconstruction theorem by independent enumeration.

This is a finite consistency test, not a substitute for the general proof.
"""
from collections import Counter
from itertools import combinations


def observed(word):
    prefix = [0]
    for bit in word:
        prefix.append(prefix[-1] + bit)
    histogram = Counter()
    for left in range(len(word)):
        for right in range(left + 1, len(word) + 1):
            ones = prefix[right] - prefix[left]
            if ones in (2, 3):
                histogram[(ones, right - left)] += 1
    return tuple(sorted(histogram.items()))


def from_gaps(a, b, c, d):
    histogram = Counter()
    # Exactly two ones, in positions 1 and 2 or in positions 2 and 3.
    for left_extension in range(a + 1):
        for right_extension in range(c + 1):
            histogram[(2, b + 2 + left_extension + right_extension)] += 1
    for left_extension in range(b + 1):
        for right_extension in range(d + 1):
            histogram[(2, c + 2 + left_extension + right_extension)] += 1
    # Exactly three ones: all ones of the word.
    for left_extension in range(a + 1):
        for right_extension in range(d + 1):
            histogram[(3, b + c + 3 + left_extension + right_extension)] += 1
    return tuple(sorted(histogram.items()))


def word(gaps):
    a, b, c, d = gaps
    return (0,) * a + (1,) + (0,) * b + (1,) + (0,) * c + (1,) + (0,) * d


def full_spectrum(word):
    prefix = [0]
    for bit in word:
        prefix.append(prefix[-1] + bit)
    histogram = Counter()
    for left in range(len(word)):
        for right in range(left + 1, len(word) + 1):
            histogram[(prefix[right] - prefix[left], right - left)] += 1
    return tuple(sorted(histogram.items()))


def main():
    checked = 0
    for n in range(3, 33):
        fingerprints = {}
        for positions in combinations(range(n), 3):
            bits = tuple(int(i in positions) for i in range(n))
            a = positions[0]
            b = positions[1] - positions[0] - 1
            c = positions[2] - positions[1] - 1
            d = n - positions[2] - 1
            assert bits == word((a, b, c, d))
            fingerprint = observed(bits)
            assert fingerprint == from_gaps(a, b, c, d)
            previous = fingerprints.get(fingerprint)
            if previous is not None:
                assert bits == previous or bits == previous[::-1], (n, bits, previous)
            else:
                fingerprints[fingerprint] = bits
            checked += 1
    x = tuple(map(int, '01001101'))
    y = tuple(map(int, '01101001'))
    assert x != y and x != y[::-1]
    assert full_spectrum(x) == full_spectrum(y)
    # A 3-one example showing why the all-three-one layer alone does not suffice.
    u = tuple(map(int, '10110'))
    v = tuple(map(int, '11010'))
    p3 = lambda s: tuple((k, value) for k, value in observed(s) if k[0] == 3)
    assert p3(u) == p3(v) and u != v and u != v[::-1]
    assert observed(u) != observed(v)
    print(f'VERIFY_OK weight_three_two_heavy_layers distinct_words={checked} lengths_3_to_32 exact_gap_polynomials distinct_rotation_free_reversal_orbits sharp_weight_four_collision')


if __name__ == '__main__':
    main()
