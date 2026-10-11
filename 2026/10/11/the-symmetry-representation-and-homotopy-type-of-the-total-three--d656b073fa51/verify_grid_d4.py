#!/usr/bin/env python3
"""Reconstruct and verify the total three-cut complex of the 4x4 grid.

Pure Python 3 standard library; all simplices, matchings, and symmetry traces
are rebuilt directly from the graph definition. No external logs or packages.
"""
from itertools import combinations
from collections import Counter, deque

SIDE = 4
N = SIDE * SIDE
ALL = (1 << N) - 1


def grid_edges():
    result = set()
    for r in range(SIDE):
        for c in range(SIDE):
            u = SIDE * r + c
            for dr, dc in ((1, 0), (0, 1)):
                rr, cc = r + dr, c + dc
                if rr < SIDE and cc < SIDE:
                    v = SIDE * rr + cc
                    result.add((u, v))
    return result


def make_complex():
    edges = grid_edges()
    assert len(edges) == 24
    adjacent = [0] * N
    for u, v in edges:
        adjacent[u] |= 1 << v
        adjacent[v] |= 1 << u
    triples = []
    for t in combinations(range(N), 3):
        if all(not (adjacent[u] & (1 << v))
               for u, v in combinations(t, 2)):
            triples.append(t)
    assert len(triples) == 276
    faces = bytearray(1 << N)
    faces[0] = 1
    for t in triples:
        facet = ALL ^ sum(1 << x for x in t)
        sub = facet
        while sub:
            faces[sub] = 1
            sub = (sub - 1) & facet
    face_vector = Counter(mask.bit_count()-1 for mask in range(1 << N)
                          if faces[mask] and mask)
    assert sum(face_vector.values()) == 64899
    assert sum(faces) == 64900
    assert face_vector[12] == 276
    return faces, face_vector


def verify_morse(faces):
    remaining = bytearray(faces)
    mates = [-1] * (1 << N)
    pairs_by_vertex = []
    for v in range(N):
        bit = 1 << v
        count = 0
        for mask in range(1 << N):
            if remaining[mask] and not (mask & bit) and remaining[mask | bit]:
                large = mask | bit
                assert mates[mask] < 0 and mates[large] < 0
                mates[mask], mates[large] = large, mask
                remaining[mask] = remaining[large] = 0
                count += 1
        pairs_by_vertex.append(count)
    critical = [s for s in range(1 << N) if remaining[s]]
    assert len(critical) == 36
    assert all(mask.bit_count() == 11 for mask in critical)
    assert sum(pairs_by_vertex) == (sum(faces) - len(critical)) // 2 == 32432
    assert not remaining[0]

    # Independent Hasse-diagram acyclicity test, including the empty face.
    # On each codimension-one edge, orient unmatched upward and matched downward.
    indeg = [0] * (1 << N)
    directed = [[] for _ in range(1 << N)]
    n_arcs = 0
    for mask in range(1 << N):
        if not faces[mask]:
            continue
        for v in range(N):
            bit = 1 << v
            if mask & bit:
                continue
            larger = mask | bit
            if not faces[larger]:
                continue
            if mates[mask] == larger:
                src, dst = larger, mask
            else:
                src, dst = mask, larger
            directed[src].append(dst)
            indeg[dst] += 1
            n_arcs += 1
    queue = deque(s for s in range(1 << N) if faces[s] and indeg[s] == 0)
    visited = 0
    while queue:
        u = queue.popleft()
        visited += 1
        for w in directed[u]:
            indeg[w] -= 1
            if indeg[w] == 0:
                queue.append(w)
    assert visited == sum(faces), (visited, sum(faces))
    return critical, pairs_by_vertex, n_arcs


def grid_permutation(transform):
    out = []
    for p in range(N):
        r, c = divmod(p, SIDE)
        rr, cc = transform(r, c)
        out.append(rr * SIDE + cc)
    assert sorted(out) == list(range(N))
    return out


def cycle_decomposition(perm):
    visited = set()
    cycles = []
    for v in range(N):
        if v in visited:
            continue
        cur = v
        orbit = []
        while cur not in visited:
            visited.add(cur)
            orbit.append(cur)
            cur = perm[cur]
        assert cur == v
        cycles.append(orbit)
    return cycles


def signed_trace(faces, perm):
    cycles = cycle_decomposition(perm)
    orbit_masks = [sum(1 << v for v in orbit) for orbit in cycles]
    reduced = 0
    for selection in range(1 << len(cycles)):
        mask = 0
        for j, orbit_mask in enumerate(orbit_masks):
            if selection & (1 << j):
                mask |= orbit_mask
        if not faces[mask]:
            continue
        # An invariant simplex has sign (-1)^(|sigma|-number_of_orbits).
        # Including the empty face, its reduced Lefschetz contribution is
        # (-1)^(|sigma|-1) times this sign = (-1)^(orbits+1).
        reduced += -1 if selection.bit_count() % 2 == 0 else 1
    return reduced


def verify_representation(faces):
    f = {
        'e': lambda r, c: (r, c),
        'r': lambda r, c: (c, 3-r),
        'r2': lambda r, c: (3-r, 3-c),
        'r3': lambda r, c: (3-c, r),
        'v': lambda r, c: (r, 3-c),
        'h': lambda r, c: (3-r, c),
        'd': lambda r, c: (c, r),
        'a': lambda r, c: (3-c, 3-r),
    }
    perms = {name: grid_permutation(fn) for name, fn in f.items()}
    assert len({tuple(perm) for perm in perms.values()}) == 8
    assert all({tuple(sorted((perm[u], perm[v]))) for u,v in grid_edges()}
               == grid_edges() for perm in perms.values())
    traces = {name: signed_trace(faces, p) for name,p in perms.items()}
    assert traces == {'e':36, 'r':0, 'r2':4, 'r3':0,
                      'v':6, 'h':6, 'd':6, 'a':6}, traces
    # Separately reconstruct the 3x3 unit-square action and its
    # permutation representation on the 36 unordered distinct square pairs.
    square_pairs = list(combinations(range(9), 2))
    pair_traces = {}
    for name, fn in f.items():
        square_permutation = []
        for sr in range(3):
            for sc in range(3):
                square_corners = {(sr, sc), (sr+1, sc),
                                  (sr, sc+1), (sr+1, sc+1)}
                image_corners = [fn(rr,cc) for rr,cc in square_corners]
                rr = min(x[0] for x in image_corners)
                cc = min(x[1] for x in image_corners)
                assert set(image_corners) == {(rr,cc),(rr+1,cc),
                                              (rr,cc+1),(rr+1,cc+1)}
                square_permutation.append(3*rr+cc)
        assert sorted(square_permutation) == list(range(9))
        pair_traces[name] = sum({square_permutation[x],
                                  square_permutation[y]} == {x,y}
                                 for x,y in square_pairs)
    assert pair_traces == traces, (pair_traces,traces)
    class_sizes = [1,1,2,2,2]
    class_trace = [traces[x] for x in ('e','r2','r','v','d')]
    char_table = {
       'A1': [1,1,1,1,1], 'A2':[1,1,1,-1,-1],
       'B1':[1,1,-1,1,-1], 'B2':[1,1,-1,-1,1],
       'E':[2,-2,0,0,0],
    }
    mult = {}
    for name, char in char_table.items():
        numerator = sum(z*t*x for z,t,x in zip(class_sizes, class_trace, char))
        assert numerator % 8 == 0
        mult[name] = numerator // 8
        assert mult[name] >= 0
    assert mult == {'A1':8,'A2':2,'B1':5,'B2':5,'E':8}, mult
    assert sum(mult[name]*char[0] for name,char in char_table.items()) == 36
    return traces, mult


def main():
    faces, face_vector = make_complex()
    critical, pairs_by_vertex, arcs = verify_morse(faces)
    traces, mult = verify_representation(faces)
    print('facet_count=276 face_count=64900 critical_10_cells=36')
    print('face_vector', sorted(face_vector.items()))
    print('pairs_by_vertex', pairs_by_vertex, 'hasse_arcs', arcs)
    print('reduced_lefschetz_traces', traces)
    print('D4_multiplicities', mult)
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
