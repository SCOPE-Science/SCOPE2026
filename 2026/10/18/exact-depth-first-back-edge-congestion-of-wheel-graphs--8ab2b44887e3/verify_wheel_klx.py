#!/usr/bin/env python3
"""Independent finite checks of KLX for wheel graphs from the ordered DFS arc definition.

This program is supporting evidence only. The general formula has a separate proof.
"""
from collections import Counter
from math import ceil


def wheel(n):
    """Rim vertices 0..n-1, hub n. Return adjacency sets and edge set."""
    assert n >= 3
    edges = set()
    for i in range(n):
        edges.add(tuple(sorted((i, (i + 1) % n))))
        edges.add((i, n))
    neighbors = [set() for _ in range(n + 1)]
    for u, v in edges:
        neighbors[u].add(v)
        neighbors[v].add(u)
    return neighbors, edges


def count_open_arcs(parent, root, edges):
    children = {v: [] for v in parent}
    for v, p in parent.items():
        if p is not None:
            children[p].append(v)
    contour = []

    def contour_walk(v):
        contour.append(v)
        for c in children[v]:
            contour_walk(c)
            contour.append(v)

    contour_walk(root)
    last = {v: max(i for i, x in enumerate(contour) if x == v) for v in parent}
    tree_edges = {tuple(sorted((v, p))) for v, p in parent.items() if p is not None}
    arcs = []
    for u, v in edges - tree_edges:
        ancestor = set()
        x = v
        while x is not None:
            ancestor.add(x)
            x = parent[x]
        if u in ancestor:
            descendant, ancestor_vertex = v, u
        else:
            ancestor = set()
            x = u
            while x is not None:
                ancestor.add(x)
                x = parent[x]
            assert v in ancestor, 'non-tree DFS edge must join comparable vertices'
            descendant, ancestor_vertex = u, v
        start = last[descendant]
        finish = next(i for i in range(start + 1, len(contour))
                      if contour[i] == ancestor_vertex)
        arcs.append((start, finish))
    value = max(sum(start <= last[c] < finish for start, finish in arcs)
                for c, p in parent.items() if p is not None)
    return value


def all_dfs_values(n):
    neighbors, edges = wheel(n)
    values = Counter()
    count_branching = 0
    for root in range(n + 1):
        parent = {root: None}
        active_stack = [root]

        def recurse():
            nonlocal count_branching
            if not active_stack:
                values[count_open_arcs(parent, root, edges)] += 1
                degrees = Counter(p for p in parent.values() if p is not None)
                count_branching += any(k > 1 for k in degrees.values())
                return
            v = active_stack[-1]
            candidates = neighbors[v] - parent.keys()
            if candidates:
                for u in sorted(candidates):
                    parent[u] = v
                    active_stack.append(u)
                    recurse()
                    active_stack.pop()
                    del parent[u]
            else:
                active_stack.pop()
                recurse()
                active_stack.append(v)

        recurse()
    return values, count_branching


def construction_value(n):
    neighbors, edges = wheel(n)
    a = n // 2
    order = list(range(a)) + [n] + list(range(a, n))
    assert len(set(order)) == n + 1
    assert all(order[i + 1] in neighbors[order[i]] for i in range(n))
    parent = {order[0]: None}
    for v, u in zip(order, order[1:]):
        parent[u] = v
    return count_open_arcs(parent, order[0], edges)


def star_congestion(n):
    """Classical spanning-tree cut congestion, hub-centered star, tree edge included."""
    neighbors, edges = wheel(n)
    return max(sum((u == v or w == v) for u, w in edges) for v in range(n))


def main():
    total = 0
    branching = 0
    for n in range(3, 10):
        values, branch = all_dfs_values(n)
        best = min(values)
        expected = (n + 1) // 2 + 1
        assert best == expected, (n, values)
        assert construction_value(n) == best, n
        assert star_congestion(n) == 3
        total += sum(values.values())
        branching += branch
        print('rim', n, 'DFS traversals', sum(values.values()),
              'branched', branch, 'minimum KLX', best, 'distribution', sorted(values.items()))
    for n in range(10, 501):
        assert construction_value(n) == (n + 1) // 2 + 1
    print('PASS', total, 'exhaustively enumerated ordered DFS traversals;',
          branching, 'branched DFS trees;', 'constructions checked through n=500')


if __name__ == '__main__':
    main()
