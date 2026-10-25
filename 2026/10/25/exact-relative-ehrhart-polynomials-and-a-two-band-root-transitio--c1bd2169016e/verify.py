#!/usr/bin/env python3
"""Exact checks for Reeve tetrahedron relative Ehrhart counting; no dependencies."""
from math import comb


def direct(m, L, t):
    # Independently check BOTH segment endpoints against ALL four original facets.
    total = 0
    for z in range(m * t + 1):
        for u in range(t + 1):
            for v in range(t + 1):
                def inside(h):
                    return h >= 0 and m*u >= h and m*v >= h and m*(t-u-v)+h >= 0
                if inside(z) and inside(z+L):
                    total += 1
    return total


def fiber(m, L, t):
    total = 0
    for z in range(m*t+1):
        lo=(z+L+m-1)//m
        hi=(m*t+z)//m
        slack=hi-2*lo
        if slack >= 0:
            total += (slack+1)*(slack+2)//2
    return total


def choose3positive(a):
    return comb(a,3) if a >= 3 else 0


def closed(m, L, t):
    q,s=divmod(L,m)
    x=t-2*q
    if s == 0:
        return choose3positive(x+3)+(m-1)*choose3positive(x+1)
    return (m-s+1)*choose3positive(x+1)+(s-1)*choose3positive(x-1)


checks=0
for m in range(2,21):
    for L in range(1,3*m+1):
        for t in range(11):
            assert fiber(m,L,t)==closed(m,L,t), (m,L,t)
            checks+=1

endpoint_checks=0
for m in range(2,10):
    for L in range(1,min(2*m,13)+1):
        for t in range(7):
            assert direct(m,L,t)==closed(m,L,t), (m,L,t)
            endpoint_checks+=1

# Exact integer polynomial identity for all parameter pairs on representative grids.
for m in range(2,121):
    for L in range(1,3*m+1):
        q,s=divmod(L,m)
        r=1 if s==0 else s-1
        discr=m*m-36*m*r+36*r*r
        for x in (-13,-7,-3,-1,0,1,3,8,25):
            if s==0:
                lhs=(x+1)*(m*x*x+(6-m)*x+6)
                rhs=(x+3)*(x+2)*(x+1)+(m-1)*(x+1)*x*(x-1)
                assert m+(6-m)*(-1)+6==2*m
                b=6-m;c=6
            else:
                lhs=(x-1)*(m*x*x+(m-6*r)*x+6*r)
                rhs=(m-s+1)*(x+1)*x*(x-1)+(s-1)*(x-1)*(x-2)*(x-3)
                assert m+(m-6*r)+6*r==2*m
                b=m-6*r;c=6*r
            assert lhs==rhs and b*b-4*m*c==discr
        assert discr!=0
        min_t=2*((L+m-1)//m)
        assert closed(m,L,min_t)>0
        assert closed(m,L,min_t-1)==0
assert all((m*m-36*m+36<0)==(2<=m<=34) for m in range(2,200))
assert 70*70-72*70+144==4
assert all(m*m-72*m+144<=0 for m in range(3,70))
print(f'VERIFY_OK fiber_counts={checks} direct_endpoint_counts={endpoint_checks} exact_polynomial_roots_checked=True')
