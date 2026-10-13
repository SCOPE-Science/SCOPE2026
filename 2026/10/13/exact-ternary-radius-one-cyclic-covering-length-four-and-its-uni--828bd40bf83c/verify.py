#!/usr/bin/env python3
"""Exact census of shortest ternary radius-one cyclic covering sequences.

Usage: python3 verify.py
Requires only the Python standard library (Python 3.10+).
"""
from itertools import permutations, product

ALPHABET = (0, 1, 2)
N = 4
UNIVERSE = tuple(product(ALPHABET, repeat=N))
COMPLETE = (1 << 81) - 1

# B[x] is a bitset of all ternary 4-words at distance at most one from x.
BALL = {}
for x in UNIVERSE:
    mask = 0
    for idx, y in enumerate(UNIVERSE):
        if sum(a != b for a, b in zip(x, y)) <= 1:
            mask |= 1 << idx
    assert mask.bit_count() == 9
    BALL[x] = mask


def windows(s):
    m = len(s)
    return tuple(tuple(s[(i + j) % m] for j in range(N)) for i in range(m))


def coverage_mask(s):
    result = 0
    for w in windows(s):
        result |= BALL[w]
    return result


def sequences_of_length(m):
    # Explicit enumeration of all 3**m ordered words, not only necklaces.
    return product(ALPHABET, repeat=m)


def orbit(s, include_reversal=False):
    size = len(s)
    out = set()
    for pi in permutations(ALPHABET):
        renamed = tuple(pi[c] for c in s)
        directions = (renamed, renamed[::-1]) if include_reversal else (renamed,)
        for w in directions:
            for shift in range(size):
                out.add(w[shift:] + w[:shift])
    return out


def main():
    counts = {}
    maxima = {}
    winners = set()
    for m in (9, 10, 11, 12):
        successes = 0
        maximum = 0
        for s in sequences_of_length(m):
            covered = coverage_mask(s)
            maximum = max(maximum, covered.bit_count())
            if covered == COMPLETE:
                successes += 1
                if m == 12:
                    winners.add(s)
        counts[m] = successes
        maxima[m] = maximum
        print('length={} total={} covering={} max_covered={}'.format(
            m, 3 ** m, successes, maximum))

    assert counts == {9: 0, 10: 0, 11: 0, 12: 48}, counts
    assert maxima == {9: 69, 10: 76, 11: 76, 12: 81}, maxima
    assert len(winners) == 48

    a = tuple(map(int, '001022021121'))
    b = a[::-1]
    left = orbit(a)
    right = orbit(b)
    assert len(left) == len(right) == 24
    assert left.isdisjoint(right)
    assert left | right == winners
    assert orbit(a, include_reversal=True) == winners
    assert coverage_mask(a) == COMPLETE
    print('orbits_without_reversal=2, each_size=24')
    print('orbits_with_reversal=1, size=48')
    print('witness=001022021121')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
