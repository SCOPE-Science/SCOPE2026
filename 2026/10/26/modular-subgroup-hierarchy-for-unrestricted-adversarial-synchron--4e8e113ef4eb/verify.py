#!/usr/bin/env python3
"""Exact finite checks for a cyclic two-letter synchronization game.

Run: python3 verify.py
The first implementation uses modular difference subgroups. The second
builds a complete perfect-information game on all nonempty state subsets,
with Bob's possible replies represented by transitive closures.
"""
from collections import Counter
from itertools import product


def subgroup_chain(mapping):
    n = len(mapping)
    subgroup = frozenset((0,))
    trace = [len(subgroup)]
    while True:
        next_group = frozenset(
            d for d in range(n)
            if all((mapping[(x + d) % n] - mapping[x]) % n in subgroup
                   for x in range(n))
        )
        if next_group == subgroup:
            return tuple(trace), len(subgroup) == n
        assert subgroup < next_group
        subgroup = next_group
        trace.append(len(subgroup))


def exhaustive_game(mapping):
    n = len(mapping)
    size = 1 << n
    letters = (tuple((i + 1) % n for i in range(n)), mapping)
    successor = [[0] * size for _ in range(2)]
    for symbol in range(2):
        for subset in range(1, size):
            low = subset & -subset
            state = low.bit_length() - 1
            successor[symbol][subset] = (
                successor[symbol][subset ^ low] | (1 << letters[symbol][state])
            )
    # Ordinary reachability transitive closure for every Bob starting position.
    # Every bit of closure[s] corresponds to a complete nonempty subset.
    closure = [1 << s for s in range(size)]
    while True:
        new = [
            closure[s] | closure[successor[0][s]] | closure[successor[1][s]]
            for s in range(size)
        ]
        if new == closure:
            break
        closure = new
    win = sum(1 << s for s in range(1, size) if s.bit_count() == 1)
    while True:
        new = win
        for s in range(1, size):
            if (win >> s) & 1:
                continue
            if any(closure[successor[c][s]] & ~win == 0 for c in range(2)):
                new |= 1 << s
        if new == win:
            return bool((win >> (size - 1)) & 1)
        win = new


def test_all():
    expected = {2: 2, 3: 3, 4: 8, 5: 5, 6: 36}
    for n, target in expected.items():
        count = 0
        hist = Counter()
        for raw in product(range(n), repeat=n):
            trace, arithmetic_win = subgroup_chain(raw)
            game_win = exhaustive_game(raw)
            assert arithmetic_win == game_win, (n, raw, trace, arithmetic_win, game_win)
            hist[trace] += 1
            count += arithmetic_win
        assert count == target, (n, count, target)
        print(f"n={n} maps={n**n} omega_winners={count} traces={dict(sorted(hist.items()))}")
    # Multi-stage composite example, not captured by a single period/image coset.
    sample = (0, 2, 4, 6, 0, 2, 4, 6)
    trace, result = subgroup_chain(sample)
    assert result and trace == (1, 2, 4, 8), (trace, result)
    assert exhaustive_game(sample)
    print("VERIFY_OK")


if __name__ == '__main__':
    test_all()
