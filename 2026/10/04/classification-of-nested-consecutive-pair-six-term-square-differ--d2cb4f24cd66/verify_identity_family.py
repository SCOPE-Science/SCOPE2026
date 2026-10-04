#!/usr/bin/env python3
from fractions import Fraction

def coeff(a,c):
    u=2*a+1
    return (3,4*u-2*c,u*u-c*c)

def offsets(q):
    return [0,1,2-3*q,2*q-1,2*q,5*q-2]

def F(a,b):
    return abs(a*a-b*b)

# Family coefficient identity for a=0, t=q.
for q in range(-1000,1001):
    assert coeff(0,2-3*q)==coeff(2*q-1,5*q-2)
    # direct common factor identity on a deterministic x grid
    for x in (-37,-11,-1,0,1,8,29):
        lhs=F(F(x,x+1),x+2-3*q)
        rhs=F(F(x+2*q-1,x+2*q),x+5*q-2)
        target=3*abs((x+1-q)*(x+3*q-1))
        assert lhs==rhs==target

# All integral pair-collision parameters are exactly 0 and 1.
forms=[(0,0),(0,1),(-3,2),(2,-1),(2,0),(5,-2)] # alpha*q+beta
coll=set()
for i in range(len(forms)):
    for j in range(i+1,len(forms)):
        a,b=forms[i]; c,d=forms[j]
        if a==c:
            assert b!=d
            continue
        q=Fraction(d-b,a-c)
        if q.denominator==1:
            coll.add(int(q))
assert coll=={0,1}

# Shape equivalence q <-> 1-q up to translation.
def normalized_shape(q):
    v=offsets(q)
    m=min(v)
    return tuple(sorted(x-m for x in v))
for q in range(-1000,1001):
    assert normalized_shape(q)==normalized_shape(1-q)
    if q not in (0,1):
        assert len(set(offsets(q)))==6
        span=max(offsets(q))-min(offsets(q))
        expected=(8*q-4) if q>=2 else (4-8*q)
        assert span==expected and span>=12

assert normalized_shape(2)==(0,4,5,7,8,12)
assert normalized_shape(-1)==(0,4,5,7,8,12)
assert normalized_shape(3)==(0,7,8,12,13,20)
assert normalized_shape(-2)==(0,7,8,12,13,20)
print('VERIFY_OK')
