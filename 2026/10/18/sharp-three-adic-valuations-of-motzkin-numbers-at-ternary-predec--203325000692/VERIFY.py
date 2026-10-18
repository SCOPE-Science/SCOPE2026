#!/usr/bin/env python3
"""Exact arithmetic checks for a Motzkin three-adic valuation theorem.

These finite tests supplement, rather than replace, the proof for all exponents.
"""
from math import comb

def v3(x):
    assert x != 0
    d=0
    while x % 3 == 0:
        d += 1
        x //= 3
    return d

def central_carries(n):
    carry=0
    count=0
    while n or carry:
        digit=n%3
        total=2*digit+carry
        carry=total//3
        count += (carry != 0)
        n//=3
    return count

def catalan_valuation(n):
    return central_carries(n)-v3(n+1)

# Independently compare Catalan Kummer valuations with exact binomial values.
for m in range(1,1000):
    c=comb(2*m,m)//(m+1)
    assert catalan_valuation(m)==v3(c),m

last=3**8-3
m0,m1=1,1
values=[1,1]
for n in range(2,last+1):
    top=(2*n+1)*m1+3*(n-1)*m0
    assert top%(n+2)==0,n
    m2=top//(n+2)
    values.append(m2)
    m0,m1=m1,m2

for r in range(1,9):
    q=3**r
    n=q-3
    N=q-1
    m=n+1
    c=comb(2*m,m)//(m+1)
    assert catalan_valuation(m)==r-1
    actual=values[n]
    assert v3(actual)==r-1,(r,n,v3(actual))
    assert (actual-c*pow(2,-2*N,3**r))%(3**r)==0,(r,n)
    for j in range(1,N+1):
        if j>=r: continue
        if N-j==0:continue
        cj=catalan_valuation(N-j-1)
        assert j+cj>=r,(r,j,cj)
    print('r',r,'index',n,'valuation',v3(actual),'congruence_mod',3**r)
print('VERIFY_OK')
