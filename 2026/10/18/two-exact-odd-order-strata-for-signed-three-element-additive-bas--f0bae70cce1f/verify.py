#!/usr/bin/env python3
"""Exact finite checks of the signed three-element basis theorem; standard library only."""
from math import gcd

def represented(h,a,x,y):
    out=set()
    for j in range(h+1):
        base=h*a+j*y
        for i in range(h-j+1):
            out.add(base+i*x)
    return out

def cover(h,a,x,y):
    s=represented(h,a,x,y)
    n=0
    while n in s:
        n+=1
    return n-1

def check_construction():
    cases=0
    for m in range(3,61):
        for t in range(1,(m-1)//2+1):
            if gcd(2*t+1,m+1)>1:
                continue
            h=2*m+1
            obtained=cover(h,-t,2*t+1,m+1)
            expected=m*m+4*m+1-t
            assert obtained==expected,(m,t,obtained,expected)
            cases+=1
    return cases

def check_high_range():
    cases=0
    for k in range(10):
        h=12*k+11
        m=(h-1)//2
        N=m*m+4*m+2
        for d in ([2,3] if (k+1)%5==0 else [2]):
            # Exhaust all high-cover candidates compatible with two sharp
            # endpoint inequalities, without using the final modular argument.
            for y in range(1,h+2):
                if (y-m-2)**2>d:
                    continue
                for x in range(1,y):
                    if gcd(x,y)!=1:
                        continue
                    U=(y-1)*(1-x)
                    L=N-d-h*y+(y-1)*(y-x-1)
                    for z in range(L,U+1):
                        if z<0 and z%h==0:
                            a=z//h
                            s=represented(h,a,x,y)
                            assert not all(n in s for n in range(N-d+1)),(h,d,a,x,y)
                            cases+=1
        t=3 if (k+1)%5==0 else 2
        if (k+1)%5==0 and (k+1)%7==0:
            continue
        expected=N-t-1
        actual=cover(h,-t,2*t+1,m+1)
        assert actual==expected,(h,t,actual,expected)
    return cases

if __name__=='__main__':
    x=check_construction()
    y=check_high_range()
    print('VERIFY_OK construction_cases=%d upper_candidates=%d'%(x,y))
