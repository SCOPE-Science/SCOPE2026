#!/usr/bin/env python3
"""Reconstruct and verify graph Čech complexes of the Fano incidence graph.

Requires only the Python standard library. All faces are nonzero 14-bit integers;
bit positions 0..6 are points, and 7..13 are lines.
"""

from collections import Counter, deque

N = 14
ALL = (1 << N) - 1
FANO_DIFF = (0, 1, 3)
ORDER_3 = (9, 11, 10, 0, 4, 2, 6, 1, 3, 13, 12, 8, 5, 7)
ORDER_4 = (10, 3, 8, 0, 2, 5, 11, 6, 9, 1, 7, 4, 12, 13)
EXPECTED = {
    0: (14,),
    1: (14, 21),
    2: (14, 63, 56, 14),
    3: (14, 91, 308, 287, 126, 21),
    4: (14, 91, 364, 1001, 2002, 2219, 1472, 602, 140, 14),
}


def neighbors():
    out = [set() for _ in range(N)]
    for p in range(7):
        for l in range(7):
            if (p - l) % 7 in FANO_DIFF:
                out[p].add(7 + l)
                out[7 + l].add(p)
    assert all(len(s) == 3 for s in out)
    assert sum(map(len, out)) == 42
    # Every pair of distinct points, or lines, shares exactly one neighbor.
    for x in range(7):
        for y in range(x + 1, 7):
            assert len(out[x] & out[y]) == 1
            assert len(out[7+x] & out[7+y]) == 1
    return out


def bitset(vertices):
    return sum(1 << v for v in vertices)


def facets_at(r, adj):
    if r == 0:
        return {1 << x for x in range(N)}
    if r == 1:
        return {bitset((u,v)) for u in range(N) for v in adj[u] if u < v}
    one = [{x} | adj[x] for x in range(N)]
    if r == 2:
        return {bitset(s) for s in one}
    if r == 3:
        return {bitset(one[u] | one[v]) for u in range(N) for v in adj[u] if u < v}
    two = [{x} | adj[x] | set().union(*(adj[z] for z in adj[x])) for x in range(N)]
    if r == 4:
        return {bitset(s) for s in two}
    if r == 5:
        fs = {bitset(two[u] | two[v]) for u in range(N) for v in adj[u] if u < v}
        assert fs == {ALL}
        return fs
    raise ValueError('r must lie in 0..5')


def subfaces(s):
    t = s
    while t:
        yield t
        t = (t - 1) & s


def all_faces(facets):
    return set().union(*(set(subfaces(f)) for f in facets))


def face_vector(faces):
    c = Counter(s.bit_count()-1 for s in faces)
    return tuple(c.get(i, 0) for i in range(max(c)+1))


def match_toggle(faces, order):
    """Deterministic element matching, tested by complete directed Hasse DAG."""
    assert sorted(order) == list(range(N))
    available = set(faces)
    pairs = []
    for i in order:
        mask = 1 << i
        for s in sorted(available):
            t = s | mask
            if (s & mask) == 0 and t in available:
                available.remove(s)
                available.remove(t)
                pairs.append((s, t))
    return pairs, available


def check_matching_acyclic(faces, pairs, critical):
    matched = set()
    ups = {}
    for low, high in pairs:
        assert low in faces and high in faces
        assert high.bit_count() == low.bit_count()+1
        assert high & low == low
        assert low not in matched and high not in matched
        matched.add(low)
        matched.add(high)
        ups[low] = high
    assert set(faces) == matched | critical
    assert not (matched & critical)
    # Hasse incidence goes high->low, except matched low->high.
    # Kahn's algorithm detects directed cycles exactly (not heuristically).
    indegree = {s: 0 for s in faces}
    out = {s: [] for s in faces}
    covers = 0
    for t in faces:
        if t.bit_count() == 1:
            continue
        for i in range(N):
            if t & (1 << i):
                s = t ^ (1 << i)
                assert s in faces
                if ups.get(s) == t:
                    tail, head = s, t
                else:
                    tail, head = t, s
                out[tail].append(head)
                indegree[head] += 1
                covers += 1
    todo = deque(s for s in faces if indegree[s] == 0)
    visited = 0
    while todo:
        s = todo.popleft()
        visited += 1
        for t in out[s]:
            indegree[t] -= 1
            if indegree[t] == 0:
                todo.append(t)
    assert visited == len(faces), 'matching has a closed gradient path'
    return covers


def check_relative_r2(faces, adj, original_edges):
    """Replay explicit collapses, ensuring each deletion is a free-face pair."""
    active = set(faces)
    deleted = []
    def elementary(low, high):
        assert low in active and high in active and low != high
        assert high.bit_count() == low.bit_count()+1 and (low & high) == low
        # A free face is contained in exactly one simplex of larger dimension,
        # not merely one direct coface.
        containing = [s for s in active if s != low and (s & low) == low]
        assert containing == [high], (low, containing)
        active.remove(low)
        active.remove(high)
        deleted.append((low,high))
    # Four-vertex tetrahedra have unique triangular faces of their 3 neighbors.
    for center in range(N):
        t = bitset(adj[center])
        tet = t | (1 << center)
        elementary(t,tet)
    # Each length-two pair has one common neighbor (girth >= 6).
    for x in range(N):
        for y in range(x+1,N):
            if x//7 != y//7:
                continue
            common = adj[x] & adj[y]
            assert len(common)==1
            middle = next(iter(common))
            edge = (1 << x)|(1 << y)
            triangle = edge | (1 << middle)
            elementary(edge,triangle)
    original = {1 << x for x in range(N)} | {bitset((u,v)) for u,v in original_edges}
    assert active == original
    assert len(deleted) == 56
    return deleted


def mod2_reduced_betti(faces):
    """Independent exact homology check using binary Gaussian elimination."""
    layers = {}
    for s in faces:
        layers.setdefault(s.bit_count() - 1, []).append(s)
    for v in layers.values():
        v.sort()
    rank = {-1: 0}
    for k in range(max(layers)+1):
        if k == 0:
            rank[k] = 0
            continue
        row_ids = {s: i for i, s in enumerate(layers[k-1])}
        pivots = {}
        for face in layers[k]:
            vec = 0
            for bit in range(N):
                if face & (1 << bit):
                    vec ^= 1 << row_ids[face ^ (1 << bit)]
            while vec:
                pivot = vec.bit_length()-1
                if pivot in pivots:
                    vec ^= pivots[pivot]
                else:
                    pivots[pivot] = vec
                    break
        rank[k] = len(pivots)
    result = {}
    for k in layers:
        b = len(layers[k]) - rank[k] - rank.get(k+1,0)
        if k==0:
            b -= 1
        if b:
            result[k]=b
    return result


def verify():
    adj = neighbors()
    E = {(u,v) for u in range(N) for v in adj[u] if u < v}
    assert len(E) == 21
    counts={}
    for r in range(5):
        facets=facets_at(r,adj)
        faces=all_faces(facets)
        counts[r]=len(faces)
        assert face_vector(faces)==EXPECTED[r],(r,face_vector(faces))
        if r==2:
            check_relative_r2(faces,adj,E)
        if r in (3,4):
            order=ORDER_3 if r==3 else ORDER_4
            pairs,critical=match_toggle(faces,order)
            dim=2 if r==3 else 4
            assert Counter(s.bit_count()-1 for s in critical)=={0:1,dim:(48 if r==3 else 64)}
            assert len(pairs)*2+len(critical)==len(faces)
            covers=check_matching_acyclic(faces,pairs,critical)
            assert mod2_reduced_betti(faces) == {dim:(48 if r==3 else 64)}
            if r==3:
                assert len(faces)==847 and len(pairs)==399 and covers==sum(len([i for i in range(N) if (s>>i)&1]) for s in faces if s.bit_count()>1)
            else:
                assert len(faces)==7919 and len(pairs)==3927
            print('r=%d f_vector=%s pairs=%d critical=%s directed_cover_incidents=%d DAG=OK' % (
                r, face_vector(faces), len(pairs),dict(Counter(s.bit_count()-1 for s in critical)),covers))
    assert facets_at(5,adj)=={ALL}
    print('r=0..4_face_counts=%s r=2_relative_collapse_pairs=56 r>=5=full_simplex' % counts)
    print('VERIFY_OK')

if __name__ == '__main__':
    verify()
