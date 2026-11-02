#!/usr/bin/env python3
"""Exact finite corroboration of a dyadic support theorem for a quadratic arithmetic recurrence."""
from math import factorial
from collections import Counter

LIMIT=16384
s=[0]*(LIMIT+1)
s[1]=1
# use independent divisor recursion, derived from floor differences
for n in range(2,LIMIT+1):
    total=0
    d=2
    while d*d<=n:
        if n%d==0:
            q=n//d
            total+=s[d]*(2*q-1)
            if d!=q:
                total+=s[q]*(2*d-1)
        d+=1
    s[n]=-1-total

# Independently run original floor-sum recursion on the first 512 values
f=[0]*513
f[1]=1
for n in range(2,513):
    f[n]=1-n-sum(f[d]*(n//d)**2 for d in range(2,n))
    assert f[n]==s[n],(n,f[n],s[n])

def factor(n):
    c=Counter()
    d=2
    while d*d<=n:
        while n%d==0:
            n//=d
            c[d]+=1
        d+=1
    if n>1:c[n]+=1
    return c

tested_boundary=tested_vanish=odd_parts=0
for m in range(1,LIMIT+1,2):
    p=factor(m);k=sum(p.values())
    boundary=2**(k+2)*m
    if boundary>LIMIT:continue
    odd_parts+=1
    goal=2**(k+1)*factorial(k)
    for q,e in p.items():
        goal*= (q-1)**e
        goal//= factorial(e)
    # factorial denominator division issue? all individual factorial divides running value from factorial(k)
    assert s[boundary]==goal,('boundary',m,boundary,s[boundary],goal)
    tested_boundary+=1
    a=k+3
    while (2**a)*m<=LIMIT:
        assert s[(2**a)*m]==0,('vanishing',m,a,s[(2**a)*m])
        tested_vanish+=1
        a+=1
print('VERIFY_OK limit=',LIMIT,'floor_crosscheck=512','odd_parts_with_boundary=',odd_parts,'exact_boundaries=',tested_boundary,'zero_tail_checks=',tested_vanish)
for m in [1,3,9,15,27,45,105]:
 p=factor(m);k=sum(p.values()); b=m*2**(k+2)
 if b<=LIMIT:
  print('EXAMPLE',m,'omega=',k,'boundary=',b,'value=',s[b], 'next=',s[2*b] if 2*b<=LIMIT else None)
