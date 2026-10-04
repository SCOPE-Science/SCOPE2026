#!/usr/bin/env python3
from collections import Counter
from math import ceil, log2

def partitions(n):
    # Restricted-growth strings for all set partitions of {0,...,n-1}.
    if n == 0:
        yield ()
        return
    a = [0] * n
    def rec(i, mx):
        if i == n:
            yield tuple(a)
            return
        for x in range(mx + 2):
            a[i] = x
            yield from rec(i + 1, max(mx, x))
    a[0] = 0
    yield from rec(1, 0)

def stirling2(n, k):
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            dp[i][j] = dp[i - 1][j - 1] + j * dp[i - 1][j]
    return dp[n][k]

expected_profiles = {
    1: (1, 1),
    2: (1, 7, 7),
    3: (1, 127, 2667, 1345),
}

for n in range(1, 4):
    N = 2 ** n
    profile = Counter()
    total = 0
    by_k = Counter()

    for rg in partitions(N):
        total += 1
        k = max(rg) + 1
        by_k[k] += 1
        m = 0 if k == 1 else ceil(log2(k))
        profile[m] += 1

        # Assign block j the ordinary binary code of j.
        codes = [j for j in range(k)]

        # Equality of all code bits must be exactly equality of partition blocks.
        for x in range(N):
            for y in range(N):
                same_partition_block = rg[x] == rg[y]
                same_code = codes[rg[x]] == codes[rg[y]]
                assert same_partition_block == same_code

        # Pigeonhole lower bound is strict for m-1 bits whenever m>0.
        if m > 0:
            assert k > 2 ** (m - 1)
        assert k <= 2 ** m

    # Independent Stirling and Bell checks.
    bell = sum(stirling2(N, k) for k in range(1, N + 1))
    assert total == bell
    for k in range(1, N + 1):
        assert by_k[k] == stirling2(N, k)

    tup = tuple(profile[m] for m in range(n + 1))
    assert tup == expected_profiles[n], (n, tup)
    assert max(profile) == n

print("VERIFY_OK")
