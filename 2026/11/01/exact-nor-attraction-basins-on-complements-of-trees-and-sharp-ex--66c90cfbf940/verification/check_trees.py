#!/usr/bin/env python3
"""Exhaustive orbit census for open-neighborhood NOR on complements of trees."""
from collections import Counter
import networkx as nx


def enumerated_basin(T):
    n = len(T)
    full = (1 << n) - 1
    closed = [1 << v for v in range(n)]
    for a, b in T.edges():
        closed[a] |= 1 << b
        closed[b] |= 1 << a
    complement_neighbors = [full ^ closed[v] for v in range(n)]
    transition = [sum(1 << v for v in range(n)
                      if not (S & complement_neighbors[v]))
                  for S in range(1 << n)]
    # Orbit classes are extracted solely from the transition array.
    basins = Counter()
    first_entry = Counter()
    for S in range(1 << n):
        visited = {}
        trajectory = []
        cur = S
        while cur not in visited:
            visited[cur] = len(trajectory)
            trajectory.append(cur)
            cur = transition[cur]
        start = visited[cur]
        cyc = tuple(sorted(trajectory[start:]))
        basins[cyc] += 1
        first_entry[start] += 1
    return transition, basins, first_entry


def predicted_basins(T):
    n = len(T)
    full = (1 << n) - 1
    degree = dict(T.degree())
    internal = [v for v in T if degree[v] > 1]
    leaf_count = n - len(internal)
    star = max(degree.values()) == n - 1
    if star:
        center = max(degree, key=degree.get)
        universal = (1 << center, full)
        basins = {tuple(sorted(universal)): (1 << n) - 2 * (n - 1)}
        for u, v in T.edges():
            key = ((1 << u) | (1 << v),)
            basins[key] = 2
        return basins
    basins = {(0, full): (1 << n) - 2 * n + 1 -
              sum(2 ** (degree[v] + 1) - 2 * degree[v] - 2 for v in internal)}
    for u, v in T.edges():
        key = ((1 << u) | (1 << v),)
        basins[key] = 1 + (degree[u] == 1) + (degree[v] == 1)
    for v in internal:
        closed = (1 << v) | sum(1 << w for w in T.neighbors(v))
        key = tuple(sorted((1 << v, closed)))
        basins[key] = 2 ** (degree[v] + 1) - 2 * degree[v] - 1
    return basins


def main():
    graph_count = state_count = 0
    extrema = {}
    for n in range(4, 12):
        basins_seen = []
        this_graphs = 0
        for raw in nx.generators.nonisomorphic_trees(n):
            T = nx.convert_node_labels_to_integers(raw)
            trans, actual, first = enumerated_basin(T)
            expected = predicted_basins(T)
            assert dict(actual) == expected, (n, tuple(T.edges()), dict(actual), expected)
            assert first.get(1, 0) + first.get(0, 0) == (1 << n)
            assert all(trans[trans[trans[x]]] == trans[x] for x in range(1 << n))
            full = (1 << n) - 1
            target = next(key for key in actual if full in key)
            basins_seen.append(actual[target])
            graph_count += 1
            state_count += (1 << n)
            this_graphs += 1
        min_b, max_b = min(basins_seen), max(basins_seen)
        assert min_b == 2 ** (n - 1) - 3, (n, min_b)
        assert max_b == 2 ** n - 2 * n + 2, (n, max_b)
        extrema[n] = (min_b, max_b)
        print(f'n={n:2d} trees={this_graphs:4d} min_universal={min_b:5d} max_universal={max_b:5d}')
    print(f'PASS trees={graph_count} configurations={state_count} extrema={extrema}')

if __name__ == '__main__':
    main()
