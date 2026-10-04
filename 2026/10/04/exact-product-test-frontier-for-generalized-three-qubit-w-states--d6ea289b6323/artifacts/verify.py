#!/usr/bin/env python3
import math, random
from fractions import Fraction

def frontier(w):
    if w < 4/9 - 1e-13 or w > 1 + 1e-13:
        raise ValueError(w)
    if w <= 0.5 + 1e-13:
        T=(9*w-4+3*math.sqrt(max(0.0,w*(9*w-4))))/2
        return (8+T*T)/12, T
    return 1-w+w*w, None

def overlap_w(p,q,r):
    m=max(p,q,r)
    if m >= 0.5-1e-13:
        return m
    s=p*p+q*q+r*r
    return 4*p*q*r/(1-2*s)

def acceptance(p,q,r):
    return (1+p*p+q*q+r*r)/2

# Exact endpoint arithmetic.
assert Fraction(2,3) == Fraction(1,2)*(1+Fraction(1,3))
df = 1 - 2*Fraction(4,9) + 3*Fraction(4,9)**2
assert df == Fraction(19,27)
assert df - Fraction(2,3) == Fraction(1,27)

# Equality family and deficit factorization on a deterministic grid.
for k in range(101):
    t=k/100
    p=(1-t)/3
    q=r=(2+t)/6
    if t < 1:
        w=4*p*q*r/(1-2*(p*p+q*q+r*r))
    else:
        w=0.5
    expected=(t+2)**2/(9*(t+1))
    assert abs(w-expected) < 2e-12
    F=(8+t*t)/12
    assert abs(acceptance(p,q,r)-F) < 2e-12
    D=(1-t)*(t+2)*(5*t*t+5*t+2)/(108*(1+t)**2)
    dimfree=1-2*w+3*w*w
    assert abs(dimfree-F-D) < 3e-12
    assert D >= -1e-14

# High-overlap equality family.
for k in range(51):
    w=0.5+k/100
    if w>1: break
    p,q,r=w,1-w,0.0
    assert abs(overlap_w(p,q,r)-w) < 1e-12
    assert abs(acceptance(p,q,r)-(1-w+w*w)) < 1e-12

# Sample arbitrary W triples and check the global family frontier.
rng=random.Random(20261002)
for _ in range(5000):
    a,b,c=rng.random(),rng.random(),rng.random()
    z=a+b+c
    p,q,r=a/z,b/z,c/z
    w=overlap_w(p,q,r)
    F,_=frontier(w)
    P=acceptance(p,q,r)
    if P > F + 3e-11:
        raise AssertionError((p,q,r,w,P,F))

# Monotonicity of low-overlap equality parameter.
prev=4/9
for k in range(1,1001):
    t=k/1000
    w=(t+2)**2/(9*(t+1))
    assert w >= prev-1e-15
    prev=w
assert abs(prev-0.5) < 1e-15
print('VERIFY_OK')
