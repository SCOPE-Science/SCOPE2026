#!/usr/bin/env python3
"""Exact finite certificate for the scale-three intrinsic Cech nerve of PG(2,3)."""
from collections import Counter, defaultdict
from heapq import heappop, heappush
from itertools import combinations, product

Q = 3

def projective_points():
    classes = set()
    for v in product(range(Q), repeat=3):
        if not any(v):
            continue
        first = next(x for x in v if x)
        classes.add(tuple(x * pow(first, -1, Q) % Q for x in v))
    return sorted(classes)

def incidence_graph():
    points = projective_points()
    assert len(points) == 13
    n = len(points)
    adj = [set() for _ in range(2*n)]
    for i, point in enumerate(points):
        for j, line in enumerate(points):
            if sum(a*b for a, b in zip(point, line)) % Q == 0:
                adj[i].add(n+j)
                adj[n+j].add(i)
    assert all(len(a) == 4 for a in adj)
    for i, j in combinations(range(n), 2):
        assert len(adj[i] & adj[j]) == 1
        assert len(adj[n+i] & adj[n+j]) == 1
    return adj

def facets_of_radius_three(adj):
    n = len(adj)//2
    facets = []
    for p in range(n):
        for l in sorted(adj[p]):
            facet = {p, l} | adj[p] | adj[l]
            facets.append(sum(1<<v for v in facet))
    assert len(facets) == 52 and len(set(facets)) == 52
    assert all(f.bit_count() == 8 for f in facets)
    return facets

def all_nonempty_faces(facets):
    faces = set()
    for facet in facets:
        bits = [1<<i for i in range(26) if facet & (1<<i)]
        for k in range(1, len(bits)+1):
            for selection in combinations(bits, k):
                faces.add(sum(selection))
    return faces

def face_vector(faces):
    count = Counter(face.bit_count()-1 for face in faces)
    return tuple(count[d] for d in range(max(count)+1))

def verify_full_star(faces):
    # Every two vertices lie in some facet, hence the 1-skeleton is complete.
    assert all(((1<<i)|(1<<j)) in faces
               for i, j in combinations(range(26), 2))
    triangles = [face for face in faces if face.bit_count() == 3]
    # Basepoint 0 and the star tree determine 300 chord generators.
    killed = set()
    for face in triangles:
        if face & 1:
            other = tuple(i for i in range(1,26) if face & (1<<i))
            assert len(other) == 2
            killed.add(other)
    changed = True
    while changed:
        changed = False
        for face in triangles:
            if face & 1:
                continue
            indices = [i for i in range(1,26) if face & (1<<i)]
            edges = list(combinations(indices, 2))
            if sum(edge in killed for edge in edges) >= 2:
                for edge in edges:
                    if edge not in killed:
                        killed.add(edge)
                        changed = True
    assert len(killed) == 300 == len(list(combinations(range(1,26),2)))
    return len(killed)

def elementary_collapses(faces):
    active = set(faces)
    # immediate[small] is the *complete* set of active codimension-one cofaces
    immediate = defaultdict(set)
    for larger in active:
        remaining = larger
        while remaining:
            bit = remaining & -remaining
            remaining -= bit
            smaller = larger ^ bit
            if smaller:
                immediate[smaller].add(larger)
    candidates = []
    for small in active:
        if len(immediate[small]) == 1:
            heappush(candidates, (-small.bit_count(), small))
    pairs = 0
    while candidates:
        _, small = heappop(candidates)
        if small not in active or len(immediate[small]) != 1:
            continue
        large = next(iter(immediate[small]))
        if large not in active or immediate[large]:
            continue
        assert large.bit_count() == small.bit_count()+1
        assert large & small == small
        for deleted in (small, large):
            active.remove(deleted)
            b = deleted
            while b:
                bit = b & -b
                b -= bit
                subface = deleted ^ bit
                if subface in active:
                    immediate[subface].remove(deleted)
                    if len(immediate[subface]) == 1:
                        heappush(candidates, (-subface.bit_count(), subface))
        pairs += 1
    # Independent simplicial-closure check of every surviving face.
    for f in active:
        for i in range(26):
            if f & (1<<i):
                smaller = f ^ (1<<i)
                if smaller:
                    assert smaller in active
    return active, pairs

def rank_mod2(vectors):
    pivots = {}
    for col in vectors:
        while col:
            lead = col.bit_length()-1
            if lead not in pivots:
                pivots[lead] = col
                break
            col ^= pivots[lead]
    return len(pivots)

def independent_homology_check(active):
    vertices = sorted(face for face in active if face.bit_count() == 1)
    edges = sorted(face for face in active if face.bit_count() == 2)
    triangles = sorted(face for face in active if face.bit_count() == 3)
    edge_index = {edge: j for j, edge in enumerate(edges)}
    vindex = {v: j for j, v in enumerate(vertices)}
    d1 = []
    for edge in edges:
        ends = [bit for bit in vertices if bit & edge]
        assert len(ends) == 2
        d1.append(sum(1<<vindex[bit] for bit in ends))
    d2 = []
    for triangle in triangles:
        edges_of_triangle = [edge for edge in edges if edge & triangle == edge]
        assert len(edges_of_triangle) == 3
        d2.append(sum(1<<edge_index[edge] for edge in edges_of_triangle))
    assert rank_mod2(d1) == 25
    assert rank_mod2(d2) == 183
    assert 507-183 == 324
    assert 208-25-183 == 0
    return (25,183)

def main():
    adj = incidence_graph()
    facets = facets_of_radius_three(adj)
    faces = all_nonempty_faces(facets)
    assert len(faces) == 10491
    assert face_vector(faces) == (26,325,2132,3250,2834,1456,416,52)
    assert verify_full_star(faces) == 300
    active, npairs = elementary_collapses(faces)
    assert npairs == 4875
    assert len(active) == 741 and face_vector(active) == (26,208,507)
    assert independent_homology_check(active) == (25,183)
    assert 26-208+507-1 == 324
    print('PG(2,3): vertices=26; edge-facets=52; nonempty faces=10491')
    print('Full f-vector=(26,325,2132,3250,2834,1456,416,52)')
    print('Exact elementary free-face pairs=4875; residual f-vector=(26,208,507)')
    print('Triangle relations kill all 300 fundamental-group chord generators')
    print('mod-2 residual ranks: boundary_1=25, boundary_2=183')
    print('Simply connected 2-complex; reduced integral H_2=Z^324')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
