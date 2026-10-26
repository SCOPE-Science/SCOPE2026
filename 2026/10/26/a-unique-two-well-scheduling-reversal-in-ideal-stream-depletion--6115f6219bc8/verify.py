"""Reproducible finite numerical checks for the two-well stream-depletion ordering theorem.

Only Python standard-library modules are required. These finite checks are
not a substitute for the analytic proof of uniqueness or limiting behavior.
"""
import math
import random


def g(z):
    return math.erfc(z / math.sqrt(2)) - 2.0 * math.erfc(z)


def gprime(z):
    return (4.0 * math.exp(-z*z) - math.sqrt(2.0)*math.exp(-z*z/2.0))/math.sqrt(math.pi)


def crossing(r):
    assert r > 1.0
    zmax = math.sqrt(3.0*math.log(2.0))
    lo, hi = zmax/r, zmax
    for _ in range(115):
        mid = (lo + hi)/2.0
        if g(mid) - g(r*mid) > 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi)/2.0


def depletion(alpha, dt, start, finish, final=0):
    # Stream-depletion rate due to a finite constant pumping interval.
    if final == 0:
        final = 2.0*dt
    F = lambda t: math.erfc(alpha/math.sqrt(t)) if t > 0 else 0.0
    return F(final - start) - F(final - finish)


def test():
    zmax = math.sqrt(3.0*math.log(2.0))
    zp_lo, zp_hi = 0.01, zmax
    for _ in range(110):
        m = (zp_lo+zp_hi)/2
        if g(m) > 0:
            zp_hi = m
        else:
            zp_lo = m
    zp = (zp_lo+zp_hi)/2
    assert abs(zmax - 1.442026886600883) < 2e-14
    assert abs(zp - 0.9922696553820495) < 2e-14
    rng = random.Random(20261023)
    repetitions = 5000
    for _ in range(repetitions):
        r=math.exp(rng.uniform(0.005, 3.5))
        alpha=math.exp(rng.uniform(-1.5,1.5))
        z=crossing(r)
        assert zp - 1e-12 <= z <= zmax + 1e-12
        dcrit=(alpha/z)**2
        assert alpha**2/(zmax*zmax) < dcrit + 1e-12
        assert dcrit < alpha**2/(zp*zp) + 1e-12
        for mult, wanted in [(0.35,1),(2.5,-1)]:
            dt=mult*dcrit
            dn=depletion(alpha,dt,0,dt)+depletion(r*alpha,dt,dt,2*dt)
            df=depletion(r*alpha,dt,0,dt)+depletion(alpha,dt,dt,2*dt)
            analytic=g(alpha/math.sqrt(dt))-g(r*alpha/math.sqrt(dt))
            assert math.isclose(dn-df,analytic,rel_tol=1e-9, abs_tol=3e-14)
            assert (dn-df)*wanted > -1e-14
        assert gprime(z)>0 and gprime(r*z)<0
    for r in [1.0001,1.1,2,5,20,100]:
        z=crossing(r)
        assert abs(g(z)-g(r*z)) < 1e-12
    for i in range(1,1000):
        r1=1.0+i/200.0
        r2=r1+0.003
        assert crossing(r1)>crossing(r2)
    z=crossing(2.0)
    assert abs(1/z**2-0.8596011817017304)<1e-11
    assert g(2)>g(4) and g(.5)<g(1)
    print('PASS: 5000 varied-parameter cases (10000 endpoint comparisons);')
    print('PASS: 999 monotonic-ratio tests; root and limiting constants;')
    print('PASS: direct schedule superposition and closed-form difference.')
    print('For ratio 2: normalized critical duration =',1/z**2)
    print('Absolute normalized duration range:',1/zmax**2,1/zp**2)


if __name__=='__main__':
    test()
