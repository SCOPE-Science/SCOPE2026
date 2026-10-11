#!/usr/bin/env python3
"""Exact one-skeleton census of the fourth consecutive-permutation pattern polytope.

All input data are generated from the 24 permutations of four symbols.
No precomputed incidence table or third-party packages are required.
"""
from collections import Counter, defaultdict, deque
from itertools import permutations
from math import comb


def standardize(seq):
    return tuple(1 + sum(y < x for y in seq) for x in seq)


def graph():
    vertices = tuple(permutations((1, 2, 3)))
    rank = {v: i for i, v in enumerate(vertices)}
    arcs = []
    outgoing = defaultdict(list)
    for perm in permutations((1, 2, 3, 4)):
        i = rank[standardize(perm[:3])]
        j = rank[standardize(perm[1:])]
        e = len(arcs)
        arcs.append((i, j, perm))
        outgoing[i].append(e)
    assert len(vertices) == 6 and len(arcs) == 24
    return vertices, arcs, outgoing


def vertex_first_cycles(vertices, arcs, outgoing):
    cycles = []
    for start in range(len(vertices)):
        def visit(v, seen, path):
            for e in outgoing[v]:
                w = arcs[e][1]
                if w == start:
                    cycles.append(tuple(path + [e]))
                elif w > start and w not in seen:
                    visit(w, seen | {w}, path + [e])
        visit(start, {start}, [])
    return cycles


def edge_first_cycles(vertices, arcs, outgoing):
    cycles = []
    for first, (start, nxt, _) in enumerate(arcs):
        if nxt == start:
            cycles.append((first,))
            continue
        def visit(v, seen, path):
            for e in outgoing[v]:
                if e <= first:
                    continue
                w = arcs[e][1]
                if w == start:
                    cycles.append(tuple(path + [e]))
                elif w not in seen:
                    visit(w, seen | {w}, path + [e])
        visit(nxt, {start, nxt}, [first])
    return cycles


def canonical(cycle):
    pos = cycle.index(min(cycle))
    return cycle[pos:] + cycle[:pos]


def cycle_rank(edge_set, arcs):
    incident = set()
    for e in edge_set:
        u, v, _ = arcs[e]
        incident.update((u, v))
    parent = {v: v for v in incident}

    def root(v):
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v

    for e in edge_set:
        u, v, _ = arcs[e]
        parent[root(u)] = root(v)
    components = len({root(v) for v in incident})
    return len(edge_set) - len(incident) + components


def main():
    vertices, arcs, outgoing = graph()
    cycles1 = vertex_first_cycles(vertices, arcs, outgoing)
    cycles2 = edge_first_cycles(vertices, arcs, outgoing)
    assert len(cycles1) == len(cycles2) == 160
    assert {canonical(c) for c in cycles1} == {canonical(c) for c in cycles2}
    cycles = sorted(map(canonical, cycles1))
    support = [frozenset(c) for c in cycles]
    assert len(set(support)) == 160
    assert len(set().union(*support)) == 24  # All coordinates occur in cycles.
    assert cycle_rank(set(range(24)), arcs) - 1 == 18
    assert Counter(map(len, cycles)) == {1: 2, 2: 6, 3: 26, 4: 20, 5: 34, 6: 72}

    adjacency = [set() for _ in cycles]
    for i in range(len(cycles)):
        for j in range(i + 1, len(cycles)):
            union = support[i] | support[j]
            dimension = cycle_rank(union, arcs) - 1
            # Independent characterization by counting simple cycles entirely within
            # the union support; a face is an edge iff exactly two are contained.
            allowed_cycles = sum(s.issubset(union) for s in support)
            assert (dimension == 1) == (allowed_cycles == 2), (i, j)
            if dimension == 1:
                adjacency[i].add(j)
                adjacency[j].add(i)

    degree_hist = Counter(map(len, adjacency))
    expected_degrees = {18: 72, 22: 34, 26: 4, 43: 16,
                        59: 16, 61: 2, 71: 8, 81: 4,
                        111: 2, 159: 2}
    assert degree_hist == expected_degrees
    joint = Counter((len(c), len(adjacency[i])) for i, c in enumerate(cycles))
    expected_joint = {
        (1, 159): 2,
        (2, 81): 4, (2, 111): 2,
        (3, 59): 16, (3, 61): 2, (3, 71): 8,
        (4, 26): 4, (4, 43): 16,
        (5, 22): 34,
        (6, 18): 72,
    }
    assert joint == expected_joint
    skeleton_edges = sum(degree_hist[d] * d for d in degree_hist) // 2
    assert sum(map(len, adjacency)) == 2 * skeleton_edges
    assert skeleton_edges == 2667

    eccentricities = Counter()
    distance_pairs = Counter()
    for start in range(len(cycles)):
        distances = [-1] * len(cycles)
        distances[start] = 0
        queue = deque([start])
        while queue:
            u = queue.popleft()
            for v in adjacency[u]:
                if distances[v] == -1:
                    distances[v] = distances[u] + 1
                    queue.append(v)
        assert -1 not in distances
        eccentricities[max(distances)] += 1
        distance_pairs.update(distances)
    assert eccentricities == {1: 2, 2: 158}
    assert distance_pairs == {0: 160, 1: 2 * 2667,
                              2: 2 * (comb(160, 2) - 2667)}
    loops = [arcs[c[0]][2] for c in cycles if len(c) == 1]
    assert sorted(loops) == [(1, 2, 3, 4), (4, 3, 2, 1)]
    assert sum(1 for a in adjacency if len(a) == 159) == 2
    print('VERIFY_OK pattern-four cycle-polytope: vertices=160 '
          'edges=2667 dimension=18 diameter=2 '
          'independent_cycle_enumerations=yes '
          'two_independent_adjacency_tests=yes '
          'all_12720_pairs=yes full_degree_profile=yes')
    for length in sorted(set(len(c) for c in cycles)):
        print('length', length, 'degree:count',
              sorted((degree, count) for (n, degree), count in joint.items()
                     if n == length))


if __name__ == '__main__':
    main()
