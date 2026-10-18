#!/usr/bin/env python3
"""Exact rational identities and independent numerical checks for a normal-mixture curvature theorem."""
from fractions import Fraction as F
from math import cosh, sinh, exp, log, sqrt, isclose


def R(c, z):
    return (1 + c*z)/(c + z)**2


def M(c):
    return 1/(1+c) if c <= 2 else c*c/(4*(c*c-1))


def check_exact():
    checks=0
    cs=[F(1,9),F(1,2),F(1),F(3,2),F(2),F(5,2),F(4),F(7),F(32)]
    zs=[F(1),F(5,4),F(3,2),F(2),F(7,2),F(5),F(12),F(64)]
    for c in cs:
        for z in zs:
            if c <= 2:
                cert=(z-1)*(z+1+c-c*c)/((c+1)*(c+z)**2)
            else:
                cert=(c*c-c*z-2)**2/(4*(c*c-1)*(c+z)**2)
            assert M(c)-R(c,z)==cert
            assert cert>=0
            checks+=1
    c=F(32); s2=F(4)
    assert 1-s2*M(c)==-F(1,1023)
    assert 1-s2*R(c,F(1))==F(29,33)
    assert c-F(2)/c==F(511,16)
    assert 1-s2*M(F(2))==-F(1,3)
    return checks


def independent_curvature(s,c,u):
    # Unit-variance original three-Gaussian density; normalizing common factor cancels.
    w=c/(c+exp(s*s/2))
    means=(-s,0,s)
    weights=((1-w)/2,w,(1-w)/2)
    terms=[p*exp(-(u-m)**2/2) for p,m in zip(weights,means)]
    density=sum(terms)
    first=sum(t*(m-u) for t,m in zip(terms,means))
    second=sum(t*((m-u)**2-1) for t,m in zip(terms,means))
    return (first/density)**2-second/density


def check_numeric():
    tests=0
    for s in (0.6,1.0,1.2,1.65,sqrt(3),1.85,2.0,2.3):
        for c in (0.25,0.75,1.8,2.0,2.8,4.0,32.0):
            for u in (-3.5,-2.0,-0.7,0.0,0.8,2.0,3.5):
                derived=1-s*s*(1+c*cosh(s*u))/(c+cosh(s*u))**2
                direct=independent_curvature(s,c,u)
                assert isclose(derived,direct,rel_tol=1e-9,abs_tol=1e-10),(s,c,u,direct,derived)
                assert derived>=1-s*s*M(c)-1e-10
                tests+=1
    assert exp(1)<11/4
    assert sinh(4)<32
    # Crossover at exactly three in s squared and c=2.
    assert isclose(1-3*M(F(2)),0.0,abs_tol=1e-15)
    return tests


if __name__=='__main__':
    n=check_exact()
    m=check_numeric()
    print('PASS: %d exact rational identities, %d independent density-curvature comparisons.'%(n,m))
    print('All-parameter statements require the analytic proof in RESULT.md.')
