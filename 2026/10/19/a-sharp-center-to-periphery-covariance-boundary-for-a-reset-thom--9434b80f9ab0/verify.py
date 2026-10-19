#!/usr/bin/env python3
"""Independent quadratures for reset-age-induced Thomas--Fermi profile covariance.

Requires Python >=3.10 and SciPy >=1.10. No data files or randomness.
These are numerical checks, not a substitute for the asymptotic proof.
"""
import math
from scipy.integrate import quad

ROOT2 = math.sqrt(2.0)


def t_of_lambda(lam, omega=1.0):
    assert lam >= 1.0 and omega > 0.0
    v = math.sqrt(lam - 1.0)
    return (v * math.sqrt(lam) + math.asinh(v)) / (ROOT2 * omega)


def lambda_of_t(t, omega=1.0):
    assert t >= 0.0
    lo, hi = 1.0, 2.0 + ROOT2 * omega * t
    for _ in range(67):
        mid = (lo + hi) / 2.0
        if t_of_lambda(mid, omega) < t:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def profile_u(u, z):
    return u * max(1.0 - z*z*u*u, 0.0)


def covariance_scale_quadrature(r, z, omega=1.0):
    """Calculate covariance via the source's random scale h(lambda) d lambda."""
    assert r > 0 and z >= 0
    s0 = math.sqrt(max(z-1.0, 0.0))
    def rho(s):
        lam = 1.0 + s*s
        age = t_of_lambda(lam, omega)
        return r * math.exp(-r*age) * ROOT2 / omega * math.sqrt(lam)
    def integ(h, lower=0.0):
        return quad(lambda s: rho(s)*h(1.0/(1.0+s*s)),lower, math.inf,
                    epsabs=2.e-14,epsrel=3.e-12,limit=300)[0]
    mean_u = integ(lambda u:u)
    mean_g = integ(lambda u:profile_u(u,z),s0)
    mean_ug= integ(lambda u:u*profile_u(u,z),s0)
    return 9.0/16.0*(mean_ug-mean_u*mean_g)


def covariance_age_quadrature(r, z, omega=1.0):
    """Independently calculate covariance directly over Exp(r) ages."""
    def integ(h):
        def inner(q):
            u = 1.0/lambda_of_t(q/r,omega)
            return math.exp(-q)*h(u)
        return quad(inner,0.0,45.0,epsabs=2.e-14,epsrel=5.e-12,
                    limit=350)[0]
    eu=integ(lambda u:u)
    eg=integ(lambda u:profile_u(u,z))
    eug=integ(lambda u:u*profile_u(u,z))
    return 9.0/16.0*(eug-eu*eg)


def slow_rate_coefficient(z, omega=1.0):
    """Exact coefficient A(z): C(r,z) ~ (9/16) r A(z) (x0=1)."""
    # Numerical integration of A, independent of h(lambda).
    lower=math.sqrt(max(z-1.,0.))
    def integrand(s):
        lam=1+s*s
        u=1/lam
        return ROOT2/omega*math.sqrt(lam)*u*profile_u(u,z)
    return quad(integrand, lower,math.inf,epsabs=5.e-13)[0]


def checks():
    examples=[(.03,.2),(.03,.8),(.03,1.5),(.5,.8),
              (1.,.8),(5.,.8),(1.,1.5),(5.,1.5),
              (20.,1/math.sqrt(3))]
    for r,z in examples:
        a=covariance_scale_quadrature(r,z)
        b=covariance_age_quadrature(r,z)
        assert abs(a-b)<2.e-8+2.e-5*max(abs(a),abs(b)),(r,z,a,b)
        print(f'r={r:.5g} z={z:.8g} C_scale={a:+.12e} C_age={b:+.12e}')
    # Spatial positivity below the sharp center-to-periphery radius.
    for r in [.03,.2,1.,4.,20.]:
        for z in [0.,.25,1/math.sqrt(3)]:
            assert covariance_scale_quadrature(r,z)>0,(r,z)
    # Examples of slow-positive and fast-negative off-center covariance.
    for z,high in [(.7,20.),(.8,5.),(1.,5.),(1.5,1.)]:
        assert covariance_scale_quadrature(.003,z)>0,z
        assert covariance_scale_quadrature(high,z)<0,z
    # The beta-integral identity for the exact slow-rate coefficient.
    for z in [0.,.25,.75,1.]:
        exact=ROOT2*(1.-8*z*z/15.)
        assert abs(slow_rate_coefficient(z)-exact)<5.e-10,(z,exact)
    # Three distinct rapid-reset regimes, all obtained analytically.
    for z in [.25,.8]:
        r=100.
        exact=9./16.*5.*(1.-3*z*z)/r**4
        num=covariance_scale_quadrature(r,z)
        print('high-r inner',z,'num=',num,'leading=',exact)
        assert num*exact>0 and .5< num/exact <1.5
    z=1/math.sqrt(3);r=40.
    exact=9./16.*84./r**6
    num=covariance_scale_quadrature(r,z)
    print('high-r critical',z,'num=',num,'leading=',exact)
    assert num>0 and .5<num/exact<1.5
    print('All independent quadrature, sign, and coefficient checks passed.')

if __name__=='__main__':
    checks()
