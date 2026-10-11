#!/usr/bin/env python3
"""Standalone exact checks of cardinality-weighted star hypergraphic polytope diameters."""
from itertools import permutations, combinations
from math import comb, factorial
from fractions import Fraction


def predicted(r, weight):
    a = tuple(sum(weight[h - 1] * comb(r - j, h - 1)
                  for h in range(1, min(r-j+1, r) + 1))
              for j in range(1, r + 1))
    T = sum(comb(r, h) * weight[h-1] for h in range(1, r+1))
    assert T == sum(a)
    return a, T, T*T + sum(v*v for v in a)


def direct_vertices(r, weight):
    hyperedges=[]
    for h in range(1,r+1):
        if weight[h-1]:
            for leaves in combinations(range(1,r+1),h):
                hyperedges.append(((0,)+leaves,weight[h-1]))
    vertices=set()
    for order in permutations(range(r+1)):
        rank={v:i for i,v in enumerate(order)}
        z=[Fraction(0)]*(r+1)
        for S,w in hyperedges:
            z[min(S,key=rank.get)]+=w
        vertices.add(tuple(z))
    return vertices


def verify(r, weight):
    a,T,D2=predicted(r,weight)
    vert=direct_vertices(r,weight)
    expected=set()
    for s in range(r+1):
        for order in permutations(range(1,r+1),s):
            v=[T-sum(a[:s])]+[Fraction(0)]*r
            for j,u in enumerate(order):v[u]=a[j]
            expected.add(tuple(v))
    assert vert==expected,(r,weight,len(vert),len(expected))
    apex=(T,)+tuple(Fraction(0) for _ in range(r))
    tips={tuple([Fraction(0)]+list(p)) for p in set(permutations(a))}
    diameter_pairs=0
    for i,u in enumerate(sorted(vert)):
        for v in sorted(vert)[i+1:]:
            d2=sum((x-y)**2 for x,y in zip(u,v))
            assert d2<=D2,(r,weight,u,v,d2,D2)
            if d2==D2:
                diameter_pairs+=1
                assert (u==apex and v in tips) or (v==apex and u in tips)
    assert diameter_pairs==len(tips),(r,weight,diameter_pairs,len(tips))
    return len(vert),diameter_pairs,D2


def main():
    cases=0
    for r in range(2,6):
        for m in range(1,r+1):
            w=tuple(Fraction(1 if h<=m else 0) for h in range(1,r+1))
            v,p,d=verify(r,w)
            assert p==(1 if m==1 else factorial(r))
            cases+=1
            print('m-graph',r,m,'vertices',v,'pairs',p,'diameter_squared',d)
        for k in range(4):
            w=tuple(Fraction((h+2*k)%4+1 if h==1 else (k*h+1)%4) for h in range(1,r+1))
            v,p,d=verify(r,w)
            cases+=1
            print('weighted',r,k,'vertices',v,'pairs',p,'diameter_squared',d)
    for r in range(2,25):
        for m in range(1,r+1):
            w=tuple(Fraction(h<=m) for h in range(1,r+1))
            a,T,d=predicted(r,w)
            assert a==tuple(sum(comb(r-j,t) for t in range(0,m) if t<=r-j) for j in range(1,r+1))
            if m==1: assert d==r*(r+1)
            if m==2: assert d==(r*(r+1)//2)**2 + r*(r+1)*(2*r+1)//6
            if m==r: assert d==(2**r-1)**2+(4**r-1)//3
    print('PASS',cases,'complete small vertex/pair checks; 299 symbolic instances')

if __name__=='__main__':main()
