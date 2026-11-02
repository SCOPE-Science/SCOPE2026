#!/usr/bin/env python3
"""Reproducible supplementary checks for the symmetric-energy spectral theorem.

Run with Python 3 standard library. Finite checks are not the theorem's proof.
"""
from fractions import Fraction
import math
import random


def near(x, y, tol=1e-10):
    assert abs(x-y) <= tol * (1+abs(x)+abs(y)), (x,y)


def quantities(lams, coeffs, h):
    z = [math.exp(h*a) for a in lams]
    drop = sum(c*(x*x-1) for c,x in zip(coeffs,z))/2
    defect = sum(c*(x-1)*(x-3) for c,x in zip(coeffs,z))/4
    effective = sum(c*(x-1)**2 for c,x in zip(coeffs,z)) / sum(c*(x-1) for c,x in zip(coeffs,z))
    return drop, defect, effective


def spectral_ratio(a, h):
    z=math.exp(a*h)
    return (z-3)/(2*(z+1))


def main():
    tests=0
    # The exactly representable two-mode witness: exp(h)=2, exp(2h)=4.
    z=[Fraction(2),Fraction(4)]
    l=[Fraction(1),Fraction(2)]
    sq=[Fraction(6),Fraction(1)]
    e_now=sum(a*x for a,x in zip(l,sq))/2
    e_prev=sum(a*x*q*q for a,x,q in zip(l,sq,z))/2
    e_extrap=sum(a*x*(2-q)**2 for a,x,q in zip(l,sq,z))/2
    defect=(e_extrap-e_now)/2
    assert (e_now,e_prev,e_extrap,defect,e_prev-e_now)==(4,28,4,0,24)
    tests+=5
    r=random.Random(20261026)
    for repetition in range(350):
        n=r.randint(1,8)
        lams=sorted(r.uniform(.3,4) for _ in range(n))
        v=[r.uniform(-2,2) for _ in range(n)]
        if not any(v): v[0]=1
        coeffs=[a*x*x for a,x in zip(lams,v)]
        h=r.uniform(.01, 1.1)
        drop,defect,eff=quantities(lams,coeffs,h)
        enow=sum(a*x*x for a,x in zip(lams,v))/2
        prev=sum(a*x*x*math.exp(2*h*a) for a,x in zip(lams,v))/2
        ext=sum(a*x*x*(2-math.exp(h*a))**2 for a,x in zip(lams,v))/2
        near(prev-enow,drop);tests+=1
        near((enow+ext)/2-enow,defect);tests+=1
        assert drop>0;tests+=1
        lo=spectral_ratio(lams[0],h)
        hi=spectral_ratio(lams[-1],h)
        assert lo-1e-11 <= defect/drop <= hi+1e-11;tests+=1
        assert (defect>0)==(eff>2) or abs(defect)<1e-12;tests+=1
        # The effective amplification mean increases strictly with the lookback.
        hs=[(k+1)*math.log(3)/lams[-1]/12 for k in range(55)]
        es=[quantities(lams,coeffs,t)[2] for t in hs]
        assert all(y>x for x,y in zip(es,es[1:]));tests+=1
        # Precisely one defect-zero crossing between the active spectral extremes.
        left=math.log(3)/lams[-1]
        right=math.log(3)/lams[0]
        assert quantities(lams,coeffs,left)[1] <= 1e-9;tests+=1
        assert quantities(lams,coeffs,right)[1] >= -1e-9;tests+=1
        for _ in range(90):
            mid=(left+right)/2
            if quantities(lams,coeffs,mid)[2] < 2:
                left=mid
            else: right=mid
        near(quantities(lams,coeffs,(left+right)/2)[2],2,1e-9);tests+=1
        if lams[0]!=lams[-1]:
            assert math.log(3)/lams[-1]-1e-10 < (left+right)/2 < math.log(3)/lams[0]+1e-10
            tests+=1
    for k in range(1,51):
        a=0.1*k
        h=math.log(3)/a
        d,D,M=quantities([a],[a*2],h)
        near(D,0);near(M,2);near(d,8*a)
        tests+=3
    print('VERIFIED: %d supplementary checks (exact rational and seeded spectral cases)' % tests)

if __name__=='__main__': main()
