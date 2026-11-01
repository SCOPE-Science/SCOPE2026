#!/usr/bin/env python3
"""Numerical cross-checks for a two-frequency sine fixed-point census.
Not a proof of the large-amplitude limit or of exhaustive finite root counts.
Requires Python 3 standard library only.
"""
import math

FREQUENCIES = (1.0, math.sqrt(2.0))

def coefficient_grid(n):
    a,b = FREQUENCIES
    c = [math.cos(2*math.pi*j/n) for j in range(n)]
    return sum(abs(a*u+b*v) for u in c for v in c)/(n*n)

def sign_change_count(A, phase, step=0.025):
    a,b = FREQUENCIES
    def h(x):
        return A*(math.sin(a*(x-phase))+math.sin(b*(x-phase)))-x
    left=-2*A
    right=2*A
    old=h(left)
    count=0
    x=left+0.37*step
    while x<right:
        new=h(x)
        count += (old*new<0)
        old=new
        x+=step
    count+=(old*h(right)<0)
    return count

def check():
    c1=coefficient_grid(256)
    c2=coefficient_grid(512)
    assert abs(c1-c2)<0.0002, (c1,c2)
    a,b=FREQUENCIES
    assert 2*max(a,b)/math.pi<c2<2*(a+b)/math.pi
    results=[]
    for phi in (0.0, 0.37, 2.0):
        for A in (160.0,320.0,640.0,1280.0):
            n=sign_change_count(A,phi)
            diff=abs(n/A-c2)
            results.append((A,phi,n,n/A,diff))
            assert diff<0.085,(A,phi,n,n/A,c2)
    for row in results:
        print('A=%g phase=%g observed_sign_changes=%d count/A=%.7f error=%.7f'%row)
    print('quadrature C_256=%.12f C_512=%.12f'% (c1,c2))
    print('PASS: 12 finite sign-change trials and 2 torus-grid quadratures')

if __name__=='__main__': check()
