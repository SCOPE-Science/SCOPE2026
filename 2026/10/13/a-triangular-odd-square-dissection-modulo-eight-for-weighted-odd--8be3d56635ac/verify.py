#!/usr/bin/env python3
"""Verify an odd-excludant congruence by independent finite constructions."""

from collections import Counter
from functools import lru_cache
from math import isqrt

LIMIT = 600


def even_distinct_partition_counts(limit):
    """Odd parts unrestricted, even parts at most once."""
    ans = [0] * (limit + 1)
    ans[0] = 1
    for part in range(1, limit + 1):
        if part & 1:
            for n in range(part, limit + 1):
                ans[n] += ans[n - part]
        else:
            for n in range(limit, part - 1, -1):
                ans[n] += ans[n - part]
    return ans


def coefficients_via_theta(base):
    result = base[:]
    bound = len(base) - 1
    for r in range(1, isqrt(bound) + 1):
        square = r * r
        for n in range(square, bound + 1):
            result[n] += 2 * base[n - square]
    return result


def predicted_residue(n):
    j = (isqrt(8 * n + 1) - 1) // 2
    triangular = j * (j + 1) // 2 == n
    ans = (-1 if n & 1 else 1) if triangular else 0
    for odd in range(1, isqrt(n) + 1, 2):
        m = n - odd * odd
        t = (isqrt(8 * m + 1) - 1) // 2
        if t * (t + 1) // 2 == m:
            ans += 4
    return ans % 8


@lru_cache(None)
def partitions_of(n, largest):
    if n == 0:
        return ((),)
    ans = []
    for part in range(min(n, largest), 0, -1):
        for smaller in partitions_of(n - part, part):
            ans.append((part,) + smaller)
    return tuple(ans)


def direct_statistic(n):
    total = 0
    for parts in partitions_of(n, n):
        evens = [p for p in parts if p % 2 == 0]
        if len(set(evens)) != len(evens):
            continue
        odd_missing = 1
        part_set = set(parts)
        while odd_missing in part_set:
            odd_missing += 2
        total += odd_missing
    return total


def main():
    base = even_distinct_partition_counts(LIMIT)
    actual = coefficients_via_theta(base)
    for n in range(LIMIT + 1):
        assert actual[n] % 8 == predicted_residue(n), (n, actual[n], predicted_residue(n))
    for n in range(23):
        assert direct_statistic(n) == actual[n], (n, direct_statistic(n), actual[n])
    triangular = {j * (j + 1) // 2 for j in range(isqrt(2 * LIMIT) + 2)}
    for n in range(LIMIT + 1):
        assert (actual[n] % 4 != 0) == (n in triangular)
    print('VERIFY_OK coefficient_indices=601 independent_partition_enumerations=23')
    print('mod8_frequency_0_to_600=', dict(sorted(Counter(v % 8 for v in actual).items())))
    print('initial_residues=', [v % 8 for v in actual[:24]])


if __name__ == '__main__':
    main()
