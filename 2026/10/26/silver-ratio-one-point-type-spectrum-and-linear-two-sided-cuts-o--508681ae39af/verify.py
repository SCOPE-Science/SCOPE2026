#!/usr/bin/env python3
"""Independent finite checks for cyclic triple-incidence one-point types.

Run: python3 verify.py (Python 3 standard library only).
"""
from itertools import product


def pell_trace(n):
    a, b = 2, 2
    if n == 0:
        return a
    for _ in range(2, n + 1):
        a, b = b, 2 * b + a
    return b


def target_count(n):
    assert n >= 5
    return 2 * pell_trace(n) + 12 * n + 1


def incidence(n):
    # Edges (lower i, upper j), with each upper j covering j,j+1,j+2.
    return [(i, j) for j in range(n) for i in ((j + k) % n for k in range(3))]


def count_direct(n):
    """Enumerate all ternary comparison labels, not the trace formula."""
    edges = incidence(n)
    down = [0] * (2 * n)
    up = [0] * (2 * n)
    for i, j in edges:
        down[n + j] |= 1 << i
        up[i] |= 1 << (n + j)
    answer = 0
    for lab in product((0, 1, 2), repeat=2*n):
        lower = sum(1 << i for i, label in enumerate(lab) if label == 0)
        upper = sum(1 << i for i, label in enumerate(lab) if label == 1)
        # A lower label requires all predecessors lower.
        if any((down[i] & ~lower) for i in range(n, 2 * n) if lower & (1 << i)):
            continue
        # An upper label requires all successors upper.
        if any((up[i] & ~upper) for i in range(n) if upper & (1 << i)):
            continue
        # Every lower-labelled point must be strictly below every upper-labelled point.
        if upper and any(lower & (1 << i) for i in range(n, 2 * n)):
            continue
        if lower and any(upper & (1 << i) for i in range(n)):
            continue
        if any((up[i] & upper) != upper for i in range(n) if lower & (1 << i)):
            continue
        answer += 1
    return answer


def count_ideals_by_subsets(n):
    # Choose upper vertices in the ideal, forcing their lower neighbours.
    total = 0
    for topmask in range(1 << n):
        forced = 0
        for j in range(n):
            if topmask >> j & 1:
                for k in range(3):
                    forced |= 1 << ((j+k) % n)
        total += 1 << (n - forced.bit_count())
    return total


def count_mixed_by_subsets(n):
    # Choose nonempty lower and nonempty upper with all required comparabilities.
    edges = incidence(n)
    masks = [0] * n
    for i, j in edges:
        masks[i] |= 1 << j
    all_uppers = (1 << n) - 1
    total = 0
    for subset in range(1, 1 << n):
        common = all_uppers
        for i in range(n):
            if subset >> i & 1:
                common &= masks[i]
        total += (1 << common.bit_count()) - 1
    return total


def trace_weighted_triples(n):
    # Enumerate top-selection bit strings with weight 2 per cyclic zero triple.
    total = 0
    for mask in range(1 << n):
        n000 = sum(not ((mask >> i) & 1 or (mask >> ((i+1) % n)) & 1 or
                        (mask >> ((i+2) % n)) & 1) for i in range(n))
        total += 1 << n000
    return total


def main():
    n_ternary = 0
    n_ideals = 0
    for n in range(5, 8):
        direct = count_direct(n)
        assert direct == target_count(n), (n, direct, target_count(n))
        print('TERNARY_OK', n, direct)
        n_ternary += 1
    for n in range(5, 15):
        ideals = count_ideals_by_subsets(n)
        mixed = count_mixed_by_subsets(n)
        trace = trace_weighted_triples(n)
        assert ideals == trace == pell_trace(n) + 1, (n, ideals, trace)
        assert mixed == 12 * n, (n, mixed)
        assert 2 * ideals - 1 + mixed == target_count(n)
        n_ideals += 1
    print('BINARY_IDEAL_MIXED_OK', n_ideals)
    print('DIRECT_TERNARY_CONFIGURATIONS', n_ternary)
    print('ALL_TESTS_PASS')


if __name__ == '__main__':
    main()
