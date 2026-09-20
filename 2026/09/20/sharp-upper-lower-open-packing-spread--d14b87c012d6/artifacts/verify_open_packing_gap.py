"""Finite checks for the sharp upper/lower open-packing spread theorem."""

import itertools
import networkx as nx


def is_open_packing(G, S):
    S = list(S)
    neighborhoods = [set(G.neighbors(v)) for v in S]
    return all(neighborhoods[i].isdisjoint(neighborhoods[j])
               for i in range(len(S)) for j in range(i + 1, len(S)))


def open_packing_parameters(G):
    V = list(G.nodes())
    open_sets = []
    for r in range(len(V) + 1):
        for S in itertools.combinations(V, r):
            if is_open_packing(G, S):
                open_sets.append(frozenset(S))
    upper = max(map(len, open_sets))
    maximal = [S for S in open_sets
               if not any(S < T for T in open_sets)]
    lower = min(map(len, maximal))
    return lower, upper


def graph_atlas_check():
    maxima = {}
    counts = {}
    checked = 0
    for G in nx.graph_atlas_g():
        n = G.number_of_nodes()
        if n < 2:
            continue
        lower, upper = open_packing_parameters(G)
        checked += 1
        assert 2 * upper <= n + lower
        if lower == 1:
            assert 2 * upper <= n
        gap = upper - lower
        target = (n - 2) // 2
        assert gap <= target
        if n not in maxima or gap > maxima[n]:
            maxima[n] = gap
            counts[n] = 1
        elif gap == maxima[n]:
            counts[n] += 1
    print(f"Graph Atlas graphs checked: {checked}")
    for n in sorted(maxima):
        print(f"atlas n={n}: max_gap={maxima[n]}, extremal_graphs={counts[n]}")


def tree_check(max_n=12):
    for n in range(2, max_n + 1):
        best = -1
        count = 0
        for T in nx.generators.nonisomorphic_trees(n):
            lower, upper = open_packing_parameters(T)
            gap = upper - lower
            if gap > best:
                best = gap
                count = 1
            elif gap == best:
                count += 1
        target = 0 if n <= 4 else (n - 2) // 2
        assert best == target
        print(f"trees n={n}: max_gap={best}, extremal_trees={count}")


if __name__ == "__main__":
    graph_atlas_check()
    tree_check()
