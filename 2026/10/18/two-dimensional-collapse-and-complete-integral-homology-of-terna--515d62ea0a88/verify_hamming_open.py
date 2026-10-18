#!/usr/bin/env python3
"""Exact finite checks for open-neighborhood complexes of Hamming graphs.

All integer reductions are unimodular generator/relation eliminations.
This program tests small cases only; the uniform proof is mathematical.
"""
import itertools
import collections
import heapq
import math


def complex_data(d, q):
    words = list(itertools.product(range(q), repeat=d))
    number = {w: i for i, w in enumerate(words)}
    neighborhoods = []
    for word in words:
        nb = []
        for j in range(d):
            for value in range(q):
                if value != word[j]:
                    other = list(word)
                    other[j] = value
                    nb.append(number[tuple(other)])
        neighborhoods.append(tuple(sorted(nb)))
    faces = set()
    for nb in neighborhoods:
        for size in range(1, len(nb) + 1):
            faces.update(itertools.combinations(nb, size))
    edge_set = {f for f in faces if len(f) == 2}
    triangle_set = {f for f in faces if len(f) == 3}
    euler = sum((-1) ** (len(f) - 1) for f in faces)
    assert len(faces) == len(set(faces))
    intersections = [len(set(neighborhoods[i]) & set(neighborhoods[j]))
                     for i in range(len(words)) for j in range(i + 1, len(words))]
    assert max(intersections) <= 2
    return len(words), edge_set, triangle_set, euler, neighborhoods


def presentation(n, edge_set, triangle_set):
    edges = sorted(edge_set)
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    seen = {0}
    queue = collections.deque([0])
    tree = set()
    while queue:
        x = queue.popleft()
        for y in sorted(adj[x]):
            if y not in seen:
                seen.add(y)
                queue.append(y)
                tree.add((min(x, y), max(x, y)))
    assert len(seen) == n and len(tree) == n - 1
    non_tree = {edge: i for i, edge in enumerate(e for e in edges if e not in tree)}
    relations = []
    for a, b, c in sorted(triangle_set):
        row = {}
        for edge, sign in (((a,b),1),((a,c),-1),((b,c),1)):
            if edge in non_tree:
                row[non_tree[edge]] = sign
        if row:
            relations.append(row)
    return len(non_tree), relations


def reduce_by_units(n_generators, relations):
    rows = {i: r.copy() for i, r in enumerate(relations)}
    incidence = [set() for _ in range(n_generators)]
    for i, row in rows.items():
        for j in row:
            incidence[j].add(i)
    candidates = [(len(r), i) for i, r in rows.items() if any(abs(v) == 1 for v in r.values())]
    heapq.heapify(candidates)
    removed = set()
    while candidates:
        _, i = heapq.heappop(candidates)
        if i not in rows:
            continue
        pivot_row = rows[i]
        eligible = [j for j, v in pivot_row.items() if abs(v) == 1]
        if not eligible:
            continue
        k = min(eligible, key=lambda j: len(incidence[j]))
        scale = pivot_row[k]
        for j in pivot_row:
            incidence[j].discard(i)
        del rows[i]
        for other_index in list(incidence[k]):
            row = rows[other_index]
            coefficient = row[k]
            for j in row:
                incidence[j].discard(other_index)
            for j, val in pivot_row.items():
                new = row.get(j, 0) - coefficient * scale * val
                if new:
                    row[j] = new
                else:
                    row.pop(j, None)
            if row:
                for j in row:
                    incidence[j].add(other_index)
                if any(abs(v) == 1 for v in row.values()):
                    heapq.heappush(candidates, (len(row), other_index))
            else:
                del rows[other_index]
        incidence[k].clear()
        removed.add(k)
    remaining = sorted(set(range(n_generators)) - removed)
    # If all relators vanish, the remaining lattice is free.
    if not rows:
        return len(remaining), 0, len(removed)
    # For the selected cases, relators are contained in the even sublattice,
    # and individual doubles generate the entire even sublattice.
    assert all(all(coef % 2 == 0 for coef in row.values()) for row in rows.values())
    assert all(any(row == {j: 2} or row == {j: -2} for row in rows.values()) for j in remaining)
    return 0, len(remaining), len(removed)


def check(d, q):
    n, edges, triangles, chi, neighborhoods = complex_data(d, q)
    g, relations = presentation(n, edges, triangles)
    free, two_torsion, eliminated = reduce_by_units(g, relations)
    assert free == (d if q == 3 else 0)
    assert two_torsion == (0 if q == 3 else d - 1)
    predicted_chi = (n * (d-1) * (d-2) if q == 3 else n * (9*d*d-15*d+8) // 4)
    assert chi == predicted_chi
    b2 = chi - 1 + free
    assert b2 == ((3**d)*(d-1)*(d-2)+d-1 if q==3
                  else 4**d*(9*d*d-15*d+8)//4-1)
    print(f'd={d},q={q},vertices={n},edges={len(edges)},triangles={len(triangles)},chi={chi},'
          f'H1_free={free},H1_2torsion={two_torsion},H2_rank={b2},unit_pivots={eliminated}')

if __name__ == '__main__':
    for d, q in ((1,3),(2,3),(3,3),(4,3),(1,4),(2,4),(3,4)):
        check(d,q)
    print('all exact finite cross-checks passed')
