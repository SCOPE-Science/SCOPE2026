#!/usr/bin/env python3
"""Exact intrinsic Čech homology/persistence verification for GP(8,3).

No nonstandard libraries or external data. Every simplicial face and incidence
in the eight integral Čech stages is constructed from the stated graph.
Disjoint vertex-toggle matching pairs and complete Hasse-DAG acyclicity checks
are followed by an exact signed integer Morse boundary at scale five.
"""
from collections import Counter, deque
from functools import lru_cache
from itertools import combinations

N = 16
EXPECTED_FACES = (16, 40, 168, 976, 11028, 64444, 65534, 65535)
EXPECTED_CRITICAL = (
    {0: 16}, {0: 1, 1: 9}, {0: 1, 1: 9}, {0: 1, 2: 47},
    {0: 1, 4: 41, 6: 2}, {0: 1, 9: 2, 10: 5},
    {0: 1, 14: 1}, {0: 1},
)


def mobius_kantor():
    """Vertices 0..7 are u_i; 8..15 are v_i, all indices mod eight."""
    graph = [set() for _ in range(N)]
    def add(a, b):
        graph[a].add(b)
        graph[b].add(a)
    for i in range(8):
        add(i, (i+1) % 8)
        add(i, 8+i)
        add(8+i, 8+(i+3) % 8)
    assert len({(a,b) for a in range(N) for b in graph[a] if a < b}) == 24
    assert all(len(z) == 3 for z in graph)
    return graph


def all_distances(graph):
    distances = []
    for root in range(N):
        d = [-1]*N
        d[root] = 0
        queue = deque([root])
        while queue:
            x = queue.popleft()
            for y in sorted(graph[x]):
                if d[y] < 0:
                    d[y] = d[x]+1
                    queue.append(y)
        assert Counter(d) == {0:1,1:3,2:6,3:5,4:1}
        distances.append(d)
    assert all(distances[a][b] == distances[b][a] for a in range(N) for b in range(N))
    return distances


def vertices(mask):
    return [i for i in range(N) if mask & (1<<i)]


def simplices(graph, distances, scale):
    t = scale // 2
    neighborhoods = [sum(1<<v for v in range(N) if distances[c][v] <= t)
                     for c in range(N)]
    if scale % 2 == 0:
        generators = neighborhoods
    else:
        generators = [neighborhoods[a] | neighborhoods[b]
                      for a in range(N) for b in graph[a] if a < b]
    generators = set(generators)
    facets = sorted(g for g in generators
                    if not any(g != h and g & h == g for h in generators))
    faces = set()
    for facet in facets:
        face = facet
        while face:
            faces.add(face)
            face = (face-1) & facet
    assert all(faces.__contains__(f ^ (1<<i)) for f in faces
               for i in vertices(f) if f != (1<<i))
    return faces, facets


def toggle_matching(faces):
    """Match all available pairs toggling vertices 0,1,...,15 in order."""
    unmatched = set(faces)
    pairs = []
    for i in range(N):
        bit = 1<<i
        for low in sorted(list(unmatched)):
            high = low | bit
            if low & bit == 0 and low in unmatched and high in unmatched:
                unmatched.remove(low)
                unmatched.remove(high)
                pairs.append((low, high))
    assert len(faces) == len(unmatched)+2*len(pairs)
    assert len({f for p in pairs for f in p}) == 2*len(pairs)
    return unmatched, pairs


def hasse_toposort(faces, pairs):
    """Matched incidences up, all other codimension-one incidences down."""
    upper_for_lower = {lo:hi for lo,hi in pairs}
    outgoing = {f: [] for f in faces}
    incoming = {f: 0 for f in faces}
    incidences = 0
    for hi in faces:
        for i in vertices(hi):
            lo = hi ^ (1<<i)
            if lo == 0:
                continue
            if upper_for_lower.get(lo) == hi:
                a,b = lo,hi
            else:
                a,b = hi,lo
            outgoing[a].append(b)
            incoming[b] += 1
            incidences += 1
    queue = deque(sorted(x for x in faces if incoming[x] == 0))
    visited = 0
    while queue:
        x = queue.popleft()
        visited += 1
        for y in outgoing[x]:
            incoming[y] -= 1
            if incoming[y] == 0:
                queue.append(y)
    assert visited == len(faces), ('cyclic Morse matching', visited, len(faces))
    return incidences


def signed_boundary(face):
    return [(face ^ (1<<i), -1 if j%2 else 1)
            for j,i in enumerate(vertices(face))]


def scale_five_morse_boundary(critical, pairs):
    """Signed critical degree-10 to critical degree-9 matrix over integers.

    Standard gradient-path elimination in dimension nine: a matched lower
    9-face is eliminated by its paired 10-face with unit incidence; an upper
    9-face paired down to degree eight does not contribute to degree-nine
    Morse generators. Acyclicity was checked before calling this function.
    """
    target = sorted(f for f in critical if f.bit_count() == 10)
    domain = sorted(f for f in critical if f.bit_count() == 11)
    assert len(target) == 2 and len(domain) == 5
    index = {x:i for i,x in enumerate(target)}
    up = dict(pairs)

    @lru_cache(None)
    def project(x):
        if x in index:
            return tuple(1 if i==index[x] else 0 for i in range(len(target)))
        hi = up.get(x)
        if hi is None or hi.bit_count() != 11:
            return (0,0)
        rows = signed_boundary(hi)
        pivot = next(s for y,s in rows if y == x)
        ans = [0,0]
        for y,s in rows:
            if y == x:
                continue
            coeff = project(y)
            for j in range(2):
                ans[j] -= pivot*s*coeff[j]
        return tuple(ans)

    columns = []
    for hi in domain:
        ans = [0,0]
        for lo,s in signed_boundary(hi):
            coeff = project(lo)
            for j in range(2):
                ans[j] += s*coeff[j]
        columns.append(tuple(ans))
    assert columns == [(0,0),(1,1),(-1,-1),(0,0),(0,0)], columns
    # Nonzero image is the primitive direct summand generated by (1,1).
    return target,domain,columns



def mod_two_betti(faces):
    """Independent mod-two rank reduction of ordinary simplicial boundaries."""
    layers = {d:sorted(f for f in faces if f.bit_count()==d+1)
              for d in range(max(f.bit_count() for f in faces))}
    rank = {0:0}
    for d in range(1,len(layers)):
        position = {x:i for i,x in enumerate(layers[d-1])}
        pivots = {}
        for face in layers[d]:
            col = 0
            for i in vertices(face):
                col ^= 1<<position[face^(1<<i)]
            while col:
                head = col.bit_length()-1
                if head not in pivots:
                    pivots[head] = col
                    break
                col ^= pivots[head]
        rank[d] = len(pivots)
    out = {}
    for d,layer in layers.items():
        val = len(layer)-rank[d]-rank.get(d+1,0)-(1 if d==0 else 0)
        if val:
            out[d]=val
    return out


def verify_relative_scale_two_collapse(graph, faces):
    """64 elementary codimension-one free-face collapses down to GP(8,3)."""
    remainder = set(faces)
    collapses = 0
    for center in range(N):
        nbrs = sorted(graph[center])
        clique = sum(1<<v for v in nbrs)
        tetrahedron = clique | (1<<center)
        pairs = [(clique,tetrahedron)]
        pairs.extend(((1<<a)|(1<<b), (1<<a)|(1<<b)|(1<<center))
                     for a,b in combinations(nbrs,2))
        for lo,hi in pairs:
            assert lo in remainder and hi in remainder
            assert hi.bit_count() == lo.bit_count()+1
            assert [x for x in remainder if x != lo and lo & x == lo] == [hi], (lo,hi)
            remainder.remove(lo)
            remainder.remove(hi)
            collapses += 1
    expected = {1<<v for v in range(N)}
    expected.update((1<<a)|(1<<b) for a in range(N) for b in graph[a] if a<b)
    assert remainder == expected
    assert collapses == 64
    return collapses


def compute():
    graph = mobius_kantor()
    distances = all_distances(graph)
    report = []
    for scale in range(8):
        faces,facets = simplices(graph,distances,scale)
        assert len(faces) == EXPECTED_FACES[scale]
        if scale == 3:
            assert len(facets) == 24 and all(x.bit_count() == 6 for x in facets)
        if scale == 4:
            assert len(facets) == 16 and all(x.bit_count() == 10 for x in facets)
        critical,pairs = toggle_matching(faces)
        counts = dict(sorted(Counter(f.bit_count()-1 for f in critical).items()))
        assert counts == EXPECTED_CRITICAL[scale], (scale,counts)
        incidences = hasse_toposort(faces,pairs)
        if scale in (3,4,5):
            expected_betti = {3:{2:47},4:{4:41,6:2},5:{9:1,10:4}}[scale]
            assert mod_two_betti(faces) == expected_betti
        if scale == 2:
            verify_relative_scale_two_collapse(graph,faces)
        if scale == 5:
            _,_,m = scale_five_morse_boundary(critical,pairs)
            assert m[1] == (1,1) and m[2] == (-1,-1)
        if scale == 6:
            assert len(facets) == 16
            assert set(facets) == {(1<<N)-1 ^ (1<<i) for i in range(N)}
        if scale == 7:
            assert len(facets) == 1 and facets[0] == (1<<N)-1
        report.append((scale,len(faces),len(pairs),counts,incidences))
    assert report[0][3] == {0:16}
    # Morse-chain gap principle at scales 1,2,3,4,6,7, and
    # one primitive rank-one differential at scale 5 imply the barcode.
    expected_bars = {0:(15,0,1),1:(9,1,3),2:(47,3,4),
                     4:(41,4,5),6:(2,4,5),9:(1,5,6),
                     10:(4,5,6),14:(1,6,7)}
    print('Exact intrinsic Čech scales 0..7:')
    for scale,total,matched,critical_count,incidences in report:
        print('scale=%d faces=%d pairs=%d critical=%s hasse_incidences=%d'
              % (scale,total,matched,critical_count,incidences))
    print('BARCODE '+repr(expected_bars))
    print('VERIFY_OK')


if __name__ == '__main__':
    compute()
