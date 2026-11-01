#!/usr/bin/env python3
"""Reproducibility checks for two-cycle trace splitting in an analytic torus map.

No symbolic or third-party numerical libraries are required. These checks do
not replace the implicit-function/Taylor argument proving the asymptotics.
"""
from math import acos, asin, cos, pi, sin, sqrt, atan


def deformation(x, mu):
    t = 2*pi*x - acos(-mu)
    return atan(mu*sin(t)/(1-mu*cos(t)))/pi


def derivative(x, mu):
    t = 2*pi*x - acos(-mu)
    return 2*mu*(cos(t)-mu)/(1-2*mu*cos(t)+mu*mu)


def two_cycle(mu, a0, b0, k0, k1):
    a, b = a0, b0
    for _ in range(30):
        fa, fb = deformation(a, mu), deformation(b, mu)
        h0 = 2*b-3*a-fa-k0
        h1 = 2*a-3*b-fb-k1
        if max(abs(h0),abs(h1)) < 4e-15:
            break
        A = -3-derivative(a, mu)
        D = -3-derivative(b, mu)
        det = A*D-4
        da = -(D*h0-2*h1)/det
        db = -(-2*h0+A*h1)/det
        a, b = a+da, b+db
    res = max(abs(2*b-3*a-deformation(a,mu)-k0),
              abs(2*a-3*b-deformation(b,mu)-k1))
    assert res < 8e-13, (mu, res)
    assert abs(a-b) > 0.05
    d0, d1 = derivative(a,mu), derivative(b,mu)
    tr = 7+3*(d0+d1)+d0*d1
    return a,b,tr,res


def verify():
    eps = 1e-12
    for mu in [1e-4, 1e-3, 0.01, 0.03, 0.1, 0.4, 0.8]:
        # Source fixed-point formula and exact fixed derivative cancellation.
        xf = asin(mu)/pi
        assert abs(xf+deformation(xf,mu)) < eps
        assert abs(derivative(xf,mu)) < eps

    # The formal Taylor coefficient is derived exactly in the theorem proof.
    q5=sqrt(5)
    branches = [
        (4/5,1/5,-2,1,(25-7*q5)/2),
        (3/5,2/5,-1,0,(25+7*q5)/2),
    ]
    for a0,b0,k0,k1,coeff in branches:
        # Check the implicit equations at the cat map and the quadratic slope.
        assert 2*b0-3*a0 == k0 or abs(2*b0-3*a0-k0)<1e-14
        assert abs(2*a0-3*b0-k1) < 1e-14
        for mu in [1e-4, 3e-4, 1e-3, 3e-3, 1e-2]:
            a,b,tr,_=two_cycle(mu,a0,b0,k0,k1)
            assert abs((tr-7)/(mu*mu)-coeff) < 0.05
            s=cos(2*pi*a0)
            assert abs((a-a0)/mu-s/pi)<0.03
            assert abs((b-b0)/mu-s/pi)<0.03
        print('branch', a0, b0, 'coefficient', format(coeff,'.12f'),
              'verified')

    # Independent two-orbit spectral separation at a physically finite perturbation.
    mu=0.01
    trace1=two_cycle(mu,*branches[0][:4])[2]
    trace2=two_cycle(mu,*branches[1][:4])[2]
    assert 7<trace1<trace2
    print('mu=0.01, traces',format(trace1,'.12f'),format(trace2,'.12f'))
    print('all numerical checks passed; asymptotic universality is proved analytically')

if __name__=='__main__':
    verify()
