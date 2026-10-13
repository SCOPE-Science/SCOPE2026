#!/usr/bin/env python3
"""Independent finite checks of the parity-fiber construction for cubelike graphs."""
from itertools import combinations
from math import comb
from random import Random


def parity(x):
    return x.bit_count() & 1


def bit_projection(word, index_set):
    return sum(((word >> j) & 1) << k for k, j in enumerate(index_set))


def odd_fiber_witness(d, connection):
    """Return a minimal nonempty coordinate set with an odd upper containment tally."""
    for size in range(1, d + 1):
        for index_set in combinations(range(d), size):
            mask = sum(1 << j for j in index_set)
            if sum((s & mask) == mask for s in connection) & 1:
                return index_set
    raise AssertionError('no witness for nonempty connection set')


def check_case(d, functional_mask, connection):
    assert connection and all(s and parity(s & functional_mask) for s in connection)
    n = 1 << d
    degree = len(connection)
    if degree % 2:
        colors = [parity(x & functional_mask) for x in range(n)]
        expected = 2
    else:
        coords = odd_fiber_witness(d, connection)
        counts = [0] * (1 << len(coords))
        for s in connection:
            counts[bit_projection(s, coords)] += 1
        assert all(k & 1 for k in counts), (d, connection, coords, counts)
        colors = [(parity(x & functional_mask) << 1) +
                  (bit_projection(x, coords) == 0) for x in range(n)]
        expected = 4
        # Each pair of steps either cancels or occurs with its reversed order.
        for x in range(n):
            for y in range(n):
                two_step_count = sum((x ^ s ^ t) == y
                                     for s in connection for t in connection)
                assert two_step_count % 2 == 0
    assert len(set(colors)) == expected
    for x in range(n):
        neighbor_colors = [colors[x ^ s] for s in connection]
        assert all(colors[x] != c for c in neighbor_colors)
        assert all(k % 2 for c in set(neighbor_colors)
                   for k in [neighbor_colors.count(c)])
        if degree % 2 == 0:
            assert len(set(neighbor_colors)) == 2
    return 1


def main():
    exhaustive = 0
    random_samples = 0
    distance_samples = 0
    for d in range(1, 5):
        for functional_mask in range(1, 1 << d):
            allowable = [s for s in range(1, 1 << d)
                         if parity(s & functional_mask)]
            for selection in range(1, 1 << len(allowable)):
                connection = [s for j, s in enumerate(allowable)
                              if selection >> j & 1]
                exhaustive += check_case(d, functional_mask, connection)
    rng = Random(581302)
    for d in (5, 6):
        for _ in range(120):
            mask = rng.randrange(1, 1 << d)
            allowable = [s for s in range(1, 1 << d) if parity(s & mask)]
            connection = [s for s in allowable if rng.randrange(2)]
            if not connection:
                connection = [allowable[0]]
            random_samples += check_case(d, mask, connection)
    for d in range(1, 9):
        for r in range(1, d + 1, 2):
            connection = [s for s in range(1, 1 << d) if s.bit_count() == r]
            distance_samples += check_case(d, (1 << d) - 1, connection)
            assert len(connection) == comb(d, r)
    print('EXHAUSTIVE_ELL_S_CASES', exhaustive)
    print('DETERMINISTIC_RANDOM_CASES', random_samples)
    print('HAMMING_SHELL_CASES', distance_samples)
    print('ALL_CHECKS_PASSED')


if __name__ == '__main__':
    main()
