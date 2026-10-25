#!/usr/bin/env python3
"""Standalone checks for longest Lyndon subsequences of four-run binary words.

Python 3 standard library only. This program checks finite cases; infinite
claims are proved mathematically in RESULT.md, not by this computation.
"""
from collections import Counter
from itertools import product
from math import comb


def is_lyndon(s):
    return bool(s) and all(s < s[i:] for i in range(1, len(s)))


def independent_length(a, b, c, d):
    """Enumerate every distinct subsequence; do not use run formulas."""
    w = '0' * a + '1' * b + '0' * c + '1' * d
    subsequences = {''}
    for char in w:
        additions = {s + char for s in subsequences}
        subsequences.update(additions)
    return max(map(len, (s for s in subsequences if is_lyndon(s))))


def proposed_deficiency(a, b, c, d):
    return min(b, max(0, c - a + int(b >= d)))


def coefficient_first(m):
    if m < 0:
        return 0
    return sum(comb(m - 2 * j + 2, 2) for j in range(m // 2 + 1))


def coefficient_second(m):
    if m < 0:
        return 0
    return sum(j + 1 for j in range(m // 2 + 1))


def predicted_tail(n, k):
    return coefficient_first(n - 2 * k - 2) - coefficient_second(n - 3 * k - 2)


def compositions_four(n):
    for a in range(1, n-2):
        for b in range(1, n-a-1):
            for c in range(1, n-a-b):
                yield a, b, c, n-a-b-c


def main():
    count = 0
    for a, b, c, d in product(range(1, 6), repeat=4):
        observed = independent_length(a, b, c, d)
        expected = a + b + c + d - proposed_deficiency(a, b, c, d)
        assert observed == expected, (a, b, c, d, observed, expected)
        count += 1

    enumerated = 0
    for n in range(4, 41):
        hist = Counter(proposed_deficiency(*x) for x in compositions_four(n))
        assert sum(hist.values()) == comb(n - 1, 3)
        for k in range(1, n+1):
            observed = sum(m for j, m in hist.items() if j >= k)
            expected = predicted_tail(n, k)
            assert observed == expected, (n, k, observed, expected)
        max_loss = max(hist)
        assert max_loss == (n-2)//2
        assert min(hist) == (1 if n == 4 else 0)
        enumerated += comb(n - 1, 3)

    print('VERIFY_OK direct_subsequence_sets=%d complete_compositions=%d lengths=4..40 tail_distributions=true sharp_extrema=true' % (count, enumerated))


if __name__ == '__main__':
    main()
