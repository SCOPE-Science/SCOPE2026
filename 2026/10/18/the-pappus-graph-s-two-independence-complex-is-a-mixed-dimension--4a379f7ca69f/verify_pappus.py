#!/usr/bin/env python3
"""Exact independent verification of the two-independence complex of the Pappus graph.
Run with Python 3.10+; only the standard library is needed.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache

N_VERTICES = 18
LCF = (5, 7, -7, 7, -7, -5) * 3
TOGGLE_ORDER = (7, 12, 17, 11, 13, 10, 0, 9, 2, 4, 14, 5, 6, 15, 8, 3, 16, 1)
EXPECTED_F = (18, 153, 762, 2394, 4806, 6027, 4428, 1728, 308, 27)
EXPECTED_CRITICAL = {
    0x6621, 0xcc03, 0x12264, 0x18846, 0x20b18,
    0x22360, 0x2c409, 0x2c902, 0x3404c, 0x3212a,
}


def graph():
    edges = set()
    for v in range(N_VERTICES):
        for w in ((v + 1) % N_VERTICES, (v + LCF[v]) % N_VERTICES):
            edges.add(tuple(sorted((v, w))))
    assert len(edges) == 27
    neighbors = [0] * N_VERTICES
    for u, v in edges:
        neighbors[u] |= 1 << v
        neighbors[v] |= 1 << u
    assert all(n.bit_count() == 3 for n in neighbors)
    return neighbors


def valid_faces(neighbors):
    # Direct construction: reject every induced vertex of degree >= 2.
    # Every induced component then has one or two vertices, and conversely.
    return {
        face for face in range(1 << N_VERTICES)
        if all((neighbors[v] & face).bit_count() <= 1
               for v in range(N_VERTICES) if face >> v & 1)
    }


def staged_matching(faces):
    remain = set(faces)
    upwards, downwards = {}, {}
    for v in TOGGLE_ORDER:
        bit = 1 << v
        eligible = [(face, face | bit) for face in remain
                    if face & bit == 0 and (face | bit) in remain]
        for lower, upper in eligible:
            assert lower in remain and upper in remain
            remain.remove(lower)
            remain.remove(upper)
            upwards[lower] = upper
            downwards[upper] = lower
    return upwards, downwards, remain


def gradient_dag(faces, upwards):
    # Every Hasse cover: unmatched upper -> lower; matched lower -> upper.
    out = defaultdict(list)
    indegree = {face: 0 for face in faces}
    cover_count = 0
    for upper in faces:
        for v in range(N_VERTICES):
            if upper >> v & 1:
                lower = upper ^ (1 << v)
                assert lower in faces
                a, b = (lower, upper) if upwards.get(lower) == upper else (upper, lower)
                out[a].append(b)
                indegree[b] += 1
                cover_count += 1
    queue = deque(v for v in faces if indegree[v] == 0)
    visited = 0
    while queue:
        face = queue.popleft()
        visited += 1
        for other in out[face]:
            indegree[other] -= 1
            if indegree[other] == 0:
                queue.append(other)
    assert visited == len(faces), ('gradient cycle', visited)
    return cover_count


def morse_boundary(upwards, critical):
    critical_five = {face: i for i, face in enumerate(sorted(
        f for f in critical if f.bit_count() == 6))}
    critical_six = [f for f in critical if f.bit_count() == 7]
    assert len(critical_five) == 9 and len(critical_six) == 1

    @lru_cache(None)
    def project(face):
        if face in critical_five:
            return {critical_five[face]: 1}
        if face not in upwards:
            # A dimension-five cell matched with a dimension-four cell.
            return {}
        upper = upwards[face]
        verts = [j for j in range(N_VERTICES) if upper >> j & 1]
        added = (upper ^ face).bit_length() - 1
        sign_pivot = (-1) ** verts.index(added)
        total = Counter()
        for index, vertex in enumerate(verts):
            subface = upper ^ (1 << vertex)
            if subface == face:
                continue
            for target, amount in project(subface).items():
                total[target] -= sign_pivot * (-1) ** index * amount
        return {k: v for k, v in total.items() if v}

    upper = critical_six[0]
    boundary = Counter()
    for index, v in enumerate(i for i in range(N_VERTICES) if upper >> i & 1):
        for target, amount in project(upper ^ (1 << v)).items():
            boundary[target] += (-1) ** index * amount
    vector = [boundary[j] for j in range(9)]
    assert vector == [0] * 9, vector
    return vector, project.cache_info().currsize


def modular_ranks(faces):
    # Direct augmented simplicial chain homology over F_2; no Morse matching.
    by_size = defaultdict(list)
    for face in sorted(faces):
        by_size[face.bit_count()].append(face)
    assert len(by_size[0]) == 1
    ranks = []
    for size in range(1, 11):
        rows = {face: i for i, face in enumerate(by_size[size - 1])}
        pivots = {}
        for face in by_size[size]:
            col = 0
            for v in range(N_VERTICES):
                if face >> v & 1:
                    col ^= 1 << rows[face ^ (1 << v)]
            while col:
                pivot = col.bit_length() - 1
                if pivot not in pivots:
                    pivots[pivot] = col
                    break
                col ^= pivots[pivot]
        ranks.append(len(pivots))
    expected = (1, 17, 136, 626, 1768, 3038, 2980, 1447, 281, 27)
    assert tuple(ranks) == expected, ranks
    betti = []
    for d in range(10):
        c = len(by_size[d + 1])
        incoming = ranks[d]
        outgoing = ranks[d + 1] if d < 9 else 0
        betti.append(c - incoming - outgoing)
    assert betti == [0, 0, 0, 0, 0, 9, 1, 0, 0, 0], betti
    return ranks, betti


def main():
    neighbors = graph()
    faces = valid_faces(neighbors)
    fvector = tuple(sum(1 for f in faces if f.bit_count() == k) for k in range(1, 11))
    assert fvector == EXPECTED_F
    assert len(faces) == 20652  # includes empty simplex
    up, down, critical = staged_matching(faces)
    assert len(up) == len(down) == 10321
    assert critical == EXPECTED_CRITICAL
    assert sum((-1) ** d * n for d, n in enumerate(fvector)) - 1 == -8
    covers = gradient_dag(faces, up)
    assert covers == sum((d+1)*f for d,f in enumerate(fvector))
    vector, visited = morse_boundary(up, critical)
    ranks, betti = modular_ranks(faces)
    print('Pappus graph: 18 vertices, 27 edges; Ind_2 faces:', len(faces)-1)
    print('f-vector:', fvector)
    print('matching pairs:', len(up), 'critical cell dimensions:', dict(Counter(f.bit_count()-1 for f in critical)))
    print('Hasse covers checked:', covers, 'acyclic: yes')
    print('exact integral Morse boundary:', vector, 'projection states:', visited)
    print('augmented F2 boundary ranks:', ranks)
    print('reduced F2 Betti degrees 0..9:', betti)
    print('PASS: homotopy equivalence S^6 wedge nine S^5')

if __name__ == '__main__':
    main()
