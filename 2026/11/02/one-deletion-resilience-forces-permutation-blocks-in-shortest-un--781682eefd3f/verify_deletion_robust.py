#!/usr/bin/env python3
"""Exhaustive small-case check for one-erasure universal words.

Tests actual subsequence embeddings after each possible one-position deletion,
without using the occurrence-order proof in RESULT.md.
"""
from itertools import product
from math import factorial


def contains_subsequence(word, pattern):
    cursor = 0
    for symbol in word:
        if symbol == pattern[cursor]:
            cursor += 1
            if cursor == len(pattern):
                return True
    return False


def all_multiset_words(q, copies):
    remaining = [copies] * q
    word = [0] * (q * copies)

    def generate(i):
        if i == len(word):
            yield tuple(word)
            return
        for symbol in range(q):
            if remaining[symbol]:
                remaining[symbol] -= 1
                word[i] = symbol
                yield from generate(i + 1)
                remaining[symbol] += 1
    yield from generate(0)


def check_case(q, k):
    n = q * (k + 1)
    patterns = list(product(range(q), repeat=k))
    candidates = 0
    resilient = 0
    qualifying_blocks = 0
    exceptions = []
    for word in all_multiset_words(q, k + 1):
        candidates += 1
        blocks = all(len(set(word[b:b + q])) == q for b in range(0, n, q))
        if blocks:
            qualifying_blocks += 1
        valid = True
        for deleted_position in range(n):
            reduced = word[:deleted_position] + word[deleted_position + 1:]
            if not all(contains_subsequence(reduced, p) for p in patterns):
                valid = False
                break
        if valid:
            resilient += 1
        if valid != (blocks if k >= 2 else True) and len(exceptions) < 3:
            exceptions.append(''.join(map(str, word)))
    expected_total = factorial(n) // (factorial(k + 1) ** q)
    expected_resilient = (factorial(q) ** (k + 1) if k >= 2
                          else factorial(2 * q) // 2 ** q)
    assert candidates == expected_total, (q, k, candidates, expected_total)
    assert resilient == expected_resilient, (q, k, resilient, expected_resilient)
    assert not exceptions, (q, k, exceptions)
    if k >= 2:
        assert qualifying_blocks == resilient
    print(f'q={q} k={k} candidates={candidates} resilient={resilient} '
          f'permutation_block_words={qualifying_blocks}')
    return candidates


def main():
    cases = [(2, i) for i in range(1, 7)] + [(3, i) for i in range(1, 4)] + [(4, 1), (4, 2)]
    total = 0
    for q, k in cases:
        total += check_case(q, k)
    print(f'VERIFY_OK parameter_cases={len(cases)} multiset_words={total}')


if __name__ == '__main__':
    main()
