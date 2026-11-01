#!/usr/bin/env python3
"""Reproducibility checks for a central-section distribution of cube-octahedron intersections.
Uses only the Python standard library. Finite sampling is corroboration, not proof.
"""
from fractions import Fraction as F
from itertools import permutations, product
from collections import Counter
from math import acos, atan2, pi, sqrt
from random import Random

def dot(u,v):
    return sum(x*y for x,y in zip(u,v))

def det(u,v,w):
    return u[0]*(v[1]*w[2]-v[2]*w[1])-u[1]*(v[0]*w[2]-v[2]*w[0])+u[2]*(v[0]*w[1]-v[1]*w[0])

def omega(u,v,w):
    A,B,C=[sqrt(dot(t,t)) for t in (u,v,w)]
    d=A*B*C+dot(u,v)*C+dot(u,w)*B+dot(v,w)*A
    return 2*atan2(abs(det(u,v,w)),d)

def distribution(t):
    assert 1<=t<=3
    if t==1: return {6:1.}
    if t==2: return {8:1.}
    if t==3:
        p4=6/pi*__import__('math').asin(1/3)
        return {4:p4,6:1-p4}
    if t<2:
        s=t-1
        mean=24/pi*acos(1/(1+s*s))+12/pi*acos(2*s/(1+s*s))
        q=12/pi*omega((1,0,0),(1,s,s*s),(1,s,s))
        result={6:4-mean/2+q,8:(mean-6)/2-2*q,10:q}
    else:
        s=t-2
        mean=24/pi*acos((1+2*s)/(2+s*s))+12/pi*acos((2-s*s)/(2+s*s))
        p=6/pi*omega((1,0,0),(1,s,0),(1,0,s))
        q=12/pi*omega((1,1,0),(1,1,1-s),(1+s,1+s*s,1-s))
        result={4:p,6:4-mean/2-2*p+q,8:mean/2-3+p-2*q,10:q}
    assert abs(sum(result.values())-1)<1e-12
    assert min(result.values())>-1e-12
    assert abs(sum(k*v for k,v in result.items())-mean)<1e-11
    return result

def vertices(c):
    assert 1<c<3
    s=c-1 if c<2 else c-2
    base=(F(1),s,F(0)) if c<2 else (F(1),F(1),s)
    return sorted({tuple(p[i]*e[i] for i in range(3))
                   for p in permutations(base) for e in product((-1,1),repeat=3)})

def active(v,c):
    A=[]
    for i in range(3):
        if abs(v[i])==1: A.append(('cube',i,1 if v[i]>0 else -1))
    for ss in product((-1,1),repeat=3):
        if dot(ss,v)==c: A.append(('octa',ss))
    return set(A)

def edges(V,c):
    ac=[active(v,c) for v in V]
    E=[(i,j) for i in range(len(V)) for j in range(i)
       if len(ac[i]&ac[j])>=2]
    return E

def check_chamber(t,n):
    a,b,c=sorted(map(abs,n),reverse=True)
    if t<2:
        s=t-1
        I1=b<s*a;I2=c<s*a;I3=c<s*b
        return 6+2*(I1+I2-I3)
    if t>2:
        s=t-2
        I=a-b<s*c;J=a-c<s*b;L=b-c<s*a;K=b+c<s*a
        return 8+2*I-2*J-2*L-2*K
    a,b,c=sorted(map(abs,n),reverse=True)
    return 8

def crossings(V,E,n):
    vals=[dot(v,n) for v in V]
    if 0 in vals: return None
    return sum(vals[i]*vals[j]<0 for i,j in E)

def main():
    r=Random(215003)
    for c in (F(6,5),F(3,2),F(9,5),F(11,5),F(5,2),F(14,5)):
        V=vertices(c);E=edges(V,c)
        assert len(V)==24 and len(E)==36,(c,len(V),len(E))
        for _ in range(450):
            x=(r.randint(1,1001),r.randint(1,1001),r.randint(1,1001))
            got=crossings(V,E,x)
            if got is None: continue
            predicted=check_chamber(c,x)
            assert got==predicted, (c,x,got,predicted)
        print('EXACT_RATIONAL_POLYTOPE_EDGE_AND_CHAMBER_TESTS_PASSED',str(c))
    # All possible sign chambers for the generic cuboctahedron yield 8 sides.
    cubo=sorted({tuple(p[i]*e[i] for i in range(3)) for p in set(permutations((1,1,0))) for e in product((-1,1),repeat=3)})
    cubo_edges=[(i,j) for i in range(len(cubo)) for j in range(i) if sum((cubo[i][k]-cubo[j][k])**2 for k in range(3))==2]
    assert len(cubo)==12 and len(cubo_edges)==24
    for _ in range(3000):
        x=(r.randint(1,3001),r.randint(1,3001),r.randint(1,3001))
        got=crossings(cubo,cubo_edges,x)
        if got is not None: assert got==8,(x,got)
    print('CUBOCTAHEDRON_EIGHT_VERTEX_CHAMBER_TESTS_PASSED')
    # Haar-uniform normals from independent centered Gaussians.
    for t in (1.2,1.5,1.8,2.2,2.5,2.8):
        c=F(str(t)); V=vertices(c);E=edges(V,c)
        counts=Counter(); m=65000
        for _ in range(m):
            n=tuple(r.gauss(0,1) for i in range(3))
            counts[crossings(V,E,n)]+=1
        theory=distribution(t)
        for k,prob in theory.items():
            empirical=counts[k]/m
            tol=max(.009,7*sqrt(max(prob*(1-prob),.00001)/m))
            assert abs(empirical-prob)<tol,(t,k,empirical,prob,tol)
        assert set(counts)==set(theory), (t,counts,theory)
        print('INDEPENDENT_HAAR_MONTE_CARLO_PASSED',t,[(k,round(counts[k]/m,5),round(theory[k],5)) for k in sorted(theory)])
    # Strict mean monotonicity and deterministic phase endpoints.
    def mean(t):return sum(k*p for k,p in distribution(t).items())
    left=[mean(1+i/1000) for i in range(1001)]
    right=[mean(2+i/1000) for i in range(1001)]
    assert all(x<y for x,y in zip(left,left[1:]))
    assert all(x>y for x,y in zip(right,right[1:]))
    assert abs(mean(2)-8)<1e-12 and abs(mean(1)-6)<1e-12
    print('EXACT_ENDPOINTS_AND_MONOTONICITY_DIAGNOSTICS_PASSED')
    print('ALL_CHECKS_PASSED')
if __name__=='__main__':main()
