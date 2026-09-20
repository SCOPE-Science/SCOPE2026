#!/usr/bin/env python3
"""Finite verification for the sharp dissociation-independence gap theorem."""

import networkx as nx


def independence_number_tree(T):
    root = next(iter(T))
    parent = {root: None}
    order = [root]
    for v in order:
        for w in T[v]:
            if w != parent[v]:
                parent[w] = v
                order.append(w)

    dp = {}
    for v in reversed(order):
        children = [w for w in T[v] if parent.get(w) == v]
        without_v = sum(max(dp[w]) for w in children)
        with_v = 1 + sum(dp[w][0] for w in children)
        dp[v] = (without_v, with_v)
    return max(dp[root])


def dissociation_number_tree(T):
    root = next(iter(T))
    parent = {root: None}
    order = [root]
    for v in order:
        for w in T[v]:
            if w != parent[v]:
                parent[w] = v
                order.append(w)

    # dp[v][selected][parent_selected]
    dp = {}
    for v in reversed(order):
        children = [w for w in T[v] if parent.get(w) == v]

        unselected = sum(
            max(dp[w][0][0], dp[w][1][0]) for w in children
        )

        # If v and its parent are selected, no selected child is allowed.
        selected_parent_selected = 1 + sum(dp[w][0][1] for w in children)

        # If v is selected and its parent is not, at most one child may be selected.
        base = 1 + sum(dp[w][0][1] for w in children)
        gains = [dp[w][1][1] - dp[w][0][1] for w in children]
        selected_parent_unselected = base + max([0] + gains)

        dp[v] = {
            0: {0: unselected, 1: unselected},
            1: {0: selected_parent_unselected, 1: selected_parent_selected},
        }

    return max(dp[root][0][0], dp[root][1][0])


def brute_parameters(G):
    vertices = list(G)
    alpha = 0
    diss = 0
    for mask in range(1 << len(vertices)):
        S = [vertices[i] for i in range(len(vertices)) if (mask >> i) & 1]
        H = G.subgraph(S)
        if H.number_of_edges() == 0:
            alpha = max(alpha, len(S))
        if all(H.degree(v) <= 1 for v in H):
            diss = max(diss, len(S))
    return alpha, diss


def arm_signature(G):
    """Return sorted component orders after a valid subdivided-star center, if one exists."""
    for c in G:
        H = G.copy()
        H.remove_node(c)
        comps = [H.subgraph(C) for C in nx.connected_components(H)]
        if all(len(C) in (1, 2) and (len(C) == 1 or C.number_of_edges() == 1) for C in comps):
            return tuple(sorted((len(C) for C in comps), reverse=True))
    return None


print("connected bipartite graphs from Graph Atlas")
atlas = nx.graph_atlas_g()
for n in range(2, 8):
    extremals = []
    best = -1
    for G in atlas:
        if len(G) != n or not nx.is_connected(G) or not nx.is_bipartite(G):
            continue
        alpha, diss = brute_parameters(G)
        gap = diss - alpha
        if gap > best:
            best = gap
            extremals = [G]
        elif gap == best:
            extremals.append(G)

    expected = 1 if n == 2 else (n - 2) // 2
    assert best == expected
    if n >= 3:
        assert all(G.number_of_edges() == n - 1 for G in extremals)
        assert all(arm_signature(G) is not None for G in extremals)

    expected_count = 1 if n <= 4 or n % 2 == 0 else 2
    assert len(extremals) == expected_count
    print(n, best, len(extremals))

print("nonisomorphic trees")
for n in range(2, 18):
    best = -1
    count = 0
    for T in nx.generators.nonisomorphic_trees(n):
        alpha = independence_number_tree(T)
        diss = dissociation_number_tree(T)
        gap = diss - alpha
        if gap > best:
            best = gap
            count = 1
        elif gap == best:
            count += 1

    expected = 1 if n == 2 else (n - 2) // 2
    expected_count = 1 if n <= 4 or n % 2 == 0 else 2
    assert best == expected
    assert count == expected_count
    print(n, best, count)
