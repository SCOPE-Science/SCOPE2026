#!/usr/bin/env python3
"""Independent finite arithmetic and sampling checks for cross-polytope brightness endpoint laws."""
from fractions import Fraction as Q
from itertools import product, combinations
from math import acos, pi, sqrt, isclose
from random import Random

def det(a):
    n=len(a)
    if n==1: return a[0][0]
    if n==2: return a[0][0]*a[1][1]-a[0][1]*a[1][0]
    return sum((-1)**j*a[0][j]*det([row[:j]+row[j+1:] for row in a[1:]]) for j in range(n))

def extreme_rays(dim, extra):
    inequalities=[[Q(int(i==j))-Q(int(i==j+1)) for i in range(dim)] for j in range(dim-1)]
    inequalities += [[Q(int(i==dim-1)) for i in range(dim)]]
    inequalities += [[Q(x) for x in row] for row in extra]
    rays=set()
    for ids in combinations(range(len(inequalities)),dim-1):
        mat=[inequalities[i] for i in ids]
        z=[(-1)**j*det([row[:j]+row[j+1:] for row in mat]) for j in range(dim)]
        if z==[0]*dim: continue
        for mul in (1,-1):
            v=[mul*q for q in z]
            if v[0]>0 and all(sum(a*b for a,b in zip(q,v))>=0 for q in inequalities):
                rays.add(tuple(t/v[0] for t in v)); break
    return rays

def expected_brightness(v):
    dim=len(v)
    return sum(abs(sum(s*a for s,a in zip(signs,v))) for signs in product((-1,1), repeat=dim))/Q(2**dim)

def closed_brightness(v):
    a=sorted((abs(q) for q in v),reverse=True)
    if len(v)==3:
        return max(a[0],sum(a)/2)
    return max(a[0],sum(a[:3])/2,(3*a[0]+sum(a[1:]))/4)

for dim in (4,):
    tested=0
    for v in product(range(-3,4),repeat=dim):
        if not any(v): continue
        x=tuple(Q(k) for k in v)
        assert expected_brightness(x)==closed_brightness(x), (dim,v)
        tested+=1
    print('SIGN_AVERAGE_IDENTITY_OK',dim,tested)

reg3={
'A':([[1,-1,-1]],{(Q(1),Q(0),Q(0)),(Q(1),Q(1),Q(0)),(Q(1),Q(1,2),Q(1,2))}),
'C':([[-1,1,1]],{(Q(1),Q(1),Q(0)),(Q(1),Q(1,2),Q(1,2)),(Q(1),Q(1),Q(1))})}
reg4={
'A':([[1,-1,-1,-1]],{(Q(1),Q(0),Q(0),Q(0)),(Q(1),Q(1,3),Q(1,3),Q(1,3)),(Q(1),Q(1,2),Q(1,2),Q(0)),(Q(1),Q(1),Q(0),Q(0))}),
'B':([[-1,1,1,1],[1,-1,-1,1]],{(Q(1),Q(1,3),Q(1,3),Q(1,3)),(Q(1),Q(1,2),Q(1,2),Q(0)),(Q(1),Q(1),Q(0),Q(0)),(Q(1),Q(1),Q(1),Q(1))}),
'C':([[-1,1,1,-1]],{(Q(1),Q(1,2),Q(1,2),Q(0)),(Q(1),Q(1),Q(0),Q(0)),(Q(1),Q(1),Q(1),Q(0)),(Q(1),Q(1),Q(1),Q(1))})}
for dim, regimes in ((4,reg4),):
    for name,(ineq,expected) in regimes.items():
        rays=extreme_rays(dim,ineq)
        assert rays==expected, (dim,name,rays^expected)
        assert all(closed_brightness(v)**2 >= sum(x*x for x in v)/2 for v in rays)
        eq={v for v in rays if closed_brightness(v)**2==sum(x*x for x in v)/2}
        assert eq=={(Q(1),Q(1))+tuple(Q(0) for i in range(dim-2))}
    print('COMPLETE_CONE_EXTREME_RAYS_OK',dim, {name:len(a[1]) for name,a in regimes.items()})

# Full signed-average norm in the transverse coordinates: an independent check of
# the local tangent polytope at the two-coordinate extremizers.
for dim in (4,):
    count=0
    for v in product(range(-5,6),repeat=dim-1):
        y,*z=map(Q,v)
        N=sum(abs(y+sum(a*s for a,s in zip(z,eps))) for eps in product((-1,1),repeat=dim-2))/Q(2**(dim-2))
        M=max(abs(y),abs(z[0])) if dim==3 else max(abs(y),abs(z[0]),abs(z[1]),(abs(y)+abs(z[0])+abs(z[1]))/2)
        assert N==M,(dim,v,N,M)
        count+=1
    print('TANGENT_NORM_OK',dim,count)

# C_4 tangent body is [-2,2]^3 intersect {|x|+|y|+|z|<=4}.
# In each octant, exactly a simplex of volume (2^3)/6 is deleted.
cubocta_volume=Q(4**3) - 8*Q(2**3,6)
assert cubocta_volume==Q(160,3)
print('EXACT_CUBOCTAHEDRAL_TANGENT_VOLUME_OK', 'volume=160/3', 'rescaled=80sqrt(2)/3')

# Independent direct numerical integration via sphere Monte Carlo, with robust
# tolerance sized to be > 8 estimated standard deviations at these sample sizes.
rng=Random(775928)
for dim in (4,):
    n=150000
    cutoff=0.90
    seen=0
    for _ in range(n):
        g=[rng.gauss(0,1) for i in range(dim)]
        norm=sqrt(sum(x*x for x in g))
        u=[x/norm for x in g]
        val=sum(abs(sum(a*b for a,b in zip(signs,u))) for signs in product((-1,1),repeat=dim))/(2**dim)
        if val>=cutoff: seen+=1
    t=1-cutoff
    exact=3*t if dim==3 else 8/pi*(acos(cutoff)-cutoff*sqrt(1-cutoff**2))
    empirical=seen/n
    assert abs(empirical-exact)<0.014,(dim,empirical,exact)
    print('INDEPENDENT_HAAR_UPPER_TAIL_OK',dim,round(empirical,5),round(exact,5))
print('ALL_CHECKS_OK')
