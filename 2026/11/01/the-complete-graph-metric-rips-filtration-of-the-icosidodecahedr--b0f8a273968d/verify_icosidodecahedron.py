#!/usr/bin/env python3
"""Reproduce and verify elementary-collapse certificates for graph Rips complexes
of the icosidodecahedron (the rectification of the icosahedron).
Only the Python standard library is required.

Usage:
  python icosidodeca_vr_check.py --generate collapse_certificate.json
  python icosidodeca_vr_check.py collapse_certificate.json
"""
import json
import sys
import heapq
from collections import Counter
from itertools import combinations
from pathlib import Path


def icosahedron():
    # Top and bottom poles 0 and 11; staggered pentagonal rings 1..5, 6..10.
    edges = set()
    def add(a,b):
        edges.add(tuple(sorted((a,b))))
    for i in range(5):
        a=1+i; an=1+(i+1)%5
        b=6+i; bn=6+(i+1)%5
        bp=6+(i-1)%5
        add(0,a);add(11,b)
        add(a,an);add(b,bn)
        add(a,b);add(a,bp)
    edges=sorted(edges)
    assert len(edges)==30
    g=[set() for _ in range(12)]
    for u,v in edges:
        g[u].add(v);g[v].add(u)
    assert all(len(x)==5 for x in g)
    triangles=[]
    for tri in combinations(range(12),3):
        if all(v in g[u] for u,v in combinations(tri,2)):
            triangles.append(tri)
    assert len(triangles)==20
    return edges,triangles,g


def graph_and_surface():
    edges,triangles,g0=icosahedron()
    idx={e:i for i,e in enumerate(edges)}
    g=[set() for _ in range(30)]
    for tri in triangles:
        three=[idx[tuple(sorted(x))] for x in combinations(tri,2)]
        for u,v in combinations(three,2):
            g[u].add(v);g[v].add(u)
    assert all(len(x)==4 for x in g)
    assert sum(len(x) for x in g)//2==60
    surface_tri=[]
    for tri in triangles:
        three=tuple(sorted(idx[tuple(sorted(x))] for x in combinations(tri,2)))
        surface_tri.append(three)
    # One pentagonal face surrounds each of the icosahedron's twelve vertices.
    pentagons=[]
    for v in range(12):
        cyc=[idx[tuple(sorted((v,w)))] for w in g0[v]]
        neighbors={x:set(g[x]).intersection(cyc) for x in cyc}
        assert all(len(s)==2 for s in neighbors.values())
        start=min(cyc)
        second=min(neighbors[start]);walk=[start,second]
        while len(walk)<5:
            nxt=next(iter(neighbors[walk[-1]]-{walk[-2]}))
            assert nxt not in walk
            walk.append(nxt)
        assert start in neighbors[walk[-1]]
        pentagons.append(walk)
        for j in (1,2,3):
            surface_tri.append(tuple(sorted((start,walk[j],walk[j+1]))))
    assert len(surface_tri)==56
    surface=set()
    for tri in surface_tri:
        t=sum(1<<v for v in tri)
        z=t
        while z:
            surface.add(z);z=(z-1)&t
    sizes=Counter(x.bit_count() for x in surface)
    assert sizes=={1:30,2:84,3:56}
    # Combinatorial surface check: all edges have precisely two incident triangles.
    incid=Counter()
    for tri in surface_tri:
        for u,v in combinations(tri,2):
            incid[tuple(sorted((u,v)))]+=1
    assert len(incid)==84 and all(v==2 for v in incid.values())
    # Every vertex link is one cycle. Together with connectedness and
    # Euler characteristic two, this proves the target is a 2-sphere.
    for v in range(30):
        link = {}
        for a,b,c in surface_tri:
            if v not in (a,b,c):
                continue
            u,w = [x for x in (a,b,c) if x != v]
            link.setdefault(u,set()).add(w)
            link.setdefault(w,set()).add(u)
        assert link and all(len(nb)==2 for nb in link.values())
        visited={next(iter(link))}
        todo=list(visited)
        for u in todo:
            for w in link[u]:
                if w not in visited:
                    visited.add(w);todo.append(w)
        assert len(visited)==len(link)
    assert 30-84+56==2
    surf_neighbor={v:set() for v in range(30)}
    for edge in (x for x in surface if x.bit_count()==2):
        a,b=[v for v in range(30) if edge&(1<<v)]
        surf_neighbor[a].add(b);surf_neighbor[b].add(a)
    visited={0}; todo=[0]
    for v in todo:
        for u in surf_neighbor[v]:
            if u not in visited:visited.add(u);todo.append(u)
    assert len(visited)==30
    # The triangles are exactly the original triangular faces and fans in each pentagon.
    assert len(pentagons)==12
    # Distances in the rectified graph.
    D=[]
    for v in range(30):
        q=[v];dist={v:0}
        for x in q:
            for y in g[x]:
                if y not in dist:
                    dist[y]=dist[x]+1;q.append(y)
        assert len(dist)==30
        D.append(dist)
    expected={0:1,1:4,2:8,3:8,4:8,5:1}
    assert all(dict(Counter(D[v].values()))==expected for v in range(30))
    return g,surface,triangles,pentagons,D


def rips_faces(D,r):
    # List every clique of the graph containing precisely the distance-<=r pairs.
    adj=[]
    for v in range(30):
        adj.append(sum((1<<w) for w in range(30) if w!=v and D[v][w]<=r))
    faces=set()
    def extend(current,candidates):
        while candidates:
            bit=candidates & -candidates
            candidates-=bit
            vertex=bit.bit_length()-1
            face=current|bit
            faces.add(face)
            extend(face,candidates&adj[vertex])
    extend(0,(1<<30)-1)
    return faces


def all_upper(faces):
    up={m:set() for m in faces}
    for mask in faces:
        rest=mask
        while rest:
            bit=rest&-rest;rest-=bit
            facet=mask^bit
            if facet in up:up[facet].add(mask)
    return up


def make_pairs(faces,target):
    alive=set(faces);up=all_upper(faces);queue=[]
    def offer(face):
        if face in alive and face not in target and len(up[face])==1:
            co=next(iter(up[face]))
            if not up[co]:
                heapq.heappush(queue,(-face.bit_count(),face))
    for f in alive:offer(f)
    pairs=[]
    while queue:
        _,sigma=heapq.heappop(queue)
        if sigma not in alive or sigma in target or len(up[sigma])!=1:continue
        tau=next(iter(up[sigma]))
        if tau not in alive or len(up[tau])!=0:continue
        assert sigma.bit_count()+1==tau.bit_count()
        for m in (tau,sigma):
            alive.remove(m)
            rest=m
            while rest:
                bit=rest&-rest;rest-=bit
                lower=m^bit
                if lower in alive:
                    up[lower].remove(m)
                    offer(lower)
        pairs.append([sigma,tau])
    assert alive==target,(len(alive-target),len(target-alive))
    return pairs


def replay(faces,target,pairs):
    alive=set(faces)
    assert target<=alive
    up=all_upper(faces)
    for step,pair in enumerate(pairs):
        assert len(pair)==2
        sigma,tau=pair
        assert isinstance(sigma,int) and isinstance(tau,int)
        assert sigma in alive and tau in alive and sigma not in target and tau not in target,step
        assert sigma.bit_count()+1==tau.bit_count() and sigma&tau==sigma,step
        assert up[sigma]=={tau} and not up[tau],step
        for m in (tau,sigma):
            alive.remove(m)
            rest=m
            while rest:
                bit=rest&-rest;rest-=bit
                lower=m^bit
                if lower in alive:up[lower].remove(m)
    assert alive==target,(len(alive-target),len(target-alive))
    return len(pairs)


def main():
    G,S,triangles,pentagons,D=graph_and_surface()
    K1=rips_faces(D,1)
    K2=rips_faces(D,2)
    K3=rips_faces(D,3)
    assert S<=K2<=K3
    assert Counter(m.bit_count() for m in K1)=={1:30,2:60,3:20}
    assert Counter(m.bit_count() for m in K2)=={1:30,2:180,3:380,4:330,5:102}
    assert Counter(m.bit_count() for m in K3)=={1:30,2:300,3:1340,4:3150,5:4374,6:3800,7:2100,8:720,9:140,10:12}
    # The scale-one 20 triangles have pairwise-disjoint edges, so may be
    # collapsed along any one of their three edges. Resulting connected graph
    # has 30 vertices and 40 edges, thus is wedge of 11 circles.
    edge_tri=Counter()
    for triangle in (m for m in K1 if m.bit_count()==3):
        for v in range(30):
            if triangle&(1<<v):edge_tri[triangle^(1<<v)]+=1
    assert len(edge_tri)==60 and set(edge_tri.values())=={1}
    # Diameter five: each vertex has one unique antipode. 15 forbidden
    # antipodal pairs at radius four give exactly a join of 15 zero-spheres.
    antipodes={tuple(sorted((u,v))) for u in range(30) for v in range(30) if D[u][v]==5}
    assert len(antipodes)==15
    assert sorted(u for e in antipodes for u in e)==list(range(30))
    if len(sys.argv)==3 and sys.argv[1]=='--generate':
        pairs32=make_pairs(K3,K2)
        pairs2s=make_pairs(K2,S)
        data={'certificate_format':1,'graph':'rectified-icosahedron-30-vertices',
              'scale_3_to_2':pairs32,'scale_2_to_surface':pairs2s}
        with open(sys.argv[2],'w',encoding='utf-8') as f:
            json.dump(data,f,separators=(',',':'))
            f.write('\n')
    else:
        assert len(sys.argv)==2, 'Supply collapse_certificate.json'
        with open(sys.argv[1],encoding='utf-8') as f:data=json.load(f)
        assert data['certificate_format']==1
        assert data['graph']=='rectified-icosahedron-30-vertices'
        assert set(data)=={'certificate_format','graph','scale_3_to_2','scale_2_to_surface'}
        pairs32=data['scale_3_to_2'];pairs2s=data['scale_2_to_surface']
    assert replay(K3,K2,pairs32)==7472
    assert replay(K2,S,pairs2s)==426
    print('ICOSI_RIPS_GRAPH: 30 vertices, 60 edges; 12 pentagons, 20 triangles')
    print('ICOSI_RIPS_DISTANCE_SHELLS: 1,4,8,8,8,1; 15 antipodal pairs')
    print('ICOSI_RIPS_FACES_R1: (30,60,20)')
    print('ICOSI_RIPS_FACES_R2: (30,180,380,330,102)')
    print('ICOSI_RIPS_FACES_R3: (30,300,1340,3150,4374,3800,2100,720,140,12)')
    print('ICOSI_RIPS_TARGET_SURFACE: (30,84,56); triangulated icosidodecahedral boundary')
    print('ICOSI_RIPS_COLLAPSES: radius3->radius2 7472; radius2->surface 426')
    print('ICOSI_RIPS_HOMOTOPY: r0 29 S0; r1 11 S1; r2/r3 S2; r4 S14; r5 contractible')
    print('ICOSI_RIPS_BARCODE: H0[0,1)x29 H1[1,2)x11 H2[2,4)x1 H14[4,5)x1')
    print('ICOSIDODECAHEDRON_RIPS_COLLAPSE_CERTIFICATE_VERIFIED')

if __name__=='__main__':
    main()
