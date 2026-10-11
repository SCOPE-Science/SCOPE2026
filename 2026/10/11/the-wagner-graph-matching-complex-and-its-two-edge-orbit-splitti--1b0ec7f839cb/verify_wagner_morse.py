#!/usr/bin/env python3
"""Exact reproducible discrete Morse certificate for ordinary matching complexes.
All Hasse arrows are tested, not just a sample. Python standard library only.
"""
from collections import Counter, deque

EDGES = tuple(sorted(
    {tuple(sorted((i, (i + 1) % 8))) for i in range(8)}
    | {(i, i + 4) for i in range(4)}
))
assert len(EDGES) == 12
CYCLE = (0, 1)
RUNG = (0, 4)
CASES = {
    'whole': (EDGES, tuple(reversed(range(12))), (12, 42, 44, 7), {0: 1, 2: 6}, 49),
    'cycle_delete': (
        tuple(e for e in EDGES if e != CYCLE),
        (4, 2, 9, 7, 5, 0, 10, 8, 1, 6, 3),
        (11, 35, 33, 5), {0: 1, 2: 3}, 40,
    ),
    'cycle_link': (
        tuple(e for e in EDGES if set(e).isdisjoint(CYCLE)),
        tuple(range(7)), (7, 11, 2), {0: 1, 1: 3}, 8,
    ),
    'rung_delete': (
        tuple(e for e in EDGES if e != RUNG),
        tuple(range(11)), (11, 35, 33, 4), {0: 1, 2: 4}, 39,
    ),
    'rung_link': (
        tuple(e for e in EDGES if set(e).isdisjoint(RUNG)),
        tuple(range(7)), (7, 11, 3), {0: 1, 1: 2}, 9,
    ),
}

def all_matching_faces(edges):
    result = set()
    for face in range(1, 1 << len(edges)):
        chosen = [edges[i] for i in range(len(edges)) if (face >> i) & 1]
        endpoints = [u for e in chosen for u in e]
        if len(endpoints) == len(set(endpoints)):
            result.add(face)
    return result

def pair_faces(faces, order, n):
    assert sorted(order) == list(range(n))
    remaining = set(faces)
    pairs = []
    for i in order:
        bit = 1 << i
        candidate_lower = sorted(
            x for x in remaining if not (x & bit) and (x | bit) in remaining
        )
        for lo in candidate_lower:
            hi = lo | bit
            assert lo in remaining and hi in remaining
            assert hi.bit_count() == lo.bit_count() + 1
            remaining.remove(lo)
            remaining.remove(hi)
            pairs.append((lo, hi))
    assert len(set(y for pair in pairs for y in pair)) == 2 * len(pairs)
    assert len(faces) == 2 * len(pairs) + len(remaining)
    return pairs, remaining

def verify_acyclic(faces, pairs):
    """Matched Hasse cover is directed UP; every other cover directed DOWN."""
    matched = set(pairs)
    adj = {x: [] for x in faces}
    indegree = {x: 0 for x in faces}
    directed_incidences = 0
    for hi in faces:
        for i in range(hi.bit_length()):
            if hi & (1 << i):
                lo = hi ^ (1 << i)
                if lo not in faces:
                    continue   # nonempty face poset: exclude empty face
                u, v = (lo, hi) if (lo, hi) in matched else (hi, lo)
                adj[u].append(v)
                indegree[v] += 1
                directed_incidences += 1
    queue = deque(x for x, k in indegree.items() if k == 0)
    removed = 0
    while queue:
        x = queue.popleft()
        removed += 1
        for y in adj[x]:
            indegree[y] -= 1
            if indegree[y] == 0:
                queue.append(y)
    assert removed == len(faces), (removed, len(faces))
    return directed_incidences

def symmetry_orbits():
    e2i = {e: i for i, e in enumerate(EDGES)}
    classes = []
    for e in EDGES:
        images = set()
        for t in range(8):
            for sign in (-1, 1):
                def f(v): return (sign * v + t) % 8
                ee = tuple(sorted((f(e[0]), f(e[1]))))
                assert ee in e2i
                images.add(ee)
        classes.append(frozenset(images))
    assert len(set(classes)) == 2
    assert {len(x) for x in classes} == {4, 8}
    assert CYCLE in next(x for x in classes if len(x) == 8)
    assert RUNG in next(x for x in classes if len(x) == 4)
    return (8, 4)

if __name__ == '__main__':
    print('GRAPH', 'vertices=8', 'edges=12', 'edge_orbits=', symmetry_orbits())
    for name, (edges, order, expected_fvec, expected_critical, expected_pairs) in CASES.items():
        fs = all_matching_faces(edges)
        fvec = Counter(x.bit_count() - 1 for x in fs)
        actual_fvec = tuple(fvec.get(i, 0) for i in range(len(expected_fvec)))
        assert actual_fvec == expected_fvec, (name, actual_fvec)
        pairs, critical = pair_faces(fs, order, len(edges))
        counts = Counter(x.bit_count() - 1 for x in critical)
        assert counts == expected_critical, (name, counts)
        assert len(pairs) == expected_pairs, (name, len(pairs))
        covers = verify_acyclic(fs, pairs)
        print(name, 'faces=', len(fs), 'f_vector=', actual_fvec,
              'paired=', len(pairs), 'critical=', dict(sorted(counts.items())),
              'checked_hasse_covers=', covers, 'acyclic=True')
    print('VERIFY_OK: exact acyclic matchings, all faces and dihedral edge orbits')
