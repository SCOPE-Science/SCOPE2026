#!/usr/bin/env python3
"""Exact certificate for transient depths in random 3-by-3 zero-sum games.

Two independent counting routes: all 9! rank matrices and all 3^6 possible
row-minimum/column-maximum maps weighted by nine-element poset extensions.
Only the Python standard library is required. No random sampling is used.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import product, permutations
from math import factorial


def successor_from_maps(row_min, col_max):
    n = len(row_min)
    return tuple(n + x for x in row_min) + tuple(col_max)


def maps_from_ranks(ranks, n):
    row_min = tuple(min(range(n), key=lambda j: ranks[n * i + j]) for i in range(n))
    col_max = tuple(max(range(n), key=lambda i: ranks[n * i + j]) for j in range(n))
    return row_min, col_max


def recurrent_data(successor):
    """Return lengths of all cycles, distances of vertices to first cycle."""
    n2 = len(successor)
    cycle_lengths = []
    seen = set()
    for root in range(n2):
        # Detect cycles of a functional graph without assuming injectivity.
        if root in seen:
            continue
        positions, path = {}, []
        v = root
        while v not in positions and v not in seen:
            positions[v] = len(path)
            path.append(v)
            v = successor[v]
        if v in positions:
            cycle_lengths.append(len(path) - positions[v])
        seen.update(path)
    distance = []
    for root in range(n2):
        positions, path = {}, []
        v = root
        while v not in positions:
            positions[v] = len(path)
            path.append(v)
            v = successor[v]
        distance.append(positions[v])
    return tuple(sorted(cycle_lengths)), tuple(distance)


def constraints_for_maps(n, row_min, col_max):
    pred = [0] * (n * n)
    for i, j0 in enumerate(row_min):
        for j in range(n):
            if j != j0:
                pred[i * n + j] |= 1 << (i * n + j0)
    for j, i0 in enumerate(col_max):
        for i in range(n):
            if i != i0:
                pred[i0 * n + j] |= 1 << (i * n + j)
    return tuple(pred)


def number_of_linear_extensions(pred):
    """All permutations satisfying the row-minimum and column-maximum inequalities."""
    count_cells = len(pred)
    full = (1 << count_cells) - 1

    @lru_cache(maxsize=None)
    def extend(mask):
        if mask == full:
            return 1
        total = 0
        for x in range(count_cells):
            bit = 1 << x
            if mask & bit == 0 and pred[x] & mask == pred[x]:
                total += extend(mask | bit)
        return total

    return extend(0)


def census_from_maps(n=3):
    joint = Counter()
    depths = Counter()
    rank_matrices = 0
    feasible_maps = 0
    for row_min in product(range(n), repeat=n):
        for col_max in product(range(n), repeat=n):
            weight = number_of_linear_extensions(constraints_for_maps(n, row_min, col_max))
            if not weight:
                continue
            feasible_maps += 1
            cycles, dist = recurrent_data(successor_from_maps(row_min, col_max))
            joint[(cycles, max(dist))] += weight
            for depth in dist:
                depths[depth] += weight
            rank_matrices += weight
    return joint, depths, rank_matrices, feasible_maps


def census_from_permutations(n=3):
    joint = Counter()
    depths = Counter()
    for ranks in permutations(range(n * n)):
        row_min, col_max = maps_from_ranks(ranks, n)
        cycles, dist = recurrent_data(successor_from_maps(row_min, col_max))
        joint[(cycles, max(dist))] += 1
        depths.update(dist)
    return joint, depths


def main():
    expected_joint = {
        ((2,), 1): 9576, ((2,), 2): 69264,
        ((2,), 3): 22464, ((2,), 4): 6912,
        ((4,), 1): 127872, ((4,), 2): 110592,
        ((6,), 0): 15552, ((2, 4), 0): 648,
    }
    expected_depths = {0:1267488,1:625536,2:247968,3:29376,4:6912}
    joint1, depth1, total, feasible = census_from_maps()
    joint2, depth2 = census_from_permutations()
    assert total == factorial(9)
    assert joint1 == joint2 == expected_joint, (joint1, joint2)
    assert depth1 == depth2 == expected_depths, (depth1, depth2)
    assert sum(depth1.values()) == 6 * factorial(9)

    # Probability law for the hitting time from a uniformly chosen strategy.
    probabilities = (Fraction(163,280), Fraction(181,630),
                     Fraction(41,360), Fraction(17,1260), Fraction(1,315))
    assert sum(probabilities) == 1
    for t, p in enumerate(probabilities):
        assert Fraction(depth1[t], 6 * factorial(9)) == p
    assert sum(t*probabilities[t] for t in range(5)) == Fraction(179,315)

    # A length-four path on all four nonrecurrent vertices of the digraph.
    chain_row_min = (0,1,2)
    chain_col_max = (0,2,0)
    assert number_of_linear_extensions(constraints_for_maps(3,chain_row_min,chain_col_max)) == 96
    assert recurrent_data(successor_from_maps(chain_row_min,chain_col_max))[1] == (0,4,2,0,3,1)
    assert 9 * 2 * 2 * 2 * 96 == 6912   # saddle, start-side, permutations on both sides
    assert Fraction(6912, factorial(9)) == Fraction(2,105)
    assert Fraction(6912, 6 * factorial(9)) == Fraction(1,315)
    assert maps_from_ranks((4,5,7,1,0,6,3,8,2), 3) == (chain_row_min,chain_col_max)
    print('EXACT_VERIFY_OK: 3^6 row/column maps, all 9! rank orders,')
    print('  8 cycle-depth strata, five hitting-time probabilities, mean 179/315,')
    print('  and the sharp 4-step delay probability 2/105.')
    print('feasible row/column maps =',feasible)


if __name__ == '__main__':
    main()
