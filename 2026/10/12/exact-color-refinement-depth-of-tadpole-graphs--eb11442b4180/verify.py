#!/usr/bin/env python3

def tadpole(m, k):
    assert m >= 3 and k >= 1
    adj = [[] for _ in range(m + k)]
    for i in range(m):
        j = (i + 1) % m
        if j not in adj[i]:
            adj[i].append(j)
            adj[j].append(i)
    adj[0].append(m)
    adj[m].append(0)
    for v in range(m, m + k - 1):
        adj[v].append(v + 1)
        adj[v + 1].append(v)
    return adj

def depth_and_separation(adj, u, v):
    colors = [0] * len(adj)
    sep = None
    for r in range(len(adj) + 2):
        signatures = [
            (colors[x], tuple(sorted(colors[y] for y in adj[x])))
            for x in range(len(adj))
        ]
        names = {}
        new = [names.setdefault(s, len(names)) for s in signatures]
        if sep is None and new[u] != new[v]:
            sep = r + 1
        if new == colors:
            return r, sep
        colors = new
    raise AssertionError("refinement did not stabilize")

def predicted(m, k):
    return max(m // 2, (k + 1) // 2, min(m, k))

depth_checks = 0
witness_checks = 0
for m in range(3, 51):
    for k in range(1, 81):
        observed, sep = depth_and_separation(tadpole(m, k), 1, m)
        expected = predicted(m, k)
        assert observed == expected, (m, k, observed, expected)
        assert sep == min(m, k), (m, k, sep, min(m, k))
        depth_checks += 1
        witness_checks += 1

order_checks = 0
for N in range(4, 101):
    observed = max(predicted(m, N - m) for m in range(3, N))
    expected = 1 if N == 4 else N // 2
    assert observed == expected, (N, observed, expected)
    order_checks += 1

print(
    "VERIFY_OK "
    f"depth_checks={depth_checks} "
    f"cross_witness_checks={witness_checks} "
    f"order_checks={order_checks} "
    "m=3..50 k=1..80 N=4..100"
)
