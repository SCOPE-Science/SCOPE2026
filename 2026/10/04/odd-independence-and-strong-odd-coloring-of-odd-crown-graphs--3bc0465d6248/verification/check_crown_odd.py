#!/usr/bin/env python3
from functools import lru_cache


def crown_adj(n):
    N = 2 * n
    adj = [0] * N
    for i in range(n):
        for j in range(n):
            if i != j:
                a, b = i, n + j
                adj[a] |= 1 << b
                adj[b] |= 1 << a
    return adj


def is_odd_independent(mask, adj):
    N = len(adj)
    for v in range(N):
        if (mask >> v) & 1 and (adj[v] & mask):
            return False
    for v in range(N):
        if not ((mask >> v) & 1):
            k = (adj[v] & mask).bit_count()
            if k and k % 2 == 0:
                return False
    return True


def invariants(n):
    adj = crown_adj(n)
    N = 2 * n
    full = (1 << N) - 1
    odd = [m for m in range(1, 1 << N) if is_odd_independent(m, adj)]
    alpha = max(m.bit_count() for m in odd)
    maxima = [m for m in odd if m.bit_count() == alpha]
    containing = [[] for _ in range(N)]
    for m in odd:
        for v in range(N):
            if (m >> v) & 1:
                containing[v].append(m)

    @lru_cache(None)
    def dp(rem):
        if rem == 0:
            return 0
        v = (rem & -rem).bit_length() - 1
        return 1 + min(dp(rem ^ m) for m in containing[v] if not (m & ~rem))

    @lru_cache(None)
    def count_opt(rem):
        if rem == 0:
            return 1
        target = dp(rem)
        v = (rem & -rem).bit_length() - 1
        return sum(count_opt(rem ^ m) for m in containing[v]
                   if not (m & ~rem) and 1 + dp(rem ^ m) == target)

    return alpha, dp(full), len(maxima), count_opt(full), len(odd)


def main():
    total_subsets = 0
    for n in (3, 5, 7, 9):
        alpha, chi, max_count, partition_count, odd_count = invariants(n)
        assert alpha == 2, (n, alpha)
        assert chi == n, (n, chi)
        assert max_count == n, (n, max_count)
        assert partition_count == 1, (n, partition_count)
        total_subsets += (1 << (2 * n)) - 1
        print(f"n={n}: alpha_od={alpha}, chi_so={chi}, maxima={max_count}, optimal_partitions={partition_count}, odd_sets={odd_count}")
    print(f"ALL CHECKS PASSED; odd_n=3,5,7,9; subsets_examined={total_subsets}")


if __name__ == '__main__':
    main()
