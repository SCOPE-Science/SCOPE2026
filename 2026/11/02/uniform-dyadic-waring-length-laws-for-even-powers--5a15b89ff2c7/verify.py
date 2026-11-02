#!/usr/bin/env python3
"""Exact enumeration of additive kth-power images modulo powers of two."""
from math import gcd

def expected(k,t,n):
    b=1<<( (k & -k).bit_length()-1+2)
    def rec(n):
        if n<=b.bit_length()-1: return min(t+1,1<<n)
        if n<=k: return t*(1<<(n-b.bit_length()+1))+1
        return t*(1<<(n-b.bit_length()+1))+rec(n-k)
    return rec(n)

def verify(k,n):
    m=1<<n; b=1<<((k&-k).bit_length()+1)
    powers=set(pow(x,k,m) for x in range(m))
    state=1 # 0 representable
    mask=(1<<m)-1
    tests=0
    for t in range(1,b+1):
        nex=0
        for v in powers:
            if v==0: nex|=state
            else: nex|=((state<<v)|(state>>(m-v)))&mask
        state=nex
        e=expected(k,t,n) if t<b else m
        got=state.bit_count()
        if got!=e: raise AssertionError((k,n,t,b,got,e))
        tests+=1
    return tests

if __name__=='__main__':
    total=0
    for k in (4,6,8,10,12,14):
        for n in range(1,13):
            tests=verify(k,n);total+=tests
        print('passed',k,'base',1<<((k&-k).bit_length()+1),'n<=12')
    print('VERIFY_OK total='+str(total))
    comparisons=0
    for n in range(1,31):
        for t in range(3,16):
            r=n%4
            if r==1: value=(t*(1<<n)-2*t+30)//15
            elif r==2: value=(t*(1<<n)-4*t+60)//15
            elif r==3: value=(t*(1<<n)+7*t+15)//15 if t<=7 else (t*(1<<n)-8*t+120)//15
            else: value=(t*(1<<n)-t+15)//15
            assert value==expected(4,t,n), (n,t,value,expected(4,t,n))
            comparisons+=1
    print('PUBLISHED_FORMULA_COMPATIBILITY_OK comparisons='+str(comparisons))
