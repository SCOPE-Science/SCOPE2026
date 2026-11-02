#!/usr/bin/env python3
"""Self-contained finite checks of closed radius-one Hamming-ball shattering profiles."""
from itertools import combinations, product
from math import comb


def prediction(d, q):
    if d == 1:
        return (1, 0, 0, 0, 0)
    n = q ** d
    if (d, q) == (2, 2):
        return (1, n, 0, 0, 0)
    twos = n * (d * (q - 1) + comb(d, 2) * (q - 1) ** 2) // 2
    if d == 2:
        threes = n * d * (d - 1) * comb(q - 1, 2) * (q - 1) if q >= 4 else 0
    else:
        threes = n * (q - 1) ** 3 * comb(d + 1, 3)
    return (1, n, twos, threes, 0)


def direct_traces(d, q, max_k):
    vertices = list(product(range(q), repeat=d))
    n = len(vertices)
    balls = []
    for center in vertices:
        mask = sum(1 << i for i, v in enumerate(vertices)
                   if sum(x != y for x, y in zip(center, v)) <= 1)
        balls.append(mask)
    # Independent of the geometric triple-type classification: trace enumeration.
    counts = [1]
    for k in range(1, max_k + 1):
        wanted = 1 << k
        number = 0
        for ids in combinations(range(n), k):
            signatures = set()
            for b in balls:
                signature = 0
                for j, vid in enumerate(ids):
                    signature |= ((b >> vid) & 1) << j
                signatures.add(signature)
                if len(signatures) == wanted:
                    number += 1
                    break
        counts.append(number)
    return counts


def type_counts(d, q):
    n = q ** d
    v = n * comb(d, 2) * (q - 1) ** 2
    distinct = n * comb(d, 3) * (q - 1) ** 3
    double = n * d * (d - 1) * comb(q - 1, 2) * (q - 1)
    return v, distinct, double


def main():
    cases = [(1, q, 2) for q in range(2, 6)] + [
        (2, 2, 4), (2, 3, 4), (2, 4, 4), (2, 5, 4), (2, 6, 3),
        (3, 2, 4), (3, 3, 4), (3, 4, 3),
        (4, 2, 4), (4, 3, 3), (5, 2, 4), (6, 2, 3)
    ]
    checked = 0
    for d, q, maximum in cases:
        actual = direct_traces(d, q, maximum)
        expected = prediction(d, q)[:maximum + 1]
        assert actual == list(expected), (d, q, actual, expected)
        if d >= 3:
            v, distinct, double = type_counts(d, q)
            assert v + distinct + double == expected[3]
        print('PASS d=%d q=%d support_counts=%s' % (d, q, actual))
        checked += 1
    print('ALL_HAMMING_CLOSED_BALL_PROFILE_CHECKS_PASS cases=%d' % checked)


if __name__ == '__main__':
    main()
