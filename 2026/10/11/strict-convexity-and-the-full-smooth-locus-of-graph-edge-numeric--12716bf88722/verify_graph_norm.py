#!/usr/bin/env python3
"""Finite deterministic checks for edge-adjacency numerical-radius norms.
This is a supplement to, not a replacement for, the all-graph proof.
Python 3 standard library only.
"""
from itertools import combinations
from math import atan2, cos, sin, hypot, sqrt

def largest_eigenvalue_symmetric(a):
    b=[list(map(float,row)) for row in a]
    n=len(b)
    for _ in range(100*n*n):
        p,q=max(combinations(range(n),2),key=lambda ij: abs(b[ij[0]][ij[1]]))
        if abs(b[p][q])<1e-13: break
        angle=.5*atan2(2*b[p][q],b[q][q]-b[p][p])
        c,s=cos(angle),sin(angle)
        app,aqq,apq=b[p][p],b[q][q],b[p][q]
        for k in range(n):
            if k==p or k==q: continue
            u,v=b[k][p],b[k][q]
            b[p][k]=b[k][p]=c*u-s*v
            b[q][k]=b[k][q]=s*u+c*v
        b[p][p]=c*c*app-2*c*s*apq+s*s*aqq
        b[q][q]=s*s*app+2*c*s*apq+c*c*aqq
        b[p][q]=b[q][p]=0.
    else: raise AssertionError('Jacobi did not converge')
    return max(b[i][i] for i in range(n))

def norm(n,edges,weights):
    assert len(edges)==len(weights)
    a=[[0.]*n for _ in range(n)]
    for (u,v),w in zip(edges,weights):
        a[u][v]=a[v][u]=abs(w)
    return largest_eigenvalue_symmetric(a)/2.

def matching_ge_two(edges):
    return next(((i,j) for i,(u,v) in enumerate(edges)
                  for j,(s,t) in enumerate(edges) if i<j and len({u,v,s,t})==4), None)

def star_or_triangle(edges):
    common=set(edges[0]); common.intersection_update(*map(set,edges[1:]))
    if common:return True
    vertices=set(x for e in edges for x in e)
    return len(vertices)==3 and len(edges)==3

classes=[0,0]; checked=0
for n in range(2,6):
    all_edges=list(combinations(range(n),2))
    for bits in range(1,1<<len(all_edges)):
        edges=[e for i,e in enumerate(all_edges) if bits>>i&1]
        match=matching_ge_two(edges)
        if match is None:
            assert star_or_triangle(edges)
            classes[0]+=1
        else:
            assert not star_or_triangle(edges)
            i,j=match
            a=[0]*len(edges);b=[0]*len(edges)
            a[i]=2;b[i]=2;b[j]=.8
            assert abs(norm(n,edges,a)-1)<1e-10
            assert abs(norm(n,edges,b)-1)<1e-10
            assert abs(norm(n,edges,[(x+y)/2 for x,y in zip(a,b)])-1)<1e-10
            classes[1]+=1
        checked+=1

tri=[(0,1),(1,2),(0,2)]
assert abs(norm(3,tri,[1,1,0])-sqrt(2)/2)<1e-10
assert abs(norm(3,tri,[1,1,1])-1)<1e-10
h=1e-5
base=norm(3,tri,[1,1,0])
rate=(norm(3,tri,[1,1,h])-base)/h
assert abs(rate-.25)<1e-4
axis_base=norm(3,tri,[1,0,0])
axis_rate=(norm(3,tri,[1,h,0])-axis_base)/h
assert abs(axis_rate)<1e-4
cycle4=[(0,1),(1,2),(2,3),(3,0)]
p=[1,1,1,0]
r0=norm(4,cycle4,p)
rplus=(norm(4,cycle4,[1,1,1,h])-r0)/h
assert rplus>.05
print('VERIFY_OK graphs=%d matching_one=%d disjoint_matching=%d triangle_cusp=%.7f triangle_axis_slope=%.7g cycle4_cusp=%.7f analytic_proof_needed=True'%
      (checked,classes[0],classes[1],rate,axis_rate,rplus))
