#!/usr/bin/env python3
"""Exact edge-intersection and numerical spherical-tail checks for tetrahedral central sections.

Only Python's standard library is required. Finite checks supplement, not replace, the proof.
"""
from fractions import Fraction
from itertools import combinations, product
from math import sqrt, pi
import random

VERTICES = ((1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1))
EDGES = tuple(combinations(range(4), 2))

def dot(v, w):
    return sum(a*b for a, b in zip(v, w))

def sqdist(v, w):
    return sum((a-b)**2 for a, b in zip(v, w))

def section_points(u):
    values = [dot(v, u) for v in VERTICES]
    found = []
    for i,j in EDGES:
        a,b = values[i],values[j]
        if a*b < 0:
            v,w = VERTICES[i],VERTICES[j]
            found.append(tuple((a*w[k]-b*v[k])/(a-b) for k in range(3)))
        elif a == 0:
            found.append(VERTICES[i])
        elif b == 0:
            found.append(VERTICES[j])
    return list(dict.fromkeys(found))

def diameter2(u):
    ps = section_points(u)
    return max(sqdist(p,q) for p,q in combinations(ps,2))

def midpoint_quadrilateral2(y,z):
    y,z = Fraction(y), Fraction(z)
    dy2 = 4 + 4*y*y*(1+z*z)/(1-z*z)**2
    dz2 = 4 + 4*z*z*(1+y*y)/(1-y*y)**2
    return dy2,dz2

# Check both exact squared-diagonal identities from rational edge intersections.
for y0,z0 in product(range(-4,5),repeat=2):
    y,z = Fraction(y0,12),Fraction(z0,12)
    if abs(y)+abs(z)>=1: continue
    u=(Fraction(1),y,z)
    P=section_points(u)
    assert len(P)==4
    ds=sorted(sqdist(p,q) for p,q in combinations(P,2))
    expected=sorted(midpoint_quadrilateral2(y,z))
    assert ds[-2:]==expected, (u,ds,expected)

# Check exact global inequalities on a deterministic rational lattice of normals.
for aa,bb,cc in product(range(-7,8,3),repeat=3):
    if (aa,bb,cc)==(0,0,0): continue
    D2=diameter2(tuple(Fraction(t) for t in (aa,bb,cc)))
    assert Fraction(4)<=D2<=Fraction(8), (aa,bb,cc,D2)
assert diameter2((1,0,0))==4
assert diameter2((0,1,-1))==8
assert diameter2((1,1,1))==Fraction(9,2)

# Independent finite verification of the two local asymptotic area ratios.
# The normal-coordinate spherical Jacobian is (1+x*x+y*y)^(-3/2).
def lower_ratio(epsilon, steps=300):
    b=1.25*sqrt(epsilon)
    h=2*b/steps
    area=0.0
    for i in range(steps):
        y=-b+(i+0.5)*h
        for j in range(steps):
            z=-b+(j+0.5)*h
            dy=2*sqrt(1+y*y*(1+z*z)/(1-z*z)**2)
            dz=2*sqrt(1+z*z*(1+y*y)/(1-y*y)**2)
            if max(dy,dz)<=2+epsilon:
                area+=(1+y*y+z*z)**(-1.5)
    return (6*area*h*h/(4*pi))/epsilon

def upper_chord(x,y):
    # Unnormalized normal u=u0+x*(1,0,0)+y*(0,1,1)/sqrt(2).
    # Signs identify the two section points approaching opposite edge endpoints.
    a=x+sqrt(2)*y; b=x-sqrt(2)*y
    c=sqrt(2)-x; d=-sqrt(2)-x
    ta=a/(a-d) if a>=0 else -a/(c-a)
    tb=b/(b-d) if b>=0 else -b/(c-b)
    A=VERTICES[0];B=VERTICES[1]
    VA=VERTICES[3] if a>=0 else VERTICES[2]
    VB=VERTICES[3] if b>=0 else VERTICES[2]
    PA=[A[k]+ta*(VA[k]-A[k]) for k in range(3)]
    PB=[B[k]+tb*(VB[k]-B[k]) for k in range(3)]
    return sqrt(sqdist(PA,PB))

def upper_ratio(epsilon,steps=300):
    bx=0.7*epsilon; by=0.5*epsilon
    hx=2*bx/steps; hy=2*by/steps
    area=0.0
    for i in range(steps):
        x=-bx+(i+0.5)*hx
        for j in range(steps):
            y=-by+(j+0.5)*hy
            if upper_chord(x,y)>=2*sqrt(2)-epsilon:
                area+=(1+x*x+y*y)**(-1.5)
    return (12*area*hx*hy/(4*pi))/(epsilon**2)

l=lower_ratio(0.001)
h=upper_ratio(0.002)
assert abs(l-6/pi)<0.035, (l,6/pi)
assert abs(h-3/(pi*sqrt(2)))<0.025, (h,3/(pi*sqrt(2)))

# Pairwise section chords confirm the candidate near upper maximizers, including
# both triangle and quadrilateral section regimes.
rng=random.Random(987765)
s2=sqrt(2)
for _ in range(2200):
    x=rng.uniform(-0.06,0.06);y=rng.uniform(-0.06,0.06)
    u=(x,(1+y)/s2,(-1+y)/s2)
    actual=sqrt(diameter2(u))
    assert abs(actual-upper_chord(x,y))<1e-10, (x,y,actual,upper_chord(x,y))

print('VERIFY_OK: exact quad-diagonal lattice, global bounds, upper long-pair cases, and two spherical tail constants')
print('lower ratio:',round(l,8),'target:',round(6/pi,8))
print('upper ratio:',round(h,8),'target:',round(3/(pi*sqrt(2)),8))
