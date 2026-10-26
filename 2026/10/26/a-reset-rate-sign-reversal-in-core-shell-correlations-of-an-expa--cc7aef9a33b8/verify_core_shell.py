#!/usr/bin/env python3
"""Independent numerical checks for two-window Thomas-Fermi reset-age covariances.
Run with: python verify_core_shell.py  (requires scipy and Python 3).
The analytical proof is in RESULT.md; finite checks are not a replacement.
"""
import math
from scipy.integrate import quad


def fraction(a, lam):
    if lam <= a:
        return 1.0
    z = a / lam
    return (3*z - z**3)/2


def time_from_y(y, omega):
    return (y*math.sqrt(1+y*y)+math.asinh(y))/(math.sqrt(2)*omega)


def jac_y(y, omega):
    return math.sqrt(2)*math.sqrt(1+y*y)/omega


def calculation(u, c, v, omega, r):
    assert 0 < u < 1 < c < v and omega > 0 and r > 0
    yc, yv = math.sqrt(c-1), math.sqrt(v-1)
    def core(y): return fraction(u, 1+y*y)
    def shell(y): return fraction(v, 1+y*y)-fraction(c, 1+y*y)
    def mix(fn):
        def g(y): return r*math.exp(-r*time_from_y(y, omega))*jac_y(y, omega)*fn(y)
        return sum(quad(g, l, h, epsabs=2e-12, epsrel=2e-11)[0]
                   for l, h in [(0,yc), (yc,yv), (yv,math.inf)])
    ea, eb = mix(core), mix(shell)
    eab = mix(lambda y: core(y)*shell(y))
    return ea, eb, eab, eab-ea*eb


def coeffs(u, c, v, omega):
    yc, yv = math.sqrt(c-1), math.sqrt(v-1)
    def integrand(y):
        lam = 1+y*y
        return fraction(u,lam)*(fraction(v,lam)-fraction(c,lam))*jac_y(y,omega)
    small = quad(integrand,yc,yv,epsabs=2e-12)[0] + quad(integrand,yv,math.inf,epsabs=2e-12)[0]
    cutoff = time_from_y(yc,omega)
    speed2 = 2*omega**2*(1-1/c)
    large = 3*speed2/c**2*(fraction(u,1)-fraction(u,c))
    return cutoff, small, large


def main():
    checks = 0
    # Mass-fraction formulas versus direct integration of normalized parabola.
    for lam in [1., 1.03, 1.2, 1.5, 2., 5., 20.]:
        for a in [0.1,0.5,0.95,1.,1.5,2.,4.,30.]:
            numeric = quad(lambda x: .75/lam*(1-(x/lam)**2),
                           -min(a,lam),min(a,lam),epsabs=1e-13)[0]
            assert abs(numeric-fraction(a,lam))<1e-12
            checks += 1
    configs = [(0.5,1.5,2.,1.),(0.3,1.2,1.8,2.),(0.75,2.,3.,0.8)]
    for u,c,v,omega in configs:
        tc,small,large = coeffs(u,c,v,omega)
        assert tc>0 and small>0 and large>0
        checks += 3
        for rate in [0.002,0.005,0.01,0.02,0.05,0.1,0.2,0.5,1.,2.,3.,5.,8.]:
            ea, eb, eab, cov = calculation(u,c,v,omega,rate)
            assert 0 < ea < 1 and 0 <= eb < 1 and 0<= eab <= min(ea,eb)
            assert math.isclose(cov,eab-ea*eb,rel_tol=1e-12,abs_tol=1e-15)
            checks += 5
        # Sign reversals for all displayed geometries at extreme but finite rates.
        left = calculation(u,c,v,omega,0.0001)[-1]
        right = calculation(u,c,v,omega,10*omega)[-1]
        assert left > 0 and right < 0, (u,c,v,left,right)
        checks += 2
    u,c,v,omega=0.5,1.5,2.,1.
    tc,small,large = coeffs(u,c,v,omega)
    assert abs(large-89/486)<1e-14
    # Convergence to the high-rate coefficient in its proper Laplace regime.
    for rate in [8., 10., 12.]:
        k=calculation(u,c,v,omega,rate)[-1]
        ratio=k/(-large*math.exp(-rate*tc)/rate**2)
        assert 0.7 < ratio < 1.3, (rate,ratio)
        checks += 1
    print('PASS:',checks,'independent numerical assertions')
    print('benchmark cutoff time:',repr(tc))
    print('weak-reset coefficient:',repr(small))
    print('strong-reset coefficient:',repr(large),'= 89/486')
    for rate in [0.01,0.1,1.,10.]:
        print('rate',rate,'covariance',repr(calculation(u,c,v,omega,rate)[-1]))

if __name__ == '__main__':
    main()
