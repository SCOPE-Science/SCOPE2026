"""Supplementary finite checks for the Bloch-Hilbert critical transition.

Run: python3 CHECK.py (dependencies in requirements.txt).
Numerical quadrature is not a proof of an asymptotic theorem.
"""
from math import pi, sin, sqrt, isfinite
import numpy as np
from scipy.integrate import quad
from scipy.optimize import minimize_scalar
from scipy.special import hyp2f1, gamma, beta


def primitive_at_one_minus_v2(alpha, v):
    """P_alpha(1-v²), with an analytic connection formula at v=0."""
    t = 1-v*v
    if t <= 0.75:
        return t*hyp2f1(0.5, alpha, 1.5, t*t)
    w = v*v*(2-v*v)
    d = sqrt(pi)*gamma(1-alpha)/(2*gamma(1.5-alpha))
    return d + t*w**(1-alpha)*hyp2f1(1, 1.5-alpha, 2-alpha, w)/(2*(alpha-1))


def D(alpha, r):
    assert 1 < alpha < 2 and 0 <= r < 1
    def integrand(v):
        t = 1-v*v
        return 2*v*t*primitive_at_one_minus_v2(alpha, v)/(1-r*t)**2
    return (1-r*r)**alpha * quad(integrand, 0, 1, epsabs=5e-10, epsrel=3e-11, limit=250)[0]


def critical_coefficients(alpha):
    K = alpha*beta(2-alpha, alpha)+(5-3*alpha)*beta(3-alpha, alpha-1)
    R = beta(3-alpha, alpha-1)/(2-alpha)
    return K, R, K/(2*(alpha-1))+R


def run():
    K, R, c = critical_coefficients(1.5)
    assert abs(K-pi) < 1e-12
    assert abs(R-pi) < 1e-12
    assert abs(c-2*pi) < 1e-12
    for h in (0.0003, 0.0001, 0.00003):
        ratio = (pi-D(1.5,1-h))/h
        print('critical-slope',h,ratio,'target',2*pi)
        assert isfinite(ratio) and abs(ratio-2*pi) < 0.16
    earlier = None
    records=[]
    for eps in (0.06, 0.02, 0.005, 0.002):
        alpha = 1.5+eps
        L = pi/sin(pi*(alpha-1))
        result = minimize_scalar(lambda h:-D(alpha,1-h),bounds=(0.04*eps**2,5*eps**2),method='bounded',options={'xatol':1e-11})
        assert result.success
        h=result.x
        gain=-result.fun-L
        radius_ratio=h/eps**2
        gain_ratio=gain/eps**2
        print('alpha-offset',eps,'1-r',h,'radius_ratio',radius_ratio,'gain_ratio',gain_ratio)
        assert gain>0 and radius_ratio>0 and gain_ratio>0
        records.append((radius_ratio,gain_ratio))
        if earlier is not None:
            assert abs(radius_ratio-0.5)<abs(earlier[0]-0.5)
            assert abs(gain_ratio-pi)<abs(earlier[1]-pi)
        earlier=(radius_ratio,gain_ratio)
    assert abs(records[-1][0]-.5)<.025
    assert abs(records[-1][1]-pi)<.20
    print('SUPPLEMENTARY_CHECKS_PASSED')


if __name__ == '__main__':
    run()
