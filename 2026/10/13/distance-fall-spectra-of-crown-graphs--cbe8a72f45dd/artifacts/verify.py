#!/usr/bin/env python3
from collections import deque


def crown(n):
    N = 2*n
    adj = [[False]*N for _ in range(N)]
    for i in range(n):
        for j in range(n):
            if i != j:
                adj[i][n+j] = adj[n+j][i] = True
    return adj


def distances(adj):
    N = len(adj)
    D = [[10**9]*N for _ in range(N)]
    for s in range(N):
        D[s][s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for v in range(N):
                if adj[u][v] and D[s][v] > D[s][u] + 1:
                    D[s][v] = D[s][u] + 1
                    q.append(v)
    return D


def independent(mask, adj):
    N = len(adj)
    vs = [v for v in range(N) if (mask >> v) & 1]
    return all(not adj[u][v] for i,u in enumerate(vs) for v in vs[i+1:])


def distance_dominating(mask, D, k):
    N = len(D)
    vs = [u for u in range(N) if (mask >> u) & 1]
    if not vs:
        return False
    return all(any(D[v][u] <= k for u in vs) for v in range(N))


def rgs_partitions(N):
    a = [0]*N
    def rec(pos, current_max):
        if pos == N:
            yield tuple(a)
            return
        for x in range(current_max + 2):
            a[pos] = x
            yield from rec(pos+1, max(current_max, x))
    a[0] = 0
    yield from rec(1, 0)


def valid_coloring(rgs, adj, D, k):
    N = len(adj)
    for u in range(N):
        for v in range(u+1, N):
            if adj[u][v] and rgs[u] == rgs[v]:
                return False
    q = max(rgs) + 1
    for v in range(N):
        for c in range(q):
            if not any(rgs[u] == c and D[v][u] <= k for u in range(N)):
                return False
    return True


subset_checks = 0
for n in range(3, 9):
    adj = crown(n)
    D = distances(adj)
    # The only distance-3 pairs must be the deleted matching pairs.
    for i in range(n):
        for j in range(n):
            expected = 3 if i == j else 1
            assert D[i][n+j] == expected
    # Among nonempty independent sets, distance-2 domination is equivalent
    # to cardinality at least two.
    for mask in range(1, 1 << (2*n)):
        if independent(mask, adj):
            subset_checks += 1
            lhs = distance_dominating(mask, D, 2)
            rhs = mask.bit_count() >= 2
            assert lhs == rhs, (n, mask, lhs, rhs)

coloring_checks = 0
for n in range(3, 6):
    adj = crown(n)
    D = distances(adj)
    got = {1:set(), 2:set(), 3:set()}
    for rgs in rgs_partitions(2*n):
        coloring_checks += 1
        for k in got:
            if valid_coloring(rgs, adj, D, k):
                got[k].add(max(rgs)+1)
    assert got[1] == {2, n}, (n, got[1])
    assert got[2] == set(range(2, n+1)), (n, got[2])
    assert got[3] == set(range(2, 2*n+1)), (n, got[3])

print("ALL CHECKS PASSED")
print(f"independent_subset_checks={subset_checks}")
print(f"canonical_partition_checks={coloring_checks}")
print("crown_orders_for_full_coloring_enumeration=6,8,10")
print("distance2_structural_orders=6..16")
