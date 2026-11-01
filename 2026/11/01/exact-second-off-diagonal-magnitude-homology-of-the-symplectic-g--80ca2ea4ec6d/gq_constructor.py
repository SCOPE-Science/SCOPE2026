#!/usr/bin/env python3
"""Construct finite symplectic incidence graphs and their shortest-path distances."""
from itertools import product

def make_quad(q):
    def norm(a):
        a=tuple(x%q for x in a)
        j=next((i for i,x in enumerate(a) if x),None)
        if j is None:return None
        c=pow(a[j],-1,q)
        return tuple(c*x%q for x in a)
    def symp(a,b):
        return (a[0]*b[2]-a[2]*b[0]+a[1]*b[3]-a[3]*b[1])%q
    pts=sorted({norm(a) for a in product(range(q),repeat=4)}-{None})
    plen=len(pts); pindex={v:i for i,v in enumerate(pts)}
    line_sets=set()
    for i,a in enumerate(pts):
        for b in pts[i+1:]:
            if symp(a,b)==0:
                line=frozenset(norm(tuple(u*a[k]+v*b[k] for k in range(4))) for u in range(q) for v in range(q) if u or v)
                if len(line)==q+1:line_sets.add(frozenset(pindex[v] for v in line))
    lines=sorted(line_sets,key=lambda z:tuple(sorted(z)))
    nbr=[set() for _ in range(plen+len(lines))]
    for j,line in enumerate(lines):
        for i in line:
            nbr[i].add(plen+j);nbr[plen+j].add(i)
    return pts,lines,nbr

def shortest_paths(nbr):
    ds=[]
    for i in range(len(nbr)):
        d=[-1]*len(nbr);d[i]=0;todo=[i]
        for u in todo:
            for v in nbr[u]:
                if d[v]<0:
                    d[v]=d[u]+1;todo.append(v)
        assert len(todo)==len(nbr)
        ds.append(d)
    return ds

