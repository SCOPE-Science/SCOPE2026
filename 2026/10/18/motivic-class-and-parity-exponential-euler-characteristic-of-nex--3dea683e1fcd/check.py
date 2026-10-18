#!/usr/bin/env python3
"""Independent integer-polynomial and finite-field checks for the stated hypersurface class."""
from math import comb
from itertools import product

def add(a,b):
    c=[0]*max(len(a),len(b))
    for i,v in enumerate(a):c[i]+=v
    for i,v in enumerate(b):c[i]+=v
    return trim(c)
def trim(a):
    while len(a)>1 and a[-1]==0:a.pop()
    return a
def scale(a,t):return trim([t*x for x in a])
def mult(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return trim(c)
def power(a,n):
    p=[1]
    for _ in range(n):p=mult(p,a)
    return p
def mono(k):return [0]*k+[1]
def H(s):
    a=add(power([-1,1],s-1),[(-1)**s])
    assert a[0]==0
    return trim(a[1:])
def Q(s):
    if s==1:return [1]
    a=[1]*(s-1)
    if s%2==0:a[(s-2)//2]+=1
    return a
def first_expression(n):
    a=[0]
    for s in range(1,n-2):a=add(a,scale(power([-1,1],s-1),comb(n,s)))
    a=add(a,scale(H(n-1),n))
    for s in range(1,n+1):a=add(a,scale(Q(s),(-1)**(n-s)*comb(n,s)))
    return a
def closed_expression(n):
    a=[0]
    for s in range(1,n-2):a=add(a,scale(power([-1,1],s-1),comb(n,s)))
    a=add(a,scale(H(n-1),n))
    a=add(a,H(n))
    for j in range(1,n//2+1):a=add(a,scale(mono(j-1),(-1)**n*comb(n,2*j)))
    return add(a,[(-1)**(n-1)*n])

def proj_count(n,q):
    count=0
    for first in range(n):
        for tail in product(range(q),repeat=n-first-1):
            x=[0]*first+[1]+list(tail)
            e=[0]*(n-1)
            e[0]=1
            for a in x:
                for d in range(n-2,0,-1):
                    e[d]=(e[d]+a*e[d-1])%q
            count+=(e[n-2]==0)
    return count

def value(a,t):return sum(v*t**i for i,v in enumerate(a))
for n in range(5,16):
    p=first_expression(n)
    assert p==closed_expression(n),(n,p,closed_expression(n))
    expected=(2**(n-1)-n if n%2==0 else -2**(n-1)+3*n)
    assert value(p,1)==expected
assert first_expression(5)==[1,-4,1,1]
assert first_expression(6)==[1,16,7,1,1]
assert first_expression(7)==[1,-34,-27,15,1,1]
assert proj_count(5,7)==value(first_expression(5),7)==365
# Over F_7 the six-variable quadratic has the opposite splitting sign.
assert proj_count(6,7)==value(first_expression(6),7)-2*7**2==3102
print('VERIFY_OK: 11 exact polynomial identities, 11 Euler specializations, F7 projective tests')
