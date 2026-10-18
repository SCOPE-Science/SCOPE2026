#!/usr/bin/env python3
"""Standalone finite certificate for an octagonal Alexander-dual sphere.

The unbounded block-retraction argument is mathematical; the finite loops
below are consistency tests, not an exhaustive proof over all parameters.
"""
from collections import Counter, defaultdict
from itertools import combinations

PAIRS = (
    ('013','0123'), ('012','0127'), ('123','1234'), ('024','0246'),
    ('234','2345'), ('135','1357'), ('345','3456'), ('016','0167'),
    ('056','0567'), ('456','4567'), ('01','017'), ('03','023'),
    ('23','235'), ('04','046'), ('05','057'), ('15','157'),
    ('25','245'), ('45','457'), ('16','167'), ('47','467'),
)


def face(s):
    return frozenset(int(x) for x in s)


def connected_triple(G, t):
    a, b, c = t
    return int(b in G[a]) + int(c in G[a]) + int(c in G[b]) >= 2


def dual_faces(n, p):
    G = [{(i+d) % n for d in range(-p, p+1) if d}
         for i in range(n)]
    result = set()
    for mask in range(1, 1 << n):
        f = frozenset(i for i in range(n) if mask & (1 << i))
        if all(connected_triple(G, t) for t in combinations(sorted(f), 3)):
            result.add(f)
    return result


def verify_sphere():
    faces = dual_faces(8, 2)
    assert Counter(map(len, faces)) == {1: 8, 2: 28, 3: 32, 4: 10}
    for a, b in PAIRS:
        low, high = face(a), face(b)
        assert low in faces and high in faces
        assert len(high) == len(low) + 1 and low < high
        all_cofaces = [f for f in faces if low < f]
        assert all_cofaces == [high], (a, b, all_cofaces)
        faces.difference_update([low, high])
        for f in faces:
            for v in f:
                assert f - {v} in faces or len(f) == 1
    assert Counter(map(len, faces)) == {1: 8, 2: 18, 3: 12}
    verts = {next(iter(f)) for f in faces if len(f) == 1}
    assert verts == set(range(8))
    edges = {f for f in faces if len(f) == 2}
    tris = {f for f in faces if len(f) == 3}
    assert all(sum(e <= t for t in tris) == 2 for e in edges)
    # Links of every vertex are connected 2-regular graphs (circles).
    for v in verts:
        le = [t - {v} for t in tris if v in t]
        ln = set().union(*le)
        assert ln
        assert all(sum(u in e for e in le) == 2 for u in ln)
        seen = {min(ln)}
        while True:
            more = {u for e in le for u in e if e & seen} - seen
            if not more:
                break
            seen |= more
        assert seen == ln
    # Connected surface, Euler characteristic 2 -> 2-sphere.
    seen = {0}
    while True:
        more = {u for e in edges for u in e if e & seen} - seen
        if not more:
            break
        seen |= more
    assert seen == verts
    assert len(verts) - len(edges) + len(tris) == 2
    print('octagonal complex: 78 faces; 20 certified collapses; sphere triangulation (8,18,12)')


def verify_folding(p):
    assert p >= 2
    n = 4*p
    sizes = [1, p-1]*4
    starts = [sum(sizes[:i]) for i in range(8)]
    f = [None]*n
    for i, (x, length) in enumerate(zip(starts, sizes)):
        for j in range(x, x+length):
            f[j] = i
    assert all(f[starts[i]] == i for i in range(8))
    dist = lambda x, y, m: min((x-y)%m, (y-x)%m)
    for i in range(n):
        for j in range(i):
            if dist(i,j,n) <= p and f[i] != f[j]:
                assert dist(f[i],f[j],8) <= 2, (p,i,j)
    for i in range(8):
        for j in range(i):
            assert (dist(starts[i],starts[j],n) <= p) == (dist(i,j,8) <= 2)
    return True


def sphere_cycle():
    faces = dual_faces(8, 2)
    for a,b in PAIRS:
        faces -= {face(a), face(b)}
    triangles = sorted(tuple(sorted(t)) for t in faces if len(t)==3)
    def bdry(t):
        return [(t[:i]+t[i+1:], (-1)**i) for i in range(len(t))]
    edge_tri = defaultdict(list)
    for tri in triangles:
        for edge,sign in bdry(tri):
            edge_tri[edge].append((tri,sign))
    orientations={triangles[0]:1}
    while len(orientations) < len(triangles):
        for entries in edge_tri.values():
            if len(entries)!=2:
                continue
            (t, a), (u, b) = entries
            if t in orientations and u not in orientations:
                orientations[u] = -orientations[t]*a//b
            if u in orientations and t not in orientations:
                orientations[t] = -orientations[u]*b//a
    assert all(sum(orientations[t]*sgn for t,sgn in entries)==0
               for entries in edge_tri.values())
    return orientations, triangles[0]


def degree_on_sphere(mapping, orientations, reference):
    # Push forward the certified fundamental 2-cycle, then eliminate
    # the triangles paired with 3-simplices by adding tetrahedral boundaries.
    coeff = defaultdict(int)
    for tri,sgn in orientations.items():
        image = [mapping[v] for v in tri]
        if len(set(image))<3:
            continue
        parity = (-1)**sum(image[i]>image[j] for i in range(3) for j in range(i+1,3))
        coeff[tuple(sorted(image))] += sgn*parity
    for a,b in PAIRS:
        lower=tuple(sorted(face(a)))
        upper=tuple(sorted(face(b)))
        if len(lower)==3 and coeff[lower]:
            boundaries={upper[:i]+upper[i+1:]:(-1)**i for i in range(4)}
            multiple=coeff[lower]//boundaries[lower]
            for tri,sign in boundaries.items():
                coeff[tri]-=multiple*sign
        if len(lower)==2:
            assert coeff[upper]==0
    d=coeff[reference]//orientations[reference]
    assert all(coeff[t]==d*orientations[t] for t in orientations)
    assert all(not val or tri in orientations for tri,val in coeff.items())
    return d


def verify_degree_matrix(p, orientations, reference):
    # Use alternating singleton/long blocks. For each p rotations,
    # compose an 8-vertex section with each block quotient.
    n=4*p
    lengths=[1,p-1]*4
    starts=[sum(lengths[:j]) for j in range(8)]
    quotients=[]
    for shift in range(p):
        q={}
        for j,length in enumerate(lengths):
            for h in range(length):
                q[(shift+starts[j]+h)%n]=j
        assert len(q)==n
        quotients.append(q)
    for s in range(p):
        for t in range(p):
            section=[(t+z)%n for z in starts]
            mapping=[quotients[s][u] for u in section]
            degree=degree_on_sphere(mapping, orientations, reference)
            expected=int(s==t)-int(t==(s-1)%p)
            assert degree==expected, (p,s,t,mapping,degree,expected)
    return True


if __name__ == '__main__':
    verify_sphere()
    for p in range(2,65):
        verify_folding(p)
    print('block-map sanity: all p from 2 through 64; symbolic proof required beyond')
    orientations,reference=sphere_cycle()
    for p in range(2,17):
        verify_degree_matrix(p, orientations, reference)
    print('degree-matrix sanity: p=2..16, identity-minus-cyclic-shift integral pairing')
