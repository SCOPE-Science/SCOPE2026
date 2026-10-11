#!/usr/bin/env python3
"""Exact finite certificate checker for the graph Čech complex of the 4-permutohedron.

Requires only the Python 3 standard library. Run from the directory containing
certificate.json, or pass its path as the first command-line argument.
"""
import collections
import itertools
import json
import pathlib
import sys

def build_complex():
    vertices = list(itertools.permutations((1, 2, 3, 4)))
    index = {v: i for i, v in enumerate(vertices)}
    neighborhoods = [(1 << i) for i in range(24)]
    edges = set()
    for i, permutation in enumerate(vertices):
        for j in range(3):
            other = list(permutation)
            other[j], other[j+1] = other[j+1], other[j]
            k = index[tuple(other)]
            a,b = sorted((i,k))
            edges.add((a,b))
            neighborhoods[i] |= (1 << k)
    assert len(edges) == 36
    assert all(n.bit_count() == 4 for n in neighborhoods)
    facets = {neighborhoods[i] | neighborhoods[j] for i,j in edges}
    assert len(facets) == 36
    assert all(f.bit_count() == 6 for f in facets)
    faces = set()
    for facet in facets:
        s = facet
        while s:
            faces.add(s)
            s = (s - 1) & facet
    return faces, facets, neighborhoods

def boundary(m):
    rest = m
    while rest:
        b = rest & -rest
        yield m ^ b
        rest ^= b

def check_matching(faces, certificate):
    matches = [tuple(pair) for pair in certificate['matching_pairs']]
    critical = set(certificate['critical_masks'])
    assert len(matches) == 606
    assert len(critical) == 18
    assert collections.Counter(m.bit_count()-1 for m in critical) == {0:1,2:17}
    used = set(critical)
    matched = set()
    for lo,hi in matches:
        assert lo and hi and lo in faces and hi in faces
        assert lo.bit_count()+1 == hi.bit_count()
        assert lo & hi == lo
        assert lo not in used and hi not in used
        used.add(lo);used.add(hi)
        matched.add((lo,hi))
    assert used == faces
    # The first 502 pairs are independently checked as genuine elementary
    # simplicial collapses, in their recorded order.
    rest = set(faces)
    for lo, hi in matches[:502]:
        assert lo in rest and hi in rest
        proper_cofaces = {co for co in rest if co != lo and (lo & co) == lo}
        assert proper_cofaces == {hi}
        rest.remove(lo)
        rest.remove(hi)
    assert len(rest) == 226
    # Orient every cover downward, except a matched cover oriented upward.
    indegree = {face:0 for face in faces}
    successors = {face:[] for face in faces}
    hasse_count = 0
    for hi in faces:
        if hi.bit_count() == 1:
            continue
        for lo in boundary(hi):
            assert lo in faces
            hasse_count += 1
            if (lo,hi) in matched:
                u,v = lo,hi
            else:
                u,v = hi,lo
            successors[u].append(v)
            indegree[v] += 1
    assert hasse_count == certificate['expected_hasse_incidence_count'] == 4344
    frontier = [f for f in faces if indegree[f] == 0]
    seen = 0
    while frontier:
        f = frontier.pop()
        seen += 1
        for v in successors[f]:
            indegree[v] -= 1
            if indegree[v] == 0:
                frontier.append(v)
    assert seen == len(faces), 'matching is not acyclic'
    return hasse_count

def gf2_rank(columns):
    pivots = {}
    for column in columns:
        while column:
            pivot = column.bit_length()-1
            if pivot in pivots:
                column ^= pivots[pivot]
            else:
                pivots[pivot] = column
                break
    return len(pivots)

def check_homology(faces):
    by_dim = {k:sorted(f for f in faces if f.bit_count() == k+1) for k in range(6)}
    assert [len(by_dim[k]) for k in range(6)] == [24,168,408,402,192,36]
    ranks = {0:0}
    for k in range(1,6):
        row = {face:i for i,face in enumerate(by_dim[k-1])}
        columns=[]
        for face in by_dim[k]:
            bits = 0
            for lo in boundary(face):
                bits ^= (1 << row[lo])
            columns.append(bits)
        ranks[k] = gf2_rank(columns)
    assert [ranks[k] for k in range(6)] == [0,23,145,246,156,36]
    betti = [len(by_dim[k])-ranks[k]-ranks.get(k+1,0) for k in range(6)]
    assert betti == [1,0,17,0,0,0]
    return betti

def check_rips_comparison(neighborhoods):
    """Independent field-two comparison with the graph-metric Rips nerve."""
    adj = [mask ^ (1 << i) for i, mask in enumerate(neighborhoods)]
    distance = []
    for start in range(24):
        ds = [-1] * 24
        ds[start] = 0
        queue = collections.deque([start])
        while queue:
            v = queue.popleft()
            candidate = adj[v]
            while candidate:
                bit = candidate & -candidate
                candidate ^= bit
                w = bit.bit_length()-1
                if ds[w] < 0:
                    ds[w] = ds[v] + 1
                    queue.append(w)
        assert min(ds) == 0 and max(ds) == 6
        distance.append(ds)
    near = []
    for i in range(24):
        near.append(sum(1 << j for j in range(24) if i != j and distance[i][j] <= 3))
    # Recursively generate every clique exactly once, increasing vertex indices.
    faces = set()
    def enumerate_cliques(mask, options):
        while options:
            bit = options & -options
            options ^= bit
            v = bit.bit_length()-1
            nxt = mask | bit
            faces.add(nxt)
            enumerate_cliques(nxt, options & near[v])
    enumerate_cliques(0, (1 << 24)-1)
    by_dim = {k:sorted(f for f in faces if f.bit_count()==k+1) for k in range(6)}
    assert [len(by_dim[k]) for k in range(6)] == [24,168,472,618,384,92]
    ranks = [0]
    for k in range(1,6):
        lower = {face:i for i,face in enumerate(by_dim[k-1])}
        columns = []
        for face in by_dim[k]:
            bits = 0
            for codim_one in boundary(face):
                bits ^= 1 << lower[codim_one]
            columns.append(bits)
        ranks.append(gf2_rank(columns))
    assert ranks == [0,23,145,326,292,92]
    betti = [len(by_dim[k]) - ranks[k] - (ranks[k+1] if k+1 < 6 else 0) for k in range(6)]
    assert betti == [1,0,1,0,0,0]
    return betti

def main():
    path = pathlib.Path(sys.argv[1]) if len(sys.argv)>1 else pathlib.Path(__file__).with_name('certificate.json')
    certificate=json.loads(path.read_text('utf-8'))
    assert certificate['schema_version'] == 1
    faces,facets,neighborhoods=build_complex()
    assert len(faces)==certificate['simplex_count']==1230
    hasse=check_matching(faces,certificate)
    betti=check_homology(faces)
    rips_betti=check_rips_comparison(neighborhoods)
    print('VERIFY_OK vertices=24 edges=36 facets=36 faces=1230 matching_pairs=606 critical_0=1 critical_2=17 hasse='+str(hasse)+' cech_gf2_betti='+str(betti)+' rips_gf2_betti='+str(rips_betti))

if __name__ == '__main__':
    main()
