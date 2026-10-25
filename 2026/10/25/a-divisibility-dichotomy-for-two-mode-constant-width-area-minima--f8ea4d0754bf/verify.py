#!/usr/bin/env python3
"""Independent numerical and arithmetic checks for the two-cosine constant-width theorem.
The all-integer and symbolic arguments are given in RESULT.md; finite checks are supplementary.
Uses only Python standard library.
"""
from fractions import Fraction
from math import cos, sin, pi, gcd
from random import Random

rng=Random(610304)

# Rational core of the all-d>=5 comparison, not a substitute for its monotonic proof.
for d in range(5,1002,2):
    assert 2*d*d-5*d-10 > 0
    assert Fraction(d+2,d) * (1-Fraction(5,d*d)) > 1
print('RATIONAL_COSINE_LOWER_CERTIFICATE_FAMILIES_OK')

pairs=[]
for n in range(3,102,2):
    for m in range(n+2,202,2):
        d=n//gcd(n,m)
        if d==1:
            continue
        assert d>=3 and d%2==1
        r2=Fraction(n*n-1,m*m-1)
        if d==3:
            assert m*3 >= 5*n
            assert r2 < Fraction(1,2)
            kap2=.5
        else:
            assert m*d >= n*(d+2)
            assert r2 < Fraction(d*d,(d+2)**2)
            kap2=cos(pi/d)**2
            assert float(r2)<kap2
        pairs.append((n,m,kap2,float(r2)))
assert len(pairs)>1000
print('ALL_NONRESONANT_INDEX_PAIRS_AND_STRICT_GAPS_OK',len(pairs))

# Direct sphere-of-directions norm bounds sampled on a fine angular mesh.
# Test random normalized coefficients and several hardest cases; continuous proof is separate.
for n,m in [(3,5),(5,7),(7,9),(9,15),(15,25),(33,55),(25,27),(21,35)]:
    d=n//gcd(n,m)
    kap2=.5 if d==3 else cos(pi/d)**2
    r2=(n*n-1)/(m*m-1)
    for _ in range(22):
        a,b=(rng.uniform(-1,1),rng.uniform(-1,1))
        N=8000
        norm=max(abs(a*cos(n*2*pi*j/N)+b*cos(m*2*pi*j/N)) for j in range(N))
        # The norm lower bound can be checked with high margin away from degenerate b=0.
        normlower=(a*a+kap2*b*b)**.5
        assert norm+1e-10>=normlower
        scale=.94/max(norm,1e-20)
        A,B=scale*a,scale*b
        assert A*A+r2*B*B<=1+1e-9
        assert 1-A*A-r2*B*B >= (kap2-r2)*B*B-1e-9
print('INDEPENDENT_TRIGONOMETRIC_NORM_AND_AREA_STABILITY_SAMPLES_OK')

# Constructive resonance: m = k*n, k odd >=3.
for n in range(3,40,2):
    for k in range(3,24,2):
        m=k*n
        t=Fraction(1,k*k+1)
        a,b=Fraction(1)+t,-t
        r2=Fraction(n*n-1,m*m-1)
        assert a*a+r2*b*b > 1
        samples=[a*cos(n*2*pi*j/8000)+b*cos(m*2*pi*j/8000) for j in range(8000)]
        assert max(map(abs,samples)) <= 1+1e-10
        assert abs(samples[0]-1)<1e-12
print('RESONANT_FEASIBLE_STRICT_IMPROVEMENT_FAMILY_OK')

# Verify the support-area formula by a direct trapezoid integral for smooth feasible pairs.
for n,m in [(3,5),(5,7),(9,15),(15,25),(13,39)]:
    w=1.7; x=.33; y=-.23
    A=w*x/(2*(n*n-1));B=w*y/(2*(m*m-1))
    N=8192
    integ=0
    for j in range(N):
        theta=2*pi*j/N
        h=w/2+A*cos(n*theta)+B*cos(m*theta)
        hp=-n*A*sin(n*theta)-m*B*sin(m*theta)
        integ+=(h*h-hp*hp)/2
    area_quad=2*pi*integ/N
    area_exact=pi*w*w/4-pi*w*w/8*(x*x/(n*n-1)+y*y/(m*m-1))
    assert abs(area_quad-area_exact)<2e-11,(n,m,area_quad-area_exact)
print('DIRECT_GEOMETRIC_SUPPORT_AREA_INTEGRALS_OK')
print('ALL_TWO_MODE_DIVISIBILITY_CERTIFICATES_OK')
