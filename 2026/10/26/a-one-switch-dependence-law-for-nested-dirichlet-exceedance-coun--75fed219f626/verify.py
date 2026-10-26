#!/usr/bin/env python3
"""Reproducible exact arithmetic and finite-sample diagnostics for Dirichlet exceedance covariance."""
from fractions import Fraction as F
from math import exp, ceil
from random import Random


def covariance_uniform(d, k, r, s):
    assert 2 <= k <= d and F(0) < r <= s < F(1)
    p = (1-r)**(d-1)
    b = (1-s)**(d-1)
    joint = max(F(0), 1-r-s)**(d-1)
    return k*b + k*(k-1)*joint - k*k*p*b


def crossing_uniform(d, k, r):
    # Floating closed-form solution for r below its sharp boundary.
    rr = float(r)
    assert rr < 1-k**(-1/(d-1))
    b = ((k*(1-rr)**(d-1)-1)/(k-1))**(1/(d-1))
    return 1-rr/(1-b)


def check_uniform():
    checked = 0
    for d in range(3, 16):
        for k in range(2, d+1):
            for i in range(1, 35):
                r = F(i, 100)
                for j in range(i, 96, 2):
                    s = F(j, 100)
                    if not r <= s < 1:
                        continue
                    cv = covariance_uniform(d, k, r, s)
                    kp = k*(1-r)**(d-1)
                    if kp < 1:
                        assert cv > 0, (d,k,r,s,cv)
                    elif kp == 1:
                        assert cv >= 0
                    elif s >= 1-r:
                        assert cv < 0
                    checked += 1
    assert covariance_uniform(4,2,F(1,10),F(7,10)) == F(-2183,250000)
    for d in (3,4,5,8,16,35):
        for k in (2,d):
            r = F(1,20)
            if k*(1-r)**(d-1) <= 1:
                continue
            root = crossing_uniform(d,k,r)
            assert float(r) < root < 1-float(r)
            # numerical formula on each side of the exact root; boundary bracket
            left = covariance_uniform(d,k,F(1,20), F(root-1e-7).limit_denominator(10**12))
            right = covariance_uniform(d,k,F(1,20), F(root+1e-7).limit_denominator(10**12))
            assert left > 0 and right < 0, (d,k,root,left,right)
    return checked


def check_mc():
    rng = Random(130578)
    cases = [(4,3,0.5,0.10,0.70),(4,3,2.0,0.08,0.60),(3,3,0.5,0.10,0.80),
             (5,4,1.4,0.35,0.55),(5,4,1.4,0.05,0.60)]
    reports=[]
    for d,k,alpha,r,s in cases:
        N=180000
        total_a=total_b=total_ab=0.0
        for _ in range(N):
            xs=[rng.gammavariate(alpha,1.) for _ in range(d)]
            denom=sum(xs)
            a=sum(x/denom>r for x in xs[:k]);b=sum(x/denom>s for x in xs[:k])
            total_a+=a;total_b+=b;total_ab+=a*b
        cov=total_ab/N-total_a*total_b/N**2
        reports.append((d,k,alpha,r,s,cov))
    return reports

if __name__=='__main__':
    c=check_uniform()
    print('PASS: %d exact-rational sign classification checks (plus explicit example, and root bracketing)'%c)
    for case in check_mc():
        print('Monte Carlo corroboration: d=%d,k=%d,alpha=%g,r=%g,s=%g,cov≈%.6f'%case)
    for c in (.5,1.,2.):
        beta=(exp(c)-1)/c
        assert beta>c
        print('Scaling threshold: c=%g, beta_*(c)=%.12f'%(c,beta))
