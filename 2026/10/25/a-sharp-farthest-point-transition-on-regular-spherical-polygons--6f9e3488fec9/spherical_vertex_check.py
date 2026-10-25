#!/usr/bin/env python3
"""Independent numerical sampling checks for a spherical regular-polygon farthest-point formula."""
from math import acos,cos,sin,pi,sqrt,atan
import numpy as np

def point(r,phi):
    return np.array([sin(r)*cos(phi),sin(r)*sin(phi),cos(r)])

def analytic(n,r):
    if n%2==0:
        return 2*r
    m=cos(r)**2-sin(r)**2*cos(pi/n)
    c=sqrt(1-sin(r)**2*sin(pi/n)**2)
    return acos(max(-1.,min(1.,m/c if m<0 else m)))

def brute(n,r,samples=1001):
    vs=[point(r,2*pi*i/n) for i in range(n)]
    v0=vs[0]
    mins=(1.0,None)
    for i in range(n):
        a,b=vs[i],vs[(i+1)%n]
        for lam in np.linspace(0,1,samples):
            z=lam*a+(1-lam)*b
            z/=np.linalg.norm(z)
            dot=float(v0@z)
            if dot<mins[0]:mins=(dot,(i,lam))
    return acos(max(-1,min(1,mins[0]))),mins[1]

if __name__=='__main__':
    for n in (3,4,5,6,7,8,9,11):
        rs=(0.18,0.7,1.05,1.35)
        for r in rs:
            exact=analytic(n,r)
            trial,arg=brute(n,r,1001)
            assert abs(exact-trial)<2e-6,(n,r,exact,trial,arg)
            print(f'n={n:2d} rho={r:4.2f} theory={exact:.12f} edge_sample={trial:.12f} arg={arg}')
