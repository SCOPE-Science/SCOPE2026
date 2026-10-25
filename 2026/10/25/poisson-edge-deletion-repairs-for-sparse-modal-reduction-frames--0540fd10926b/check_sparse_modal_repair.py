#!/usr/bin/env python3
"""Finite checks for sparse modal reduction and edge-deletion repair.

No finite computation is an asymptotic probability proof.
"""
from itertools import permutations, combinations


def reach_rows(n, edges, steps):
    adjacency = [0] * n
    for u, v in edges:
        adjacency[u] |= 1 << v
    current = [1 << u for u in range(n)]
    rows = [current]
    for _ in range(steps):
        next_rows = []
        for bits in current:
            out = 0
            for v in range(n):
                if bits & (1 << v):
                    out |= adjacency[v]
            next_rows.append(out)
        rows.append(next_rows)
        current = next_rows
    return rows


def paths_of_length(n, edges, m):
    adjacency = [[] for _ in range(n)]
    for u, v in edges:
        adjacency[u].append(v)
    paths = []
    def visit(prefix):
        if len(prefix) == m+1:
            paths.append(tuple(prefix))
            return
        for v in adjacency[prefix[-1]]:
            visit(prefix+[v])
    for u in range(n):
        visit([u])
    return paths


def all_isolated_paths(n, edges, paths):
    occupied = set()
    edge_set = set(edges)
    for path in paths:
        vertices = set(path)
        if len(vertices) != len(path) or occupied & vertices:
            return False
        occupied.update(vertices)
        allowable = set(zip(path, path[1:]))
        for u, v in edge_set:
            if (u in vertices or v in vertices) and (u, v) not in allowable:
                return False
    return True


def count_minimum_deletions(n, edges, m, L):
    size = len(edges)
    for d in range(size+1):
        count = 0
        for positions in combinations(range(size), d):
            deleted = set(positions)
            kept = [e for i, e in enumerate(edges) if i not in deleted]
            rels = reach_rows(n, kept, L)
            if all((rels[m][u] & ~rels[L][u]) == 0 for u in range(n)):
                count += 1
        if count:
            return d, count
    raise AssertionError('deletion to empty frame always works')


def run():
    checked_frames = 0
    checked_valuations = 0
    checked_repairs = 0
    for n in (2, 3, 4):
        all_arcs = [(i, j) for i in range(n) for j in range(n) if i != j]
        for mask in range(1 << len(all_arcs)):
            edges = [a for i, a in enumerate(all_arcs) if mask & (1 << i)]
            for m in (2, 3):
                for k in (1, 2):
                    L = m + k
                    rels = reach_rows(n, edges, L)
                    inclusion = all((rels[m][u] & ~rels[L][u]) == 0 for u in range(n))
                    all_valuations_valid = True
                    for subset in range(1 << n):
                        for u in range(n):
                            box_L = (rels[L][u] & ~subset) == 0
                            box_m = (rels[m][u] & ~subset) == 0
                            if box_L and not box_m:
                                all_valuations_valid = False
                        checked_valuations += 1
                    assert inclusion == all_valuations_valid
                    checked_frames += 1
                    paths = paths_of_length(n, edges, m)
                    if all_isolated_paths(n, edges, paths) and not any(rels[L]):
                        expected = (len(paths), m ** len(paths))
                        measured = count_minimum_deletions(n, edges, m, L)
                        assert measured == expected, (n, m, k, edges, expected, measured)
                        checked_repairs += 1
    assert checked_frames > 10000 and checked_repairs > 100
    print('SPARSE_MODAL_REPAIR_FINITE_OK', checked_frames, 'frame_formulas',
          checked_valuations, 'valuations', checked_repairs, 'repair_counts')


if __name__ == '__main__':
    run()
