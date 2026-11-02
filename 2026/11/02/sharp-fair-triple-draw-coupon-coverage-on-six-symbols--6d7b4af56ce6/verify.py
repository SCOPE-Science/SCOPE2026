"""Exact reproducibility checks for six-symbol fair triple coverage.

This script uses only the Python standard library. It is a finite check,
not a substitute for the strict discrete-convexity proof in RESULT.md.
"""

from collections import Counter
from fractions import Fraction as Q
from itertools import combinations
from functools import lru_cache


def upper_bound(m):
    a = m // 5
    b = 3 * m - 15 * a
    assert m % 2 == 0 and 2 <= m <= 20
    return Q(22) + Q(m, m - 1) - (15 - b) * Q(m, m - a) - b * Q(m, m - a - 1)


def masks_from_strings(strings):
    return tuple(sum(1 << (int(ch) - 1) for ch in s) for s in strings.split())


def inclusion_exclusion(n, blocks):
    m = len(blocks)
    total = Q(0)
    for a in range(1, 1 << n):
        touched = sum(bool(b & a) for b in blocks)
        assert touched > 0
        total += (1 if a.bit_count() % 2 else -1) * Q(m, touched)
    return total


def dynamic_expectation(n, blocks):
    m = len(blocks)
    final = (1 << n) - 1

    @lru_cache(None)
    def remaining(seen):
        if seen == final:
            return Q(0)
        stay = 0
        next_sum = Q(0)
        for b in blocks:
            newer = seen | b
            if newer == seen:
                stay += 1
            else:
                next_sum += remaining(newer)
        assert stay < m
        return (Q(m) + next_sum) / (m - stay)

    return remaining(0)


def run():
    expected_table = {
        2: Q(3), 4: Q(13, 3), 6: Q(43, 10), 8: Q(30, 7),
        10: Q(157, 36), 12: Q(236, 55), 14: Q(1231, 286),
        16: Q(838, 195), 18: Q(2551, 595), 20: Q(327, 76),
    }
    tests = 0
    for m, expected in expected_table.items():
        assert upper_bound(m) == expected
        tests += 1
        if m != 10:
            assert expected < Q(157, 36)
            tests += 1

    design = masks_from_strings("123 124 135 245 345 236 146 346 156 256")
    all6 = tuple(sum(1 << j for j in c) for c in combinations(range(6), 3))
    assert len(set(design)) == 10
    tests += 1
    for v in range(6):
        assert sum(bool(b & (1 << v)) for b in design) == 5
        tests += 1
    pair_degrees = Counter()
    for triple in design:
        vertices = [v for v in range(6) if triple & (1 << v)]
        for p in combinations(vertices, 2):
            pair_degrees[p] += 1
    for pair in combinations(range(6), 2):
        assert pair_degrees[pair] == 2
        tests += 1
    for blocks, wanted in ((design, Q(157, 36)), (all6, Q(327, 76))):
        assert inclusion_exclusion(6, blocks) == wanted
        assert dynamic_expectation(6, blocks) == wanted
        tests += 2
    assert inclusion_exclusion(6, design) - inclusion_exclusion(6, all6) == Q(10, 171)
    tests += 1

    # The 5-block family is the complement of a cycle on five vertices.
    edges5 = ((0, 1), (1, 2), (2, 3), (3, 4), (4, 0))
    all_mask5 = (1 << 5) - 1
    sparse5 = tuple(all_mask5 ^ ((1 << x) | (1 << y)) for x, y in edges5)
    all5 = tuple(sum(1 << j for j in c) for c in combinations(range(5), 3))
    for blocks, wanted in ((sparse5, Q(37, 12)), (all5, Q(29, 9))):
        assert inclusion_exclusion(5, blocks) == wanted
        assert dynamic_expectation(5, blocks) == wanted
        tests += 2
    assert Q(37, 12) < Q(29, 9)
    tests += 1
    # n=3 and n=4 are forced full: sum of degrees = 3m.
    assert len(tuple(combinations(range(3), 3))) == 1
    assert len(tuple(combinations(range(4), 3))) == 4
    tests += 2
    print(f"PASS: {tests} exact rational assertions; sharp bound = 157/36")


if __name__ == "__main__":
    run()
