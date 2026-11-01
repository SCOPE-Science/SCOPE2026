#!/usr/bin/env python3
"""Independent numerical cross-checks for the ellipse crossing-angle identity.

Requires Python 3 standard library only. These finite checks do not replace proof.
"""
from math import pi, sin, cos, log, sqrt
from random import Random


def li2_series(z, tolerance=2e-15):
    if not 0 <= z < 1:
        raise ValueError('argument must lie in [0,1)')
    if z == 0:
        return 0.0
    term = z
    total = 0.0
    k = 1
    while k <= 300000:
        increment = term / (k * k)
        total += increment
        if increment < tolerance * max(1.0, total):
            return total
        k += 1
        term *= z
    raise AssertionError('series truncation limit')


def exact_q(r):
    x = ((r - 1.0) / (r + 1.0))**2
    if x == 0:
        return 0.5 + 1.5 / pi**2
    return (1.0 - x) / 2 + (3.0 / (2*pi**2)) * ((1-x)**2 / x) * li2_series(x)


def simpson(f, n=8192):
    if n % 2:
        raise ValueError('n must be even')
    h = pi/n
    s = f(0) + f(pi)
    for j in range(1,n):
        s += (4 if j%2 else 2)*f(j*h)
    return s*h/3


def angular_integral(r):
    x = ((r-1.0)/(r+1.0))**2
    def f(t):
        dens = 6*t*(pi-t)/pi**3
        kernel = (1-x*x)/(1-2*x*cos(2*t)+x*x)
        return dens * sin(t)**2 * kernel
    return simpson(f)


def empirical_q(r, seed, count=160000):
    rng=Random(seed)
    cross=0
    val_sum=0.0
    for _ in range(count):
        a,b,c,d=[2*pi*rng.random() for _ in range(4)]
        u=(c-a)%(2*pi)<(b-a)%(2*pi)
        v=(d-a)%(2*pi)<(b-a)%(2*pi)
        if u == v:
            continue
        ux=r*(cos(b)-cos(a))
        uy=sin(b)-sin(a)
        vx=r*(cos(d)-cos(c))
        vy=sin(d)-sin(c)
        crossprod=ux*vy-uy*vx
        val_sum += crossprod**2 / ((ux**2+uy**2)*(vx**2+vy**2))
        cross+=1
    return cross/count, val_sum/cross, cross


def test():
    from math import isclose
    assert isclose(exact_q(1),0.5+1.5/pi**2,abs_tol=1e-14)
    for k in range(1,9):
        coefficient=simpson(lambda t:6*t*(pi-t)/pi**3*cos(2*k*t),2048)
        assert abs(coefficient+3/(pi*pi*k*k)) < 5e-10,(k,coefficient)
    print('INDEPENDENT_CYCLIC_GAP_FOURIER_COEFFICIENTS_PASSED 8')
    for r in [1.,1.1,1.5,2.,3.,6.,15.,40.]:
        a,b=exact_q(r),angular_integral(r)
        assert abs(a-b)<2e-8,(r,a,b)
    print('INDEPENDENT_BETA_POISSON_QUADRATURE_AND_DILOG_IDENTITY_PASSED 8')
    qprev=exact_q(1.)
    for r in [1.05,1.2,1.6,2.,3.,4.,6.,10.,30.,100.]:
        q=exact_q(r)
        assert 0<q<qprev
        x=((r-1)/(r+1))**2
        assert exact_q(1.0)-q > x/2
        qprev=q
    print('STRICT_INVERSE_RANGE_DIAGNOSTICS_PASSED')
    for r,seed in [(1,51),(1.5,52),(3,53),(10,54)]:
        cp,mc,number=empirical_q(r,seed)
        assert abs(cp-1/3)<.006, (r,cp)
        assert abs(mc-exact_q(r)) < .014, (r,mc,exact_q(r))
        print('INDEPENDENT_ORIGINAL_LABELLED_ENDPOINT_SIMULATION_PASSED',r,number)
    print('ALL_CHECKS_PASSED')


if __name__=='__main__':
    test()
