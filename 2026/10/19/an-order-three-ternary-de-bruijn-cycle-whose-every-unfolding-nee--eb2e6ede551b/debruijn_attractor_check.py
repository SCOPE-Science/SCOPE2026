#!/usr/bin/env python3
"""Verify an order-3 de Bruijn word whose 27 unfoldings require ten attractor positions.

The mathematical lower bound uses unique length-three factors and a covering
partition; this script independently checks all length-one through length-29
factors for each displayed ten-position witness.
"""
from collections import Counter, defaultdict

CYCLE = "000110120102202002122211121"
ALPHABET = "012"
N = 27
ORDER = 3


def factors(word, length):
    return {word[i:i + length] for i in range(len(word) - length + 1)}


def coverage(word, selected, max_length=None):
    """Return precise (distinct) missing substrings for every requested length."""
    if max_length is None:
        max_length = len(word)
    covered = set()
    all_factors = set()
    for length in range(1, max_length + 1):
        for i in range(len(word) - length + 1):
            substring = word[i:i + length]
            all_factors.add(substring)
            if any(i <= position < i + length for position in selected):
                covered.add(substring)
    return all_factors - covered


def main():
    assert len(CYCLE) == N
    assert set(CYCLE) == set(ALPHABET)
    cyclic_tri = ["".join(CYCLE[(i + j) % N] for j in range(ORDER))
                  for i in range(N)]
    assert len(set(cyclic_tri)) == len(ALPHABET) ** ORDER == N
    assert set(cyclic_tri) == {a + b + c for a in ALPHABET
                              for b in ALPHABET for c in ALPHABET}

    starts = defaultdict(list)
    for i in range(N):
        starts[CYCLE[i] + CYCLE[(i + 1) % N]].append(i)
    assert len(starts) == len(ALPHABET) ** 2
    assert all(len(v) == len(ALPHABET) for v in starts.values())
    EXPECTED = {0: ("02", (10, 13, 16)),
                1: ("01", (2, 5, 8)),
                2: ("12", (6, 18, 24))}
    for residue in range(ORDER):
        uncovered_pairs = []
        for pair, positions in starts.items():
            if all(i % ORDER != residue and (i + 1) % ORDER != residue
                   for i in positions):
                uncovered_pairs.append(pair)
        assert uncovered_pairs == [EXPECTED[residue][0]], (residue, uncovered_pairs)
        assert tuple(starts[EXPECTED[residue][0]]) == EXPECTED[residue][1]
        assert {CYCLE[i] for i in range(residue, N, ORDER)} == set(ALPHABET)

    unique_ten_sets = set()
    profiles = Counter()
    for cut in range(N):
        rot = CYCLE[cut:] + CYCLE[:cut]
        unfolded = rot + rot[:ORDER - 1]
        assert len(unfolded) == N + ORDER - 1 == 29
        base = set(range(ORDER - 1, N, ORDER))  # zero-based {2,5,...,26}
        assert len(base) == N // ORDER == 9
        assert len(factors(unfolded, ORDER)) == N
        short_missing = coverage(unfolded, base, ORDER)
        assert len(short_missing) == 1 and len(next(iter(short_missing))) == 2, (
            cut, short_missing)
        missing_pair = next(iter(short_missing))
        assert missing_pair == EXPECTED[(cut + ORDER - 1) % ORDER][0], (
            cut, missing_pair)
        assert short_missing == coverage(unfolded, base), (cut, short_missing)
        candidates = [i for i in range(len(unfolded))
                      if i not in base and any(
                          unfolded[j:j + 2] == missing_pair and j <= i <= j + 1
                          for j in range(len(unfolded) - 1))]
        assert candidates, cut
        chosen = min(candidates)
        selected = base | {chosen}
        assert len(selected) == 10
        assert not coverage(unfolded, selected), (cut, chosen)
        profiles[missing_pair] += 1
        unique_ten_sets.add((cut, chosen + 1))
    assert profiles == {"01": 9, "02": 9, "12": 9}, profiles
    assert len(unique_ten_sets) == 27
    print("PASS deBruijn=27_distinct_trigrams all_27_cuts="
          "gamma_exactly_10 shortest_missing_pairs=01:9,02:9,12:9")
    for residue in range(ORDER):
        label, positions = EXPECTED[residue]
        print(f"residue={residue} omitted_pair={label} "
              f"cyclic_zero_based_starts={positions}")


if __name__ == "__main__":
    main()
