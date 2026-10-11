#!/usr/bin/env python3
from fractions import Fraction
from itertools import product, combinations

def prufer_tree(seq):
    n=len(seq)+2
    deg=[1]*n
    for x in seq:
        deg[x]+=1
    seq=list(seq)
    edges=[]
    for x in seq:
        leaf=min(i for i,d in enumerate(deg) if d==1)
        edges.append((leaf,x))
        deg[leaf]-=1
        deg[x]-=1
    rem=[i for i,d in enumerate(deg) if d==1]
    edges.append(tuple(rem))
    return edges

def connected_edge_subset(edges, chosen):
    verts=set()
    adj={}
    for idx in chosen:
        u,v=edges[idx]
        verts.update((u,v))
        adj.setdefault(u,[]).append(v)
        adj.setdefault(v,[]).append(u)
    if not verts:
        return False
    start=next(iter(verts))
    seen={start}
    stack=[start]
    while stack:
        u=stack.pop()
        for v in adj.get(u,()):
            if v not in seen:
                seen.add(v)
                stack.append(v)
    return seen==verts

formula_checks=0
for n in range(3,201):
    d=n-1
    C=n*(n-1)//2
    r2=Fraction((n-1)*(n-2),4)
    # Singleton upper bound.
    upper2=Fraction((C-d)**2,d*(d-1))
    assert upper2==r2
    for s in range(1,n-1):
        slack=Fraction(s*n,2)-Fraction(s*(s+1),2)
        norm2=Fraction(s*(d-s),d)
        d2=slack*slack/norm2
        closed=Fraction(d*s*(d-s),4)
        assert d2==closed
        assert d2>=r2
        assert (d2==r2)==(s in (1,n-2))
        formula_checks+=1

tree_checks=0
for n in range(3,7):
    seqs=[()] if n==2 else product(range(n), repeat=n-2)
    for seq in seqs:
        edges=prufer_tree(seq)
        assert len(edges)==n-1
        m=len(edges)
        for mask in range(1,(1<<m)-1):
            chosen=[i for i in range(m) if (mask>>i)&1]
            if not connected_edge_subset(edges,chosen):
                continue
            s=len(chosen)
            # A connected edge set in a tree has s+1 vertices.
            verts=set()
            for i in chosen:
                verts.update(edges[i])
            assert len(verts)==s+1
            height=s*(s+1)//2
            slack=Fraction(s*n,2)-height
            norm2=Fraction(s*(n-1-s),n-1)
            d2=slack*slack/norm2
            assert d2==Fraction((n-1)*s*(n-1-s),4)
            assert (d2==Fraction((n-1)*(n-2),4))==(s in (1,n-2))
            tree_checks+=1

print(f"VERIFY_OK operahedron-facet-shells formula_checks={formula_checks} tree_nest_checks={tree_checks}")
