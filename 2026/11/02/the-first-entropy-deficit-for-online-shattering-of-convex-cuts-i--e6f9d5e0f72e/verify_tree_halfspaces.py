#!/usr/bin/env python3
"""Exact finite checks for convex-cut halfspace Littlestone dimensions on trees.

Requires Python 3 standard library only. Enumerates every labeled tree through
order eight by Prufer sequences, canonicalizes unlabeled shapes, and computes
the optimal binary shattering depth directly from membership predicates.
"""
from collections import defaultdict
from functools import lru_cache
from heapq import heapify, heappop, heappush
from itertools import combinations, product


def prufer_edges(sequence, n):
    degrees = [1] * n
    for vertex in sequence:
        degrees[vertex] += 1
    heap = [v for v in range(n) if degrees[v] == 1]
    heapify(heap)
    edges = []
    for vertex in sequence:
        leaf = heappop(heap)
        edges.append((leaf, vertex))
        degrees[vertex] -= 1
        if degrees[vertex] == 1:
            heappush(heap, vertex)
    edges.append((heappop(heap), heappop(heap)))
    return edges


def neighbors(n, edges):
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph


def canonical_code(graph):
    def rooted(u, parent):
        parts = [rooted(v, u) for v in graph[u] if v != parent]
        return '(' + ''.join(sorted(parts)) + ')'
    return min(rooted(root, -1) for root in range(len(graph)))


def halfspaces(graph):
    n = len(graph)
    full = (1 << n) - 1
    concepts = [0, full]
    for u in range(n):
        for v in graph[u]:
            if v <= u:
                continue
            visited = {u, v}
            queue = [u]
            component = 0
            for w in queue:
                component |= 1 << w
                for x in graph[w]:
                    if x not in visited:
                        visited.add(x)
                        queue.append(x)
            concepts.extend((component, full ^ component))
    assert len(concepts) == 2*n == len(set(concepts))
    return concepts


def littlestone_dimension(n, concepts):
    columns = [sum(1 << j for j, concept in enumerate(concepts)
                   if (concept >> vertex) & 1) for vertex in range(n)]
    @lru_cache(None)
    def rank(version_space):
        result = 0
        for column in columns:
            positive = version_space & column
            negative = version_space ^ positive
            if positive and negative:
                result = max(result, 1 + min(rank(positive), rank(negative)))
        return result
    return rank((1 << len(concepts)) - 1)


def qualifying_motif(graph):
    n = len(graph)
    distances = []
    for start in range(n):
        depth = [-1]*n
        depth[start] = 0
        queue = [start]
        for v in queue:
            for w in graph[v]:
                if depth[w] < 0:
                    depth[w] = depth[v] + 1
                    queue.append(w)
        distances.append(depth)
    for a, b in combinations(range(n), 2):
        if distances[a][b] != 4:
            continue
        path = [v for v in range(n)
                if distances[a][v]+distances[v][b] == 4]
        for x in range(n):
            if min(distances[x][v] for v in path) == 2:
                return True
    return False


def main():
    expected_shape_counts = {2:1, 3:1, 4:2, 5:3, 6:6, 7:11, 8:23}
    for n in range(2, 9):
        shapes = {}
        counts = defaultdict(int)
        for sequence in product(range(n), repeat=n-2):
            graph = neighbors(n, prufer_edges(sequence, n))
            shape = canonical_code(graph)
            counts[shape] += 1
            shapes.setdefault(shape, graph)
        assert len(shapes) == expected_shape_counts[n]
        assert sum(counts.values()) == n**(n-2)
        ranks = defaultdict(int)
        shape_ranks = defaultdict(int)
        for shape, graph in shapes.items():
            dimension = littlestone_dimension(n, halfspaces(graph))
            motif = qualifying_motif(graph)
            shape_ranks[dimension] += 1
            ranks[dimension] += counts[shape]
            if n <= 3:
                assert dimension == 2
            elif n <= 7:
                assert dimension == 3
            else:
                assert dimension == (4 if motif else 3)
        if n == 8:
            assert dict(shape_ranks) == {3:12, 4:11}, shape_ranks
            assert dict(ranks) == {3:43744, 4:218400}, ranks
        print(f'n={n} unlabeled={len(shapes)} labeled={sum(counts.values())}'
              f' dimension_by_labeled={dict(sorted(ranks.items()))}'
              f' dimension_by_shapes={dict(sorted(shape_ranks.items()))}')
    for n in range(2, 15):
        path = neighbors(n, [(i, i+1) for i in range(n-1)])
        assert littlestone_dimension(n, halfspaces(path)) == (2*n).bit_length()-1
    print('PATH_FAMILY_EXTENDED_CHECK_PASS n=2..14')
    print('EIGHT_VERTEX_MOTIF_AND_COMPLETE_LABELLED_CENSUS_PASS')
    print('ALL_TREE_HALFSPACE_SHATTERING_CHECKS_PASS')


if __name__ == '__main__':
    main()
