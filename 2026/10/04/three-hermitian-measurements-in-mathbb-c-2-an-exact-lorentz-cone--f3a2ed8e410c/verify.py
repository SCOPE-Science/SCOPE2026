#!/usr/bin/env python3
from fractions import Fraction as F


def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

def norm2(a):
    return dot(a,a)

def rational_sphere(u,v):
    u=F(u); v=F(v)
    d=1+u*u+v*v
    return (2*u/d, 2*v/d, (1-u*u-v*v)/d)

def second_time(t,tau,w,n):
    q=tau*tau-norm2(w)
    B=t*(tau-dot(n,w))
    if q == 0:
        return q,B,None
    s=-2*B/q
    tp=t+s*tau
    rp=tuple(t*n[i]+s*w[i] for i in range(3))
    assert tp*tp == norm2(rp)
    expected=-t*norm2(tuple(tau*n[i]-w[i] for i in range(3)))/q
    assert tp == expected
    return q,B,tp

# Canonical Hermitian-kernel Pauli coordinates:
# I -> (2,0), diag(1,0) -> (1,(0,0,1)), sigma_z -> (0,(0,0,2)).
regimes=[
    ('timelike',F(2),(F(0),F(0),F(0)),1),
    ('null',F(1),(F(0),F(0),F(1)),0),
    ('spacelike',F(0),(F(0),F(0),F(2)),-1),
]
for name,tau,w,sgn in regimes:
    q=tau*tau-norm2(w)
    assert (q>0)-(q<0) == sgn

pairs=[(-2,-2),(-2,-1),(-2,0),(-2,1),(-2,2),
       (-1,-2),(-1,-1),(-1,0),(-1,1),(-1,2),
       (0,-2),(0,-1),(0,0),(0,1),(0,2),
       (1,-2),(1,-1),(1,0),(1,1),(1,2),
       (2,-2),(2,-1),(2,0),(2,1),(2,2)]
for u,v in pairs:
    n=rational_sphere(u,v)
    assert norm2(n)==1
    q,B,tp=second_time(F(1),F(2),(F(0),F(0),F(0)),n)
    assert q>0 and tp<0
    q,B,tp=second_time(F(1),F(0),(F(0),F(0),F(2)),n)
    assert q<0
    if B!=0:
        assert tp>0
    q,B,tp=second_time(F(1),F(1),(F(0),F(0),F(1)),n)
    assert q==0
    # In the null case, ambiguity can occur only at the north-pole direction.
    if n!=(F(0),F(0),F(1)):
        assert B!=0

# At the null north pole the whole positive ray is invisible along the kernel.
n=(F(0),F(0),F(1))
q,B,tp=second_time(F(1),F(1),(F(0),F(0),F(1)),n)
assert q==0 and B==0 and tp is None

print('VERIFY_OK regimes=3 rational_directions=25')
