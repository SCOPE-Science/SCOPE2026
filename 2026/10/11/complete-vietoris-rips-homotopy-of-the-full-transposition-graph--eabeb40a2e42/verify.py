#!/usr/bin/env python3
"""Independent exact checks for the absolute-transposition Rips complex on S4.

Run: python3 verify.py
Uses only the Python standard library.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations, permutations

V = tuple(permutations(range(4)))
assert len(V) == 24
index = {p: i for i, p in enumerate(V)}


def cycles(p):
    seen = set()
    count = 0
    for x in range(4):
        if x not in seen:
            count += 1
            y = x
            while y not in seen:
                seen.add(y)
                y = p[y]
    return count


def cycle_distance(p, q):
    inverse = [None] * 4
    for i, v in enumerate(p):
        inverse[v] = i
    return 4 - cycles(tuple(inverse[q[i]] for i in range(4)))


def edges_and_distances():
    adj = [[] for _ in V]
    for i, p in enumerate(V):
        for a, b in combinations(range(4), 2):
            q = list(p)
            q[a], q[b] = q[b], q[a]
            adj[i].append(index[tuple(q)])
    dist = []
    for i in range(24):
        row = [-1] * 24
        row[i] = 0
        queue = deque([i])
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if row[v] < 0:
                    row[v] = row[u] + 1
                    queue.append(v)
        assert all(z >= 0 for z in row)
        for j, p in enumerate(V):
            assert row[j] == cycle_distance(V[i], p)
        dist.append(row)
    assert Counter(dist[0]) == {0: 1, 1: 6, 2: 11, 3: 6}
    return adj, dist


def enumerate_cliques(dist, radius):
    neighbors = [sum(1 << j for j in range(24)
                     if i != j and dist[i][j] <= radius)
                 for i in range(24)]
    faces = []

    def go(face, candidates):
        while candidates:
            bit = candidates & -candidates
            candidates -= bit
            v = bit.bit_length() - 1
            new_face = face | bit
            faces.append(new_face)
            go(new_face, candidates & neighbors[v])

    go(0, (1 << 24) - 1)
    assert len(faces) == len(set(faces))
    return set(faces)


def staged_matching(faces):
    remaining = set(faces)
    pairs = []
    for vertex in range(24):
        bit = 1 << vertex
        lower_faces = sorted(x for x in remaining
                             if not (x & bit) and ((x | bit) in remaining))
        for lower in lower_faces:
            higher = lower | bit
            assert lower in remaining and higher in remaining
            assert higher.bit_count() == lower.bit_count() + 1
            remaining.remove(lower)
            remaining.remove(higher)
            pairs.append((lower, higher))
    return remaining, pairs


def directed_hasse_acyclic(faces, pairs):
    oriented_up = set(pairs)
    adjacency = defaultdict(list)
    indegree = {x: 0 for x in faces}
    incidences = 0
    for upper in faces:
        if upper.bit_count() == 1:
            continue
        bits = upper
        while bits:
            bit = bits & -bits
            bits -= bit
            lower = upper ^ bit
            assert lower in faces
            if (lower, upper) in oriented_up:
                start, end = lower, upper
            else:
                start, end = upper, lower
            adjacency[start].append(end)
            indegree[end] += 1
            incidences += 1
    queue = deque(x for x in faces if indegree[x] == 0)
    removed = 0
    while queue:
        x = queue.popleft()
        removed += 1
        for y in adjacency[x]:
            indegree[y] -= 1
            if indegree[y] == 0:
                queue.append(y)
    assert removed == len(faces), ('directed cycle', removed, len(faces))
    return incidences


def homology_mod_two(faces):
    layers = defaultdict(list)
    for f in faces:
        layers[f.bit_count() - 1].append(f)
    for v in layers.values():
        v.sort()
    ranks = {}
    for d in range(1, max(layers) + 1):
        idx = {f: j for j, f in enumerate(layers[d - 1])}
        pivots = {}
        for upper in layers[d]:
            column = 0
            bits = upper
            while bits:
                bit = bits & -bits
                bits -= bit
                column ^= 1 << idx[upper ^ bit]
            while column:
                top = column.bit_length() - 1
                if top in pivots:
                    column ^= pivots[top]
                else:
                    pivots[top] = column
                    break
        ranks[d] = len(pivots)
    return {d: len(layer) - ranks.get(d, 0) - ranks.get(d + 1, 0)
            for d, layer in layers.items()}


def main():
    adj, dist = edges_and_distances()
    assert sum(map(len, adj)) == 144
    assert all((i in adj[j]) == (j in adj[i]) for i in range(24) for j in range(24))
    scale_one = enumerate_cliques(dist, 1)
    assert Counter(x.bit_count() - 1 for x in scale_one) == {0: 24, 1: 72}
    scale_two = enumerate_cliques(dist, 2)
    expect_f = {0: 24, 1: 204, 2: 800, 3: 1632, 4: 2040,
                5: 2008, 6: 1608, 7: 990, 8: 440, 9: 132,
                10: 24, 11: 2}
    assert Counter(x.bit_count() - 1 for x in scale_two) == expect_f
    assert len(scale_two) == 9904
    # Scale two forbids exactly the distance-three pairs (products that are 4-cycles).
    for i in range(24):
        assert sum(dist[i][j] == 3 for j in range(24)) == 6
    critical, pairs = staged_matching(scale_two)
    assert len(pairs) == 4935
    assert Counter(x.bit_count() - 1 for x in critical) == {0: 1, 3: 33}
    assert len(critical) + 2 * len(pairs) == len(scale_two)
    incidences = directed_hasse_acyclic(scale_two, pairs)
    assert homology_mod_two(scale_two) == {**{d: 0 for d in range(12)}, 0: 1, 3: 33}
    assert max(max(row) for row in dist) == 3
    # At scale three all distances are at most three, hence the complex is the full simplex.
    print('VERIFY_OK faces=9904 pairs=4935 critical=1x0+33x3 '
          f'incidences={incidences} mod2_beta3=33 graph_edges=72')


if __name__ == '__main__':
    main()
