#!/usr/bin/env python3
"""Exact finite checks for the two-one binary self-shuffle root distribution.

Python standard library only. Run: python3 verify.py
These checks complement, rather than replace, the all-integer proof.
"""
from collections import Counter
from functools import lru_cache
from math import comb


def predicted_roots(a, b, c):
    assert min(a, b, c) >= 0 and (a + b + c) % 2 == 0
    m = (a + b + c) // 2
    lower = max((a + 1) // 2, m - c)
    upper = min(a, m - (c + 1) // 2)
    return max(0, upper - lower + 1)


def is_interleaving_square(word, root):
    """Independent two-copy interleaving automaton; no gap formula used."""
    states = {(0, 0)}
    n = len(root)
    for letter in word:
        next_states = set()
        for i, j in states:
            if i < n and root[i] == letter:
                next_states.add((i + 1, j))
            if j < n and root[j] == letter:
                next_states.add((i, j + 1))
        states = next_states
        if not states:
            return False
    return (n, n) in states


def all_shuffles_of_root(root):
    """Independent constructive shuffle generator, with deduplication."""
    n = len(root)

    @lru_cache(None)
    def from_positions(i, j):
        if i == n and j == n:
            return frozenset([''])
        words = set()
        if i < n:
            words.update(root[i] + tail for tail in from_positions(i + 1, j))
        if j < n:
            words.update(root[j] + tail for tail in from_positions(i, j + 1))
        return frozenset(words)

    return from_positions(0, 0)


def nonzero_count(m):
    return 0 if m < 0 else (3 * m * m + 3 * m + 2) // 2


def exact_count(m, number_of_roots):
    t = number_of_roots
    return nonzero_count(m - 3 * (t - 1)) - nonzero_count(m - 3 * t)


def run():
    total_words = 0
    total_positive_words = 0
    for m in range(16):
        histogram = Counter()
        for a in range(2 * m + 1):
            for b in range(2 * m - a + 1):
                c = 2 * m - a - b
                word = '0' * a + '1' + '0' * b + '1' + '0' * c
                brute = sum(is_interleaving_square(word, '0' * q + '1' + '0' * (m - q))
                            for q in range(m + 1))
                assert brute == predicted_roots(a, b, c), (m, a, b, c, brute)
                histogram[brute] += 1
                assert (brute > 0) == (b <= m and b >= (a % 2) + (c % 2))
                if brute > 0:
                    total_positive_words += 1
        assert sum(histogram.values()) == comb(2 * m + 2, 2)
        assert sum(v for k, v in histogram.items() if k > 0) == nonzero_count(m)
        assert max(histogram) == m // 3 + 1
        for t in range(1, m // 3 + 3):
            assert histogram[t] == exact_count(m, t), (m, t)
        assert sum(t * v for t, v in histogram.items()) == comb(m + 3, 3)
        total_words += sum(histogram.values())

    generated_pairs = 0
    for m in range(10):
        outputs_to_roots = Counter()
        for q in range(m + 1):
            root = '0' * q + '1' + '0' * (m - q)
            outputs = all_shuffles_of_root(root)
            assert len(outputs) == (q + 1) * (m - q + 1)
            for word in outputs:
                outputs_to_roots[word] += 1
                generated_pairs += 1
        for a in range(2 * m + 1):
            for b in range(2 * m - a + 1):
                c = 2 * m - a - b
                word = '0' * a + '1' + '0' * b + '1' + '0' * c
                assert outputs_to_roots[word] == predicted_roots(a, b, c)

    for m in range(101):
        maximum = m // 3 + 1
        assert sum(exact_count(m, t) for t in range(1, maximum + 1)) == nonzero_count(m)
        assert sum(t * exact_count(m, t) for t in range(1, maximum + 1)) == comb(m + 3, 3)
        assert exact_count(m, maximum) == (1, 4, 10)[m % 3]
        if m >= 3:
            assert exact_count(m, 1) == 9 * (m - 1)

    print('PASS independent interleaving DP, m=0..15')
    print('PASS direct self-shuffle generation, m=0..9')
    print('PASS multiplicity, incidence, and extremal identities, m=0..100')
    print('Examined linear words:', total_words)
    print('Examined positive-output words:', total_positive_words)
    print('Explicit constructive root-output pairs:', generated_pairs)


if __name__ == '__main__':
    run()
