#!/usr/bin/env python3
"""Standalone scientific checks for the four-time fractional-telegraph aging law.

Requires numpy and scipy. Simulations support but do not replace the proof.
"""
import math
import numpy as np
from scipy.special import betainc
from scipy.integrate import quad


def p(nu, x, y):
    assert 0 < nu < 1 and 0 < x < y
    return float(betainc(nu, 1 - nu, x / y))


def q(nu, a, b, c, d):
    assert 0 < a < b < c < d and 0 < nu < 1
    const = math.sin(math.pi * nu) / math.pi
    def integrand(z):
        if not z < c-a:
            return 0.
        return const*a**nu/(z**nu*(a+z))*p(nu,c-a-z,d-a-z)
    integral, err = quad(integrand, b-a, c-a, epsabs=2e-12, epsrel=2e-12)
    return p(nu,a,d)+integral, err


def simulate(n=25000, step=0.003, seed=41825):
    """Exact Levy(1/2) increments, then discretize inverse crossing times."""
    rng=np.random.default_rng(seed)
    dvals=np.zeros(n)
    e_steps=np.zeros((n,4),dtype=np.int32)
    for j in range(15000):
        g=rng.standard_normal(n)
        dvals += step*step/(2*g*g)
        for k,threshold in enumerate([1.,2.,3.,4.]):
            e_steps[:,k] += (dvals < threshold)
        if np.all(dvals >= 4):
            break
    else:
        raise AssertionError('finite simulation horizon too short')
    first = e_steps[:,0] == e_steps[:,1]
    second = e_steps[:,2] == e_steps[:,3]
    return float(np.mean(first)),float(np.mean(second)),float(np.mean(first & second)),j+1


def main():
    nu=.5
    assert abs(p(nu,1,2)-.5)<1e-13
    assert abs(p(nu,3,4)-2/3)<1e-13
    assert abs(p(nu,1,4)-1/3)<1e-13
    pred,err=q(nu,1,2,3,4)
    # Integral strictly positive; its approximate size is a numerical diagnostic.
    assert pred>1/3 and pred<.5
    assert err<1e-9
    for params in [(0.23,.4,.8,1.9,4.1),(.71,1.2,1.8,3.0,6.0)]:
        z,_=q(*params)
        assert p(params[0],params[1],params[4]) < z < p(params[0],params[1],params[2])
    x,y,z,steps=simulate()
    assert abs(x-.5)<.025,(x,'p12')
    assert abs(y-2/3)<.025,(y,'p34')
    assert abs(z-pred)<.025,(z,'Q')
    assert z-x*y>.012,(x,y,z,'connected covariance')
    print('PASS: exact arcsine pair checks and two general four-time integrals')
    print('Q(1,2,3,4), half-stable:',f'{pred:.12f}','quadrature error:',err)
    print('connected four-time limit:',f'{pred-1/3:.12f}')
    print('independent stable increments simulation:',{'n':25000,'mesh':.003,'seed':41825,'steps':steps,'p12':x,'p34':y,'Q':z})


if __name__=='__main__':
    main()
