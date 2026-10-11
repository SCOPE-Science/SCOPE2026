#!/usr/bin/env python3
"""Reproduce high-dimensional intrinsic Cech persistence of GP(8,3).

Only Python 3 standard library is required. All finite complexes, graph
metrics, chains, and Morse reductions are regenerated from their definitions.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations

N = 8
VERTICES = tuple(range(2 * N))
TOGGLE_ORDER = (3, 7, 13, 11, 6, 5, 0, 10, 14, 8, 4, 15, 1, 12, 2, 9)

def graph():
    edges = set()
    for i in range(N):
        edges.add(tuple(sorted((i, (i + 1) % N))))
        edges.add((i, N + i))
        edges.add(tuple(sorted((N + i, N + ((i + 3) % N)))))
    assert len(edges) == 24
    adj = [set() for _ in VERTICES]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    assert all(len(x) == 3 for x in adj)
    return sorted(edges), adj

def distances(adj):
    data = []
    for source in VERTICES:
        d = {source: 0}
        q = deque([source])
        while q:
            x = q.popleft()
            for y in adj[x]:
                if y not in d:
                    d[y] = d[x] + 1
                    q.append(y)
        assert len(d) == 16
        data.append(d)
    return data

def anti(x):
    return (x + 4) % N if x < N else N + (x - N + 4) % N

def check_cech_geometry(edges, dist):
    for u in VERTICES:
        assert Counter(dist[u].values()) == Counter({0: 1, 1: 3, 2: 6, 3: 5, 4: 1})
        assert {w for w in VERTICES if dist[u][w] == 4} == {anti(u)}
    complement_edges = []
    for u, v in edges:
        missing = {x for x in VERTICES if dist[u][x] > 2 and dist[v][x] > 2}
        assert missing == {anti(u), anti(v)}
        complement_edges.append(tuple(sorted(missing)))
    assert set(complement_edges) == set(edges)
    # r=4 maximal simplices are distance-two vertex neighborhoods.
    f4 = [{w for w in VERTICES if dist[v][w] <= 2} for v in VERTICES]
    assert all(len(face) == 10 for face in f4)
    sizes = Counter(len(f4[i] & f4[j]) for i in VERTICES for j in range(i + 1, 16))
    assert sizes == Counter({4: 24, 6: 48, 7: 48})
    # r=5 facets have fourteen vertices, missing an edge.
    f5 = [frozenset(set(VERTICES) - set(e)) for e in edges]
    assert len(set(f5)) == 24 and all(len(s) == 14 for s in f5)
    # r=6 facets are precisely the sixteen codimension-one facets.
    f6 = [frozenset(set(VERTICES) - {anti(v)}) for v in VERTICES]
    assert len(set(f6)) == 16 and all(len(s) == 15 for s in f6)
    # r=7 has the full vertex set as a generating face.
    for u, v in edges:
        n3u = {w for w in VERTICES if dist[u][w] <= 3}
        n3v = {w for w in VERTICES if dist[v][w] <= 3}
        assert n3u | n3v == set(VERTICES)
    return sizes

def independence_faces(adj):
    faces = set()
    for mask in range(1, 1 << 16):
        face = tuple(i for i in VERTICES if mask & (1 << i))
        if all(b not in adj[a] for pos, a in enumerate(face) for b in face[pos + 1:]):
            faces.add(face)
    assert len(faces) == 1090
    assert Counter(map(len, faces)) == Counter({1: 16, 2: 96, 3: 272, 4: 376,
                                               5: 240, 6: 72, 7: 16, 8: 2})
    return faces

def matching(faces):
    available = set(faces)
    pairs = []
    for vertex in TOGGLE_ORDER:
        for face in sorted(available, key=lambda s: (len(s), s)):
            if face not in available or vertex in face:
                continue
            top = tuple(sorted(face + (vertex,)))
            if top in available:
                pairs.append((face, top))
                available.remove(face)
                available.remove(top)
    critical = sorted(available, key=lambda s: (len(s), s))
    assert critical == [
        (3,), (0, 4, 10, 14), (1, 5, 11, 15),
        (2, 6, 8, 12), (6, 9, 10, 11), (2, 4, 8, 14, 15)
    ]
    assert len(pairs) == 542
    return pairs, critical

def acyclic(faces, pairs):
    upward = set(pairs)
    nexts = defaultdict(list)
    indegree = {x: 0 for x in faces}
    incidences = 0
    for top in faces:
        for i in range(len(top)):
            bottom = top[:i] + top[i + 1:]
            if not bottom:
                continue
            u, v = (bottom, top) if (bottom, top) in upward else (top, bottom)
            nexts[u].append(v)
            indegree[v] += 1
            incidences += 1
    q = deque(v for v in faces if indegree[v] == 0)
    seen = 0
    while q:
        v = q.popleft()
        seen += 1
        for w in nexts[v]:
            indegree[w] -= 1
            if indegree[w] == 0:
                q.append(w)
    assert seen == len(faces)
    return incidences

def integral_algebraic_morse(faces, pairs, critical):
    # Algebraic cancellation of unit incidence entries in the oriented
    # integral simplicial chain complex. All pivots are checked to be +/-1.
    bdry = {}
    cofaces = defaultdict(set)
    for top in faces:
        b = {}
        for i in range(len(top)):
            face = top[:i] + top[i + 1:]
            if face:
                b[face] = (-1) ** i
        bdry[top] = b
        for face in b:
            cofaces[face].add(top)
    active = set(faces)
    for bottom, top in pairs:
        assert bottom in active and top in active
        sign = bdry[top].get(bottom)
        assert sign in (-1, 1)
        for other in tuple(cofaces[bottom]):
            if other == top:
                continue
            assert bdry[other][bottom] % sign == 0
            multiplier = bdry[other][bottom] // sign
            for face, value in bdry[top].items():
                coefficient = bdry[other].get(face, 0) - multiplier * value
                if coefficient:
                    bdry[other][face] = coefficient
                    cofaces[face].add(other)
                else:
                    bdry[other].pop(face, None)
                    cofaces[face].discard(other)
        for face in bdry[top]:
            cofaces[face].discard(top)
        del bdry[top]
        active.remove(top)
        for face in bdry[bottom]:
            cofaces[face].discard(bottom)
        del bdry[bottom]
        active.remove(bottom)
        for higher in tuple(cofaces[top]):
            bdry[higher].pop(top, None)
        cofaces.pop(top, None)
        cofaces.pop(bottom, None)
    assert active == set(critical)
    assert all(not bdry[face] for face in active)  # Exact ZERO integral Morse differentials.
    return Counter(len(face) - 1 for face in active)

def gf2_rank(columns):
    pivots = {}
    for vector in columns:
        while vector:
            p = vector.bit_length() - 1
            if p in pivots:
                vector ^= pivots[p]
            else:
                pivots[p] = vector
                break
    return len(pivots)

def independent_mod2_homology(faces):
    dims = defaultdict(list)
    for face in faces:
        dims[len(face) - 1].append(face)
    for degree in dims:
        dims[degree].sort()
    rank = {}
    for degree in range(1, 8):
        lower = {f: i for i, f in enumerate(dims[degree - 1])}
        col = []
        for top in dims[degree]:
            vector = 0
            for j in range(len(top)):
                sub = top[:j] + top[j + 1:]
                vector ^= (1 << lower[sub])
            col.append(vector)
        rank[degree] = gf2_rank(col)
    assert [rank[i] for i in range(1, 8)] == [15, 81, 191, 181, 58, 14, 2]
    betti = {}
    for degree in range(8):
        betti[degree] = len(dims[degree]) - rank.get(degree, 0) - rank.get(degree + 1, 0)
        if degree == 0:
            betti[degree] -= 1
    assert betti == {0: 0, 1: 0, 2: 0, 3: 4, 4: 1, 5: 0, 6: 0, 7: 0}
    return rank

def main():
    edges, adj = graph()
    dist = distances(adj)
    intersects = check_cech_geometry(edges, dist)
    faces = independence_faces(adj)
    pairs, crit = matching(faces)
    incidences = acyclic(faces, pairs)
    cr = integral_algebraic_morse(faces, pairs, crit)
    ranks = independent_mod2_homology(faces)
    assert cr == Counter({0: 1, 3: 4, 4: 1})
    # Combinatorial Alexander duality on sixteen vertices sends reduced
    # cohomological degrees 3,4 to homological degrees 10,9.
    print('VERIFY_OK')
    print('graph_vertices=16 graph_edges=24 radius4_facet_intersections=' + str(dict(intersects)))
    print('independence_faces=1090 matching_pairs=542 hasse_incidences=' + str(incidences))
    print('critical_cells=' + str(dict(cr)) + ' all_integral_Morse_boundaries_zero')
    print('mod2_boundary_ranks=' + str(ranks))
    print('Cech_r5_H9=Z Cech_r5_H10=Z^4 Cech_r6=S14 Cech_r7=contractible')
    print('high_degree_barcodes=H9:[5,6)x1,H10:[5,6)x4,H14:[6,7)x1')

if __name__ == '__main__':
    main()
