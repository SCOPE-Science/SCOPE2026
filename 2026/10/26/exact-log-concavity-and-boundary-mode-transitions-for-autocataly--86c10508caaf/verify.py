"""Exact checks for stationary-count shape of the two-species autocatalytic chain.
Run with Python 3 standard library: python verify.py
Checks are finite consistency tests, not substitutes for the general proof.
"""
from fractions import Fraction as F
from math import comb


def rising(a, k):
    x=F(1)
    for j in range(k):
        x*=a+j
    return x


def weight(n, k, a, b, r):
    return comb(n,k)**2*r**k*rising(a,k)*rising(b,n-k)


def f(i, u):
    return F(i*i,(i+1)**2)*(i+u)/(i-1+u)


def ratio(n,k,a,b,r):
    return r*F((n-k)**2,(k+1)**2)*(k+a)/(n-k-1+b)


def finite_lc_condition(n,a,b):
    if n<2:
        return True
    if n==2:
        return f(1,a)*f(1,b)<=1
    return f(1,a)*f(n-1,b)<=1 and f(n-1,a)*f(1,b)<=1


def strict_peak_indices(ws):
    return [k for k in range(len(ws)) if (k==0 or ws[k]>ws[k-1]) and (k==len(ws)-1 or ws[k]>ws[k+1])]

checks=0
A=[F(1,100),F(1,10),F(1,4),F(1,3),F(1,2),F(1),F(2),F(5)]
for n in range(2,25):
    for a in A:
        for b in A:
            for r in [F(1,3),F(1),F(7,3)]:
                ws=[weight(n,k,a,b,r) for k in range(n+1)]
                for k in range(n):
                    assert ws[k+1]/ws[k]==ratio(n,k,a,b,r)
                    checks+=1
                for k in range(1,n):
                    assert (ws[k]*ws[k]>=ws[k-1]*ws[k+1]) == (f(k,a)*f(n-k,b)<=1)
                    checks+=1
                measured=all(ws[k]*ws[k]>=ws[k-1]*ws[k+1] for k in range(1,n))
                assert measured==finite_lc_condition(n,a,b)
                checks+=1

for n in range(4,32):
    tau=F(1,n+1)
    for u,should_boundary in [(tau/2,True),(tau*F(3,2),False),(F(1,2),False),(F(2),False)]:
        ws=[weight(n,k,u,u,F(1)) for k in range(n+1)]
        peaks=strict_peak_indices(ws)
        assert ((0 in peaks) and (n in peaks))==should_boundary
        mid=n//2
        if n%2==0:
            assert ws[mid]>ws[mid-1] and ws[mid]>ws[mid+1]
        else:
            assert ws[mid]==ws[mid+1] and ws[mid]>ws[mid-1] and ws[mid+1]>ws[mid+2]
        checks+=1
    ws=[weight(n,k,tau,tau,F(1)) for k in range(n+1)]
    assert ws[0]==ws[1] and ws[-1]==ws[-2]
    checks+=1

# Numerically test the sharp root and its asymptotic without using it as a proof.
for n in [3,4,5,10,20,100,1000,10000]:
    lo,hi=0.0,1.0/3.0
    def p(u):
        return ((1+u)*(n-1)**2*(n-1+u)-4*u*n*n*(n-2+u))
    assert p(lo)>0 and p(hi)<0
    for _ in range(100):
        mid=(lo+hi)/2
        if p(mid)>0:lo=mid
        else:hi=mid
    root=(lo+hi)/2
    assert root>1/(n+1) if n>=4 else root>=1/(n+1)-1e-10
    assert root<1/3
    if n>=1000:
        assert abs(n*(1/3-root)-4/9)<0.01
    checks+=1

print('PASS: {} exact finite checks and root/asymptotic spot checks'.format(checks))
