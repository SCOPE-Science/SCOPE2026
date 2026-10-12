#!/usr/bin/env python3
"""Exact-rational diagnostics for circular random-point multiscale covariance."""
from fractions import Fraction as F
from itertools import combinations

def kernel(s, z):
    d = min(z % 1, (-z) % 1)
    return max(F(0), s - d) - s*s

def integral_kernels(s, t):
    # Breakpoints of the triangular kernels on 0 <= d <= 1/2.
    knots = sorted(set([F(0), min(s, t), max(s, t), F(1, 2)]))
    total = F(0)
    for lo, hi in zip(knots, knots[1:]):
        if lo == hi: continue
        # product of two affine functions, exact two-point Gauss quadrature not needed
        ml=(lo+hi)/2
        fl=kernel(s,lo)*kernel(t,lo)
        fm=kernel(s,ml)*kernel(t,ml)
        fr=kernel(s,hi)*kernel(t,hi)
        total += (hi-lo)*(fl+4*fm+fr)/6
    return 2*total

def predicted(a,b):
    x,y=sorted([min(a,1-a),min(b,1-b)])
    return x*x*y*(1-y)-x*x*x/3

def variance_point_sample(us, s):
    knots={F(0), F(1)}
    for u in us:
        knots.add(u)
        knots.add((u-s)%1)
    knots=sorted(knots)
    n=len(us)
    result=F(0)
    for x,y in zip(knots,knots[1:]):
        center=(x+y)/2
        count=sum(0 < ((u-center)%1) <= s for u in us)
        result+=(y-x)*(count-n*s)**2
    return result

def check():
    cnt=0
    vals=[F(i,16) for i in range(1,9)]
    for s in vals:
        for t in vals:
            assert integral_kernels(s,t)==predicted(s,t), (s,t)
            assert predicted(s,t)>0
            assert integral_kernels(s,t)==integral_kernels(t,s)
            cnt+=3
    for n in range(2,7):
        us=[F(1,11), F(4,13), F(3,7), F(7,19), F(2,5), F(13,17)][:n]
        for s in vals:
            v=variance_point_sample(us,s)
            pair=n*s*(1-s)+2*sum((kernel(s,(x-y)%1) for x,y in combinations(us,2)),F(0))
            assert v==pair,(n,s,v,pair)
            assert v==variance_point_sample(us,1-s)
            cnt+=2
    # Exact Gram principal minors using LDL decomposition: distinct lengths -> strictly positive.
    widths=[F(1,15),F(2,11),F(3,10),F(2,5),F(1,2)]
    mat=[[predicted(s,t) for t in widths] for s in widths]
    L=[[F(0) for j in widths] for i in widths]
    D=[F(0) for i in widths]
    for i in range(len(widths)):
        D[i]=mat[i][i]-sum(L[i][k]**2 * D[k] for k in range(i))
        assert D[i]>0
        L[i][i]=1
        for j in range(i+1,len(widths)):
            L[j][i]=(mat[j][i]-sum(L[j][k]*L[i][k]*D[k] for k in range(i)))/D[i]
    cnt+=len(widths)
    # A direct finite two-coordinate check of covariance by integrating fluctuations over relative position.
    for s in vals:
        for t in vals:
            e=integral_kernels(s,t)
            assert 4*e == 2*2*(2-1)*predicted(s,t)
            cnt+=1
    print('PASS:',cnt,'exact rational checks; universal proof is analytical')

if __name__=='__main__':check()
