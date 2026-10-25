"""Standalone finite certificate for the Witt-pentad avoidance complex.

Run with Python 3: python witt_verifier.py
All computations use exact finite set and integer operations.
"""
from collections import Counter, deque
from itertools import combinations

N = 11
BASE_PENTADS = (
    (0, 1, 3, 4, 7),
    (0, 1, 2, 7, 8),
    (0, 1, 5, 7, 9),
    (0, 1, 2, 6, 9),
    (0, 1, 3, 6, 8),
    (0, 1, 2, 3, 5),
)
FULL = (1 << N) - 1

def mask(points):
    return sum(1 << i for i in points)

def construct_blocks():
    blocks = set()
    for pentad in BASE_PENTADS:
        orbit = {mask(((i + t) % N for i in pentad)) for t in range(N)}
        assert len(orbit) == N
        assert not (blocks & orbit)
        blocks.update(orbit)
    assert len(blocks) == 66
    return blocks

def main():
    blocks = construct_blocks()
    # Each four-subset has exactly one containing pentad: S(4,5,11).
    incidence = Counter()
    for block in blocks:
        points = [i for i in range(N) if block & (1 << i)]
        assert len(points) == 5
        for four in combinations(points, 4):
            incidence[mask(four)] += 1
    assert len(incidence) == 330
    assert all(k == 1 for k in incidence.values())

    # Full face list, no five-point block is entirely present.
    faces = {s for s in range(1, FULL + 1)
             if not any(s & b == b for b in blocks)}
    vector = [sum(s.bit_count() == i for s in faces) for i in range(1, 7)]
    assert vector == [11, 55, 165, 330, 396, 66], vector
    assert all(s.bit_count() <= 6 for s in faces)

    # Additional structural checks: facets = complements of blocks;
    # every nonblock pentad belongs to exactly one free hexad.
    free6 = {s for s in faces if s.bit_count() == 6}
    assert free6 == {FULL ^ b for b in blocks}
    for pentad in (s for s in faces if s.bit_count() == 5):
        extensions = sum((pentad | (1 << i)) in faces
                         for i in range(N) if not pentad & (1 << i))
        assert extensions == 1

    # Canonical vertex-by-vertex discrete Morse matching.
    remaining = set(faces)
    pairs = []
    per_vertex = []
    for i in range(N):
        matched_here = []
        for low in sorted(remaining, key=lambda x: (x.bit_count(), x)):
            if low & (1 << i):
                continue
            high = low | (1 << i)
            if high in remaining:
                matched_here.append((low, high))
        for low, high in matched_here:
            assert low in remaining and high in remaining
            assert (low & ~high) == 0 and (high ^ low) == (1 << i)
            remaining.remove(low)
            remaining.remove(high)
        pairs.extend(matched_here)
        per_vertex.append(len(matched_here))
    critical = Counter(s.bit_count() - 1 for s in remaining)
    assert per_vertex == [391, 36, 16, 6, 2, 0, 0, 0, 0, 0, 0]
    assert len(pairs) == 451 and critical == {0: 1, 4: 120}, critical

    # Every Hasse edge directed up if matched, down otherwise;
    # a topological sort certifies there is NO directed cycle.
    pair_set = set(pairs)
    indegree = {s: 0 for s in faces}
    adjacency = {s: [] for s in faces}
    edges = 0
    for high in faces:
        for i in range(N):
            if not high & (1 << i):
                continue
            low = high ^ (1 << i)
            if low == 0:
                continue
            assert low in faces
            tail, head = (low, high) if (low, high) in pair_set else (high, low)
            adjacency[tail].append(head)
            indegree[head] += 1
            edges += 1
    queue = deque(s for s in faces if indegree[s] == 0)
    seen = 0
    while queue:
        a = queue.popleft()
        seen += 1
        for b in adjacency[a]:
            indegree[b] -= 1
            if indegree[b] == 0:
                queue.append(b)
    assert seen == len(faces), (seen, len(faces))
    print('STEINER_4_DESIGN_OK 66 pentads, 330 uniquely covered tetrads')
    print('FACE_VECTOR', *vector)
    print('SELF_ALEXANDER_DUAL_OK 66 hexad facets')
    print('MORSE_PAIRS_BY_VERTEX', *per_vertex)
    print('CRITICAL_CELLS', sorted(critical.items()))
    print('HASSE_EDGES', edges, 'TOPOSORT_VISITED', seen)
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
