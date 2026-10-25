#!/usr/bin/env python3
"""Exact-integer incidence and independent Haar/quadrature checks for an Archimedean solid.
Run: python3 verify.py. Requires only Python >= 3.9 standard library.
This is corroboration of the separate analytic spherical-angle proof.
"""
import itertools
import math
import random
from collections import Counter

V = sorted(set(tuple(s*v for s, v in zip(signs,perm))
               for perm in set(itertools.permutations((2,1,0)))
               for signs in itertools.product((-1,1),repeat=3)))
assert len(V)==24
E = sorted((i,j) for i in range(24) for j in range(i+1,24)
           if sum((V[i][k]-V[j][k])**2 for k in range(3))==2)
assert len(E)==36
assert all(sum(i==k or j==k for i,j in E)==3 for k in range(24))
assert all(sum(x*x for x in v)==5 for v in V)
assert all(sum(V[i][k]*V[j][k] for k in range(3))==4 for i,j in E)
print('EXACT_24_VERTICES_36_EDGES_EQUAL_VERTEX_AND_EDGE_DOT_PRODUCTS_OK')

def dot(v,u): return sum(a*b for a,b in zip(v,u))
def n_intersections(u):
    dots=[dot(v,u) for v in V]
    if any(x==0 for x in dots): return None
    return sum(dots[i]*dots[j]<0 for i,j in E)
def n_formula(u):
    x,y,z=sorted(map(abs,u),reverse=True)
    if 2*y==x or 2*z==x or y==2*z: return None
    return 4+2*(2*z>y)+2*(2*y<x)+2*(2*z<x)

seen=Counter()
for a in range(1,44):
    for b in range(1,a+1):
        for c in range(1,b+1):
            u=(a,b,c)
            s=n_intersections(u)
            t=n_formula(u)
            if s is None or t is None:continue
            assert s==t,(u,s,t)
            seen[s]+=1
assert set(seen)=={6,8,10},seen
print('INDEPENDENT_EXACT_INTEGER_EDGE_CROSSING_VERSUS_FACE_FORMULA_OK',sum(seen.values()),dict(seen))

rays={
    'o':(1,0,0),'a':(4,2,1),'b':(2,1,1),
    'c':(2,2,1),'d':(1,1,1),'e':(2,1,0),'f':(1,1,0)
}
def angle(names):
    a,b,c=[rays[s] for s in names]
    def dot(a,b): return sum(x*y for x,y in zip(a,b))
    def norm(a): return math.sqrt(dot(a,a))
    v=(b[0]*c[1]-b[1]*c[0],b[1]*c[2]-b[2]*c[1],b[2]*c[0]-b[0]*c[2])
    # direct scalar triple product using (a dot b cross c)
    cross=(b[1]*c[2]-b[2]*c[1],b[2]*c[0]-b[0]*c[2],b[0]*c[1]-b[1]*c[0])
    det=abs(dot(a,cross))
    na,nb,nc=norm(a),norm(b),norm(c)
    return 2*math.atan2(det,na*nb*nc+dot(a,b)*nc+dot(b,c)*na+dot(c,a)*nb)

omega10=angle('oab')
omega6=angle('bcd')+angle('efc')+angle('eca')
p={10:12*omega10/math.pi,6:12*omega6/math.pi}
p[8]=1-p[6]-p[10]
assert all(0<v<1 for v in p.values())
assert abs(sum(p.values())-1)<1e-13
assert abs(sum(i*p[i] for i in p)-36*math.acos(4/5)/math.pi)<1e-13
print('SPHERICAL_TRIANGLE_CLOSED_FORM_AND_INDEPENDENT_EDGE_MEAN_IDENTITY_OK', {i:round(p[i],12) for i in sorted(p)})

def f(t,s):return s/((1+t*t)*math.sqrt(1+t*t+s*s))
def simpson(f,a,b,n=2000):
    assert n%2==0
    h=(b-a)/n
    return h/3*(f(a)+f(b)+4*sum(f(a+(2*k-1)*h) for k in range(1,n//2+1))
                +2*sum(f(a+2*k*h) for k in range(1,n//2)))
q10=12/math.pi*simpson(lambda t:f(t,t)-f(t,t/2),0,.5)
q6=12/math.pi*(simpson(lambda t:f(t,t/2),.5,1)
               +simpson(lambda t:f(t,t)-f(t,.5),.5,1))
assert abs(p[6]-q6)<1e-11,(p[6],q6)
assert abs(p[10]-q10)<1e-11,(p[10],q10)
assert abs(simpson(lambda t:f(t,t),0,1)-math.pi/12)<1e-11
print('INDEPENDENT_PROJECTIVE_SPHERICAL_AREA_QUADRATURE_OK')

# The random test counts crossings of true polytope edges, NOT the classification formula.
rng=random.Random(20261020)
n=250000
counts=Counter()
for k in range(n):
    u=(rng.gauss(0,1),rng.gauss(0,1),rng.gauss(0,1))
    nd=n_intersections(u)
    assert nd in p
    counts[nd]+=1
for m in (6,8,10):
    err=math.sqrt(p[m]*(1-p[m])/n)
    assert abs(counts[m]/n-p[m])<6*err+0.0006,(m,counts[m]/n,p[m],err)
print('INDEPENDENT_UNIFORM_SPHERE_HAAR_SAMPLING_OK',n,dict(counts))
print('ALL_TRUNCATED_OCTAHEDRON_CENTRAL_SECTION_LAW_CHECKS_OK')
