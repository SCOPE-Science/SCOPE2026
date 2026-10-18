#!/usr/bin/env python3
"""Exact rational checks for the triangle normal-multiplicity theorem.

Run: python3 verify_triangle_normals.py
Uses only Python's standard library. These finite checks supplement the proof.
"""
from fractions import Fraction as F
from itertools import product

def dot(a,b):
    return a[0]*b[0]+a[1]*b[1]
def sub(a,b):
    return (a[0]-b[0],a[1]-b[1])
def det(a,b):
    return a[0]*b[1]-a[1]*b[0]
def normal_count(vertices,p):
    n=0
    # A normal line through p based at a vertex exists iff its inward
    # direction lies in that vertex's inward normal cone.
    for i,v in enumerate(vertices):
        rays=[sub(vertices[j],v) for j in range(3) if j!=i]
        if all(dot(sub(p,v),z)>0 for z in rays):
            n+=1
    # One normal based at the relative interior of each side, if the foot
    # is strictly internal to the corresponding closed side.
    for i in range(3):
        a,b=vertices[i],vertices[(i+1)%3]
        z=sub(b,a)
        v=dot(sub(p,a),z)
        if 0<v<dot(z,z):
            n+=1
    return n

def interpolation(vs,i,j,k,l):
    # barycentric point of integer lattice with weights i,j,k, sum l
    return ((i*vs[0][0]+j*vs[1][0]+k*vs[2][0])/l,
            (i*vs[0][1]+j*vs[1][1]+k*vs[2][1])/l)

cases=[
 ((F(0),F(0)),(F(2),F(0)),(F(-1),F(3))),
 ((F(0),F(0)),(F(5),F(0)),(F(-2),F(1))),
 ((F(0),F(0)),(F(3),F(0)),(F(-3),F(2))),
 ((F(0),F(0)),(F(3),F(0)),(F(2),F(4))),
 ((F(0),F(0)),(F(3),F(0)),(F(0),F(4))),
 ((F(0),F(0)),(F(3),F(0)),(F(-1),F(5))),
]
checks=0
for vertices in cases:
    A,B,C=vertices
    u,v=sub(B,A),sub(C,A)
    U,V,g=dot(u,u),dot(v,v),dot(u,v)
    Delta=det(u,v)**2
    assert Delta==U*V-g*g and Delta>0
    if g<0:
        assert F(0)<Delta/((U-g)*(V-g))<F(1)
        # The signed line-parameters at which the two altitudes from A
        # intersect BC are exact rationals.
        l1=U/(U-g)
        l2=-g/(V-g)
        assert l1-l2==Delta/((U-g)*(V-g))
    for i in range(1,29):
        for j in range(1,29-i):
            k=29-i-j
            p=interpolation(vertices,i,j,k,F(29))
            # The exceptional normal bifurcation lines carry zero area.
            dots=[dot(sub(p,A),u),dot(sub(p,A),v)]
            if min(dots)==0:
                continue
            observed=normal_count(vertices,p)
            predicted=6 if g>=0 or (dots[0]>0 and dots[1]>0) else 4
            assert observed==predicted,(vertices,p,observed,predicted)
            checks+=1
# Verify exact fixed-angle quadratic gap for a substantial rational grid.
for t in [F(1,20),F(1,3),F(1,2),F(3,4),F(19,20)]:
    for r in [F(j,13) for j in range(1,100)]:
        prob=r*(1-t*t)/((r+t)*(1+r*t))
        upper=(1-t)/(1+t)
        gap=t*(1-t)*(r-1)**2/((1+t)*(r+t)*(1+r*t))
        assert upper-prob==gap and (prob==upper)==(r==1)
        checks+=1
print(f'TRIANGLE_NORMALS_EXACT_OK checks={checks}')
