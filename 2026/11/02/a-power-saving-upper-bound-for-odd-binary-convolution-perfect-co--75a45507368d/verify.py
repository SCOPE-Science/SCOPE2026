#!/usr/bin/env python3
"""Reproduce finite spot checks for a binary-convolution density bound.
No finite computation is used as a substitute for the general proof.
"""
from math import isqrt, log2


def binary_orthogonal(a, b):
    aa = [i for i in range(a.bit_length()) if (a >> i) & 1]
    bb = [j for j in range(b.bit_length()) if (b >> j) & 1]
    sums = set()
    for i in aa:
        for j in bb:
            if i + j in sums:
                return False
            sums.add(i + j)
    return True


def matching_lower_bound(t, B):
    # Edges connect j to j+t. The graph is a disjoint union of paths.
    if not (1 <= t <= B):
        raise ValueError('Need 1 <= t <= B')
    edges = [(j, j + t) for j in range(B + 1 - t)]
    used = set()
    count = 0
    for u, v in edges:
        if u not in used and v not in used:
            used.update((u, v))
            count += 1
    # Verify a particular greedy matching also meets the analytic bound
    # in the t <= B/2 regime.
    return count


def census(limit):
    total = 0
    for n in range(3, limit, 2):
        divisors = [a for a in range(3, isqrt(n) + 1, 2) if n % a == 0]
        if divisors and all(binary_orthogonal(a, n // a) for a in divisors):
            total += 1
    return total


def main():
    for B in range(2, 70):
        for t in range(1, B // 2 + 1):
            m = matching_lower_bound(t, B)
            assert 2 * m >= B + 1 - t, (t, B, m)
    theta = 1 - log2(4 / 3) / 6
    assert 0.9308 < theta < 0.9309
    assert census(10000) == 130
    assert census(100000) == 522
    print('VERIFY_OK matching_pairs=1190 theta=%.12f pi_odd_10000=130 pi_odd_100000=522' % theta)


if __name__ == '__main__':
    main()
