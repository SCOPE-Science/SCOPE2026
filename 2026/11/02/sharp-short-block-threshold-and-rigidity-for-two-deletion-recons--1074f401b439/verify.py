#!/usr/bin/env python3
"""Finite alphabet-independent checks for length <=5 deletion intersections.

Only the equality pattern among the 2n displayed symbols matters. Restricted
 growth strings enumerate each such pattern exactly once, including every
possible alphabet size. This file does not depend on network or third-party code.
"""
from itertools import combinations, product
from collections import Counter


def rgs(length):
    a = [0] * length
    def generate(i, hi):
        if i == length:
            yield tuple(a)
            return
        for v in range(hi + 2):
            a[i] = v
            yield from generate(i + 1, max(hi, v))
    yield from generate(1, 0)


def ball(x, deletions):
    keep = len(x) - deletions
    return {tuple(x[i] for i in s) for s in combinations(range(len(x)), keep)}


def canonical_scan(n):
    hist = Counter()
    best_by_q = {2: -1, 3: -1}
    eligible = 0
    patterns = 0
    maximizers = []
    best = -1
    for z in rgs(2*n):
        patterns += 1
        x, y = z[:n], z[n:]
        if ball(x, 1) & ball(y, 1):
            continue
        eligible += 1
        intersection = len(ball(x, 2) & ball(y, 2))
        hist[intersection] += 1
        q = max(z) + 1
        for Q in (2, 3):
            if q <= Q:
                best_by_q[Q] = max(best_by_q[Q], intersection)
        if intersection > best:
            best, maximizers = intersection, [z]
        elif intersection == best:
            maximizers.append(z)
    return patterns, eligible, best, best_by_q, maximizers, tuple(sorted(hist.items()))


def direct_q_scan(q, n):
    words = list(product(range(q), repeat=n))
    out = {w: (ball(w, 1), ball(w, 2)) for w in words}
    best = -1
    attaining = 0
    for i, x in enumerate(words):
        one_x, two_x = out[x]
        for y in words[:i]:
            one_y, two_y = out[y]
            if one_x.isdisjoint(one_y):
                count = len(two_x & two_y)
                if count > best:
                    best, attaining = count, 1
                elif count == best:
                    attaining += 1
    return best, attaining


def check():
    expected = {
        3: (203, 133, 3, {2: 2, 3: 3}),
        4: (4140, 3690, 4, {2: 4, 3: 4}),
        5: (115975, 113073, 6, {2: 4, 3: 6}),
    }
    special = (0, 1, 2, 0, 1, 1, 0, 2, 1, 0)
    for n in (3, 4, 5):
        count, eligible, best, cap, maximizers, hist = canonical_scan(n)
        assert (count, eligible, best, cap) == expected[n]
        if n == 5:
            assert maximizers == [special], maximizers
            assert hist == ((0, 87171), (1, 20663), (2, 4605), (3, 541), (4, 86), (5, 6), (6, 1))
        print('CANONICAL', n, count, eligible, best, cap, len(maximizers))
    for q in (3, 4, 5):
        best, num = direct_q_scan(q, 5)
        expected_n = q * (q - 1) * (q - 2) // 2
        assert (best, num) == (6, expected_n), (q, best, num)
        print('DIRECT', q, 5, best, num)
    cases = [
        ((1, 0, 0, 1), (0, 1, 1, 0), 4),
        ((0, 1, 0, 0, 1), (0, 0, 1, 1, 0), 4),
        ((0, 1, 2, 0, 1), (1, 0, 2, 1, 0), 6),
        ((1, 0, 0, 1, 1, 0), (0, 1, 0, 1, 0, 1), 6),
    ]
    for x, y, expected_count in cases:
        assert not (ball(x, 1) & ball(y, 1))
        assert len(ball(x, 2) & ball(y, 2)) == expected_count
    print('WITNESSES_OK', len(cases))
    print('SHARP_TWO_DELETION_RIGIDITY_VERIFY_OK')


if __name__ == '__main__':
    check()
