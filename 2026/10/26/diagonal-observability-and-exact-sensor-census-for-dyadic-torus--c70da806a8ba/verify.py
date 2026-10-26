#!/usr/bin/env python3
"""Finite consistency checks for diagonal observability of the north-east XOR rule."""
from itertools import combinations
from math import comb
from random import Random


def gf2_rank(vectors):
    pivots = {}
    for row in vectors:
        while row:
            lead = row.bit_length() - 1
            if lead in pivots:
                row ^= pivots[lead]
            else:
                pivots[lead] = row
                break
    return len(pivots)


def observation_rows(width, height, sensors):
    """Rows of the time-0,...,width-1 observation map over GF(2)."""
    rows = []
    for x, y in sensors:
        row = 1 << (x * height + y)
        for _ in range(width):
            rows.append(row)
            updated = 0
            for i in range(width):
                for j in range(height):
                    if row & (1 << (i * height + j)):
                        updated ^= 1 << (((i + 1) % width) * height + j)
                        updated ^= 1 << (i * height + (j + 1) % height)
            row = updated
        assert row == 0
    return rows


def prediction(width, height, sensors):
    return len({(x + y) % height for x, y in sensors}) == height


def expected_count(width, height, k):
    return sum(
        (-1) ** j * comb(height, j) * comb(width * (height - j), k)
        for j in range(height + 1) if width * (height - j) >= k
    )


def test_all_subsets(width, height):
    points = [(i, j) for i in range(width) for j in range(height)]
    actual_counts = [0] * (len(points) + 1)
    checked = 0
    for k in range(len(points) + 1):
        for sites in combinations(points, k):
            actual = gf2_rank(observation_rows(width, height, sites)) == width * height
            wanted = prediction(width, height, sites)
            assert actual == wanted, (width, height, sites)
            actual_counts[k] += actual
            checked += 1
        assert actual_counts[k] == expected_count(width, height, k)
    assert actual_counts[height] == width ** height
    return checked


def test_random(width, height, trials, rng):
    points = [(i, j) for i in range(width) for j in range(height)]
    for _ in range(trials):
        k = rng.randrange(len(points) + 1)
        sites = rng.sample(points, k)
        actual = gf2_rank(observation_rows(width, height, sites)) == width * height
        assert actual == prediction(width, height, sites), (width, height, sites)
        assert expected_count(width, height, k) >= 0


def main():
    counts = {}
    for dims in ((2, 2), (4, 2), (4, 4)):
        counts[f'{dims[0]}x{dims[1]}'] = test_all_subsets(*dims)
    rng = Random(20261020)
    cases = ((8, 2), (8, 4), (8, 8), (16, 2))
    for w, h in cases:
        test_random(w, h, 160, rng)
    print('VERIFY_OK exhaustive_subsets=' + str(counts)
          + ' random_observability_tests=' + str(160 * len(cases))
          + ' independent_GF2_rank=yes exact_count_formula=yes')

if __name__ == '__main__':
    main()
