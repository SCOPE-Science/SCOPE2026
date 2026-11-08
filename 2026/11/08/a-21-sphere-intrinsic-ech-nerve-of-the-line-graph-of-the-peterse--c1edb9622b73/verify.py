#!/usr/bin/env python3
"""Exact certificate for the intrinsic graph Cech nerve of the line graph of Petersen."""
from itertools import combinations
from collections import Counter, defaultdict, deque
import heapq
import json


def make_graph():
    vertices = tuple(combinations(range(5), 2))
    p_edges = tuple((a, b) for a, b in combinations(range(10), 2)
                    if not (set(vertices[a]) & set(vertices[b])))
    assert len(p_edges) == 15
    line_edges = tuple((i, j) for i, j in combinations(range(15), 2)
                       if set(p_edges[i]) & set(p_edges[j]))
    assert len(line_edges) == 30
    neighbor = [1 << i for i in range(15)]
    for u, v in line_edges:
        neighbor[u] |= 1 << v
        neighbor[v] |= 1 << u
    assert [n.bit_count() for n in neighbor] == [5] * 15
    return vertices, p_edges, line_edges, neighbor


def nerve_faces(line_edges, neighbor):
    generators = [neighbor[u] | neighbor[v] for u, v in line_edges]
    assert len(set(generators)) == 30
    assert all(g.bit_count() == 7 for g in generators)
    faces = set()
    for g in generators:
        s = g
        while True:
            faces.add(s)
            if not s:
                break
            s = (s - 1) & g
    # Independent metric test: compute graph distances by BFS and evaluate the
    # closed radius-1.5 ball intersection at all vertices and edge midpoints.
    graph_neighbors = [[] for _ in range(15)]
    for u, v in line_edges:
        graph_neighbors[u].append(v)
        graph_neighbors[v].append(u)
    distances = []
    for start in range(15):
        d = [-1] * 15
        d[start] = 0
        queue = deque([start])
        while queue:
            u = queue.popleft()
            for v in graph_neighbors[u]:
                if d[v] == -1:
                    d[v] = d[u] + 1
                    queue.append(v)
        assert all(z >= 0 for z in d)
        distances.append(d)
    witness_masks = [sum(1 << i for i in range(15) if distances[i][v] <= 1)
                     for v in range(15)]
    for u, v in line_edges:
        witness_masks.append(sum(1 << i for i in range(15)
                                 if min(distances[i][u], distances[i][v]) + .5 <= 1.5))
    direct = {s for s in range(1 << 15)
              if any((s & m) == s for m in witness_masks)}
    assert faces == direct
    return generators, faces


def morse_reduction(cells, reverse=False):
    cells = set(cells) - {0}
    cofaces = {x: set() for x in cells}
    for x in cells:
        for i in range(15):
            if x & (1 << i):
                continue
            y = x | (1 << i)
            if y in cells:
                cofaces[x].add(y)
    removed = set()
    pairs, critical = [], []
    choices = []

    def enqueue(x):
        if x not in removed and len(cofaces[x]) == 1:
            key = (-(x.bit_count()), -x if reverse else x)
            heapq.heappush(choices, (key, x))

    for x in cells:
        enqueue(x)
    while len(removed) < len(cells):
        matched = False
        while choices:
            _, x = heapq.heappop(choices)
            if x not in removed and len(cofaces[x]) == 1:
                y = next(iter(cofaces[x]))
                pairs.append((x, y))
                deletion = (x, y)
                matched = True
                break
        if not matched:
            maximal = [x for x in cells - removed if not cofaces[x]]
            assert maximal
            y = max(maximal, key=lambda s: (s.bit_count(), -s if reverse else s))
            critical.append(y)
            deletion = (y,)
        for z in deletion:
            assert z not in removed
            removed.add(z)
        for z in deletion:
            for i in range(15):
                if z & (1 << i):
                    boundary = z ^ (1 << i)
                    if boundary in cells and boundary not in removed:
                        assert z in cofaces[boundary]
                        cofaces[boundary].remove(z)
                        enqueue(boundary)
    return pairs, critical


def check_directed_acyclicity(faces, pairs):
    cells = set(faces) - {0}
    matched = {(x, y) for x, y in pairs}
    assert len(matched) == len(pairs)
    covered = [z for p in pairs for z in p]
    assert len(set(covered)) == len(covered)
    out = defaultdict(list)
    indeg = {x: 0 for x in cells}
    incidences = 0
    for y in cells:
        for i in range(15):
            if not (y & (1 << i)):
                continue
            x = y ^ (1 << i)
            if not x:
                continue
            incidences += 1
            u, v = (x, y) if (x, y) in matched else (y, x)
            out[u].append(v)
            indeg[v] += 1
    Q = deque(x for x in indeg if indeg[x] == 0)
    seen = 0
    while Q:
        u = Q.popleft()
        seen += 1
        for v in out[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                Q.append(v)
    assert seen == len(cells), (seen, len(cells))
    return incidences


def mod2_boundary_ranks(faces):
    by_size = {k: sorted(s for s in faces if s.bit_count() == k)
               for k in range(1, 8)}
    ranks = []
    for k in range(2, 8):
        row = {s: i for i, s in enumerate(by_size[k-1])}
        basis = {}
        for s in by_size[k]:
            column = 0
            for i in range(15):
                if s & (1 << i):
                    column ^= 1 << row[s ^ (1 << i)]
            while column:
                pivot = column.bit_length() - 1
                if pivot in basis:
                    column ^= basis[pivot]
                else:
                    basis[pivot] = column
                    break
        ranks.append(len(basis))
    assert ranks == [14, 91, 339, 405, 180, 30]
    return ranks


def main():
    vertices, p_edges, line_edges, neighbor = make_graph()
    generators, faces = nerve_faces(line_edges, neighbor)
    fvector = [sum(s.bit_count() == k for s in faces) for k in range(1, 8)]
    assert fvector == [15, 105, 430, 765, 585, 210, 30]
    boundary_ranks = mod2_boundary_ranks(faces)
    results = []
    for reverse in (False, True):
        pairs, critical = morse_reduction(faces, reverse)
        inc = check_directed_acyclicity(faces, pairs)
        ranks = Counter(z.bit_count()-1 for z in critical)
        assert len(pairs) == 1059, (reverse, len(pairs), ranks)
        assert ranks == {0: 1, 3: 21}, (reverse, ranks)
        assert inc == 8955, inc
        assert 2 * len(pairs) + len(critical) == len(faces) - 1
        results.append({'order': 'descending_masks' if reverse else 'ascending_masks',
                        'pairs': len(pairs), 'critical': dict(sorted(ranks.items())),
                        'incidences': inc, 'acyclic': True})
    print(json.dumps({'petersen_vertices': len(vertices), 'petersen_edges': len(p_edges),
                      'line_graph_vertices': len(p_edges), 'line_graph_edges': len(line_edges),
                      'nerve_generators': len(generators), 'faces_including_empty': len(faces),
                      'fvector': fvector, 'mod2_boundary_ranks': boundary_ranks,
                      'checks': results, 'homotopy': '21 copies of S^3'},
                     sort_keys=True, separators=(',', ':')))

if __name__ == '__main__':
    main()
