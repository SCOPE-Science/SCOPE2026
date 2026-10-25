#!/usr/bin/env python3
"""Exact GF(2) walk-kernel tests on finite even-branching rooted trees.

No finite test proves the all-tree theorem; the accompanying mathematical
argument establishes that theorem without exhaustive enumeration.
"""
from collections import defaultdict
from random import Random


def all_shapes(max_vertices=13):
    """Unlabelled rooted shapes whose nonleaves have positive even outdegree."""
    by_size = {1: [()]}
    for n in range(3, max_vertices + 1, 2):
        catalog = []
        for size in sorted(by_size):
            if size < n:
                catalog.extend((size, s) for s in by_size[size])
        catalog.sort(key=lambda p: (p[0], repr(p[1])))
        found = set()

        def fill(start, available, selected):
            if available == 0:
                if len(selected) >= 2 and len(selected) % 2 == 0:
                    found.add(tuple(selected))
                return
            for index in range(start, len(catalog)):
                weight, subshape = catalog[index]
                if weight > available:
                    break
                fill(index, available - weight, selected + (subshape,))

        fill(0, n - 1, ())
        by_size[n] = sorted(found, key=repr)
    return by_size


def to_parent(shape):
    parents = [-1]
    def grow(p, subtree):
        for child in subtree:
            i = len(parents)
            parents.append(p)
            grow(i, child)
    grow(0, shape)
    return parents


def heights(parents):
    depth = [0] * len(parents)
    for i in range(1, len(parents)):
        depth[i] = depth[parents[i]] + 1
    return depth


def kernel(parents, u, v, t, depth):
    ancestors = set()
    w = u
    while w != -1:
        ancestors.add(w)
        w = parents[w]
    w = v
    while w not in ancestors:
        w = parents[w]
    dist = depth[u] + depth[v] - 2 * depth[w]
    return int(dist <= t <= depth[u] + depth[v] and (t - dist) % 2 == 0)


def adjacency(parents):
    a = [0] * len(parents)
    for i in range(1, len(parents)):
        p = parents[i]
        a[i] |= 1 << p
        a[p] |= 1 << i
    return a


def step(a, configuration):
    out = 0
    for v, neighbors in enumerate(a):
        if ((configuration & neighbors).bit_count() % 2):
            out |= 1 << v
    return out


def audit_tree(parents, full=True, source_limit=None):
    n = len(parents)
    dep = heights(parents)
    h = max(dep)
    a = adjacency(parents)
    sources = range(n) if source_limit is None else range(min(n, source_limit))
    columns = 0
    for v in sources:
        state = 1 << v
        for t in range(2 * h + 2):
            expected = sum(kernel(parents, u, v, t, dep) << u for u in range(n))
            assert state == expected, (parents, v, t, state, expected)
            state = step(a, state)
            columns += 1
    if full:
        leaves_at_max = sum((dep[u] == h) << u for u in range(n))
        # The last nonzero iterate has identical columns on deepest leaves.
        for v in range(n):
            state = 1 << v
            for _ in range(2 * h):
                state = step(a, state)
            assert state == (leaves_at_max if dep[v] == h else 0)
            assert step(a, state) == 0
    return columns


def main():
    by_size = all_shapes(13)
    shapes = 0
    columns = 0
    configurations = 0
    for n in sorted(by_size):
        for shape in by_size[n]:
            parents = to_parent(shape)
            assert len(parents) == n
            columns += audit_tree(parents)
            shapes += 1
            if n <= 9:
                a = adjacency(parents)
                depth = heights(parents)
                h = max(depth)
                last_leaf_set = sum((depth[u] == h) << u for u in range(n))
                survivor_count = 0
                for x in range(1 << n):
                    state = x
                    for _ in range(2 * h):
                        state = step(a, state)
                    last_expected = last_leaf_set if (x & last_leaf_set).bit_count() % 2 else 0
                    assert state == last_expected
                    survivor_count += bool(state)
                    assert step(a, state) == 0
                    configurations += 1
                assert survivor_count == 1 << (n - 1)
    rng = Random(312577)
    sampled_trees = 0
    sampled_columns = 0
    # Non-isomorphic sizes not required here; nonuniform child counts are essential.
    for _ in range(120):
        parents = [-1]
        depth = [0]
        i = 0
        while i < len(parents):
            if depth[i] < 6 and len(parents) < 125 and rng.random() < 0.61:
                width = rng.choice((2, 4, 6))
                for j in range(width):
                    parents.append(i)
                    depth.append(depth[i] + 1)
            i += 1
        sampled_columns += audit_tree(parents, full=len(parents) <= 35, source_limit=20)
        sampled_trees += 1
    print('EVEN_BRANCHING_VERIFY_OK')
    print('unlabelled_shapes', shapes)
    print('exact_source_time_columns', columns)
    print('exhaustive_configurations', configurations)
    print('nonuniform_sampled_trees', sampled_trees)
    print('sampled_source_time_columns', sampled_columns)


if __name__ == '__main__':
    main()
