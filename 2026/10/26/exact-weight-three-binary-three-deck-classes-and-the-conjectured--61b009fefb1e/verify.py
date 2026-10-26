#!/usr/bin/env python3
"""Reproduce the exact fixed-weight-three, three-deck collision classification.

Uses only the Python standard library. Run: python3 verify.py
"""
from collections import defaultdict
from itertools import combinations
from math import comb

PATTERNS = tuple(format(v, '03b') for v in range(8))


def full_deck_by_positions(n, ones):
    """Directly select all length-three subsequence index triples."""
    s = bytearray(n)
    for p in ones:
        s[p] = 1
    hist = [0] * 8
    for i, j, k in combinations(range(n), 3):
        hist[4 * s[i] + 2 * s[j] + s[k]] += 1
    return tuple(hist)


def full_deck_by_dp(n, ones):
    """Independent streaming subsequence recursion for every binary pattern."""
    ones = set(ones)
    ans = []
    for pat in PATTERNS:
        dp = [1, 0, 0, 0]
        for i in range(n):
            c = '1' if i in ones else '0'
            for j in (2, 1, 0):
                if pat[j] == c:
                    dp[j + 1] += dp[j]
        ans.append(dp[3])
    return tuple(ans)


def partner(positions):
    a, b, c = positions
    gap1, gap2 = b - a, c - b
    if (gap1 - gap2) % 3 != 0 or gap1 == gap2:
        return None
    t = (gap1 - gap2) // 3
    return a + t, b - 2 * t, c + t


def predicted_pairs(n):
    return sum(max(0, n - 2 * y - 4 * t)
               for t in range(1, (n + 3) // 4 + 1)
               for y in range(1, (n + 1) // 2 + 1))


def coefficient_by_convolution(n):
    """Independent direct series extraction from the proposed rational product."""
    if n < 7:
        return 0
    # z^7/(1-z)^2/(1-z^2)/(1-z^4)
    out = 0
    for a in range(n - 6):
        for b in range((n - 7 - a) // 2 + 1):
            rem = n - 7 - a - 2 * b
            if rem >= 0 and rem % 4 == 0:
                out += a + 1
    return out


def main():
    direct_comparisons = 0
    total_words = 0
    paired_counts = []
    for n in range(3, 37):
        groups = defaultdict(list)
        for ones in combinations(range(n), 3):
            observed = full_deck_by_dp(n, ones)
            if n <= 12:
                assert observed == full_deck_by_positions(n, ones)
                direct_comparisons += 1
            groups[observed].append(ones)
        total_words += comb(n, 3)
        observed_pair_count = 0
        for group in groups.values():
            assert len(group) <= 2, (n, group)
            if len(group) == 2:
                observed_pair_count += 1
                left, right = group
                assert partner(left) == right, (n, group)
                assert partner(right) == left, (n, group)
        expected = predicted_pairs(n)
        assert observed_pair_count == expected == coefficient_by_convolution(n)
        assert len(groups) == comb(n, 3) - expected
        paired_counts.append((n, observed_pair_count))
    assert paired_counts[4] == (7, 1)
    assert paired_counts[0] == (3, 0)
    assert paired_counts[-1] == (36, predicted_pairs(36))
    for n in range(37, 141):
        assert predicted_pairs(n) == coefficient_by_convolution(n)
    print('THREE_DECK_WEIGHT3_PASS lengths=3..36'
          f' direct_deck_comparisons={direct_comparisons}'
          f' enumerated_words={total_words}'
          ' series_coefficients=0..140'
          ' all_classes_at_most_two=True'
          ' first_collision_length=7')


if __name__ == '__main__':
    main()
