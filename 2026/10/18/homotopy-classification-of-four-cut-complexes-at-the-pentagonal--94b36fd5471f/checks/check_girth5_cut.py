#!/usr/bin/env python3
"""Finite verification of the pentagonal correction for ordinary 4-cut complexes.

This script uses only the Python standard library. It does not replace the
uniform graph-theoretic proof and makes no inference from finitely many graphs.
"""
from itertools import combinations
from math import comb

def graph(n, edges):
    adj = [set() for _ in range(n)]
    for x,y in edges:
        a,b=sorted((x,y))
        assert 0 <= a < b < n
        adj[a].add(b); adj[b].add(a)
    return adj

def cycle(n):
    return graph(n, sorted({tuple(sorted((i,(i+1)%n))) for i in range(n)}))

def gp(n,k):
    edges=[]
    for i in range(n):
        edges.extend([(i,(i+1)%n),(i,n+i),(n+i,n+(i+k)%n)])
    return graph(2*n,sorted({tuple(sorted(x)) for x in edges}))

def heawood():
    lines=sorted({tuple(sorted((a,b,a^b))) for a in range(1,8) for b in range(1,8) if a!=b})
    assert len(lines)==7
    return graph(14,[(p-1,7+i) for i,line in enumerate(lines) for p in line])

def disjoint(A,B):
    n=len(A)
    return graph(n+len(B),[(i,j) for i in range(n) for j in A[i] if i<j]+[(n+i,n+j) for i in range(len(B)) for j in B[i] if i<j])

def connected(adj, subset):
    S=set(subset)
    if not S: return False
    seen={min(S)}
    while True:
        nextseen=seen|{w for v in seen for w in adj[v] if w in S}
        if nextseen==seen: break
        seen=nextseen
    return seen==S

def rank_gf2(bitcolumns):
    pivots={}
    for x in bitcolumns:
        while x:
            k=x.bit_length()-1
            if k in pivots: x^=pivots[k]
            else:
                pivots[k]=x
                break
    return len(pivots)

def inspect(tag,A):
    n=len(A); V=range(n)
    assert all(i not in A[i] and all(i in A[j] for j in A[i]) for i in V)
    edge_count=sum(map(len,A))//2
    # No triangles or squares: test every unordered triple/quadruple.
    for s in combinations(V,3):
        assert sum(v in A[u] for u,v in combinations(s,2))!=3
    for s in combinations(V,4):
        e=[(u,v) for u,v in combinations(s,2) if v in A[u]]
        assert not (len(e)>=4 and any(sum(i in uv for uv in e)==2 for i in s) and len(e)==4),tag
    T={tuple(s) for s in combinations(V,4) if connected(A,s)}
    F={tuple(s) for s in combinations(V,5) if all(tuple(z) in T for z in combinations(s,4))}
    pent={tuple(s) for s in combinations(V,5) if all(sum(v in A[u] for u,v in combinations(s,2) if u==x or v==x)==2 for x in s)}
    assert F==pent,(tag,'five-face classification')
    # There are no allowed six-vertex faces (and therefore no larger faces).
    assert not any(all(tuple(z) in T for z in combinations(s,4)) for s in combinations(V,6)),tag
    t_formula=sum(comb(len(A[u]),3) for u in V)+sum((len(A[u])-1)*(len(A[v])-1) for u in V for v in A[u] if u<v)
    assert len(T)==t_formula,(tag,'four-face formula',len(T),t_formula)
    index_tri={s:i for i,s in enumerate(combinations(V,3))}
    idx_tet={s:i for i,s in enumerate(sorted(T))}
    rank3=rank_gf2([sum(1<<index_tri[z] for z in combinations(t,3)) for t in sorted(T)])
    rank4=rank_gf2([sum(1<<idx_tet[z] for z in combinations(f,4)) for f in sorted(F)])
    assert rank3==len(T)-len(F),(tag,'unexpected rank boundary3')
    assert rank4==len(F),(tag,'unexpected rank boundary4')
    # Check genuine free-face simplicial collapses, rather than just ranks.
    tets=set(T); existing_tris=set(index_tri)
    for f in sorted(F):
        face=next((t for t in combinations(f,4) if t in tets and sum(set(t).issubset(f2) for f2 in F)==1),None)
        assert face is not None,(tag,'cannot remove a five-face')
        tets.remove(face)
    removed=0
    while tets:
        frequency={}
        for t in tets:
            for z in combinations(t,3): frequency[z]=frequency.get(z,0)+1
        pair=next(((t,z) for t in sorted(tets) for z in combinations(t,3) if frequency[z]==1 and z in existing_tris),None)
        assert pair is not None,(tag,'tetrahedra without free triangular face',len(tets))
        t,z=pair
        tets.remove(t); existing_tris.remove(z); removed+=1
    B=comb(n-1,3)-len(T)+len(F)
    assert len(existing_tris)==comb(n,3)-len(T)+len(F)
    assert B>=0
    return tag,n,edge_count,len(T),len(F),rank3,rank4,removed,B

def main():
    graphs=[('cycle5',cycle(5)),('cycle6',cycle(6)),('cycle9',cycle(9)),
      ('Petersen',gp(5,2)),('dodecahedron',gp(10,2)),('Heawood',heawood()),
      ('two_cycles',disjoint(cycle(5),cycle(6))),
      # Two five-cycles share the edge 0-1, with vertex 8 isolated.
      ('pentagons_one_shared_edge',graph(9,[(0,1),(1,2),(2,3),(3,4),(4,0),(1,5),(5,6),(6,7),(7,0)])),
      # Two five-cycles share edges 0-1 and 1-2; vertices 7,8 isolated.
      ('pentagons_two_shared_edges',graph(9,[(0,1),(1,2),(2,3),(3,4),(4,0),(2,5),(5,6),(6,0)]))]
    print('graph n edges connected4 pentagons rank_d3 rank_d4 tet_tri_collapses B')
    for name,G in graphs:
        print(*inspect(name,G))
    print('PASS: face classification, mod-2 boundary ranks, and explicit elementary collapses')

if __name__=='__main__': main()
