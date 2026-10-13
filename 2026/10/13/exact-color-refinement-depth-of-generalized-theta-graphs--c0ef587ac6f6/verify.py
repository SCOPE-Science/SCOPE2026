#!/usr/bin/env python3
from collections import defaultdict
from itertools import combinations_with_replacement

def build_theta(lengths):
    adj = [set(), set()]
    meta = {0: ("branch",), 1: ("branch",)}
    nxt = 2
    for ell in lengths:
        prev = 0
        for i in range(1, ell):
            v = nxt
            nxt += 1
            adj.append(set())
            meta[v] = (ell, i)
            adj[prev].add(v)
            adj[v].add(prev)
            prev = v
        adj[prev].add(1)
        adj[1].add(prev)
    return adj, meta

def partition(colors):
    classes = defaultdict(set)
    for v, c in enumerate(colors):
        classes[c].add(v)
    return frozenset(frozenset(s) for s in classes.values())

def refinement_partitions(adj, rounds):
    colors = [0] * len(adj)
    out = [partition(colors)]
    for _ in range(rounds):
        sig = [
            (colors[v], tuple(sorted(colors[w] for w in adj[v])))
            for v in range(len(adj))
        ]
        labels = {}
        colors = [labels.setdefault(s, len(labels)) for s in sig]
        out.append(partition(colors))
    return out

def depth_formula(lengths):
    vals = sorted(set(lengths))
    second_distinct = vals[-2] if len(vals) >= 2 else 0
    return max(max(vals) // 2, second_distinct)

def predicted_partition(meta, r):
    classes = defaultdict(set)
    classes[("branch",)].update((0, 1))
    for v in range(2, len(meta)):
        ell, i = meta[v]
        key = tuple(sorted((min(i, r), min(ell - i, r))))
        classes[("internal",) + key].add(v)
    return frozenset(frozenset(s) for s in classes.values())

depth_checks = 0
partition_checks = 0
by_order = defaultdict(list)

for d in range(3, 8):
    for lengths in combinations_with_replacement(range(2, 11), d):
        expected = depth_formula(lengths)
        adj, meta = build_theta(lengths)
        parts = refinement_partitions(adj, expected + 1)
        observed = next(
            r for r in range(len(parts) - 1)
            if parts[r + 1] == parts[r]
        )
        assert observed == expected, (lengths, expected, observed)
        depth_checks += 1

        for r in range(1, expected + 1):
            assert parts[r] == predicted_partition(meta, r), (lengths, r)
            partition_checks += 1

        n = 2 + sum(ell - 1 for ell in lengths)
        by_order[(d, n)].append(expected)

for d in range(3, 8):
    for n in range(d + 2, d + 11):
        observed = max(by_order[(d, n)])
        expected = (n - d + 1) // 2
        assert observed == expected, (d, n, observed, expected)

order_checks = 5 * 9
print(
    "VERIFY_OK "
    f"depth_checks={depth_checks} "
    f"partition_checks={partition_checks} "
    f"order_checks={order_checks} "
    "d=3..7 lengths=2..10"
)
