#!/usr/bin/env python3
"""Exact algebra and numerical stress tests for a two-disk hull John ellipsoid.
The infinite containment proof is in RESULT.md; finite tests are supplemental.
"""
from fractions import Fraction as F
from math import sqrt,pi,isclose
from random import Random


def axes2(t):
    if t <= 1:
        return 1-t*t/F(4), F(1,2)
    return (t+2)**2/F(12), (t+2)/(6*t)


def reduced_support_sq(t,s):
    thresh=t*t+2*t
    if s <= thresh:
        return (1+t/F(2))**2
    return 1+s/F(2)-t*t/F(4)


def exact_proof_checks():
    for t in map(F, ['0','1/10','1/2','1','5/4','2','7/2','8']):
        a2,b2=axes2(t)
        C=(1+t/F(2))**2
        D=t*t+2*t
        assert a2>0 and b2>0 and b2<=F(1,2)
        assert a2+D*b2==C
        if t<=1:
            assert b2==F(1,2) and a2==1-t*t/F(4)
        else:
            assert b2==(t+2)/(6*t) and a2==(t+2)**2/F(12)
        for s in map(F,['0','1/100','1/10','1','2','3','5','10','100']):
            assert a2+b2*s<=reduced_support_sq(t,s)
        assert a2+b2*D==reduced_support_sq(t,D)
    assert axes2(F(1))[0]==F(3,4)
    assert axes2(F(1))[1]==F(1,2)
    # The t>=1 objective is a constant times t+4+4/t; t=2 is its unique minimum.
    assert ((F(2)+2)**2/F(2))==F(8)


def stress_tests():
    rng=Random(120114514)
    n=0
    for t in [0.,0.01,0.5,0.99,1.,1.01,1.5,2.,3.,10.,30.]:
        a2,b2=map(float,axes2(F(str(t))))
        for j in range(10000):
            p=rng.uniform(-1.,1.)
            az=rng.uniform(-pi,pi)
            q=sqrt(1-p*p)*__import__('math').cos(az)
            r=sqrt(1-p*p)*__import__('math').sin(az)
            support=max(-t*p/2+sqrt(p*p+q*q),t*p/2+sqrt(p*p+r*r))
            ellipsoid=sqrt(a2*p*p+b2*(q*q+r*r))
            assert ellipsoid<=support+2e-12,(t,j,ellipsoid,support)
            n+=1
        # Exact tangent at reduced-support switching direction.
        s=t*t+2*t
        p=1/sqrt(1+s); q=sqrt(s)*p; r=0.
        support=max(-t*p/2+sqrt(p*p+q*q),t*p/2+abs(p))
        ellipsoid=sqrt(a2*p*p+b2*q*q)
        assert isclose(support,ellipsoid,abs_tol=2e-12), (t,support,ellipsoid)
    return n

if __name__=='__main__':
    exact_proof_checks()
    n=stress_tests()
    print(f'VERIFY_OK exact_cases=8 sampled_directions={n} contact_cases=11')
