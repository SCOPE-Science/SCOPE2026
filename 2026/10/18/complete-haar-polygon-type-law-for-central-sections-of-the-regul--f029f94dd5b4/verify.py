#!/usr/bin/env python3
"""Independent finite checks of the exact central-section law of a truncated octahedron.

All geometric and probability identities are proved separately in the accompanying result.
This script checks vertex/edge data, chamber combinatorics, solid angles,
and Monte Carlo statistics; sampling does not prove a universal identity.
"""
from itertools import permutations, product
from collections import Counter
from fractions import Fraction
from math import acos, atan, atan2, ceil, cos, isclose, pi, sqrt
import random

V = sorted({tuple(q[i]*signs[i] for i in range(3))
            for q in permutations((0,1,2))
            for signs in product((-1,1), repeat=3)})
assert len(V)==24 and all(sum(a*a for a in v)==5 for v in V)
E = [(u,v) for i,u in enumerate(V) for v in V[i+1:]
     if sum((u[k]-v[k])**2 for k in range(3))==2]
assert len(E)==36
assert all(sum(u[k]*v[k] for k in range(3))==4 for u,v in E)
assert all(sum((u[k]-v[k])**2 for k in range(3))==2 for u,v in E)

def dot(x,y):return sum(a*b for a,b in zip(x,y))
def norm(x):return sqrt(dot(x,x))
def det(x,y,z):return x[0]*(y[1]*z[2]-y[2]*z[1])-x[1]*(y[0]*z[2]-y[2]*z[0])+x[2]*(y[0]*z[1]-y[1]*z[0])
def omega(a,b,c):
    return 2*atan2(abs(det(a,b,c)),
       norm(a)*norm(b)*norm(c)+dot(a,b)*norm(c)
        +dot(b,c)*norm(a)+dot(c,a)*norm(b))

def sides_from_edges(u):
    assert all(dot(u,v)!=0 for v in V)
    return sum(dot(u,a)*dot(u,b)<0 for a,b in E)

def sides_formula(u):
    x,y,z=sorted(map(abs,u),reverse=True)
    assert x>y>z>0 and x!=2*y and x!=2*z and y!=2*z
    return 6+2*(x>2*z)+2*(x>2*y)-2*(y>2*z)

# Test the derived facet conditions against the original 24-vertex edges.
random.seed(20261014)
classes=Counter()
for _ in range(10000):
    u=tuple(random.randrange(-5000,5001) for i in range(3))
    x,y,z=sorted(map(abs,u),reverse=True)
    if not (x>y>z>0 and x!=2*y and x!=2*z and y!=2*z):continue
    if any(dot(u,v)==0 for v in V):continue
    n=sides_from_edges(u)
    assert n==sides_formula(u), (u,n,sides_formula(u))
    classes[n]+=1
assert set(classes)=={6,8,10}
X=(1,0,0);Y=(1,1,0);Z=(1,1,1)
P=(2,1,0);Q=(2,1,1);R=(4,2,1);H=(2,2,1)
regions={6:[(Q,H,Z),(Y,P,R),(Y,R,H)],
         8:[(Q,R,H),(X,P,R)],10:[(X,R,Q)]}
solid={i:sum(omega(*tri) for tri in tris) for i,tris in regions.items()}
fund=omega(X,Y,Z)
assert isclose(fund,pi/12,rel_tol=0,abs_tol=2e-15)
assert isclose(sum(solid.values()),fund,rel_tol=0,abs_tol=1e-14)
D=11+3*sqrt(14)+4*sqrt(6)+2*sqrt(21)
p10=24/pi*atan(1/D)
theta=acos(4/5)
p6=4+p10-18*theta/pi
p8=18*theta/pi-3-2*p10
p={6:p6,8:p8,10:p10}
assert all(0<x<1 for x in p.values()) and isclose(sum(p.values()),1,abs_tol=1e-14)
assert all(isclose(solid[k]/fund,p[k],rel_tol=0,abs_tol=3e-14) for k in p)
assert isclose(sum(k*p[k] for k in p),36*theta/pi,abs_tol=1e-13)
assert isclose(p10,solid[10]/fund,abs_tol=1e-14)

# Independent stochastic check: use direct edge-sign intersections, not the chamber formula.
c=Counter();rng=random.Random(104729)
N=200000
for _ in range(N):
    u=(rng.gauss(0,1),rng.gauss(0,1),rng.gauss(0,1))
    c[sides_from_edges(u)]+=1
assert set(c)=={6,8,10}
assert all(abs(c[k]/N-p[k])<0.005 for k in p)
print('VERIFY_OK vertices=24 edges=36 rational_tests='+str(sum(classes.values()))+
      ' spherical_chambers=6 monte_carlo='+str(N))
for k in sorted(p):print('p'+str(k)+'='+format(p[k],'.15f')+' sampled='+format(c[k]/N,'.6f'))
print('mean=',format(sum(k*p[k] for k in p),'.15f'))
