#!/usr/bin/env python3
"""Independent finite checks for circular geometric graph edge-count cumulants.
No external packages required; Python 3.10+.
"""
from fractions import Fraction as F
from math import comb, sin, pi, sqrt

def triangle(r):
    return 3*r*r + (3*r-1)**2 if r>=F(1,3) else 3*r*r

def delta(r):
    p=2*r
    return triangle(r)-p**3

def predicted_m3(n,r):
    p=2*r
    return comb(n,2)*p*(1-p)*(1-2*p)+6*comb(n,3)*delta(r)

def discrete_grid(n, M, k):
    """Exact three-vertex graph count by conditioning first point to be zero."""
    assert n==3
    counts=[0,0,0,0]
    def edge(i,j):
        d=(i-j)%M; return min(d,M-d)<=k
    for a in range(M):
        for b in range(M):
            e=int(edge(0,a))+int(edge(0,b))+int(edge(a,b))
            counts[e]+=1
    probs=[F(c,M*M) for c in counts]
    mean=sum(i*x for i,x in enumerate(probs))
    central3=sum((i-mean)**3*x for i,x in enumerate(probs))
    p=F(2*k+1,M)
    t=F(sum(1 for a in range(M) for b in range(M)
            if edge(0,a) and edge(0,b) and edge(a,b)),M*M)
    assert mean==3*p
    assert sum(probs)==1
    assert central3==3*p*(1-p)*(1-2*p)+6*(t-p**3)
    return p,t,central3

def main():
    checks=0
    # Exact independent discrete-circle enumeration (not the continuous theorem).
    for M in [12,19,28,36,48,72]:
        for k in range(1,(M-1)//2):
            p,t,m3=discrete_grid(3,M,k)
            assert F(0)<=t<=p<=1
            checks+=1
    # Finite-grid limits to continuum for non-boundary radius.
    for r in [F(1,10),F(1,4),F(1,3),F(2,5),F(9,20)]:
        M=600
        k=(r.numerator*M)//r.denominator - 1
        p,t,_=discrete_grid(3,M,k)
        assert abs(p-2*r)<=F(2,M)
        assert abs(t-triangle(r))<=F(8,M)
        checks+=1
    # Exact symbolic-like polynomial formula and the crossing over rational grid.
    for n in range(3,101):
        qstar=2/(3+sqrt(8*n-15))
        rstar=(1-qstar)/2
        for r in [F(1,20),F(1,6),F(1,4),F(3,10),F(1,3),F(7,20),F(2,5),F(9,20),F(49,100)]:
            c=predicted_m3(n,r)
            assert (c>0)==(float(r)<rstar) if r!=F(1,3) or n!=3 else c==0
            # Equivalent high-radius polynomial.
            if r>=F(1,3):
                q=1-2*r
                alt=F(comb(n,2))*q*(-1+3*q+2*(n-3)*q*q)
                assert c==alt
            checks+=1
    # Fourier trace checks: signed-third-cumulant and Parseval.
    for r in [F(1,10),F(1,4),F(1,3),F(2,5),F(9,20)]:
        rr=float(r)
        K=4000
        a=[sin(2*pi*k*rr)/(pi*k) for k in range(1,K+1)]
        assert abs(2*sum(v**3 for v in a)-float(delta(r)))<1e-7
        assert abs(sum(v*v for v in a)-float(2*r*(1-2*r)/2))<3e-5
        checks+=2
    print('PASS: ',checks, 'exact algebra/discrete-grid and Fourier numerical checks')
if __name__=='__main__': main()
