#!/usr/bin/env python3
"""Finite, reproducible discrete-Morse certificate for the 2-independence complex of the Petersen graph."""
from collections import Counter, defaultdict, deque
from itertools import combinations

N = 10
ORDER = (0, 5, 6, 8, 9, 7, 1, 4, 2, 3)
EXPECTED_F = (10, 45, 90, 80, 30, 5)
EXPECTED_CRITICAL = {1, 402}


def edge_set():
    edges = set()
    for i in range(5):
        for a, b in ((i, (i + 1) % 5),
                     (5 + i, 5 + (i + 2) % 5),
                     (i, 5 + i)):
            edges.add(tuple(sorted((a, b))))
    assert len(edges) == 15
    return edges


def generate():
    edges = edge_set()
    adj = [0] * N
    for a, b in edges:
        adj[a] |= 1 << b
        adj[b] |= 1 << a
    assert all(x.bit_count() == 3 for x in adj)
    faces = set()
    for mask in range(1, 1 << N):
        if all((adj[i] & mask).bit_count() <= 1 for i in range(N) if mask & (1 << i)):
            faces.add(mask)
    # Independent cross-check via forbidden induced 3-vertex paths.
    obstructions = [sum(1 << v for v in t) for t in combinations(range(N), 3)
                    if sum(tuple(sorted(e)) in edges for e in combinations(t, 2)) >= 2]
    assert len(obstructions) == 30
    by_obstruction = {mask for mask in range(1, 1 << N)
                      if all(mask & trip != trip for trip in obstructions)}
    assert faces == by_obstruction
    assert tuple(sum(x.bit_count() == k for x in faces) for k in range(1, 7)) == EXPECTED_F
    assert not any(x.bit_count() > 6 for x in faces)
    facets = {m for m in faces if not any((m | (1 << v)) in faces for v in range(N) if not (m & (1 << v)))}
    assert Counter(x.bit_count() - 1 for x in facets) == {3: 5, 5: 5}, Counter(x.bit_count() - 1 for x in facets)
    return faces


def make_matching(faces):
    remaining = set(faces) | {0}
    pairs = set()
    for v in ORDER:
        bit = 1 << v
        for lower in sorted(remaining):
            if lower & bit:
                continue
            upper = lower | bit
            if upper in remaining:
                remaining.remove(lower)
                remaining.remove(upper)
                pairs.add((lower, upper))
    assert remaining == {402}, remaining
    assert (0, 1) in pairs
    pairs.remove((0, 1))
    critical = remaining | {1}
    assert critical == EXPECTED_CRITICAL
    assert len(pairs) == 129
    matched_faces = {m for a, b in pairs for m in (a, b)}
    assert matched_faces.isdisjoint(critical)
    assert matched_faces | critical == faces
    return pairs, critical


def check_acyclic(faces, pairs):
    vertices = faces
    # Orient matched Hasse arcs from lower to upper; all others from upper to lower.
    matched = set(pairs)
    outgoing = defaultdict(list)
    indegree = {m: 0 for m in vertices}
    for upper in faces:
        for i in range(N):
            if upper & (1 << i):
                lower = upper & ~(1 << i)
                if not lower:
                    continue
                if (lower, upper) in matched:
                    src, dst = lower, upper
                else:
                    src, dst = upper, lower
                outgoing[src].append(dst)
                indegree[dst] += 1
    queue = deque(m for m in vertices if indegree[m] == 0)
    seen = 0
    while queue:
        m = queue.popleft()
        seen += 1
        for nxt in outgoing[m]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)
    assert seen == len(vertices), ('directed cycle', seen, len(vertices))
    return sum(map(len, outgoing.values()))


def rank_f2(columns):
    pivot = {}
    for col in columns:
        while col:
            lead = col.bit_length() - 1
            if lead in pivot:
                col ^= pivot[lead]
            else:
                pivot[lead] = col
                break
    return len(pivot)


def check_homology(faces):
    by_k = [sorted(x for x in faces if x.bit_count() == k) for k in range(1, 7)]
    ranks = [0] * 7
    for k in range(2, 7):
        rows = {m: i for i, m in enumerate(by_k[k - 2])}
        columns = []
        for simplex in by_k[k - 1]:
            col = 0
            for v in range(N):
                if simplex & (1 << v):
                    col ^= 1 << rows[simplex & ~(1 << v)]
            columns.append(col)
        ranks[k - 1] = rank_f2(columns)
    betti = [len(by_k[k - 1]) - ranks[k - 1] - ranks[k] for k in range(1, 7)]
    betti[0] -= 1
    assert betti == [0, 0, 0, 1, 0, 0], betti
    assert ranks[1:6] == [9, 36, 54, 25, 5], ranks
    return ranks, betti


def main():
    faces = generate()
    pairs, critical = make_matching(faces)
    arcs = check_acyclic(faces, pairs)
    ranks, betti = check_homology(faces)
    print('VERIFY_OK', f'faces={len(faces)}', f'matched_pairs={len(pairs)}',
          f'critical={sorted(critical)}', f'hasse_arcs={arcs}',
          f'F2_reduced_betti={betti}')

if __name__ == '__main__':
    main()
