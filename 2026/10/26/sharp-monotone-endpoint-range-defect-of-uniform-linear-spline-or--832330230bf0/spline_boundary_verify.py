#!/usr/bin/env python3
"""Exact rational checks for boundary range of uniform linear-spline L2 projectors.
No external data; n intervals means n+1 vertices. Finite checks supplement the proof.
"""
from fractions import Fraction as F

def exact_case(n):
    assert n >= 1
    r=F(1,2)
    for _ in range(n-1):
        r=1/(4-r)
    a=[6/(2-r)]
    a.append(a[0]*r)
    for j in range(1,n):
        a.append(4*a[j]-a[j-1])
    assert all(v>0 for v in a)
    assert all(a[j]>a[j+1] for j in range(n))
    assert a[-2]==2*a[-1]
    E=[F(0)]*(n+1)
    for j in range(n-1,-1,-1):
        E[j]=E[j+1]+(-1)**j*(a[j]-a[j+1])/2
    assert E[0]==1
    roots=[E[j+1]+(-1)**(j+1)*a[j+1]**2/(2*(a[j]+a[j+1])) for j in range(n)]
    defect=3/((2-r)*(1+r))-1
    assert roots[0]==-defect
    assert min(E+roots)==-defect
    assert max(E+roots)==1
    return r,defect,a,E,roots

if __name__=='__main__':
    for n in range(1,121):
        r,d,*_=exact_case(n)
        if n in [1,2,3,4,5,10,40,120]:
            print('n',n,'r',float(r),'delta',float(d),'exact',str(d) if n<=5 else '(large rational)')
    print('PASS: all candidate maxima/minima exactly checked, n=1..120')
