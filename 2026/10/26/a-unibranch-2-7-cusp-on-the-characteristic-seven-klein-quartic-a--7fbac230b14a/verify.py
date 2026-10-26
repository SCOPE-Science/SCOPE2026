#!/usr/bin/env python3
"""Exact arithmetic for the characteristic-7 Klein quartic (prime and quadratic fields)."""
from itertools import product

def add(a,b,q):
    if q==7:return (a+b)%7
    return (a%7+b%7)%7+7*((a//7+b//7)%7)
def mul(a,b,q):
    if q==7:return a*b%7
    A,B=a%7,a//7;C,D=b%7,b//7
    return (A*C+3*B*D)%7+7*((A*D+B*C)%7)
def pow_(a,n,q):
    r=1
    while n:
        if n&1:r=mul(r,a,q)
        a=mul(a,a,q);n>>=1
    return r
def sum_(q,*args):
    v=0
    for a in args:v=add(v,a,q)
    return v
def proj(q):
    for k in range(3):
        for tail in product(range(q),repeat=2-k):
            yield (0,)*k+(1,)+tail

def F(v,q):
    x,y,z=v
    return sum_(q,mul(pow_(x,3,q),y,q),mul(pow_(y,3,q),z,q),mul(pow_(z,3,q),x,q))

def grads(v,q):
    x,y,z=v
    return (
        sum_(q,mul(3,mul(mul(x,x,q),y,q),q),pow_(z,3,q)),
        sum_(q,pow_(x,3,q),mul(3,mul(mul(y,y,q),z,q),q)),
        sum_(q,pow_(y,3,q),mul(3,mul(mul(z,z,q),x,q),q))
    )
for q in [7,49]:
    pts=[p for p in proj(q) if F(p,q)==0]
    sing=[p for p in pts if not any(grads(p,q))]
    print('FIELD',q,'POINTS',len(pts),'EXPECTED',q+1,'SING',sing)
    assert len(pts)==q+1 and sing==[(1,2,4)],(q,len(pts),sing)
print('VERIFY_OK')
