#!/usr/bin/env python3
from collections import deque
from functools import lru_cache
import math

def partitions_rgs(n):
    if n == 0:
        return [()]
    out = []
    def rec(a, mx):
        if len(a) == n:
            out.append(a)
            return
        for x in range(mx + 2):
            rec(a + (x,), max(mx, x))
    rec((0,), 0)
    return out

def canon(labels):
    relabel = {}
    nxt = 0
    out = []
    for x in labels:
        if x not in relabel:
            relabel[x] = nxt
            nxt += 1
        out.append(relabel[x])
    return tuple(out)

def block_count(p):
    return 0 if not p else max(p) + 1

def neighbors(p):
    n = len(p)
    k = block_count(p)
    ans = set()
    for i in range(n):
        old = p[i]
        for b in range(k):
            if b == old:
                continue
            q = list(p)
            q[i] = b
            ans.add(canon(q))
        if p.count(old) > 1:
            q = list(p)
            q[i] = k
            ans.add(canon(q))
    ans.discard(p)
    return ans

def blocks(p):
    d = {}
    for i, b in enumerate(p):
        d.setdefault(b, set()).add(i)
    return list(d.values())

def maximum_overlap(p, q):
    A = blocks(p)
    B = blocks(q)
    if len(A) > len(B):
        A, B = B, A
    weights = [[len(a & b) for b in B] for a in A]
    @lru_cache(None)
    def dp(i, mask):
        if i == len(A):
            return 0
        best = dp(i + 1, mask)
        for j in range(len(B)):
            if not (mask >> j) & 1:
                best = max(best, weights[i][j] + dp(i + 1, mask | (1 << j)))
        return best
    return dp(0, 0)

ordered_pair_checks = 0
diameter_checks = 0
parameter_graphs = 0
full_vertices = 0

for n in range(1, 7):
    all_parts = partitions_rgs(n)
    full_vertices += len(all_parts)
    for k in range(1, n + 1):
        parameter_graphs += 1
        parts = [p for p in all_parts if block_count(p) <= k]
        index = {p: i for i, p in enumerate(parts)}
        adjacency = [[] for _ in parts]
        for i, p in enumerate(parts):
            for q in neighbors(p):
                if q in index:
                    adjacency[i].append(index[q])

        observed_diameter = 0
        for s, p in enumerate(parts):
            dist = [-1] * len(parts)
            dist[s] = 0
            queue = deque([s])
            while queue:
                u = queue.popleft()
                for v in adjacency[u]:
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        queue.append(v)
            assert all(d >= 0 for d in dist)
            for t, q in enumerate(parts):
                predicted = n - maximum_overlap(p, q)
                assert dist[t] == predicted, (n, k, p, q, dist[t], predicted)
                ordered_pair_checks += 1
                observed_diameter = max(observed_diameter, dist[t])

        predicted_diameter = n - math.ceil(n / k)
        assert observed_diameter == predicted_diameter, (
            n, k, observed_diameter, predicted_diameter
        )
        diameter_checks += 1

print(
    "ALL CHECKS PASSED; "
    "n_max=6; "
    f"bell_vertices_full={full_vertices}; "
    f"parameter_graphs={parameter_graphs}; "
    f"ordered_pair_checks={ordered_pair_checks}; "
    f"diameter_checks={diameter_checks}"
)
