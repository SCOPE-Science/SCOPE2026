#!/usr/bin/env python3
"""Standalone independent finite checks of exact random chord-crossing spectrum."""
import math
import itertools
import random
from fractions import Fraction

PI=math.pi
R=random.Random(137061)

def midpoint_half(a,b):
    delta=(b-a)%(2*PI)
    if delta<=PI:
        return ((a+delta/2)%(2*PI),delta/2)
    return ((b+(2*PI-delta)/2)%(2*PI),(2*PI-delta)/2)

def geom_cross(a,b,c,d):
    aa,bb=sorted((a,b))
    return ((aa<c<bb)!=(aa<d<bb))

def coord_cross(a,b,c,d):
    th,h=midpoint_half(a,b)
    ph,k=midpoint_half(c,d)
    dist=abs((th-ph+PI)%(2*PI)-PI)
    return abs(h-k)<dist<h+k

for _ in range(30000):
    a,b,c,d=[R.uniform(0,2*PI) for j in range(4)]
    assert geom_cross(a,b,c,d)==coord_cross(a,b,c,d)
print('INDEPENDENT_ENDPOINT_CROSSING_AND_MIDPOINT_CRITERION_PASSED')

def Fourier(m,h,k):
    lo,hi=min(h,k),max(h,k)
    if not m:
        return 2*lo/PI
    return 2*math.sin(abs(m)*lo)*math.cos(abs(m)*hi)/(PI*abs(m))

# Independent angular integration of the indicator, with exact interval endpoints.
for m,h,k in [(0,.23,.48),(1,.27,.39),(2,.45,.09),(3,.29,.41),(4,.17,.33),(5,.4,.41)]:
    a,b=abs(h-k),h+k
    integ=(b-a)/PI if not m else (math.sin(m*b)-math.sin(m*a))/(PI*m)
    assert abs(integ-Fourier(m,h,k))<1.e-13,(m,h,k,integ,Fourier(m,h,k))
print('INDEPENDENT_FOURIER_INTERVAL_INTEGRALS_PASSED')

# Integrated Fourier-mode ODE eigenfunction residual. Numerical midpoint quadrature.
N=2400
L=PI/2
ys=[(j+.5)*L/N for j in range(N)]
for m,k in [(0,1),(0,3),(1,2),(1,4),(2,1),(2,5),(3,2),(3,4),(4,1),(4,5)]:
    assert (m+k)%2==1 and k*k!=m*m
    eigen=4/(PI*PI*(k*k-m*m))
    for h in [.16,.39, .71, 1.23]:
        value=sum(Fourier(m,h,y)*math.sin(k*y) for y in ys)/N
        rhs=eigen*math.sin(k*h)
        assert abs(value-rhs)<3.e-7,(m,k,h,value,rhs)
print('FOURIER_BLOCK_DIRICHLET_NEUMANN_SPECTRAL_RESIDUALS_PASSED')

# Exhaustive independent combinatorial chord-diagram cycle probability.
def perfect_matchings(points):
    if not points:
        yield ()
        return
    first=points[0]
    for idx in range(1,len(points)):
        pair=(first,points[idx]); leftover=points[1:idx]+points[idx+1:]
        for rest in perfect_matchings(leftover):
            yield (pair,)+rest

def positions_cross(p,q):
    a,b=sorted(p)
    c,d=q
    return (a<c<b)!=(a<d<b)

expected={3:Fraction(1,15),4:Fraction(1,35),5:Fraction(31,2835)}
for n,p in expected.items():
    count=0
    total=0
    for match in perfect_matchings(tuple(range(2*n))):
        adjacency=[[False]*n for _ in range(n)]
        for i in range(n):
            for j in range(i+1,n):
                adjacency[i][j]=adjacency[j][i]=positions_cross(match[i],match[j])
        for perm in itertools.permutations(range(n)):
            total+=1
            if all(adjacency[perm[j]][perm[(j+1)%n]] for j in range(n)):
                count+=1
    assert Fraction(count,total)==p, (n,count,total,p)
    print('EXHAUSTIVE_CYCLE_CHORD_DIAGRAM_PASSED',n,count,total,str(p))

# Finite factorization multiplicity diagnostic. Odd d≤101.
for d in range(1,102,2):
    pos=neg=0
    for m in range(-101,102):
        for k in range(1,102):
            if (m+k)%2!=1:continue
            delta=k*k-m*m
            if delta==d:pos+=1
            if delta==-d:neg+=1
    tau=sum(d%u==0 for u in range(1,d+1))
    assert pos==tau and neg==tau-(math.isqrt(d)**2==d),(d,pos,neg,tau)
print('ODD_DIVISOR_SPECTRAL_MULTIPLICITIES_PASSED')

# Deterministic convergent partial sums check exact universal rational cycle values.
exact={3:Fraction(1,15),4:Fraction(1,35),5:Fraction(31,2835),6:Fraction(139,31185)}
for r,p in exact.items():
    s=0.
    for d in range(1,10001,2):
        tau=sum(d%u==0 for u in range(1,math.isqrt(d)+1))
        tau=2*tau-(math.isqrt(d)**2==d)
        pos=tau
        neg=tau-(math.isqrt(d)**2==d)
        s+=(pos+(-1)**r*neg)/d**r
    value=s*(4/PI**2)**r
    assert abs(value-float(p))<2.e-7,(r,value,float(p))
print('FINITE_SPECTRAL_SUM_DIAGNOSTICS_PASSED')
print('ALL_CHECKS_PASSED')
