#!/usr/bin/env python3
"""Independent exact checks of singleton-versus-block-size covariance at fixed block count."""
from collections import defaultdict
from fractions import Fraction
from math import comb
from itertools import product


def stirling_table(limit):
    table = [[0] * (limit + 1) for _ in range(limit + 1)]
    table[0][0] = 1
    for n in range(1, limit + 1):
        for k in range(1, n + 1):
            table[n][k] = k * table[n - 1][k] + table[n - 1][k - 1]
    return table


def singleton_mean(S, n, k):
    return Fraction(n * S[n - 1][k - 1], S[n][k])


def block_mean(S, n, k, size):
    return Fraction(comb(n, size) * S[n - size][k - 1], S[n][k])


def normalized_covariance(S, n, k, size):
    return singleton_mean(S, n - size, k - 1) - singleton_mean(S, n, k)


def cov_formula(S, n, k, size):
    return block_mean(S, n, k, size) * normalized_covariance(S, n, k, size)


def rgs_partitions(n):
    def rec(prefix, maximum):
        if len(prefix) == n:
            yield tuple(prefix)
            return
        for v in range(maximum + 2):
            yield from rec(prefix + [v], max(maximum, v))
    yield from rec([0], 0)


def check():
    S = stirling_table(100)
    tests = 0
    for n in range(4, 101):
        for k in range(2, n - 1):
            total = S[n][k]
            assert total > 0
            expectation_singleton = singleton_mean(S, n, k)
            weights = Fraction(0)
            values = []
            for size in range(2, n - k + 2):
                expected_blocks = block_mean(S, n, k, size)
                difference = normalized_covariance(S, n, k, size)
                assert expected_blocks > 0
                cov = cov_formula(S, n, k, size)
                assert cov == expected_blocks * difference
                tests += 2
                values.append(difference)
                weights += (size - 1) * cov
            assert weights == 0
            tests += 1
            if k >= 3:
                assert values[0] < 0 < values[-1]
                tests += 1
                for left, right in zip(values, values[1:]):
                    assert left < right
                    tests += 1
                signs = [0 if v == 0 else (1 if v > 0 else -1) for v in values]
                assert signs == sorted(signs)
                assert signs.count(0) <= 1
                tests += 2
            else:
                assert all(v < 0 for v in values[:-1])
                assert values[-1] > 0
                assert all(v == values[0] for v in values[:-1])
                tests += 3
            assert 0 <= expectation_singleton <= k
            tests += 1

    assert normalized_covariance(S, 6, 3, 3) == 0
    assert normalized_covariance(S, 6, 3, 2) < 0
    assert normalized_covariance(S, 6, 3, 4) > 0
    tests += 3

    # Separately enumerate labeled set partitions through their canonical
    # restricted-growth words; no use of the Stirling recurrence in enumeration.
    for n in range(1, 10):
        observed = defaultdict(lambda: [0, 0, defaultdict(int), defaultdict(int)])
        # keys k -> [population, singleton sum, block-count sums, singleton x block sums]
        for word in rgs_partitions(n):
            k = max(word) + 1
            sizes = [0] * k
            for label in word:
                sizes[label] += 1
            frequency = defaultdict(int)
            for size in sizes:
                frequency[size] += 1
            j = frequency[1]
            arr = observed[k]
            arr[0] += 1
            arr[1] += j
            for size in range(2, n + 1):
                arr[2][size] += frequency[size]
                arr[3][size] += j * frequency[size]
        for k, (population, singleton_sum, block_sums, mixed_sums) in observed.items():
            assert population == S[n][k]
            assert Fraction(singleton_sum, population) == singleton_mean(S, n, k)
            tests += 2
            if 2 <= k <= n - 2:
                for size in range(2, n - k + 2):
                    mean_blocks = Fraction(block_sums[size], population)
                    covariance = (Fraction(mixed_sums[size], population)
                                  - Fraction(singleton_sum * block_sums[size], population ** 2))
                    assert mean_blocks == block_mean(S, n, k, size)
                    assert covariance == cov_formula(S, n, k, size)
                    tests += 2
    # Independently enumerate labeled-ball allocations to equally likely boxes.
    # After fixing the number of occupied boxes, their collision-partition law
    # agrees with the uniform fixed-block-count set-partition law.
    for n in range(4, 7):
        for q in range(2, 6):
            moments = defaultdict(lambda: [0, 0, defaultdict(int), defaultdict(int)])
            for assignment in product(range(q), repeat=n):
                bins = defaultdict(int)
                for box in assignment:
                    bins[box] += 1
                k = len(bins)
                freq = defaultdict(int)
                for occupied in bins.values():
                    freq[occupied] += 1
                j = freq[1]
                arr = moments[k]
                arr[0] += 1
                arr[1] += j
                for size in range(2, n + 1):
                    arr[2][size] += freq[size]
                    arr[3][size] += j * freq[size]
            for k, (population, singleton_sum, sum_blocks, sum_mixed) in moments.items():
                if 2 <= k <= n - 2:
                    for size in range(2, n - k + 2):
                        covariance = (Fraction(sum_mixed[size], population) -
                                      Fraction(singleton_sum * sum_blocks[size], population ** 2))
                        assert covariance == cov_formula(S, n, k, size)
                        tests += 1
    print('PASS: %d exact checks; n <= 100 exact sign/identity tests; independent set-partition enumeration n <= 9 and uniform-box allocations n <= 6' % tests)
    return tests


if __name__ == '__main__':
    check()
