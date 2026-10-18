#!/usr/bin/env python3
"""Exact cuboctahedron edge-sweep certificate and spherical integral checks.
Run: python3 verify_crofton.py (Python 3 standard library only).
"""
from itertools import product
from math import sqrt, pi, atan, acos, isclose

# Each vertex is a signed pair of unit coordinates, with the third zero.
V = sorted(set(tuple((a if j == (i+1) % 3 else
                      b if j == (i+2) % 3 else 0)
                     for j in range(3))
               for i in range(3) for a, b in product((-1,1),repeat=2)))
assert len(V)==12
E = [(i,j) for i in range(12) for j in range(i)
     if sum((V[i][k]-V[j][k])**2 for k in range(3)) == 2]
assert len(E)==24
RAYS=((1,0,0),(1,1,0),(1,1,1))
def dot(u,v):return sum(a*b for a,b in zip(u,v))
def up_count(v):
    nbr=[w for w in V if sum((v[k]-w[k])**2 for k in range(3))==2]
    assert len(nbr)==4
    ups=0
    for w in nbr:
        diff=tuple(w[k]-v[k] for k in range(3))
        vals=[dot(diff,r) for r in RAYS]
        # Each neighbor comparison has a fixed strict sign in the
        # interior of the fundamental cone (all nonzero positive weights).
        assert any(t != 0 for t in vals)
        assert all(t>=0 for t in vals) or all(t<=0 for t in vals)
        if all(t>=0 for t in vals):ups+=1
    return ups
POSITIVE={
    (0,1,-1):2, (0,1,1):2,
    (1,-1,0):2, (1,0,-1):1,
    (1,0,1):1, (1,1,0):0
}
for v,count in POSITIVE.items():
    assert up_count(v)==count
# On any strict fundamental orientation x>y>z>0 the sign of each
# vertex height is fixed. Count edges that straddle the central plane.
u=(101,73,29)
assert [v for v in V if dot(u,v)>0] == sorted(POSITIVE)
Nzero=sum(dot(u,V[i])*dot(u,V[j])<0 for i,j in E)
assert Nzero==8
# Every positive vertex has valence four. As t increases past it,
# the crossing-edge count changes by 2*(number of higher neighbors)-4.
# The only nonzero changes are -2 at x-z, -2 at x+z,
# and -4 at x+y. Hence the section counts are 8/6/4 and
# their positive-offset lengths are x-z, 2z, y-z, respectively.
D={v:2*up_count(v)-4 for v in POSITIVE}
assert {v:d for v,d in D.items() if d} == {
    (1,0,-1):-2,(1,0,1):-2,(1,1,0):-4}

# The spherical fundamental triangle has vertices (1,0,0),
# (1,1,0)/sqrt(2), (1,1,1)/sqrt(3). Its vector area is
# 1/2 sum_{cyclic edges a->b} angle(a,b)*(a cross b)/|a cross b|.
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def norm(a):return sqrt(dot(a,a))
p=((1.,0.,0.),(1/sqrt(2),1/sqrt(2),0.),(1/sqrt(3),1/sqrt(3),1/sqrt(3)))
I=[0.,0.,0.]
for a,b in zip(p,p[1:]+p[:1]):
    cr=cross(a,b)
    angle=acos(max(-1.,min(1.,dot(a,b))))
    for k in range(3):I[k]+=angle*cr[k]/(2*norm(cr))
gamma=atan(sqrt(2)); beta=pi/2-gamma
expected=(beta/(2*sqrt(2)),(gamma-beta)/(2*sqrt(2)),pi/8-gamma/(2*sqrt(2)))
assert all(isclose(I[k],expected[k],rel_tol=0,abs_tol=1e-14) for k in range(3))
Z=I[0]+I[1]
p4=(I[1]-I[2])/Z
p6=2*I[2]/Z
p8=(I[0]-I[2])/Z
exact=(3-pi*(2+sqrt(2))/(4*gamma),pi*sqrt(2)/(2*gamma)-2,pi*(2-sqrt(2))/(4*gamma))
assert all(isclose(x,y,rel_tol=0,abs_tol=1e-13) for x,y in zip((p4,p6,p8),exact))
assert isclose(p4+p6+p8,1,rel_tol=0,abs_tol=1e-14)
assert isclose(4*p4+6*p6+8*p8,2*pi/gamma,rel_tol=0,abs_tol=1e-13)
print('VERIFY_OK vertices=12 edges=24 exact_neighbor_signs=24 positive_events=6')
print('p4=%.15f p6=%.15f p8=%.15f expected_sides=%.15f'%(p4,p6,p8,4*p4+6*p6+8*p8))
