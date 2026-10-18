#!/usr/bin/env python3
"""Exact checks for odd min-intersection families on {0,1,2}^n.

Usage: python3 verify.py
No external packages. This script is a finite certificate, not the proof of the
all-n upper bound or the disjoint-support extension.
"""
from itertools import product
from math import comb

BLOCK = [
    "000111", "001011", "002120", "011201", "101201",
    "111220", "112210", "121102", "211102", "221101",
]
EXPECTED = {1: (1, 1), 2: (2, 4), 3: (3, 13),
            4: (6, 40), 5: (7, 121)}


def canonical_vector(word):
    return tuple(int(s) for s in word)


def compatible(x, y):
    # First evaluation method: literal multiset meet sum.
    return sum(min(a, b) for a, b in zip(x, y)) % 2 == 0


def segment_mask(v):
    # Independent representation in a 2n-element ordinary set.
    mask = 0
    for i, value in enumerate(v):
        for level in range(value):
            mask |= 1 << (2 * i + level)
    return mask


def clique_census(n, first_forbidden_size):
    vectors = [v for v in product((0, 1, 2), repeat=n)
               if sum(v) % 2 == 1]
    masks = [segment_mask(v) for v in vectors]
    N = len(vectors)
    assert N == (3**n - 1) // 2
    for i, x in enumerate(vectors):
        assert masks[i].bit_count() % 2 == 1
        for j in range(i + 1, N):
            assert compatible(x, vectors[j]) == (
                (masks[i] & masks[j]).bit_count() % 2 == 0)
    # Larger indices only: every unordered clique is reached once.
    adjacency = [sum(1 << j for j in range(i + 1, N)
                     if compatible(vectors[i], vectors[j]))
                 for i in range(N)]
    counts = [0] * (first_forbidden_size + 1)
    witness = None
    def enumerate_extensions(depth, candidates, chosen):
        nonlocal witness
        counts[depth] += 1
        if depth == first_forbidden_size:
            return
        while candidates:
            low = candidates & -candidates
            j = low.bit_length() - 1
            candidates ^= low
            choice = chosen + (j,)
            if depth + 1 == first_forbidden_size - 1 and witness is None:
                witness = choice
            enumerate_extensions(depth + 1, candidates & adjacency[j], choice)
    enumerate_extensions(0, (1 << N) - 1, ())
    return N, counts, witness


def main():
    block = [canonical_vector(word) for word in BLOCK]
    assert len(block) == len(set(block)) == 10
    assert all(sum(v) % 2 == 1 for v in block)
    assert all(compatible(block[i], block[j])
               for i in range(10) for j in range(i + 1, 10))
    assert all(sum(v) % 2 == 1 for v in block)
    print("six_coordinate_block=10; pairs_checked=45; PASS")
    for n, (maximum, N_expected) in EXPECTED.items():
        N, counts, witness = clique_census(n, maximum + 1)
        assert N == N_expected, (n, N)
        assert counts[maximum] > 0, (n, counts)
        assert counts[maximum + 1] == 0, (n, counts)
        print(f"n={n}; odd_candidates={N}; clique_counts={counts}; max={maximum}; PASS")
    for n in range(1, 49):
        q, r = divmod(n, 6)
        words = []
        for block_id in range(q):
            for v in block:
                words.append((0,) * (6 * block_id) + v +
                             (0,) * (n - 6 * block_id - 6))
        for j in range(r):
            words.append((0,) * (6 * q + j) + (1,) +
                         (0,) * (r - j - 1))
        assert len(set(words)) == len(words) == 10 * q + r
        assert all(sum(v) % 2 == 1 for v in words)
        assert all(compatible(words[i], words[j]) for i in range(len(words))
                   for j in range(i + 1, len(words)))
    print("disjoint_support_examples_n=1..48; PASS")
    print("VERIFICATION_PASS")


if __name__ == '__main__':
    main()
