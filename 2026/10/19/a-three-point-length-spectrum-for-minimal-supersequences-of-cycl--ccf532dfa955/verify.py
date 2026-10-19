#!/usr/bin/env python3
"""Finite, exact cross-checks for minimal common supersequences of a rotated permutation.

Use: python3 verify.py
This code does not prove the assertions for untested values of n.
"""
from collections import Counter
from functools import lru_cache
from itertools import product


def embeds(pattern, word):
    t = 0
    for a in word:
        if t < len(pattern) and a == pattern[t]:
            t += 1
    return t == len(pattern)


def minimal(word, a, b):
    return embeds(a, word) and embeds(b, word) and all(
        not (embeds(a, word[:i] + word[i+1:]) and
             embeds(b, word[:i] + word[i+1:]))
        for i in range(len(word))
    )


def all_alignment_words(a, b):
    """Every minimal output is the union of two subsequence embeddings.

    The three recursive moves select a letter from A, from B, or their
    common next letter.  Deduplication is literal (not hash approximation).
    """
    @lru_cache(None)
    def go(i, j):
        if i == len(a) and j == len(b):
            return frozenset(((),))
        ans = set()
        if i < len(a):
            ans.update((a[i],) + z for z in go(i + 1, j))
        if j < len(b):
            ans.update((b[j],) + z for z in go(i, j + 1))
        if i < len(a) and j < len(b) and a[i] == b[j]:
            ans.update((a[i],) + z for z in go(i + 1, j + 1))
        return frozenset(ans)
    return go(0, 0)


def full_length_witness(n):
    w = [1, 0]
    for i in range(2, n):
        w.extend((i, i - 1))
    w.extend((0, n - 1))
    return tuple(w)


def main():
    assert not embeds((0,1), (1,0))
    summary = {}
    for n in range(2, 9):
        a = tuple(range(n))
        b = tuple(range(1, n)) + (0,)
        family = {w for w in all_alignment_words(a, b) if minimal(w, a, b)}
        lengths = dict(sorted(Counter(map(len, family)).items()))
        if n == 2:
            assert lengths == {3: 2}
        else:
            expected_small = {a + (0,), b + a[1:]}
            small = {w for w in family if len(w) < 2*n}
            assert small == expected_small, (n, small, expected_small)
            assert lengths[n + 1] == 1
            assert lengths[2*n - 1] == 1
            assert lengths[2*n] >= 1
            assert set(lengths) == {n + 1, 2*n - 1, 2*n}
            assert full_length_witness(n) in family
        summary[n] = lengths
        print(f"n={n}: {lengths}")
    # An unrelated enumeration traverses every alphabet word, not only alignments.
    for n in range(2, 5):
        a = tuple(range(n)); b = tuple(range(1, n)) + (0,)
        by_alignment = {w for w in all_alignment_words(a, b) if minimal(w, a, b)}
        by_bruteforce = {w for length in range(n, 2*n + 1)
                         for w in product(range(n), repeat=length)
                         if minimal(w, a, b)}
        assert by_alignment == by_bruteforce, n
        print(f"full independent alphabet enumeration n={n}: {len(by_bruteforce)} words, match")
    print('FINITE_CHECKS_OK; proof of all n is separate')


if __name__ == '__main__':
    main()
