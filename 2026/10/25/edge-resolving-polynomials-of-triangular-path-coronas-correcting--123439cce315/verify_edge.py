#!/usr/bin/env python3
"""Independent adjacency-metric verification of edge resolving-set enumerators for triangular-path graphs."""
from collections import deque, Counter
from itertools import combinations
from math import comb


def graph(n):
    assert n >= 2
    edges = []
    for i in range(n-1):
        edges.extend(((i,i+1),(i,n+i),(i+1,n+i)))
    return edges


def distances(n):
    edges = graph(n)
    nv = 2*n-1
    adj = [[] for _ in range(nv)]
    for a,b in edges:
        adj[a].append(b)
        adj[b].append(a)
    profiles = []
    for origin in range(nv):
        d = [-1] * nv
        d[origin] = 0
        q = deque((origin,))
        while q:
            a = q.popleft()
            for b in adj[a]:
                if d[b] == -1:
                    d[b] = d[a]+1
                    q.append(b)
        profiles.append([min(d[a],d[b]) for a,b in edges])
    return profiles


def auxiliary_edges(n):
    m = n-1
    if n == 2:
        return [(0,1),(0,2),(1,2)], {0,1,2}
    if n == 3:
        vertices = {0, n-1, n, n+1}
        return list(combinations(sorted(vertices),2)), vertices
    w = [n+i for i in range(m)]
    edges = [(w[i],w[i+1]) for i in range(m-1)]
    edges += list(combinations((0,w[0],w[1]),2))
    edges += list(combinations((n-1,w[-2],w[-1]),2))
    return list(set(tuple(sorted(e)) for e in edges)), set(w+[0,n-1])


def independent_path_poly(m):
    assert m >= -1
    if m <= 0:
        return [1]
    if m == 1:
        return [1,1]
    p0,p1=[1],[1,1]
    for j in range(2,m+1):
        out=[0]*max(len(p1),len(p0)+1)
        for k,c in enumerate(p1):out[k]+=c
        for k,c in enumerate(p0):out[k+1]+=c
        p0,p1=p1,out
    return p1


def theoretical(n):
    if n==2:return [0,0,3,1]
    if n==3:return [0,0,0,4,5,1]
    m=n-1
    p=[independent_path_poly(m),independent_path_poly(m-2),independent_path_poly(m-4)]
    ip=[0]*(m+3)
    for poly,shift,factor in zip(p,(0,1,2),(1,2,1)):
        for k,c in enumerate(poly):ip[k+shift]+=factor*c
    cp=[0]*(2*n)
    for indep,ct in enumerate(ip):
        cover=(n+1)-indep
        for chosen in range(n-1):
            cp[cover+chosen]+=ct*comb(n-2,chosen)
    return cp


def enumerated(n):
    dd=distances(n)
    nv=len(dd)
    ne=len(dd[0])
    verts=list(range(nv))
    aux, relevant=auxiliary_edges(n)
    counts=Counter()
    checked=0
    for mask in range(1<<nv):
        is_cover=all((mask>>a&1) or (mask>>b&1) for a,b in aux)
        codes=[]
        for e in range(ne):
            codes.append(tuple(dd[v][e] for v in verts if mask>>v&1))
        is_resolving=len(set(codes))==ne
        if is_cover!=is_resolving:
            raise AssertionError((n,mask,is_cover,is_resolving))
        if is_resolving:counts[mask.bit_count()]+=1
        checked+=1
    result=[counts.get(k,0) for k in range(nv+1)]
    if result!=theoretical(n):
        raise AssertionError((n,result,theoretical(n)))
    return checked,result


def independently_check_witness_pairs(n):
    if n<4:return
    dd=distances(n)
    aux,_=auxiliary_edges(n)
    got=set()
    for a,b in combinations(range(len(dd[0])),2):
        witnesses=frozenset(v for v in range(len(dd)) if dd[v][a]!=dd[v][b])
        if len(witnesses)==2:got.add(witnesses)
    expected=set(frozenset(x) for x in aux)
    if got!=expected:raise AssertionError((n,got^expected))


def verify():
    total=0
    for n in range(2,10):
        checked,coeff=enumerated(n)
        total+=checked
        print('n=%d subsets=%d edge-resolver-coefficients=%s' % (n,checked,coeff))
    for n in range(4,15):independently_check_witness_pairs(n)
    for n in range(4,65):
        co=theoretical(n)
        k=min(i for i,x in enumerate(co) if x)
        expect=(n+1)//2+1
        count=4 if n%2==0 else 2*(n-1)
        assert (k,co[k])==(expect,count),(n,k,co[k],expect,count)
    print('PASS: %d graph-vertex subsets, all coefficients and cover characterization for n=2..9; pairwise distinguishing witnesses for n=4..14; 61 extremal parameter checks.' % total)


if __name__=='__main__':verify()
