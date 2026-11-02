#!/usr/bin/env python3
"""Exhaustive, self-contained certificate for cyclic-rectangle VC dimension.

Each axis has coordinates 0,...,M-1 in cyclic order. A cyclic interval
may be empty, full, or nonempty consecutive (possibly wrapping).
Each rectangle is a product of one interval from each axis.

Only finite, complete, mathematically justified reductions are used.
"""
from itertools import combinations, permutations
from math import factorial, comb


def axis_traces(circumference, coordinates):
    """All possible intersections of a cyclic interval with an ordered sample."""
    k = len(coordinates)
    masks = {0, (1 << k) - 1}
    locations = [0] * circumference
    for i, c in enumerate(coordinates):
        assert 0 <= c < circumference
        locations[c] |= 1 << i
    for start in range(circumference):
        membership = 0
        for length in range(1, circumference):
            membership |= locations[(start + length - 1) % circumference]
            masks.add(membership)
    return masks


def trace_vector(points, m, n):
    """Bit j is set precisely when trace pattern j occurs for a rectangle."""
    k = len(points)
    x_traces = axis_traces(m, [x for x, y in points])
    y_traces = axis_traces(n, [y for x, y in points])
    present = 0
    for a in x_traces:
        for b in y_traces:
            present |= 1 << (a & b)
    return present


def shattered(points, m, n):
    k = len(points)
    assert len(set(points)) == k
    return trace_vector(points, m, n) == (1 << (1 << k)) - 1


def direct_brute_traces(points, m, n):
    """Independent construction: enumerate all actual rectangle vertex sets."""
    possible_x = [set(), set(range(m))]
    possible_y = [set(), set(range(n))]
    for L, lst in ((m, possible_x), (n, possible_y)):
        for start in range(L):
            for length in range(1, L):
                lst.append({(start + h) % L for h in range(length)})
    result = 0
    for ax in possible_x:
        for ay in possible_y:
            pattern = 0
            for i, (x, y) in enumerate(points):
                if x in ax and y in ay:
                    pattern |= 1 << i
            result |= 1 << pattern
    return result


def absence_certificate(m, n, k):
    """Translation invariance lets us fix one sample point at (0,0)."""
    ground = [(i, j) for i in range(m) for j in range(n) if (i, j) != (0, 0)]
    count = 0
    for rest in combinations(ground, k - 1):
        count += 1
        points = ((0, 0),) + rest
        assert not shattered(points, m, n), ('counterexample', m, n, k, points)
    assert count == comb(m * n - 1, k - 1)
    return count


# Explicit lower-bound shattered supports; 0-based cyclic coordinates.
WITNESSES = {
    (1, 1, 1): [(0, 0)],
    (1, 2, 2): [(0, 0), (0, 1)],
    (1, 3, 3): [(0, 0), (0, 1), (0, 2)],
    (2, 2, 2): [(0, 0), (0, 1)],
    (2, 3, 3): [(0, 0), (0, 1), (0, 2)],
    (2, 4, 4): [(0, 0), (0, 2), (1, 1), (1, 3)],
    (3, 3, 4): [(0, 0), (0, 1), (1, 2), (2, 2)],
    (4, 4, 5): [(0, 0), (0, 2), (1, 1), (2, 3), (3, 1)],
    (5, 6, 6): [(0, 0), (0, 2), (1, 1), (2, 3), (3, 4), (4, 5)],
}


def main():
    # Cross-check two implementations on every support of size <=4 in small grids.
    crosschecked = 0
    for m, n in [(1, 4), (2, 3), (3, 3), (3, 4)]:
        grid = [(i, j) for i in range(m) for j in range(n)]
        for k in range(1, min(4, len(grid)) + 1):
            for pts in combinations(grid, k):
                fast = trace_vector(pts, m, n)
                slow = direct_brute_traces(pts, m, n)
                assert fast == slow, ('independent check', m, n, pts)
                crosschecked += 1
    print('INDEPENDENT_RECTANGLE_TRACES_PASS', crosschecked)

    for (m, n, k), points in WITNESSES.items():
        assert shattered(points, m, n)
        assert direct_brute_traces(points, m, n) == (1 << (1 << k)) - 1
    print('EXPLICIT_LOWER_WITNESSES_PASS', len(WITNESSES))

    # These are all missing base cases after cyclic-order compression.
    upper_tests = [
        (1, 4, 4),
        (2, 2, 3), (2, 3, 4), (2, 5, 5),
        (3, 5, 5), (4, 6, 6), (5, 5, 6),
    ]
    all_checked = 0
    for m, n, k in upper_tests:
        count = absence_certificate(m, n, k)
        all_checked += count
        print('ABSENCE_PASS', m, n, k, count)

    # Tie-breaking lemma: every 7-point sample can be moved to one with
    # distinct x-coordinates and distinct y-coordinates without deleting traces.
    # Relabel x=0,...,6; the y-order is then one of all 7! permutations.
    count = 0
    for perm in permutations(range(7)):
        points = tuple((i, perm[i]) for i in range(7))
        assert not shattered(points, 7, 7), ('seven point witness', perm)
        count += 1
    assert count == factorial(7)
    print('SEVEN_POINT_ORDER_TYPES_PASS', count)
    print('TOTAL_ORIGIN_FIXED_ABSENCE_CASES', all_checked)
    print('ALL_FINITE_TORUS_VC_CHECKS_PASS')


if __name__ == '__main__':
    main()
