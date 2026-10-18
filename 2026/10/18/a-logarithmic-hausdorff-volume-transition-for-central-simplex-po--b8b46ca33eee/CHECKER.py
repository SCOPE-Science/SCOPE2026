#!/usr/bin/env python3
"""Reproducibility checks for the barycentric-ratio polytope theorem.

Requires Python 3 standard library only. Exact rational checks are finite;
the dimension-uniform theorem follows from the separate analytic proof.
"""
import math
from fractions import Fraction

GAMMA = 0.577215664901532860606512090082402431
ZETA2 = math.pi * math.pi / 6

def exact_volume(m, c):
    assert isinstance(c, int) and c > 1 and m >= 2
    return sum((Fraction(m*(-1)**k*math.comb(m-1,k),m+(c-1)*k)
               for k in range(m)), Fraction(0,1))

def log_volume(m,c):
    a=m/(c-1)
    return math.lgamma(1+a)+math.lgamma(m)-math.lgamma(m+a)

def hd(m,c):
    return math.sqrt(m*(m-1))/(m+c-1)

def vertex(m,c,hi):
    k=len(hi)
    lo=1/(m+(c-1)*k)
    return [c*lo if i in hi else lo for i in range(m)]

def bisect_vol(m,p):
    lo=1+1e-7
    hi=100*m*(math.log(m)+1)
    for _ in range(100):
        mid=(lo+hi)/2
        if log_volume(m,mid)<math.log(p): lo=mid
        else:hi=mid
    return (lo+hi)/2

def run():
    count=0
    for m in range(2,19):
        assert exact_volume(m,2)==Fraction(1,math.comb(2*m-1,m-1));count+=1
        for c in (2,3,4,5,7):
            exact=float(exact_volume(m,c))
            numer=math.exp(log_volume(m,c))
            assert abs(numer-exact)<=max(3e-10*exact,1e-15), (m,c,numer,exact)
            count+=1
    for m in range(2,12):
        for c in (1.01,1.2,2,5,100):
            x=vertex(m,c,(0,))
            expected=hd(m,c)
            dist=math.sqrt(sum((int(i==0)-xi)**2 for i,xi in enumerate(x)))
            assert abs(dist-expected)<2e-14, (m,c,dist,expected)
            for i in range(m):
                for j in range(m):
                    assert x[i] <= c*x[j]+1e-12
            assert abs(sum(x)-1)<1e-12
            count+=1
    for m in (50,1000,1000000):
        for p in (0.2,0.5,0.8):
            c=bisect_vol(m,p)
            q=-math.log(p);L=math.log(m)+GAMMA
            a=m/(c-1)
            d=hd(m,c)
            assert abs(math.exp(log_volume(m,c))-p)<2e-8
            assert abs(d-math.sqrt((m-1)/m)*a/(1+a)) < 1e-13
            approx=math.sqrt((m-1)/m)*(q/L-q*q/L**2+(q**3+ZETA2*q*q/2)/L**3)
            assert abs(approx-d)<20/L**4, (m,p,approx,d)
            count+=1
    # Euler-corrected volume formula has the predicted second-order sign.
    for m in (10000,1000000):
        L=math.log(m)+GAMMA
        for t in (0.5,1,2):
            vol=math.exp(log_volume(m,t*m*L))
            assert vol>math.exp(-1/t)
            assert abs(vol/math.exp(-1/t)-1-ZETA2/(2*t*t*L*L)) < 5/L**3
            count+=1
    print('PASS:',count,'separate finite-rational, geometry, and numerical checks')

if __name__ == '__main__':run()
