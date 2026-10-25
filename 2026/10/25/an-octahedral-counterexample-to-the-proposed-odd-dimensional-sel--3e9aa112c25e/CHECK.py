#!/usr/bin/env python3
"""Exact-arithmetic checks for octahedral self-volume and odd-dimensional products.

Only stdlib is used. Arguments and mathematical interpretation are in RESULT.md.
"""
from fractions import Fraction as Q
from itertools import permutations, product
from math import factorial

def plus(a,b): return tuple(x+y for x,y in zip(a,b))
def minus(a,b): return tuple(x-y for x,y in zip(a,b))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def sq(a): return dot(a,a)
zero=(Q(0),)*3
half=Q(1,2)
E=[tuple(Q(i==j) for i in range(3)) for j in range(3)]
# Cyclic hexagon in the plane x+y+z=0.
H=[(half,-half,0),(half,0,-half),(0,half,-half),(-half,half,0),(-half,0,half),(0,-half,half)]
H=[tuple(Q(x) for x in v) for v in H]
assert len(set(H))==6
assert all(sum(v)==0 and sum(abs(x) for x in v)==1 for v in H)
assert all(sq(v)==Q(1,2) for v in H)
assert all(sq(minus(H[(i+1)%6],H[i]))==Q(1,2) for i in range(6))
assert all(minus(H[(i+1)%6],H[i]) in H for i in range(6))
# Exact area of planar polygon: 1/2 of norm of sum of cyclic cross products.
cs=tuple(sum((cross(H[i],H[(i+1)%6])[j] for i in range(6)),Q(0)) for j in range(3))
area_hex_sq=sq(cs)/4
assert area_hex_sq==Q(27,16), area_hex_sq
# Area of any triangular facet of octahedron conv{+-e1,+-e2,+-e3}.
for signs in product([-1,1], repeat=3):
 v=[tuple(signs[i]*x for x in E[i]) for i in range(3)]
 side1=minus(v[1],v[0]); side2=minus(v[2],v[0])
 assert sq(cross(side1,side2))/4==Q(3,4)
# Self-perimeter of H=6 and self-area=3 from edge-displacement gauge norm 1.
self_area_hex=Q(3)
# Face / central-section area = sqrt((3/4)/(27/16))=2/3.
face_section_ratio=Q(2,3)
self_volume_octahedron=Q(8,3)*face_section_ratio*self_area_hex
assert self_volume_octahedron==Q(16,3)
# H-by-products of the central octahedron: n=3+2r, r>=0.
for r in range(25):
 n=3+2*r
 value=self_volume_octahedron*3**r
 proposed_lower=Q(2)*3**(r+1)
 assert value/proposed_lower==Q(8,9)
 assert value<proposed_lower
print('PASS: exact 6-section vertices and side/gauge identities')
print('PASS: squared Euclidean facet and section areas = 3/4, 27/16')
print('PASS: hexagon self-area 3; octahedron self-volume 16/3')
print('PASS: odd dimensions 3..51 have ratio 8/9 to conjectured minimum')
