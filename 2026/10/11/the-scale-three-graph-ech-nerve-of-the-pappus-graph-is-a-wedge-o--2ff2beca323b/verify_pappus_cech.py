#!/usr/bin/env python3
"""Reconstruct and verify a Pappus graph intrinsic Čech-complex certificate.

Standalone Python 3 standard library; preserve certificates/ directory nearby.
"""
from pathlib import Path
from itertools import combinations
from collections import Counter, deque
import json

N = 18
LCF = (5, 7, -7, 7, -7, -5)

def bit_vertices(mask):
    return [i for i in range(N) if mask & (1 << i)]

def dimension_profile(faces):
    counter = Counter(z.bit_count() for z in faces)
    return [counter.get(k, 0) for k in range(1, 1 + max(counter))]

def boundary_ranks_mod2(faces):
    layers = [[z for z in faces if z.bit_count() == k] for k in range(1, 7)]
    layers = [sorted(row) for row in layers]
    ranks = []
    for d in range(1, 6):
        idx = {mask:i for i,mask in enumerate(layers[d-1])}
        pivots = {}
        for cell in layers[d]:
            column = 0
            for i in bit_vertices(cell):
                column ^= 1 << idx[cell ^ (1 << i)]
            while column:
                pivot = column.bit_length()-1
                if pivot not in pivots:
                    pivots[pivot] = column
                    break
                column ^= pivots[pivot]
        ranks.append(len(pivots))
    return ranks

def main():
    cert = json.loads((Path(__file__).resolve().parent / 'certificates' / 'pappus_cech3.json').read_text(encoding='utf-8'))
    assert cert['vertex_count'] == N and cert['edge_count'] == 27
    edges = {tuple(sorted((i, (i+1) % N))) for i in range(N)}
    edges.update(tuple(sorted((i, (i+LCF[i % 6]) % N))) for i in range(N))
    assert len(edges) == 27
    neighbors = [{i} for i in range(N)]
    for a,b in edges:
        neighbors[a].add(b)
        neighbors[b].add(a)
    assert all(len(nbr) == 4 for nbr in neighbors)
    # Independent check that the LCF graph has girth 6 and diameter 4.
    diameter = 0
    for root in range(N):
        dist = {root:0}
        queue = deque([root])
        while queue:
            x = queue.popleft()
            for y in neighbors[x]-{x}:
                if y not in dist:
                    dist[y] = dist[x]+1
                    queue.append(y)
        assert len(dist)==N
        diameter = max(diameter,max(dist.values()))
    assert diameter == 4
    six_cycle=(0,1,2,3,4,5)
    assert all(tuple(sorted((six_cycle[j],six_cycle[(j+1)%6]))) in edges for j in range(6))
    for a,b in edges:
        # Removing an edge leaves shortest path length at least 5 (girth >= 6).
        dist = {a:0};queue=deque([a])
        while queue:
            x=queue.popleft()
            for y in neighbors[x]-{x}:
                if {x,y}=={a,b}:continue
                if y not in dist:
                    dist[y]=dist[x]+1;queue.append(y)
        assert dist[b]>=5
    facets = {sum(1<<v for v in neighbors[a]|neighbors[b]) for a,b in edges}
    assert all(z.bit_count()==6 for z in facets)
    assert sorted(facets)==cert['facets'] and len(facets)==27
    faces = set()
    for facet in facets:
        verts = bit_vertices(facet)
        for size in range(1, 7):
            for sub in combinations(verts, size):
                faces.add(sum(1<<v for v in sub))
    assert dimension_profile(faces)==cert['expected_f_vector']==[18,135,396,369,162,27]
    assert len(faces)==1107
    assert boundary_ranks_mod2(faces)==cert['expected_boundary_ranks_mod2']==[17,118,234,135,27]
    # Explicit elementary collapse: lower is contained in just one remaining
    # proper superface (upper); this is stronger than a cofacet-only check.
    remaining=set(faces)
    dims=Counter()
    for low,high in cert['collapse_pairs']:
        assert low in remaining and high in remaining
        assert low.bit_count()+1==high.bit_count()
        assert high & low == low
        supers = [x for x in remaining if x != low and (x & low)==low]
        assert supers==[high], (low,high,supers)
        remaining.remove(low)
        remaining.remove(high)
        dims[low.bit_count()-1]+=1
    assert len(cert['collapse_pairs'])==422
    assert dims=={1:26,2:234,3:135,4:27},dims
    assert dimension_profile(remaining)==cert['expected_core_f_vector']==[18,109,136]
    assert len(remaining)==263
    # Basic downclosure check, including after all free-face removals.
    for face in remaining:
        for v in bit_vertices(face):
            child=face^(1<<v)
            if child:assert child in remaining
    edges2={x for x in remaining if x.bit_count()==2}
    triangles={x for x in remaining if x.bit_count()==3}
    tree=cert['spanning_tree_edges']
    assert len(tree)==17 and len(set(tree))==17 and set(tree)<=edges2
    # The chosen 17 edges form a spanning tree.
    parent=list(range(N))
    def root(v):
        while parent[v]!=v:v=parent[v]
        return v
    for mask in tree:
        u,v=bit_vertices(mask)
        a,b=root(u),root(v)
        assert a!=b
        parent[a]=b
    assert len({root(v) for v in range(N)})==1
    trivialized=set(tree)
    for triangle,edge in cert['triangle_nullhomotopy_steps']:
        assert triangle in triangles and edge in edges2 and edge not in trivialized
        side_edges={triangle^(1<<i) for i in bit_vertices(triangle)}
        assert len(side_edges)==3 and side_edges <= edges2
        assert side_edges-trivialized == {edge}
        trivialized.add(edge)
    assert len(cert['triangle_nullhomotopy_steps'])==92
    assert trivialized==edges2
    assert 18-109+136==45
    assert boundary_ranks_mod2(remaining)==[17,92,0,0,0]
    # The tree/triangle certificate gives trivial pi_1 by van Kampen.
    # A connected simply connected 2-complex has free H_2; chi-1=44.
    # Integral Hurewicz plus homological Whitehead then gives wedge(44,S^2).
    print('VERIFY_OK')
    print('Pappus vertices=18 edges=27 girth=6 diameter=4')
    print('initial nonempty_faces=1107 f_vector=(18,135,396,369,162,27)')
    print('elementary_collapses=422 pair_dimensions=(26,234,135,27)')
    print('core nonempty_faces=263 f_vector=(18,109,136)')
    print('spanning_tree_edges=17 triangle_nullhomotopy_steps=92')
    print('mod2_boundary_ranks=(17,118,234,135,27); integral H2 rank=44')

if __name__ == '__main__': main()
