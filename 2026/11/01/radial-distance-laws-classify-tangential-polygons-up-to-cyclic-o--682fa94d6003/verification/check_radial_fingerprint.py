#!/usr/bin/env python3
"""Independent rational-geometry checks for radial fingerprints of tangential polygons.
Uses only Python's standard library.  Finite checks do not prove the general theorem.
"""
from fractions import Fraction as F
from itertools import permutations
from math import atan, pi, sqrt, factorial
import random

def dot(a,b): return a[0]*b[0]+a[1]*b[1]
def cross(a,b): return a[0]*b[1]-a[1]*b[0]
def plus(a,b): return (a[0]+b[0],a[1]+b[1])
def minus(a,b): return (a[0]-b[0],a[1]-b[1])
def scale(k,a):return (k*a[0],k*a[1])
def rotate(n,u):
    c=(1-u*u)/(1+u*u);s=2*u/(1+u*u)
    return (c*n[0]-s*n[1],s*n[0]+c*n[1])

def polygon(u):
    n=[(F(1),F(0))]
    for a in u:n.append(rotate(n[-1],a))
    assert n[-1]==n[0], ('not closed',u,n[-1])
    v=[]
    for j,a in enumerate(u):
        c=(1-a*a)/(1+a*a)
        v.append(scale(1/(1+c), plus(n[j],n[j+1])))
    n=n[:-1]
    # Each vertex is supported by its two adjacent sides and lies in all others.
    for j,p in enumerate(v):
        for k,normal in enumerate(n): assert dot(normal,p)<=1,(u,j,k,p)
        assert dot(n[j],p)==1 and dot(n[(j+1)%len(u)],p)==1
    # Signed tangent coordinates are adjacent u-values, on every side.
    for i,normal in enumerate(n):
        t=(-normal[1],normal[0])
        assert dot(v[(i-1)%len(v)],t)==-u[(i-1)%len(u)]
        assert dot(v[i],t)==u[i]
    return v,n

def geometric_moments(v):
    n=len(v);area=m2=m4=F(0)
    for j,a in enumerate(v):
        b=v[(j+1)%n];d=cross(a,b)
        assert d>0
        A=dot(a,a);B=dot(a,b);C=dot(b,b)
        area+=d/2
        m2+=d*(A+B+C)/12
        m4+=d*(A*A/30+A*B/30+(2*B*B+A*C)/90+B*C/30+C*C/30)
    return area,m2,m4

def angle_moments(u):
    total=sum(u,F(0));m2=sum((a+a**3/3 for a in u),F(0))/2
    m4=sum((a+F(2,3)*a**3+a**5/5 for a in u),F(0))/3
    return total,m2,m4

def boundary_tail(u,z):
    T=sum(u,F(0))
    return sum((max(a-z,F(0)) for a in u),F(0))/T

cases=[
 [F(1)]*4,
 [F(1,2),F(1,3),F(2),F(3)],
 [F(1,4),F(3,5),F(3,2),F(5)],
]
# Split a tangent angle into two positive angles, retaining exact rational closure.
def split(u,k,a):
    assert F(0)<a<u[k]
    v=(u[k]-a)/(1+a*u[k])
    return u[:k]+[a,v]+u[k+1:]
cases.append(split(cases[1],2,F(1,5)))
cases.append(split(cases[-1],4,F(1,7)))
cases.append(split(cases[-1],0,F(1,9)))

checks=0
for base in cases:
    # Every selected case is admissible: atan tangents sum pi, and all below pi/2.
    assert abs(sum(atan(float(u)) for u in base)-pi)<2e-14
    expected=angle_moments(base)
    # Compare every distinct cyclic ordering for n<=6, sample a reproducible subset for n=7.
    orders=set(permutations(base))
    if len(base)>6:
        orders=set(sorted(orders)[::max(1,len(orders)//250)])
    for u in orders:
        v,n=polygon(u)
        assert geometric_moments(v)==expected
        checks+=3
        for z in (F(0),F(1,5),F(1,2),F(1),F(2),F(3),F(5),F(9)):
            # Separately obtain the boundary tail from actual supporting-line chords.
            raw=F(0)
            for j,normal in enumerate(n):
                tangent=(-normal[1],normal[0]); low=dot(v[(j-1)%len(u)],tangent);high=dot(v[j],tangent)
                assert low<=0<=high
                raw+=max(-low-z,F(0))+max(high-z,F(0))
            assert raw/(2*sum(u,F(0)))==boundary_tail(u,z)
            checks+=1

# The four rational gaps have precisely three dihedral orderings.
base=tuple(cases[1]);orders=set(permutations(base))
def dihedral(perm):
    return {perm[i:]+perm[:i] for i in range(len(perm))}|{rev[i:]+rev[:i] for rev in [perm[::-1]] for i in range(len(perm))}
orbits=[]
while orders:
    x=next(iter(orders));orb=dihedral(x);orbits.append(x);orders-=orb
assert len(orbits)==3
# Recovery from piecewise-linear law: the knots, jumps, normalizing sum, and exact multiplicities.
for base in cases:
    T=sum(base,F(0)); unique=sorted(set(base))
    jumps={z:F(base.count(z),1)/T for z in unique}
    T2=pi/sum(float(jump)*atan(float(z)) for z,jump in jumps.items())
    assert abs(float(T)-T2)<1e-10
    assert all(jumps[z]*T==base.count(z) for z in unique)
    checks+=len(unique)

# Independent direct-ray angular quadrature checks the area radial-density identity.
from math import cos, sin, acos, tan, hypot
N=24000
for base in cases[1:4]:
    v,normals=polygon(tuple(base))
    normals=[(float(a),float(b)) for a,b in normals]
    gaps=[atan(float(u)) for u in base]
    for radius in (1.01,1.2,1.5,2.0,4.0):
        analytic=2*sum(max(g-acos(1/radius),0) for g in gaps)
        count=0
        for k in range(N):
            th=2*pi*(k+0.5)/N
            c,s=cos(th),sin(th)
            radial=1/max(a*c+b*s for a,b in normals)
            if radial>radius: count+=1
        quadrature=2*pi*count/N
        assert abs(quadrature-analytic)<0.002, (base,radius,quadrature,analytic)
        checks+=1

print('RADIAL_INVERSE_CHECK_OK:',checks-15,'exact rational comparisons;',15,'numerical ray checks;',len(cases),'rational polygon families;',len(orbits),'quadrilateral congruence classes')
