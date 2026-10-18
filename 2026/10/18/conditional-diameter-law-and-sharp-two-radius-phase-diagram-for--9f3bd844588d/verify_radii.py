"""Standalone numerical/exact consistency tests for the two-radius cube-section theorem.

Only finite checks are performed; the infinite-dimensional quantifiers in the
stated result are established by the accompanying analytic proof.
"""
from fractions import Fraction as F
from itertools import product
from math import sqrt
import random


def section_inradius_sq(a, b, c):
    # Assumes 0 <= a <= b <= c, with a,b,c not all zero.
    return (a*a+b*b+c*c)/(b*b+c*c)


def section_diameter_sq(a, b, c):
    if c >= a+b:
        t=(a+b)/c
    else:
        t=(c-a)/b
    return 4*(2+t*t)


def vertices(a,b,c):
    u=(a,b,c)
    ans=set()
    for k in range(3):
        others=[i for i in range(3) if i!=k]
        if u[k]==0: continue
        for x,y in product((-1,1),repeat=2):
            z=-(x*u[others[0]]+y*u[others[1]])/u[k]
            if -1 <= z <= 1:
                v=[F(0)]*3
                v[others[0]]=F(x);v[others[1]]=F(y);v[k]=z
                ans.add(tuple(v))
    return ans


def bounds(h):
    h0_lo=0.28562048; h0_hi=0.28562049
    def g(x):return 2*x/sqrt(1-x*x)+sqrt(2)*x-1
    assert g(h0_lo)<0<g(h0_hi)
    # Use a bracketed unique root and avoid external dependencies.
    lo,hi=h0_lo,h0_hi
    for _ in range(60):
        mid=(lo+hi)/2
        if g(mid)>0:hi=mid
        else:lo=mid
    h0=(lo+hi)/2
    low=2*h/sqrt(1-h*h) if h<=h0 else 1-sqrt(2)*h
    high=1 if h<=1/sqrt(5) else sqrt(1-h*h)/h-1
    return low,high,h0


def run():
    exact=0
    for ai in range(0,13):
        for bi in range(max(1,ai),15):
            for ci in range(bi,17):
                a,b,c=F(ai),F(bi),F(ci)
                if c==0: continue
                vs=vertices(a,b,c)
                assert vs
                maximum=max(x*x+y*y+z*z for x,y,z in vs)
                assert 4*maximum==section_diameter_sq(a,b,c)
                rr=section_inradius_sq(a,b,c)
                h=float(a)/sqrt(float(b*b+c*c))
                low,high,_=bounds(h)
                t=sqrt(float(maximum-2))
                assert low-1e-10<=t<=high+1e-10
                assert abs(float(rr)-(1+h*h))<1e-12
                exact+=1
    rng=random.Random(20260921)
    sampled=0
    for _ in range(25000):
        a,b,c=sorted((rng.random(),rng.random(),rng.random()))
        h=a/sqrt(b*b+c*c)
        t=sqrt(section_diameter_sq(a,b,c)/4-2)
        lo,up,_=bounds(h)
        assert lo-1e-12<=t<=up+1e-12
        sampled+=1
    for h in [0.001,0.03,0.1,0.28562048389556804,0.35,1/sqrt(5),0.49,0.6,0.7,1/sqrt(2)]:
        lo,up,_=bounds(h)
        candidate=[]
        for p in (h,1/sqrt(2)):
            q=sqrt(1-p*p)
            t=(h+p)/q if q>=h+p else (q-h)/p
            candidate.append(t)
        assert abs(min(candidate)-lo)<1e-10
        if h<=1/sqrt(5):
            p=(-h+sqrt(2-h*h))/2 # solves sqrt(1-p²)=h+p
            assert h-1e-10<=p<=1/sqrt(2)+1e-10
            assert abs(sqrt(1-p*p)-h-p)<1e-10
            assert abs(up-1)<1e-12
        else:
            assert abs(max(candidate)-up)<1e-10
    print('PASS: exact rational edge enumeration for',exact,'sorted integer triples')
    print('PASS:',sampled,'random normalized parameter samples')
    print('PASS: endpoint and transition checks; remaining continuum covered by proof')


if __name__=='__main__':run()
