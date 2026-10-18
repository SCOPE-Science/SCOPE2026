#!/usr/bin/env python3
"""Exact rational section-cell certificate and analytic Crofton check.

Polytope: K = {(x,y,z): |x|+|y|<=2, |x|+|z|<=2,
                             |y|+|z|<=2}.
Requires only Python 3's standard library.
"""
from fractions import Fraction as Q
from itertools import product, combinations
from math import sqrt, pi, atan, acos, atan2, hypot
from collections import defaultdict
import math, random

V=[]
for i in range(3):
    for sg in (-1,1):
        v=[0,0,0];v[i]=2*sg;V.append(tuple(v))
V+=list(product((-1,1), repeat=3))
facets=[]
for i,j in combinations(range(3),2):
    for a,b in product((-1,1), repeat=2):
        n=[0,0,0];n[i]=a;n[j]=b
        facet=frozenset(k for k,v in enumerate(V) if sum(n[z]*v[z] for z in range(3))==2)
        assert len(facet)==4
        facets.append(facet)
assert len(V)==14 and len(facets)==12
E=[]
for a,b in combinations(range(14),2):
    if sum(a in F and b in F for F in facets)==2:
        E.append((a,b))
assert len(E)==24
assert all(sum((V[b][i]-V[a][i])**2 for i in range(3))==3 for a,b in E)

def vec(x):return (Q(1),x[0],x[1])
def dot(a,b):return sum(a[i]*b[i] for i in range(3))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def area2(poly):
    return sum(p[0]*q[1]-p[1]*q[0] for p,q in zip(poly,poly[1:]+poly[:1]))

def tri_moment(tri):
    vs=[tuple(float(z) for z in vec(P)) for P in tri]
    moment=[0.,0.,0.]
    for a,b in zip(vs,vs[1:]+vs[:1]):
        c=cross(a,b);r=sqrt(dot(c,c));theta=atan2(r,dot(a,b))
        for i in range(3):moment[i]+=theta*c[i]/r/2
    return moment

# The seven rational subchambers resolve every vertex-height ordering.
A=(Q(0),Q(0)); B=(Q(1,3),Q(0)); C=(Q(1,4),Q(1,4))
D=(Q(2,5),Q(1,5)); E0=(Q(1,2),Q(1,2)); F=(Q(1),Q(0))
G=(Q(1),Q(2,3)); H=(Q(1),Q(1))
triangles=((A,B,C),(B,D,C),(D,E0,C),(B,F,D),(F,E0,D),(F,G,E0),(G,H,E0))
assert all(area2(list(T))>0 for T in triangles)
assert sum(area2(list(T)) for T in triangles)==1  # twice the base area 1/2

zones={
0:{4:(2,-2,-2),5:(0,0,4),6:(0,4,-4),7:(0,0,4),8:(2,-2,-2)},
1:{3:(-2,2,2),5:(4,-4,0),6:(0,4,-4),7:(2,-2,2),8:(-2,2,2)},
2:{3:(-2,2,2),5:(4,-4,0),6:(-2,2,2),7:(4,0,-4),8:(0,4,-4),9:(-2,-2,6)}
}

Ik=defaultdict(float)
for z,tri in enumerate(triangles):
    # Every pair of vertex heights has one strict sign throughout the
    # triangle's interior: check endpoints with exact rational arithmetic.
    for a,b in combinations(range(14),2):
        ss=[dot([V[a][i]-V[b][i] for i in range(3)],vec(P)) for P in tri]
        assert not (min(ss)<0<max(ss)),(z,a,b,ss)
    c=tuple(sum(v[i] for v in tri)/3 for i in range(2))
    hv=[dot(v,vec(c)) for v in V]
    order=sorted(range(14),key=lambda t:hv[t])
    assert all(hv[order[j]]<hv[order[j+1]] for j in range(13))
    coeff={k:[0,0,0] for k in range(3,10)}
    for j in range(13):
        a,b=order[j:j+2];t=(hv[a]+hv[b])/2
        sides=sum((hv[i]-t)*(hv[j]-t)<0 for i,j in E)
        assert 3<=sides<=9
        for i in range(3):coeff[sides][i]+=V[b][i]-V[a][i]
    expected=zones[0 if z<5 else 1 if z==5 else 2]
    assert {k:tuple(v) for k,v in coeff.items() if any(v)}==expected,(z,coeff)
    moment=tri_moment(list(tri))
    for k,v in coeff.items():
        Ik[k]+=dot(v,moment)

alpha=atan(1/(2*sqrt(2)));beta=atan(sqrt(2)/5)
gamma=atan(1/sqrt(2)); delta=atan(1/sqrt(11))
assert abs(alpha+beta-gamma)<1e-15
J={
3:sqrt(3)*pi/6-sqrt(2)*gamma,
4:sqrt(3)*pi/6-pi/4,
5:pi*(0.5-sqrt(3)/3)+sqrt(2)*beta,
6:-pi/2+sqrt(2)*gamma+sqrt(11)*delta,
7:pi*(0.5-sqrt(3)/6)+sqrt(2)*alpha-sqrt(11)*delta,
8:pi*(sqrt(3)/3-0.25)+sqrt(2)*(alpha-beta)-sqrt(11)*delta,
9:sqrt(11)*delta-2*sqrt(2)*alpha,
}
for k in range(3,10):
    assert abs(Ik[k]-J[k])<2e-14,(k,Ik[k],J[k])
assert all(J[k]>0 for k in J)
Z=pi*sqrt(3)/6  # Crofton mass of one 1/48 spherical symmetry sector.
assert abs(sum(J.values())-Z)<2e-14
assert abs(sum(k*J[k] for k in J)/Z-6)<1e-14
print('RATIONAL_CHAMBERS_OK vertices=14 facets=12 edges=24 triangles=7')
print('EXACT_FORMULAS_OK classes=3..9 expectation=6')
for k in range(3,10):print('p%d=%.15f'%(k,J[k]/Z))

# Independent stochastic check: directions must be weighted by width h(u)
# when a uniformly chosen intersection offset is used (Crofton sampling).
rng=random.Random(9271)
weighted=[0.]*10
for _ in range(120000):
    u=[rng.gauss(0,1) for i in range(3)]; m=sqrt(sum(x*x for x in u));u=[x/m for x in u]
    ht=[dot(u,v) for v in V]
    h=max(ht)
    t=h*(2*rng.random()-1)
    sides=sum((ht[a]-t)*(ht[b]-t)<0 for a,b in E)
    weighted[sides]+=h
s=sum(weighted)
assert sum(abs(weighted[k]/s-J[k]/Z) for k in range(3,10))<0.022
print('WEIGHTED_RANDOM_PLANES_OK samples=120000')
