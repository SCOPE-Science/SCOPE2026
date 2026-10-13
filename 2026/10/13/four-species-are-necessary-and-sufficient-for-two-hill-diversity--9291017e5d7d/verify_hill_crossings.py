#!/usr/bin/env python3
"""Exact finite checks accompanying a theorem on Hill diversity profiles.

The universal zero bound is established in the paper by a sign-variation
and extended-Chebyshev argument. These finite checks are supplementary.
"""
from itertools import combinations

P = (994, 2014, 2989, 4003)
Q = (1000, 2000, 3000, 4000)
N = 10000
EXPECTED = {2: 2362, 3: -517776, 4: 16323602434}


def moments(seq, exponent):
    return sum(v ** exponent for v in seq)


def variation(seq):
    seq = [(v > 0) - (v < 0) for v in seq if v]
    return sum(x != y for x, y in zip(seq, seq[1:]))


def count_function_signs(p, r):
    levels = sorted(set(p + r))
    doubled_levels = [a + b for a, b in zip(levels, levels[1:])]
    return [sum(2 * a > mid for a in p) - sum(2 * b > mid for b in r)
            for mid in doubled_levels]


def partitions(total, length, lower=1):
    if length == 1:
        if total >= lower:
            yield (total,)
        return
    for k in range(lower, total // length + 1):
        for rest in partitions(total - k, length - 1, k):
            yield (k,) + rest


def main():
    assert all(v > 0 for v in P + Q)
    assert sum(P) == N and sum(Q) == N
    assert sorted(P) != sorted(Q)
    for q, target in EXPECTED.items():
        assert moments(P, q) - moments(Q, q) == target
        # Normalized proportions are a/N, and the sign is
        # preserved by dividing the integer power-sum gap by N**q.
    assert EXPECTED[2] > 0 and EXPECTED[3] < 0 and EXPECTED[4] > 0
    assert variation(count_function_signs(P, Q)) == 3

    # Verify an entire finite family of ordered profiles, not only the
    # exhibited pair. The finite check is NOT a proof for arbitrary n.
    profiles_checked = 0
    pairs_checked = 0
    for k in (2, 3, 4):
        for total in range(k, 23):
            profiles = list(partitions(total, k))
            profiles_checked += len(profiles)
            for p, r in combinations(profiles, 2):
                pairs_checked += 1
                assert variation(count_function_signs(p, r)) <= k - 1
                if k == 3:
                    moment_signs = [moments(p, j) - moments(r, j)
                                    for j in range(2, 14)]
                    assert variation(moment_signs) <= 1

    # Appending equal-count species leaves every normalized power-sum
    # sign unchanged at each q>1.
    for n in range(4, 10):
        p, r = P + (1,) * (n - 4), Q + (1,) * (n - 4)
        assert len(p) == len(r) == n
        assert sum(p) == sum(r) == N + n - 4
        for q, target in EXPECTED.items():
            assert moments(p, q) - moments(r, q) == target

    print(f'VERIFY_OK witness_integer_moments=3 profiles_checked={profiles_checked} '
          f'ordered_pairs_checked={pairs_checked} padded_dimensions=4..9')

if __name__ == '__main__':
    main()
