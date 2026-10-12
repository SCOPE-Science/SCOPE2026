#!/usr/bin/env python3
from functools import lru_cache
from math import comb

def rgs_partitions(n):
    if n == 0:
        yield ()
        return
    a = [0] * n
    a[0] = 0
    def rec(i, maximum):
        if i == n:
            yield tuple(a)
            return
        for v in range(maximum + 2):
            a[i] = v
            yield from rec(i + 1, max(maximum, v))
    yield from rec(1, 0)

@lru_cache(None)
def partitions(n):
    return tuple(rgs_partitions(n))

def is_coarser(p, q):
    n = len(p)
    for i in range(n):
        for j in range(i + 1, n):
            if p[i] == p[j] and q[i] != q[j]:
                return False
    return True

@lru_cache(None)
def coarsenings(p):
    return tuple(q for q in partitions(len(p)) if is_coarser(p, q))

@lru_cache(None)
def chain_count_from(p, levels):
    if levels == 0:
        return 1
    return sum(chain_count_from(q, levels - 1) for q in coarsenings(p))

def brute_injective(rank, n):
    if n == 0:
        return 1
    discrete = tuple(range(n))
    return chain_count_from(discrete, rank - 1)

def stirling_table(N):
    s = [[0] * (N + 1) for _ in range(N + 1)]
    s[0][0] = 1
    for n in range(1, N + 1):
        for k in range(1, n + 1):
            s[n][k] = s[n - 1][k - 1] + k * s[n - 1][k]
    return s

def recurrence_rows(max_rank, N):
    S = stirling_table(N)
    rows = [[1] * (N + 1)]
    for _ in range(max_rank):
        prev = rows[-1]
        nxt = [1]
        for n in range(1, N + 1):
            nxt.append(sum(S[n][k] * prev[k] for k in range(1, n + 1)))
        rows.append(nxt)
    return rows

def main():
    N = 10
    rows = recurrence_rows(5, N)
    expected = {
        1: [1,1,1,1,1,1,1,1],
        2: [1,1,2,5,15,52,203,877],
        3: [1,1,3,12,60,358,2471,19302],
        4: [1,1,4,22,154,1304,12915,146115],
    }
    checks = 0
    for rank, vals in expected.items():
        got = rows[rank - 1][:len(vals)]
        assert got == vals, (rank, got, vals)
        checks += len(vals)
    # Independent direct chain enumeration.
    for rank in range(1, 5):
        for n in range(0, 8):
            assert brute_injective(rank, n) == rows[rank - 1][n]
            checks += 1
    # Equality-pattern Stirling transform equals next injective row.
    S = stirling_table(N)
    for rank in range(1, 5):
        for n in range(0, N + 1):
            if n == 0:
                all_orbits = 1
            else:
                all_orbits = sum(S[n][k] * rows[rank - 1][k]
                                 for k in range(1, n + 1))
            assert all_orbits == rows[rank][n]
            checks += 1
    print("VERIFY_OK")
    print("checks", checks)
    for rank in range(1, 5):
        print("rank", rank, "injective", rows[rank - 1][:11])

if __name__ == "__main__":
    main()
