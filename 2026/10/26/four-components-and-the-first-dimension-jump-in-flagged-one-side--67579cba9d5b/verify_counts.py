#!/usr/bin/env python3
"""Finite-field count check for the 4x4 strict upper-triangular zero-product pair equations.
No external package required.  Uses a polynomial basis of GF(4) over GF(2).
"""
from itertools import product

def mult(a,b,q):
    if q != 4:
        return a*b%q
    acc=0
    for i in range(2):
        for j in range(2):
            if ((a>>i)&1) and ((b>>j)&1): acc ^= 1<<(i+j)
    if acc&4: acc ^= 7  # t^2 = t+1 in GF(4)
    return acc

def plus(a,b,q): return a^b if q == 4 else (a+b)%q

def check(q):
    assert q in (2,3,4,5)
    count=0
    branch = [0]*4
    for x,y,z,p,h,r in product(range(q),repeat=6):
        if mult(x,p,q) or mult(z,r,q) or plus(mult(x,h,q),mult(y,r,q),q):
            continue
        count+=1
        if x==0 and r==0:branch[0]+=1
        if p==h==r==0:branch[1]+=1
        if x==y==z==0:branch[2]+=1
        if z==p==0:branch[3]+=1
    wanted=q**4+3*q**3-4*q**2+q
    assert count==wanted, (q,count,wanted)
    print('q',q,'active_solutions',count,'whole_pairs',count*q**6,'components_hit',branch)
for q in (2,3,4,5):check(q)
print('VERIFY_OK_FLAGGED_ZERO_PRODUCT_N4')
