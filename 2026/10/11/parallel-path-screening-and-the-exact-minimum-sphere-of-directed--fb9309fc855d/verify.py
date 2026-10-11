#!/usr/bin/env python3
"""Exact arithmetic replay of two-terminal parallel-path root-polytope certificate."""
from fractions import Fraction as Q
from itertools import product
from collections import Counter


def data(lengths):
    lengths = tuple(lengths)
    assert len(lengths) >= 2 and min(lengths) >= 1
    assert lengths.count(1) <= 1 and max(lengths) >= 2
    L = max(lengths)
    k = lengths.count(L)
    vertices = ["s", "t"]
    z = {"s": Q(L,2), "t": -Q(L,2)}
    edges = []
    multipliers = []
    for i, ell in enumerate(lengths):
        path = ["s"]
        for j in range(1,ell):
            v = (i,j)
            vertices.append(v)
            path.append(v)
            z[v] = Q(ell,2)-j
        path.append("t")
        alpha = Q(L, 2*k) if ell == L else Q(0)
        for j in range(1, ell+1):
            edges.append((path[j-1], path[j]))
            multipliers.append(alpha + Q((j-1)*(ell-j),2))
    N = Q(L*L,2)+sum((Q(ell*(ell-1)*(ell-2),12) for ell in lengths),Q(0))
    return vertices,z,edges,multipliers,N


def check(lengths):
    vertices,z,edges,lam,N = data(lengths)
    assert len(vertices)==2+sum(i-1 for i in lengths)
    assert len(edges)==sum(lengths)
    assert len(edges)==len(set(edges))
    assert sum(z.values())==0
    assert N>0 and sum(v*v for v in z.values())==N
    assert all(w>=0 for w in lam)
    assert sum(lam)==N
    gradient={v:Q(0) for v in vertices}
    gaps=[]
    for (u,v),w in zip(edges,lam):
        gap=z[u]-z[v]
        gaps.append(gap)
        assert gap>=1
        assert w*(gap-1)==0
        gradient[u]+=w
        gradient[v]-=w
    assert gradient==z
    c={v:z[v]/N for v in vertices}
    norm2=sum(t*t for t in c.values())
    assert norm2==1/N
    center_from_roots={v:Q(0) for v in vertices}
    for (u,v),w in zip(edges,lam):
        center_from_roots[u]+=w/N
        center_from_roots[v]-=w/N
    assert center_from_roots==c
    R2=2-1/N
    contact=0
    for (u,v),gap,w in zip(edges,gaps,lam):
        dist2=2+norm2-2*(c[u]-c[v])
        assert dist2<=R2
        assert R2-dist2==2*(gap-1)/N
        if gap==1:
            contact+=1
        if w>0:
            assert gap==1
    L=max(lengths)
    predicted=sum((ell if ell==L else max(ell-2,0)) for ell in lengths)
    assert contact==predicted
    assert (contact==len(edges)) == all(ell==L for ell in lengths)
    return len(edges),contact


def main():
    count=contacts=edges=0
    for k in range(2,5):
        for ls in product(range(1,7),repeat=k):
            if ls.count(1)>1 or max(ls)<2:
                continue
            m,c=check(ls)
            count+=1
            contacts+=c
            edges+=m
    # Exact invariance of adding a fresh two-edge path across an independent sweep.
    stable=0
    for k in range(2,4):
        for ls in product(range(2,8),repeat=k):
            _,z,_,_,N = data(ls)
            _,zz,_,_,N2 = data(ls+(2,))
            assert N==N2
            assert all(z[v]==zz[v] for v in z)
            stable+=1
    print(f"EXACT_OK instances={count} edges={edges} contacts={contacts} two_path_invariances={stable}")

if __name__=='__main__':
    main()
