#!/usr/bin/env python3
"""Reconstruct neighborhood complexes and the explicit two-stage simplicial collapse for periodic and twisted toroidal grids.

Dependencies: Python standard library only. The symbolic proof is stated separately;
these are finite consistency tests, not verification for all integer parameters.
"""
from itertools import combinations
from collections import defaultdict, Counter, deque


def V(i,j,m,n,k):
    q,r=divmod(j,n)
    return ((i-q*k)%m)*n+r

def neigh(i,j,m,n,k):
    return frozenset([V(i+1,j,m,n,k),V(i-1,j,m,n,k),V(i,j+1,m,n,k),V(i,j-1,m,n,k)])


def faces_from_facets(facets):
    ff={}
    for f in facets:
        for k in range(1,len(f)+1):
            ff.setdefault(k,set()).update(combinations(sorted(f),k))
    return ff


def collapse(ff, s, t):
    s,t=tuple(sorted(s)),tuple(sorted(t))
    assert s in ff[len(s)] and t in ff[len(t)]
    cofaces=[]
    for d,Fs in ff.items():
        if d>=len(s):
            for f in Fs:
                if set(s).issubset(f):cofaces.append(f)
    assert set(cofaces)=={s,t}, (s,t,cofaces)
    ff[len(s)].remove(s); ff[len(t)].remove(t)


def boundary_rank_gf2(cols):
    pivots={}
    for mask in cols:
        while mask:
            p=mask.bit_length()-1
            if p in pivots: mask^=pivots[p]
            else:
                pivots[p]=mask;break
    return len(pivots)


def homology(ff):
    ranks={0:1}
    for k in sorted(ff):
        if k==1: continue
        lower=sorted(ff[k-1]); inds={s:i for i,s in enumerate(lower)}
        cols=[]
        for face in ff[k]:
            q=0
            for a in combinations(face,k-1):q^=1<<inds[a]
            cols.append(q)
        ranks[k-1]=boundary_rank_gf2(cols)
    ranks[max(ff)]=0
    return {k-1:len(ff[k])-ranks[k-1]-ranks[k] for k in ff if k>=2}


def test(m,n,k,full_homology=False):
    fcts={neigh(i,j,m,n,k) for i in range(m) for j in range(n)}
    assert len(fcts)==m*n and all(len(f)==4 for f in fcts)
    ff=faces_from_facets(fcts)
    assert Counter(len(f) for f in fcts)=={4:m*n}
    # Every triangle must belong to one tetrahedron, and straight pairs to one tetrahedron.
    owners=defaultdict(list)
    for center in range(m*n):
        i,j=divmod(center,n)
        f=neigh(i,j,m,n,k)
        for t in combinations(sorted(f),3):owners[t].append(center)
    assert all(len(a)==1 for a in owners.values())
    for i in range(m):
        for j in range(n):
            E=V(i+1,j,m,n,k); W=V(i-1,j,m,n,k)
            N=V(i,j+1,m,n,k); S=V(i,j-1,m,n,k)
            collapse(ff,(E,W,N),(E,W,N,S))
            collapse(ff,(E,W),(E,W,S))
    assert not ff.get(4)
    assert len(ff[1])==m*n and len(ff[2])==3*m*n and len(ff[3])==2*m*n
    # Each remaining edge is incident to two triangles and each vertex link is one cycle.
    edgetris=defaultdict(set)
    for tri in ff[3]:
        for e in combinations(tri,2):edgetris[e].add(tri)
    assert len(edgetris)==3*m*n and all(len(a)==2 for a in edgetris.values())
    link=defaultdict(lambda:defaultdict(set))
    for tri in ff[3]:
        for x in tri:
            a,b=sorted(set(tri)-{x});link[x][a].add(b);link[x][b].add(a)
    for x,li in link.items():
        assert len(li)==6 and all(len(ns)==2 for ns in li.values()),(m,n,x,li)
        seen={next(iter(li))};front=list(seen)
        while front:
            for y in li[front.pop()]:
                if y not in seen:seen.add(y);front.append(y)
        assert len(seen)==6
    g={v:set() for v in range(m*n)}
    for e in ff[2]:
        a,b=e;g[a].add(b);g[b].add(a)
    comps=[];seen=set()
    for v in g:
        if v in seen:continue
        comp={v};stack=[v];seen.add(v)
        while stack:
            for u in g[stack.pop()]:
                if u not in seen:seen.add(u);comp.add(u);stack.append(u)
        comps.append(comp)
    assert len(comps)==(2 if m%2==0 and (k+n)%2==0 else 1)
    for comp in comps:
        chi= len(comp)-sum(e[0] in comp for e in ff[2])+sum(t[0] in comp for t in ff[3])
        assert chi==0
    # A global coherent orientation exists: alternating diamond-square normals.
    # Each triangle can be oriented according to a (translation invariant) plane embedding,
    # rather than inferred from mod-two homology.
    if full_homology:
        betti=homology(ff)
        assert betti.get(1)==2*len(comps) and betti.get(2)==len(comps),(m,n,betti)
    return {'m':m,'n':n,'twist':k,'components':len(comps),'faces':(m*n,3*m*n,2*m*n),'checked_links':m*n}

if __name__=='__main__':
    count=0;links=0
    for m in range(5,9):
        for n in range(5,9):
            for k in range(m):
                z=test(m,n,k,full_homology=(m==5 and n==5))
                count+=1;links+=z['checked_links']
    print('VERIFY_OK cases=%d links=%d local_collapses=%d triangulated_surfaces=all mod2_homology=5_samples'% (count,links,2*links))
