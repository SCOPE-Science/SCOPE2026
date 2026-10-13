#!/usr/bin/env python3
"""Exact finite spectral checks and numerical phase witnesses for the vertex-potential wheel theorem.
Only checks finite instances. The mathematical proof establishes the universal statements.
"""
from fractions import Fraction as F
from math import cos, sin, pi, sqrt, e, isqrt

def matvec(a,v):
    return [sum(x*y for x,y in zip(row,v)) for row in a]

def hamiltonian(q):
    a=[[F(0) for _ in range(5)] for _ in range(5)]
    for i in range(4):
        j=(i+1)%4
        a[i][j]=a[j][i]=F(1)
        a[i][4]=a[4][i]=F(1)
    a[4][4]=q
    return a

v0=[F(1,2)]*4+[F(0)]
v2=[F(1,2),F(-1,2),F(1,2),F(-1,2),F(0)]
v1=[F(1),F(0),F(-1),F(0),F(0)]
h=[F(0)]*4+[F(1)]
count=0
for numer in range(-90,91):
  for denom in (1,2,3,4,5,6,7):
    q=F(numer,denom)
    a=hamiltonian(q)
    assert matvec(a,v0)==[2*v0[i]+2*h[i] for i in range(5)]
    assert matvec(a,h)==[2*v0[i]+q*h[i] for i in range(5)]
    assert matvec(a,v2)==[-2*y for y in v2]
    assert matvec(a,v1)==[F(0)]*5
    # Characteristic polynomial of [[2,2],[2,q]]: lambda^2-(q+2)lambda+(2q-4).
    trace=q+2
    det=2*q-4
    discr=trace*trace-4*det
    assert discr==(q-2)*(q-2)+16
    assert discr>0
    count+=1

def rational_square(x):
    assert x>=0
    a,b=isqrt(x.numerator),isqrt(x.denominator)
    return a*a==x.numerator and b*b==x.denominator

# Exact boundary cases for the claimed rational predicate.
for q,want in [(F(-2),True),(F(6),True),(F(-6),True),(F(10),True),
               (F(0),False),(F(4),False),(F(2),False),(F(22,3),False),
               (F(14,3),True)]:
    discr=(q-2)*(q-2)+16
    pred=((q+2)/4).denominator%2==1 and not rational_square(discr)
    assert pred==want,(q,pred,want)

# Parity obstruction: for odd s and odd u,v, (u-s)(v-s) is a multiple of four,
# while -s*s is odd.
for s in range(1,80,2):
    for u in range(-41,42,2):
        for v in range(-41,42,2):
            assert (u-s)*(v-s)!=-s*s

# Explicit Pell approximants at q=-2: both active 2x2 eigenvalues are +-2sqrt(2).
prev=0.0
pell=[]
for p,s in [(1,1),(7,5),(41,29),(239,169),(1393,985)]:
    assert p*p-2*s*s==-1 and p%2==s%2==1
    theta=pi*s*sqrt(2)
    amp=(cos(theta)-3)/4+1j*sin(theta)/(4*sqrt(2))
    fidelity=abs(amp)**2
    assert fidelity>prev-1.e-12
    prev=fidelity
    pell.append((s,fidelity))
assert pell[-1][1]>0.999999

# For a transcendental on-site potential q=e, irrational-frequency approximation
# is sampled, but the existence theorem follows from Kronecker, not this search.
q=e
disc=sqrt((q-2)*(q-2)+16)
lambdap=(q+2+disc)/2
lambdam=(q+2-disc)/2
best=(float('inf'),None)
for s in range(1,150000,2):
    errs=[abs((s*z/4 - 0.5 + 0.5)%1 - 0.5) for z in (lambdap,lambdam)]
    err=max(errs)
    if err<best[0]: best=(err,s)
assert best[0]<0.005,best
print('VERIFY_OK exact_block_tests=%d modular_parity_tested=true rational_boundary_cases=9 Pell_final=%.12f transcendental_phase_error=%.7f at_odd_s=%d'%
      (count,pell[-1][1],best[0],best[1]))
