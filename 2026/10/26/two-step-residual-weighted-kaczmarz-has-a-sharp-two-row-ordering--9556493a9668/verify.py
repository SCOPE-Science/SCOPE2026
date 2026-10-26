#!/usr/bin/env python3
"""Exact-rational checks for two-step residual-weighted Kaczmarz."""
from fractions import Fraction as Q

rows = [tuple(Q(x, 3) for x in row)
        for row in ((2,-1,2),(2,-2,-1),(1,2,2))]
e = tuple(map(Q, (0,4,-1)))
def dot(x,y):
    return sum(a*b for a,b in zip(x,y))
def project(v, row):
    t=dot(v,row)
    return tuple(a-t*b for a,b in zip(v,row))
def sq(v):
    return dot(v,v)
def probs(v,p):
    if p==0:
        return (Q(1,3),)*3
    w=[abs(dot(row,v))**p for row in rows]
    z=sum(w)
    if z==0:
        return (Q(0),)*3
    return tuple(t/z for t in w)
def two_step(p):
    ans=Q(0)
    for i,row in enumerate(rows):
        z=project(e,row)
        for j,row2 in enumerate(rows):
            ans+=probs(e,p)[i]*probs(z,p)[j]*sq(project(z,row2))
    return ans
# Row-norm and full-rank premises.
assert all(sq(row)==1 for row in rows)
from itertools import permutations
# Leibniz determinant with inversion parity.
det=Q(0)
for p in permutations(range(3)):
    inversions=sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
    det+=(-1)**inversions*rows[0][p[0]]*rows[1][p[1]]*rows[2][p[2]]
assert det==Q(13,27)
assert tuple(dot(row,e) for row in rows)==(Q(-2),Q(-7,3),Q(2))
assert tuple(dot(rows[1],rows[j]) for j in range(3))==(Q(4,9),Q(1),Q(-4,9))
first_row2=project(e,rows[1])
assert tuple(dot(r,first_row2) for r in rows)==(Q(-26,27),Q(0),Q(26,27))
assert sq(project(first_row2,rows[0]))==sq(project(first_row2,rows[2]))==Q(7748,729)
E0=two_step(0)
E40=two_step(40)
assert E0==Q(65572,6561)
assert 7**40>200*6**40
p2=Q(7**40,7**40+2*6**40)
assert p2>Q(100,101)
assert E40>=p2*Q(7748,729)>Q(100,101)*Q(7748,729)>Q(21,2)>Q(10)>E0
# Weighted correction is better at the very first step.
first0=sum(sq(project(e,row)) for row in rows)/3
first40=sum(probs(e,40)[i]*sq(project(e,row)) for i,row in enumerate(rows))
assert first40<first0
# A separate exact two-row algebra identity for arbitrary scalar residuals
# can be checked by a grid of rational choices; the general proof is in RESULT.md.
for a in map(Q,(-3,-2,-1,0,1,2,3)):
    for b in map(Q,(-3,-2,-1,0,1,2,3)):
        for c in (Q(-1),Q(-2,3),Q(-1,4),Q(0),Q(1,4),Q(2,3),Q(1)):
            f12=-a*a-(b-c*a)**2
            f21=-b*b-(a-c*b)**2
            assert f12-f21==c*c*(b*b-a*a)
print('PASS: exact determinant, row geometry, two-step distribution, gap and 343 symbolic-identity samples')
print('uniform E2 =',E0, float(E0))
print('p=40 E2   =',E40, float(E40))
print('certified lower =',Q(100,101)*Q(7748,729))
