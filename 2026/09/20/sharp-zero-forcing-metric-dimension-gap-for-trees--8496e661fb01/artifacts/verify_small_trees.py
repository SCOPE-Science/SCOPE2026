"""Verify the sharp zero-forcing/metric-dimension gap for small trees.

Verified with NetworkX 3.6.1. Requires NetworkX.  For a tree, the path-cover number is n minus the maximum
number of edges in a spanning subgraph of maximum degree at most two.  The
dynamic program below computes that maximum.  For non-path trees, metric
dimension is leaves minus exterior major vertices.
"""

import math
import networkx as nx


def path_cover_number(T):
    root = next(iter(T.nodes()))
    parent = {root: None}
    order = [root]
    for v in order:
        for u in T[v]:
            if u != parent[v]:
                parent[u] = v
                order.append(u)

    dp0, dp1 = {}, {}
    for v in reversed(order):
        base = 0
        deltas = []
        for u in T[v]:
            if parent.get(u) == v:
                base += dp0[u]
                deltas.append((1 + dp1[u]) - dp0[u])
        deltas.sort(reverse=True)
        dp0[v] = base + sum(x for x in deltas[:2] if x > 0)
        dp1[v] = base + sum(x for x in deltas[:1] if x > 0)

    max_kept_edges = dp0[root]
    return T.number_of_nodes() - max_kept_edges


def metric_dimension_tree(T):
    n = T.number_of_nodes()
    degrees = dict(T.degree())
    if max(degrees.values(), default=0) <= 2:
        return 1 if n >= 2 else 0

    leaves = [v for v, d in degrees.items() if d == 1]
    exterior = set()
    for leaf in leaves:
        prev = None
        cur = leaf
        while True:
            nxt = [u for u in T[cur] if u != prev][0]
            prev, cur = cur, nxt
            if degrees[cur] >= 3:
                exterior.add(cur)
                break
    return len(leaves) - len(exterior)


print("n  max_gap  extremal_isomorphism_classes  predicted")
for n in range(4, 18):
    best = -1
    extremals = 0
    for T in nx.generators.nonisomorphic_trees(n):
        gap = path_cover_number(T) - metric_dimension_tree(T)
        if gap > best:
            best = gap
            extremals = 1
        elif gap == best:
            extremals += 1
    predicted = math.floor((n - 4) / 3)
    print(n, best, extremals, predicted)
    assert best == predicted
