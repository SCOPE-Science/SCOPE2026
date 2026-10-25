#!/usr/bin/env python3
"""Reproduce antipodal-component and integral-homology sanity checks."""
from collections import Counter, deque
from itertools import combinations
from math import comb, gcd


def dist_cycle(a, b, n):
    d = abs(a - b)
    return min(d, n - d)


def farthest_edges(m, n):
    pts = [(i,j) for j in range(n) for i in range(m)]
    diameter = m//2 + n//2
    edges=[]
    for p in range(len(pts)):
        for q in range(p+1,len(pts)):
            a,b=pts[p],pts[q]
            if dist_cycle(a[0],b[0],m)+dist_cycle(a[1],b[1],n)==diameter:
                edges.append((p,q))
    return pts,edges,diameter


def get_components(num_verts,edges):
    adj=[set() for _ in range(num_verts)]
    for a,b in edges:adj[a].add(b);adj[b].add(a)
    seen=set();components=[]
    for v in range(num_verts):
        if v in seen:continue
        found={v};queue=[v]
        for w in queue:
            for u in adj[w]:
                if u not in found:found.add(u);queue.append(u)
        seen |= found;components.append((len(found),Counter(len(adj[z]) for z in found)))
    return components


def independent_faces(n,edge_list):
    adj=[0]*n
    for u,v in edge_list:adj[u] |= 1<<v;adj[v] |= 1<<u
    faces=[]
    for mask in range(1<<n):
        if all(not(mask & adj[v]) for v in range(n) if mask&(1<<v)):
            faces.append(mask)
    return faces


def rank_mod2(vectors):
    pivots={}
    for w in vectors:
        while w:
            pivot=w.bit_length()-1
            if pivot in pivots:w ^= pivots[pivot]
            else:pivots[pivot]=w;break
    return len(pivots)


def betti_mod2(n, edges):
    fs=independent_faces(n,edges)
    faces=Counter(x.bit_count()-1 for x in fs if x)
    levels={d:sorted(x for x in fs if x and x.bit_count()==d+1) for d in faces}
    ranks={}
    for d in levels:
        if d==0:ranks[d]=0;continue
        rows={x:i for i,x in enumerate(levels[d-1])}
        vectors=[]
        for face in levels[d]:
            boundary=0
            for v in range(n):
                if face>>v&1:boundary ^= 1<<rows[face^(1<<v)]
            vectors.append(boundary)
        ranks[d]=rank_mod2(vectors)
    return {d:len(levels[d])-ranks[d]-ranks.get(d+1,0)-(1 if d==0 else 0) for d in levels},faces


def expected_factor(m):
    if m%3==0:return (2,2*m//3-1)
    if m%3==1:return (1,(2*m-2)//3)
    return (1,(2*m-4)//3)



def cyclic_character_direct(m,n,k):
    """Alternating trace on invariant simplices, without computing a homology basis."""
    pts,edges,_=farthest_edges(m,n)
    perm=lambda v:((v//m+k)%n)*m+v%m
    acc=0
    for face in independent_faces(m*n,edges):
        image=0
        for v in range(m*n):
            if face>>v&1:image |= 1<<perm(v)
        if image!=face:continue
        cycles=0;seen=0
        for v in range(m*n):
            if not(face>>v&1) or seen>>v&1:continue
            cycles+=1;w=v
            while not(seen>>w&1):
                seen|=1<<w;w=perm(w)
        acc+=(-1)**cycles
    reduced_lefschetz=-acc
    multiplicity,d=expected_factor(m)
    top_degree=(n//2)*(d+1)-1
    return (-1)**top_degree*reduced_lefschetz


def predicted_character(m,n,k):
    b=n//2
    if m%3==0:return (-1)**k*2**gcd(b,k)
    return (-1)**(b*k)


def main():
    num=0
    for m in (3,5,7,9,11):
        for n in (4,6,8):
            pts,edges,D=farthest_edges(m,n)
            comps=get_components(len(pts),edges)
            assert len(comps)==n//2,(m,n,comps)
            assert all(vcount==2*m and degrees=={2:2*m} for vcount,degrees in comps),(m,n,comps)
            num+=1
    print('PASS antipodal graph component decomposition:',num,'rectangular tori')
    for m in (3,5,7):
        t=2*m
        edges=[(i,(i+1)%t) for i in range(t)]
        got,faces=betti_mod2(t,edges)
        expect_multiplicity,degree=expected_factor(m)
        assert {k:v for k,v in got.items() if v} == {degree:expect_multiplicity},(m,got)
        print('PASS cycle homology',t,'vertices: nonzero reduced Betti',degree,expect_multiplicity,'faces',sum(faces.values()))
    pts,edges,D=farthest_edges(3,4)
    got,faces=betti_mod2(len(pts),edges)
    assert {d:v for d,v in got.items() if v} == {3:4},got
    print('PASS independent full metric case C3 x C4: reduced H_3 rank four,',sum(faces.values()),'nonempty faces')
    for m,n in ((3,4),(3,6),(5,4),(7,4)):
        _,edges,D=farthest_edges(m,n)
        # Verify all forbidden pairs are maximal-distance, and all others are in Rips 1-skeleton.
        assert len(edges) == m*n
        print('PASS direct metric farthest-degree test',m,n,'diameter',D,'forbidden edges',len(edges))
    for m,n in ((3,4),(3,6),(5,4)):
        for k in range(n):
            tr=cyclic_character_direct(m,n,k)
            assert tr==predicted_character(m,n,k),(m,n,k,tr,predicted_character(m,n,k))
        print('PASS full cyclic character through independent chain traces',m,n, 'power count',n)
    print('ALL CHECKS PASSED')

if __name__=='__main__':main()
