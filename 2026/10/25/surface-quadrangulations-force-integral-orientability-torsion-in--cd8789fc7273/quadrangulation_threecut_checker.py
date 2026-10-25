#!/usr/bin/env python3
"""Finite checks for a three-cut/surface-quadrangulation theorem.

Checks complete defining face sets, an explicit simplicial free-face collapse,
and finite-field boundary ranks. The all-parameter structural proof is separate.
"""
from collections import defaultdict
from itertools import combinations
from math import comb


def build(m, n):
    assert m >= 7 and n >= 7
    V = tuple(range(m * n))
    def vid(x, y): return (y % n) * m + (x % m)
    adj = [set() for _ in V]
    def edge(u, v):
        assert u != v
        adj[u].add(v); adj[v].add(u)
    squares = []
    for y in range(n):
        for x in range(m):
            edge(vid(x, y), vid(x + 1, y))
            if y + 1 < n:
                edge(vid(x, y), vid(x, y+1))
                a, b, c, d = (vid(x, y), vid(x+1,y),
                              vid(x+1,y+1), vid(x,y+1))
            else:
                edge(vid(x, y), vid(-x, 0))
                a, b, c, d = (vid(x,y), vid(x+1,y),
                              vid(-x-1,0), vid(-x,0))
            squares.append((a,b,c,d))
    E = {frozenset((u,v)) for u in V for v in adj[u] if u<v}
    assert len(E) == 2*len(V)
    assert all(len(adj[u]) == 4 for u in V)
    assert len(squares)==len(V)
    return V, adj, E, squares


def boundary_rank(simplices, p):
    """Sparse rank over F_p for oriented boundaries; integer entries +-1."""
    if not simplices: return 0
    k = len(simplices[0])-1
    rows = {s:i for i,s in enumerate(sorted(set(combinations_from(simplices,k))))}
    pivots = {}
    for t in simplices:
        col = {}
        for i in range(len(t)):
            s=t[:i]+t[i+1:]
            r=rows[s]
            z=(((-1)**i)%p)
            col[r]=(col.get(r,0)+z)%p
            if col[r]==0: del col[r]
        while col:
            r=min(col)
            if r not in pivots:
                coeff=col[r]
                inv=pow(coeff,-1,p)
                pivots[r]={a:(v*inv)%p for a,v in col.items() if v%p}
                break
            coeff=col[r]
            for a,v in pivots[r].items():
                nv=(col.get(a,0)-coeff*v)%p
                if nv: col[a]=nv
                else: col.pop(a,None)
    return len(pivots)


def combinations_from(simplices,k):
    for s in simplices:
        for t in combinations(s,k): yield t


def torus(m,n):
    assert m>=7 and n>=7
    V=tuple(range(m*n))
    def vid(x,y): return (y%n)*m+(x%m)
    adj=[set() for _ in V]
    def add(u,v): adj[u].add(v);adj[v].add(u)
    sq=[]
    for y in range(n):
        for x in range(m):
            add(vid(x,y),vid(x+1,y));add(vid(x,y),vid(x,y+1))
            sq.append((vid(x,y),vid(x+1,y),vid(x+1,y+1),vid(x,y+1)))
    E={frozenset((u,v)) for u in V for v in adj[u] if u<v}
    return V,adj,E,sq


def cube():
    V=tuple(range(8));adj=[set() for _ in V]
    for u in V:
        for i in range(3): adj[u].add(u^(1<<i))
    E={frozenset((u,v)) for u in V for v in adj[u] if u<v}
    sq=[]
    for i,j in combinations(range(3),2):
        k=({0,1,2}-{i,j}).pop()
        for z in (0,1):
            a=z*(1<<k);b=a^(1<<i);c=b^(1<<j);d=a^(1<<j)
            sq.append((a,b,c,d))
    return V,adj,E,sq


def check_case(label, data, surface, expected_q):
    V, adj, original_edges, sq = data
    N = len(V)
    # All Alexander-dual faces in dimensions >= 2, by the defining property:
    # every induced triple must be connected.
    tri = {frozenset(t) for t in combinations(V,3)
           if sum(1 for u,v in combinations(t,2) if v in adj[u]) >= 2}
    assert all(sum(1 for u,v in combinations(t,2) if v in adj[u]) == 2
               for t in tri)  # no triangles in the graph
    tet = {frozenset(t) for t in combinations(V,4)
           if all(frozenset(r) in tri for r in combinations(t,3))}
    assert len(tri)==sum(comb(len(adj[u]),2) for u in V), (N,len(tri))
    assert tet == {frozenset(s) for s in sq}
    assert len(tet)==len(sq)
    assert all(len(adj[u]&adj[v])<=2 for u,v in combinations(V,2) if v not in adj[u])
    assert len(original_edges)==2*len(sq)  # closed quadrangulation
    edges = {frozenset(pair) for pair in combinations(V,2)}
    # Own copy, manipulated by exact free-face removals.
    F={1:set(edges),2:set(tri),3:set(tet)}
    def remove_pair(sigma,tau):
        d=len(sigma)-1
        assert tau in F[d+1]
        assert sigma in F[d]
        assert sigma.issubset(tau)
        assert sum(sigma.issubset(z) for z in F[d+1])==1
        assert all(not sigma.issubset(z) for h in range(d+2,4) for z in F[h])
        F[d].remove(sigma)
        F[d+1].remove(tau)
    retained_tri=set()
    retained_diag=set()
    for a,b,c,d in sq:
        # Collapse the tetrahedron with one face, then a leftover triangle
        # across the opposite graph-distance-two diagonal.
        remove_pair(frozenset((a,b,c)),frozenset((a,b,c,d)))
        remove_pair(frozenset((a,c)),frozenset((a,c,d)))
        retained_tri.update((frozenset((a,b,d)),frozenset((b,c,d))))
        retained_diag.add(frozenset((b,d)))
    assert len(retained_diag)==len(sq)
    # Unique-midpoint two-step triples are paired with their free diagonal.
    axis_tri=[]
    for t in sorted(F[2],key=lambda a:tuple(sorted(a))):
        ends=[]
        for u,v in combinations(sorted(t),2):
            if v not in adj[u]: ends.append(frozenset((u,v)))
        assert len(ends)==1
        diagonal=ends[0]
        u,v=tuple(diagonal)
        if len(adj[u]&adj[v])==1:
            axis_tri.append((diagonal,t))
    assert len(axis_tri)==len(tri)-4*len(sq)
    for e,t in axis_tri: remove_pair(e,t)
    assert not F[3]
    assert F[2]==retained_tri
    assert len(F[2])==2*len(sq)
    surface_edges=set(original_edges)|retained_diag
    assert len(surface_edges)==len(original_edges)+len(sq)
    # No leftover non-surface edges support triangles. Every such edge is
    # freely adjoined at two points of a connected surface.
    assert all(all(frozenset(pair) in surface_edges for pair in combinations(t,2))
               for t in F[2])
    long_edges=F[1]-surface_edges
    assert len(long_edges)==comb(N,2)-len(tri)==expected_q
    # Test that remaining surface is a closed (triangulated) 2-manifold:
    counts=defaultdict(int)
    links=defaultdict(lambda: defaultdict(set))
    for t in F[2]:
        for e in combinations(t,2): counts[frozenset(e)]+=1
        for u in t:
            v,w=list(t-{u})
            links[u][v].add(w)
            links[u][w].add(v)
    assert len(counts)==len(surface_edges) and all(counts[e]==2 for e in surface_edges)
    for u in V:
        nbr=links[u]
        assert len(nbr)>=3
        assert all(len(a)==2 for a in nbr.values())
        seen=set(); stack=[next(iter(nbr))]
        while stack:
            v=stack.pop()
            if v not in seen: seen.add(v);stack.extend(nbr[v]-seen)
        assert len(seen)==len(nbr)
    chi=N-len(surface_edges)+len(F[2])
    assert chi=={'sphere':2,'torus':0,'klein':0}[surface]
    simplices2=sorted(tuple(sorted(s)) for s in F[2])
    ranks={p:boundary_rank(simplices2,p) for p in (2,3,5)}
    b1={};b2={}
    for p,rank in ranks.items():
        b1[p]=len(surface_edges)-(N-1)-rank
        b2[p]=len(F[2])-rank
    expected={'sphere':({2:0,3:0,5:0},{2:1,3:1,5:1}),
              'torus':({2:2,3:2,5:2},{2:1,3:1,5:1}),
              'klein':({2:2,3:1,5:1},{2:1,3:0,5:0})}[surface]
    assert (b1,b2)==expected,(label,b1,b2)
    return dict(case=label,N=N,surface=surface,chi=chi,
        graph_edges=len(original_edges),connected_triples=len(tri),
        square_tetrahedra=len(tet),
        elementary_pairs=len(tri)-2*len(sq),
        surface_triangles=len(F[2]),surface_edges=len(surface_edges),
        free_chords=len(long_edges),boundary2_ranks=ranks,
        b1_mod_p=b1,b2_mod_p=b2)

if __name__=='__main__':
    cases=(('cube',cube(),'sphere',4),
           ('torus7x7',torus(7,7),'torus',882),
           ('klein7x7',build(7,7),'klein',882),
           ('klein7x8',build(7,8),'klein',1204))
    for label,data,surface,q in cases:
        print('PASS',check_case(label,data,surface,q))
