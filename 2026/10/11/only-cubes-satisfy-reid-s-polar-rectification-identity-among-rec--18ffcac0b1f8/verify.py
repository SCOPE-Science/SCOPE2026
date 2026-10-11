#!/usr/bin/env python3
from fractions import Fraction
from itertools import product

# Enumerate cube edge midpoints exactly.
verts=list(product((-1,1), repeat=3))
mids=set()
for i,v in enumerate(verts):
    for w in verts[i+1:]:
        if sum(x!=y for x,y in zip(v,w))==1:
            mids.add(tuple(Fraction(x+y,2) for x,y in zip(v,w)))
assert len(mids)==12
for m in mids:
    assert max(abs(x) for x in m)==1
    assert sum(abs(x) for x in m)==2
    assert sorted(abs(x) for x in m)==[0,1,1]

# The positive triangular facet has the three expected vertices.
pos={m for m in mids if all(x>=0 for x in m)}
assert pos=={
    (Fraction(1),Fraction(1),Fraction(0)),
    (Fraction(1),Fraction(0),Fraction(1)),
    (Fraction(0),Fraction(1),Fraction(1)),
}

# Interior barycentric coordinates for q1,q2,q3 on that facet.
qs=[(Fraction(4,5),Fraction(3,5),Fraction(3,5)),
    (Fraction(3,5),Fraction(4,5),Fraction(3,5)),
    (Fraction(3,5),Fraction(3,5),Fraction(4,5))]
for u,v,w in qs:
    alpha=(u+v-w)/2
    beta=(u+w-v)/2
    gamma=(v+w-u)/2
    assert alpha>0 and beta>0 and gamma>0
    assert alpha+beta+gamma==1
    assert u+v+w==2
    assert max(u,v,w)<1

# Explicit noncubic box (a,b,c)=(1,2,3).
a,b,c=map(Fraction,(1,2,3))
L1=(4*a*a+3*b*b+3*c*c)/5
L2=(3*a*a+4*b*b+3*c*c)/5
L3=(3*a*a+3*b*b+4*c*c)/5
assert (L1,L2,L3)==(Fraction(43,5),Fraction(46,5),Fraction(51,5))
assert len({L1,L2,L3})==3

# Cubic case: lambda = 2 s^2 makes lambda P^o have l1 bound 2s.
for s in map(Fraction,(1,2,5,11)):
    lam=2*s*s
    assert lam/s==2*s

print('VERIFY_OK')
print('cube_edge_midpoints = exact')
print('facet_points = exact')
print('noncubic_box_obstruction = exact')
print('cubic_scale = exact')
