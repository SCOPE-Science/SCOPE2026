#!/usr/bin/env python3
"""Exact algebra and independent geodesic-arc crossing checks for a flat torus."""
from fractions import Fraction as Q
import random
import math

def det(a,b):
    return a[0]*b[1]-a[1]*b[0]

def add(a,b):
    return (a[0]+b[0], a[1]+b[1])

def sector_integral(B,q):
    z=[(1,0),(1,B),(q-1,B),(-1,B-q),(-1,0)]
    d=[det(z[i],z[i+1]) for i in range(4)]
    w=[add(z[i],z[i+1]) for i in range(4)]
    return Q(4,27)*sum(v**3 for v in d)+Q(2,9)*sum(d[i]*d[j]*det(w[i],w[j]) for i in range(4) for j in range(i+1,4))

# The expression difference has bidegree <= (3,6), so 4 x 7 grid exact zeros
# prove the polynomial identity (not just a finite sample of the theorem).
for B in [Q(1),Q(4,3),Q(2),Q(3)]:
    for j in range(7):
        q=Q(j,6)
        lhs=54*sector_integral(B,q)
        rhs=5*(4*B-q*q)**3-3*q*q*(2*B-q)**2*(2-q)**2
        assert lhs==rhs,(B,q,lhs,rhs)
print('EXACT_BIDEGREE_INTERPOLATION_IDENTITY_PASSED 28')

def profile(B,q):
    return Q(5,54)-q*q*(2*B-q)**2*(2-q)**2/(18*(4*B-q*q)**3)
assert profile(Q(1),Q(0))==Q(5,54)
assert profile(Q(1),Q(1))==Q(22,243)
assert Q(5,54)-Q(22,243)==Q(1,486)
assert profile(Q(3),Q(0))==Q(5,54)
print('EXACT_SHARP_ENDPOINTS_PASSED')

# Unlike the sector integral, this computation directly solves the
# intersection equations for two lifted shortest geodesic arcs modulo a lattice.
# Sampling the Voronoi cell from its triangular sectors avoids relying on the
# symbolic integral in the independent geometry experiment.
rng=random.Random(54819011)
def sample_H(B,q):
    zz=[(1.,0.),(1.,B),(q-1.,B),(-1.,B-q),(-1.,0.)]
    ds=[det(zz[i],zz[i+1]) for i in range(4)]
    r=rng.random()*sum(ds)
    acc=0.
    ix=3
    for i,dd in enumerate(ds):
        acc+=dd
        if r<=acc:
            ix=i
            break
    t=rng.random()
    radius=math.sqrt(rng.random())
    sign=-1 if rng.getrandbits(1) else 1
    x=(1-t)*zz[ix][0]+t*zz[ix+1][0]
    y=(1-t)*zz[ix][1]+t*zz[ix+1][1]
    return (sign*radius*x,sign*radius*y)

for B,q in [(1.,0.),(1.,1.),(1.4,.5)]:
    L1=(2.,q); L2=(q,2.*B)
    area=4*B-q*q
    N=85000; count=0; duplicate=0; determinant_average=0.
    for _ in range(N):
        u=sample_H(B,q); v=sample_H(B,q)
        determinant=det(u,v)
        determinant_average+=abs(determinant)/area
        alpha=rng.random(); beta=rng.random()
        w=(alpha*L1[0]+beta*L2[0],alpha*L1[1]+beta*L2[1])
        hits=0
        if abs(determinant)>1e-14:
            for i in range(-2,3):
                for j in range(-2,3):
                    shifted=(w[0]+i*L1[0]+j*L2[0],w[1]+i*L1[1]+j*L2[1])
                    s=det(shifted,v)/determinant
                    t=-det(u,shifted)/determinant
                    if 1e-10<s<1-1e-10 and 1e-10<t<1-1e-10:
                        hits+=1
        count+=hits>0
        duplicate+=hits>1
    p=profile(B,q)
    assert duplicate==0,(B,q,duplicate)
    assert abs(count/N-p)<(.006),(B,q,count/N,p)
    assert abs(determinant_average/N-p)<(.005),(B,q,determinant_average/N,p)
    print('GEOMETRIC_CASE_PASSED',B,q,'probability',round(count/N,5),'exact',round(p,5))
print('INDEPENDENT_PERIODIC_SEGMENT_CROSSINGS_PASSED 3')
print('NO_DUPLICATE_INTERSECTIONS_PASSED')
print('ALL_CHECKS_PASSED')
