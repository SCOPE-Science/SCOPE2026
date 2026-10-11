#!/usr/bin/env python3
"""Exact rational and independent low-dimensional checks for signed chain volumes."""
from fractions import Fraction as F
from math import comb, factorial
from itertools import product

def simple_integral(a,b):
    # integral of s^a(2-s)^b on [1,2], for a,b >= 0
    assert a>=0 and b>=0
    return sum((F(comb(a,j)*2**(a-j)*(-1)**j,b+j+1) for j in range(a+1)), F(0))

def range_formula(p,q):
    n=p+q
    return F(n+1)+ (p*(p-1)*simple_integral(p-2,q+1) if p>=2 else 0) + (q*(q-1)*simple_integral(q-2,p+1) if q>=2 else 0)

def conditional_formula(p,q):
    # condition on signs and the positive and negative extrema of the first group
    base=2*p*sum((F(comb(q,i)*2**(q-i)*(-1)**i,p+i) for i in range(q+1)),F(0))
    for k in range(1,p):
        integral=F(0)
        for i in range(q+1):
            for j in range(q+1-i):
                mult=comb(q,i)*comb(q-i,j)
                integral+=F(mult*2**(q-i-j)*(-1)**(i+j),(k+i)*(p-k+j))
        base+=comb(p,k)*k*(p-k)*integral
    return base

for p in range(1,7):
    for q in range(1,7):
        a=range_formula(p,q)
        b=conditional_formula(p,q)
        assert a==b, (p,q,a,b)
        assert a==range_formula(q,p)
        assert (a*factorial(p+q)).denominator==1
print('PASS: 36 parameter pairs, two distinct exact rational integrations, symmetry and normalized-volume integrality')

for n in range(4,13):
    vals=[range_formula(p,n-p) for p in range(1,n)]
    assert all(vals[p-1]>vals[p] for p in range(1,n//2)) if n%2==0 else all(vals[p-1]>vals[p] for p in range(1,(n-1)//2))
print('PASS: strict imbalance monotonicity on total dimensions 4 to 12')

# Independent direct H-to-V geometry check for small dimensions.
try:
    import numpy as np
    from scipy.spatial import HalfspaceIntersection, ConvexHull
    for p,q in [(1,1),(1,2),(2,2),(1,3),(2,3),(3,2),(1,4)]:
        d=p+q
        normals=[]
        for i in range(d):
            a=[0.0]*d;a[i]=1.0
            normals.extend([a,[-v for v in a]])
        for i in range(p):
            for j in range(p,d):
                a=[0.0]*d;a[i]=a[j]=1.0
                normals.extend([a,[-v for v in a]])
        hs=np.array([a+[-1.0] for a in normals])
        vertices=HalfspaceIntersection(hs, np.zeros(d)).intersections
        got=ConvexHull(vertices).volume
        want=float(range_formula(p,q))
        assert abs(got-want)<2e-8*(1+want),(p,q,got,want)
    print('PASS: seven independent H-representation to convex hull volume reconstructions, dimensions 2 through 5')
except ImportError:
    print('NOTE: scipy unavailable, convex-hull corroboration skipped')
print('Examples:',[(p,q,str(range_formula(p,q))) for p,q in [(1,1),(1,2),(2,2),(2,3),(3,3)]])
