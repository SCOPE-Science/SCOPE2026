#!/usr/bin/env python3
"""Exact integer cross-checks for a reciprocal quadratic divisibility theorem."""
from math import gcd, isqrt

def least_prime_factor(n):
    assert n >= 4
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            return d
    return n

def Q(k,x):
    return x*x-k*x+1

def test_seed(k,d,a,b,H,steps=32):
    assert k>=1 and d>=1 and 2<=a<b and H>=2
    assert Q(k,a)==-d*b
    assert b==H*a+d+k
    x,y=-d,a
    assert x*x+y*y-k*(x+y)+1-H*x*y==0
    z=a
    prev=-d
    cur=a
    nxt=b
    for j in range(steps):
        assert nxt==H*cur-prev+k
        assert Q(k,cur)==prev*nxt
        assert nxt>cur>=2
        assert nxt and Q(k,cur)%nxt==0
        next2=H*nxt-cur+k
        assert next2>nxt
        assert Q(k,nxt)==cur*next2
        assert Q(k,nxt)%cur==0
        assert gcd(cur,nxt)==1
        prev,cur,nxt=cur,nxt,next2
    return steps

cases=0
for k in range(10,4001):
    a=least_prime_factor(k+2)
    if a==k+2: continue
    c=(k+2)//a
    b=a*(k-a)-1
    H=k-a-c
    assert H>=2
    assert (H==2)==(k==10)
    cases+=test_seed(k,1,a,b,H,30)

progress=0
for t in range(301):
    k=41+21*t
    progress+=test_seed(k,3,7,79+49*t,5+4*t,24)

parabolic=[2,15]
for n in range(1,501):
    parabolic.append(2*parabolic[-1]-parabolic[-2]+10)
assert all(v==5*n*n+8*n+2 for n,v in enumerate(parabolic))
print(f'VERIFY_OK composite_steps={cases} prime_progression_steps={progress} seeds={cases//30}+301')
