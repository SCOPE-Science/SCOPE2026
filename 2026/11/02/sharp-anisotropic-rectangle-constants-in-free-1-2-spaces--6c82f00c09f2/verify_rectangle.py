#!/usr/bin/env python3
"""Finite, independent checks of a weighted-rectangle free 1/2 interpolation identity.

The continuum theorem requires its mathematical proof; this checker only validates
finite tree enumeration, sharp witnesses and randomized domain comparisons.
"""
from itertools import combinations
from fractions import Fraction
from math import sqrt, isclose
from random import Random

VERTICES = ((0, 0), (1, 0), (0, 1), (1, 1))
EDGES = tuple(combinations(range(4), 2))

def connected(edges):
    seen = {0}
    while True:
        old = len(seen)
        for i, j in edges:
            if i in seen: seen.add(j)
            if j in seen: seen.add(i)
        if len(seen) == old: return len(seen) == 4

TREES = tuple(edges for edges in combinations(EDGES, 3) if connected(edges))
assert len(TREES) == 16

def cutflow(masses, edges, edge):
    i, j = edge
    other = tuple(x for x in edges if x != edge)
    seen = {i}
    while True:
        old = len(seen)
        for u, v in other:
            if u in seen: seen.add(v)
            if v in seen: seen.add(u)
        if len(seen) == old: break
    assert j not in seen
    return sum((masses[k] for k in seen), masses[0]*0)

def costs(masses, r):
    assert abs(float(sum(masses))) <= 2e-12
    out=[]
    for tree in TREES:
        flow=[]
        for e in tree:
            (i,j)=e
            dij=abs(VERTICES[i][0]-VERTICES[j][0])+r*abs(VERTICES[i][1]-VERTICES[j][1])
            flow.append(abs(cutflow(masses,tree,e))*dij)
        out.append(tuple(sorted(flow)))
    return out

def free_half(masses, r):
    return min(sum(sqrt(float(v)) for v in t)**2 for t in costs(masses, r))

def weights(x,y):
    return ((1-x)*(1-y), x*(1-y), (1-x)*y, x*y)

def predicted(r):
    return (2*sqrt(r)+sqrt(r+1))**2/(3*r+1)

def main():
    cases=0
    # Exact arithmetic for sharp 16-tree patterns and all 16 costs.
    for r in (Fraction(1),Fraction(11,10),Fraction(2),Fraction(3),Fraction(5),Fraction(10),Fraction(37)):
        a=Fraction(2*r+1,3*r+1)
        b=Fraction(1,3*r+1)
        q=Fraction(r+1,3*r+1)
        masses=(q-a-b,a-q,b-q,q)
        assert sum(masses)==0
        costlist=costs(masses,r)
        assert len(costlist)==16
        lead=tuple(sorted((r,r,r+1)))
        sharpcount=0
        for trip in costlist:
            scaled=sorted((v*(3*r+1) for v in trip))
            if scaled==list(lead): sharpcount+=1
            if any(v==0 for v in scaled):
                assert isclose(sum(sqrt(float(v)) for v in scaled),float(r+1)+sqrt(float(r*(r+1))),rel_tol=1e-12)
            else:
                assert all(u>=v for u,v in zip(scaled,lead)),(r,scaled,lead)
            cases+=1
        assert sharpcount==3,(r,sharpcount)
        assert isclose(free_half(masses,r),predicted(float(r)),rel_tol=4e-14)
        # Symmetric interior secants give *exactly* the sharp norm ratio.
        h=Fraction(1,10000)
        x1=Fraction(1,2)+h*a/2; x0=Fraction(1,2)-h*a/2
        y1=Fraction(1,2)+h*b/2; y0=Fraction(1,2)-h*b/2
        mw=[v-u for v,u in zip(weights(x1,y1), weights(x0,y0))]
        ratio=free_half(mw,r)/float(h)
        assert isclose(ratio,predicted(float(r)),rel_tol=2e-11),(r,ratio,predicted(float(r)))
    # Boundary + random tangent tests, all 16 tree transports evaluated.
    rng=Random(472164)
    for r in (1., 1.01, 1.1, 1.2, 1.5, 2., 3., 5., 10., 25., 100.):
        lip=predicted(r)
        for i in range(280):
            x= rng.random() if i%10 else (0. if i%20 else 1.)
            y= rng.random() if i%12 else (0. if i%24 else 1.)
            speed_x=rng.random();speed_y=(1-speed_x)/r
            sx=-1 if i%2 else 1;sy=-1 if i%3 else 1
            a=sx*speed_x; b=sy*speed_y
            # derivatives of bilinear weights
            masses=(-(a*(1-y)+b*(1-x)), a*(1-y)-b*x, -a*y+b*(1-x), a*y+b*x)
            got=free_half(masses,r)
            assert got<=lip+1e-9,(r,x,y,got,lip)
            cases+=1
    print(f'PASS: {len(TREES)} exhaustive spanning trees; {cases} total exact/rand comparisons; all sharp witnesses and bounds verified.')

if __name__=='__main__':main()
