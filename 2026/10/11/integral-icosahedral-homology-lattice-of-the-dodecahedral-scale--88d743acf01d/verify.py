#!/usr/bin/env python3
"""Exact finite verification of the full dodecahedral Rips homology character.

No third-party dependencies. The literature supplies the nonequivariant homology
concentration; the present script verifies every group character value and
its representation-theoretic identification by exact integer enumeration.
"""
from collections import Counter, deque
from itertools import combinations

N = 20
EDGES = ((0,1),(0,10),(0,19),(1,2),(1,8),(2,3),(2,6),(3,4),(3,19),
         (4,5),(4,17),(5,6),(5,15),(6,7),(7,8),(7,14),(8,9),(9,10),
         (9,13),(10,11),(11,12),(11,18),(12,13),(12,16),(13,14),
         (14,15),(15,16),(16,17),(17,18),(18,19))
GEN3 = (0,19,18,11,12,16,17,4,3,2,1,8,7,6,5,15,14,13,9,10)
GEN5 = (10,0,19,18,17,4,3,2,1,8,9,13,14,7,6,5,15,16,12,11)
INV = (15,16,12,13,9,10,11,18,17,4,5,6,2,3,19,0,1,8,7,14)
IDENTITY = tuple(range(N))


def mul(p, q):
    return tuple(p[q[v]] for v in range(N))


def closure(generators):
    seen = {IDENTITY}
    queue = [IDENTITY]
    for p in queue:
        for q in generators:
            r = mul(p, q)
            if r not in seen:
                seen.add(r)
                queue.append(r)
    return seen


def parity_of_permutation(sequence):
    return -1 if sum(sequence[i] > sequence[j]
                     for i in range(len(sequence))
                     for j in range(i + 1, len(sequence))) % 2 else 1


def main():
    assert len(EDGES) == 30
    adj = [set() for _ in range(N)]
    for u, v in EDGES:
        assert 0 <= u < v < N and v not in adj[u]
        adj[u].add(v)
        adj[v].add(u)
    assert {len(a) for a in adj} == {3}

    distance = [[None] * N for _ in range(N)]
    for root in range(N):
        distance[root][root] = 0
        todo = deque([root])
        while todo:
            u = todo.popleft()
            for v in adj[u]:
                if distance[root][v] is None:
                    distance[root][v] = distance[root][u] + 1
                    todo.append(v)
    assert {max(row) for row in distance} == {5}
    assert tuple(row.index(5) for row in distance) == INV

    # Build every nonempty clique inductively, using the graph-distance <= 3 rule.
    near3 = [set(v for v in range(N) if v != u and distance[u][v] <= 3)
             for u in range(N)]
    faces_by_size = {1: {(v,) for v in range(N)}}
    for size in range(2, N + 1):
        grown = set()
        for face in faces_by_size[size - 1]:
            for v in range(face[-1] + 1, N):
                if all(v in near3[u] for u in face):
                    grown.add(face + (v,))
        if not grown:
            break
        faces_by_size[size] = grown
    fvector = tuple(len(faces_by_size[k]) for k in sorted(faces_by_size))
    assert fvector == (20, 150, 540, 1000, 972, 490, 100), fvector
    assert sum((-1)**(k - 1) * len(v) for k, v in faces_by_size.items()) == -8

    # Independent complete mod-two augmented chain-complex rank computation.
    ranks = {0: 1}
    for size in range(2, len(fvector) + 1):
        lower = sorted(faces_by_size[size - 1])
        index = {f: i for i, f in enumerate(lower)}
        pivots = {}
        for face in sorted(faces_by_size[size]):
            col = 0
            for omitted in range(size):
                facet = face[:omitted] + face[omitted + 1:]
                col ^= 1 << index[facet]
            while col:
                leading = col.bit_length() - 1
                if leading not in pivots:
                    pivots[leading] = col
                    break
                col ^= pivots[leading]
        ranks[size - 1] = len(pivots)
    ranks[len(fvector)] = 0
    reduced_betti = tuple(fvector[k] - ranks[k] - ranks[k + 1]
                          for k in range(len(fvector)))
    assert reduced_betti == (0, 0, 0, 9, 0, 0, 0), reduced_betti

    rotations = closure([GEN3, GEN5])
    group = closure([GEN3, GEN5, INV])
    assert len(rotations) == 60 and len(group) == 120
    assert all(set((min(p[u], p[v]), max(p[u], p[v])) for u, v in EDGES)
               == set(EDGES) for p in group)
    assert mul(INV, INV) == IDENTITY
    assert all(mul(INV, p) == mul(p, INV) for p in group)
    assert rotations.isdisjoint({mul(INV, h) for h in rotations})

    # The ten pairwise-distance-3 tetrahedra, split into two 5-point orbits.
    special = {t for t in combinations(range(N), 4)
               if all(distance[u][v] == 3 for u, v in combinations(t, 2))}
    assert len(special) == 10
    # The ten tetrahedra are maximal, making their deletion a subcomplex.
    assert not any(set(t).issubset(set(face)) for t in special
                   for size, faces in faces_by_size.items() if size > 4
                   for face in faces)
    representative = min(special)
    orbit = {tuple(sorted(h[i] for i in representative)) for h in rotations}
    assert len(orbit) == 5 and orbit <= special
    assert {tuple(sorted(INV[i] for i in t)) for t in orbit} == special - orbit
    ordered_pairs = {(tuple(sorted(h[i] for i in a)),
                      tuple(sorted(h[i] for i in b)))
                     for h in rotations for a, b in [tuple(sorted(orbit))[:2]]}
    assert len(ordered_pairs) == 20  # A5 acts doubly transitively on five tetra.

    # Lefschetz trace: each setwise fixed simplex contributes orientation sign.
    # Source theorem: reduced rational homology is Q^9 in degree three only.
    counts = Counter()
    for g in sorted(group):
        tr = [0] * len(fvector)
        for k, faces in faces_by_size.items():
            for face in faces:
                image = tuple(g[u] for u in face)
                if tuple(sorted(image)) == face:
                    tr[k - 1] += parity_of_permutation(image)
        lefschetz = sum((-1) ** i * t for i, t in enumerate(tr))
        character = 1 - lefschetz
        if g in rotations:
            fixed_tetra = sum(tuple(sorted(g[i] for i in t)) == t for t in orbit)
            expected = 2 * fixed_tetra - 1
        else:
            fixed_tetra = None
            expected = 1
        assert character == expected, (g, character, expected, tr)
        counts[('rotation' if g in rotations else 'inversion_coset', character,
                fixed_tetra)] += 1
    assert sum(n for key, n in counts.items() if key[0] == 'rotation') == 60
    assert sum(n for key, n in counts.items() if key[0] == 'inversion_coset') == 60
    assert counts[('rotation', 9, 5)] == 1
    assert counts[('rotation', 1, 1)] == 15
    assert counts[('rotation', 3, 2)] == 20
    assert counts[('rotation', -1, 0)] == 24
    assert counts[('inversion_coset', 1, None)] == 60
    print('VERTICES', N, 'EDGES', len(EDGES), 'DIAMETER', 5)
    print('F_VECTOR', fvector)
    print('MOD2_BOUNDARY_RANKS', tuple(ranks[k] for k in range(len(fvector) + 1)))
    print('MOD2_REDUCED_BETTI', reduced_betti)
    print('ROTATIONS', len(rotations), 'FULL_GROUP', len(group))
    print('SPECIAL_TETRA', len(special), 'ROTATION_ORBIT_SIZES', (5, 5))
    print('CHARACTER_MULTIPLICITIES', sorted(counts.items(), key=str))
    print('INVARIANTS_H', sum((2 * sum(tuple(sorted(g[i] for i in t)) == t
                          for t in orbit) - 1) for g in rotations) // 60)
    print('INVARIANTS_G', (sum((2 * sum(tuple(sorted(g[i] for i in t)) == t
                          for t in orbit) - 1) for g in rotations) + 60) // 120)
    # Actual averaging formula including the extra 60 inversion-coset traces.
    assert (sum(2*sum(tuple(sorted(g[i] for i in t)) == t for t in orbit)-1
                for g in rotations) + 60) // 120 == 1
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
