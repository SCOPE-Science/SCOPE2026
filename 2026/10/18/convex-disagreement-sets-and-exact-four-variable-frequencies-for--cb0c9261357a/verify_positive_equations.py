#!/usr/bin/env python3
"""Exact finite checks for positive-formula disagreement classification."""
from collections import Counter
from itertools import combinations


def functions(n):
    points = list(range(1 << n))
    edges = [(x, x | (1 << bit)) for x in points for bit in range(n) if not (x >> bit & 1)]
    return [mask for mask in range(1 << (1 << n))
            if all((mask >> x & 1) <= (mask >> y & 1) for x, y in edges)
            and not (mask & 1) and (mask >> (len(points) - 1) & 1)]


def functions_by_slicing(n):
    """Independent term-function enumeration via monotone Shannon slices."""
    all_fns = [0, 1]  # both maps from the zero-dimensional singleton
    for m in range(1, n + 1):
        block = 1 << (m - 1)
        all_fns = [lower | (upper << block)
                   for lower in all_fns for upper in all_fns
                   if lower & ~upper == 0]
    full = (1 << (1 << n)) - 1
    return [f for f in all_fns if f not in (0, full)]


def convex_masks(n):
    points = list(range(1, (1 << n) - 1))
    violations = []
    for a, c in combinations(points, 2):
        if (a & c) == a:
            middle = sum(1 << points.index(b) for b in points
                         if b != a and b != c and (a & b) == a and (b & c) == b)
            if middle:
                violations.append(((1 << points.index(a)) | (1 << points.index(c)), middle))
        if (a & c) == c:
            middle = sum(1 << points.index(b) for b in points
                         if b != a and b != c and (c & b) == c and (b & a) == b)
            if middle:
                violations.append(((1 << points.index(a)) | (1 << points.index(c)), middle))
    return {mask for mask in range(1 << len(points))
            if all(not (mask & endpoints == endpoints) or (mask & between == between)
                   for endpoints, between in violations)}


def run():
    expected_functions = (1, 4, 18, 166)
    expected_convex = (1, 4, 64, 3605)
    for n in range(1, 5):
        fns = functions(n)
        recursive = functions_by_slicing(n)
        assert len(recursive) == len(fns) and set(recursive) == set(fns)
        assert len(fns) == expected_functions[n - 1], (n, len(fns))
        sampled = {((a ^ b) >> 1) & ((1 << ((1 << n) - 2)) - 1) for a in fns for b in fns}
        convex = convex_masks(n)
        assert sampled == convex, (n, len(sampled), len(convex))
        assert len(convex) == expected_convex[n - 1]
        if n == 4:
            dist = Counter((a ^ b).bit_count() for a in fns for b in fns)
            independent_dist = Counter((a ^ b).bit_count()
                                       for a in recursive for b in recursive)
            assert dist == independent_dist
            assert sum(dist.values()) == 166 * 166
            assert set(dist) == set(range(15))
            assert dist == {
                0:166,1:904,2:2560,3:4616,4:5824,
                5:5312,6:3736,7:2176,8:1188,9:568,
                10:296,11:136,12:56,13:16,14:2,
            }, dict(dist)
            print('four_variables_distance_histogram', sorted(dist.items()))
    print('POSITIVE_EQUATIONAL_CONVEXITY_VERIFY_OK')

if __name__ == '__main__':
    run()
