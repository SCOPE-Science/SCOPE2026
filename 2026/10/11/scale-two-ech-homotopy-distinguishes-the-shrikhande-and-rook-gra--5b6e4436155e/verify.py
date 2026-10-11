#!/usr/bin/env python3
"""Reproduce the intrinsic scale-two Čech calculations for two (16,6,2,2) graphs.

Python 3, standard library only. Vertex index 4*i+j represents (i,j) in Z/4 x Z/4.
All face enumerations, directed-Hasse acyclicity checks, and mod-two
boundary-matrix ranks are performed from the stated graph definitions.
"""
from collections import Counter, deque

N = 16
GENERATORS = {(1, 0), (3, 0), (0, 1), (0, 3), (1, 1), (3, 3)}


def graph(which):
    adj = []
    for i in range(4):
        for j in range(4):
            if which == "shrikhande":
                neighbors = {4 * ((i + di) % 4) + (j + dj) % 4
                             for di, dj in GENERATORS}
            elif which == "rook":
                neighbors = {4 * x + y for x in range(4) for y in range(4)
                             if (x, y) != (i, j) and (x == i or y == j)}
            else:
                raise ValueError(which)
            adj.append(neighbors)
    for i in range(N):
        assert len(adj[i]) == 6 and i not in adj[i]
        for j in range(N):
            if i != j:
                assert (j in adj[i]) == (i in adj[j])
                assert len(adj[i] & adj[j]) == 2
    return adj


def local_signature(adj):
    # Degree-two local graph: connected 6-cycle versus two disjoint triangles.
    vertices = set(adj[0])
    degree = {u: len(adj[u] & vertices) for u in vertices}
    assert set(degree.values()) == {2}
    unseen = set(vertices)
    components = []
    while unseen:
        root = min(unseen)
        reached = {root}
        todo = [root]
        while todo:
            u = todo.pop()
            for v in adj[u] & vertices:
                if v not in reached:
                    reached.add(v)
                    todo.append(v)
        components.append(len(reached))
        unseen.difference_update(reached)
    return sorted(components)


def faces(adj):
    all_faces = set()
    facets = []
    for v in range(N):
        mask = 1 << v
        for w in adj[v]:
            mask |= 1 << w
        facets.append(mask)
        sub = mask
        while sub:
            all_faces.add(sub)
            sub = (sub - 1) & mask
    assert len(set(facets)) == N
    assert set(facets) <= all_faces
    assert all(m.bit_count() == 7 for m in facets)
    return all_faces


def matching(all_faces):
    # Each stage pairs every remaining lower face not containing v with
    # the remaining upper face obtained by adjoining v, in integer order.
    remaining = set(all_faces)
    pairs = []
    for v in range(N):
        bit = 1 << v
        for low in sorted(remaining):
            if low & bit:
                continue
            high = low | bit
            if high in remaining:
                assert low in remaining
                remaining.remove(low)
                remaining.remove(high)
                pairs.append((low, high))
    assert 2 * len(pairs) + len(remaining) == len(all_faces)
    return pairs, remaining


def hasse_acyclic(all_faces, pairs):
    matched = set(pairs)
    assert len(matched) == len(pairs)
    incident = set()
    for low, high in pairs:
        assert high.bit_count() == low.bit_count() + 1
        assert low & high == low
        assert low in all_faces and high in all_faces
        assert low not in incident and high not in incident
        incident.add(low)
        incident.add(high)
    next_faces = {f: [] for f in all_faces}
    incoming = {f: 0 for f in all_faces}
    incidence_count = 0
    for high in all_faces:
        if high.bit_count() < 2:
            continue
        for v in range(N):
            bit = 1 << v
            if not high & bit:
                continue
            low = high ^ bit
            assert low in all_faces
            if (low, high) in matched:
                src, dst = low, high
            else:
                src, dst = high, low
            next_faces[src].append(dst)
            incoming[dst] += 1
            incidence_count += 1
    ready = deque(sorted(f for f in all_faces if incoming[f] == 0))
    visited = 0
    while ready:
        f = ready.popleft()
        visited += 1
        for g in next_faces[f]:
            incoming[g] -= 1
            if incoming[g] == 0:
                ready.append(g)
    assert visited == len(all_faces), "directed Hasse cycle"
    return incidence_count


def mod_two_homology(all_faces):
    by_dim = {d: sorted(m for m in all_faces if m.bit_count() == d + 1)
              for d in range(7)}
    ranks = {0: 0, 7: 0}
    for d in range(1, 7):
        target_index = {f: i for i, f in enumerate(by_dim[d - 1])}
        pivots = {}
        for high in by_dim[d]:
            column = 0
            for v in range(N):
                if high & (1 << v):
                    low = high ^ (1 << v)
                    column ^= 1 << target_index[low]
            while column:
                p = column.bit_length() - 1
                if p in pivots:
                    column ^= pivots[p]
                else:
                    pivots[p] = column
                    break
        ranks[d] = len(pivots)
    betti = {d: len(by_dim[d]) - ranks[d] - ranks[d + 1] for d in range(7)}
    return ranks, betti


def verify(which, expected_vector, expected_pairs, expected_hasse, expected_betti):
    adj = graph(which)
    local = local_signature(adj)
    assert local == ([6] if which == "shrikhande" else [3, 3])
    all_faces = faces(adj)
    f_vector = [sum(f.bit_count() == d + 1 for f in all_faces)
                for d in range(7)]
    assert f_vector == expected_vector
    pairs, critical = matching(all_faces)
    assert len(pairs) == expected_pairs
    critical_dims = Counter(f.bit_count() - 1 for f in critical)
    assert critical_dims == Counter({0: 1, 2: expected_betti})
    assert len(all_faces) == 2 * len(pairs) + len(critical)
    directed_hasse = hasse_acyclic(all_faces, pairs)
    assert directed_hasse == expected_hasse
    ranks, betti = mod_two_homology(all_faces)
    assert betti == {d: (1 if d == 0 else expected_betti if d == 2 else 0)
                     for d in range(7)}
    euler = sum((-1) ** d * number for d, number in enumerate(f_vector))
    assert euler == 1 + expected_betti
    print(which, "f", f_vector, "matched", len(pairs),
          "critical", dict(critical_dims), "Hasse", directed_hasse,
          "GF2_ranks", [ranks[d] for d in range(1, 7)], "Euler", euler)


def main():
    verify("shrikhande", [16, 120, 400, 512, 336, 112, 16],
           744, 5952, 23)
    verify("rook", [16, 120, 464, 536, 336, 112, 16],
           768, 6240, 63)
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
