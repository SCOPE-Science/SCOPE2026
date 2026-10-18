"""Finite reproducibility diagnostics for finite-annulus Hardy constants.

This program checks finite matrix identities and asymptotic numerics only.
It is not a substitute for the analytic proof of the full function-space inequality.
Requires Python 3.9+; no third-party dependencies.
"""

from math import cos, pi, sqrt
from random import Random


def parameters(prime, dimension, order):
    assert prime >= 2 and dimension >= 1 and 0 < order < dimension
    r = prime ** (-(dimension + order) / 2.0)
    C = (prime ** order - 1) / (1 - prime ** (-dimension - order))
    B = C * (1 - prime ** (-dimension))
    return r, B, C


def theta_of(r, M):
    assert 0 < r < 1 and M >= 1
    lo, hi = 0.0, pi / (M + 1)
    for _ in range(85):
        t = (lo + hi) / 2
        if cos((M + 1) * t / 2) > r * cos((M - 1) * t / 2):
            lo = t
        else:
            hi = t
    return (lo + hi) / 2


def sharp_gap(r, B, M):
    th = theta_of(r, M)
    lam = (1 - r*r) / (1 - 2*r*cos(th) + r*r)
    gap = B * ((1 + r)/(1 - r) - lam)
    return gap, th, lam


def rayleigh(r, B, v):
    M = len(v)
    norm = sum(x*x for x in v)
    assert norm > 0
    gram = sum(v[i]*v[j]*r**abs(i-j)
               for i in range(M) for j in range(M))
    return B * ((1+r)/(1-r) - gram/norm)


def diagnostics():
    rng = Random(20261015)
    total = 0
    for prime, dimension, order in [(2,1,.5),(3,2,.8),(5,3,1.25), (7,1,.2)]:
        r,B,C=parameters(prime,dimension,order)
        for M in [1,2,3,4,5,8,13,23,37]:
            gap,theta,top=sharp_gap(r,B,M)
            assert 0 < theta < pi/(M+1)
            assert gap > 0
            v=[cos((j-(M-1)/2)*theta) for j in range(M)]
            assert all(a>0 for a in v)
            for j in range(M):
                val=sum(r**abs(j-k)*v[k] for k in range(M))
                assert abs(val-top*v[j]) < 1.e-9 * (1+abs(top*v[j]))
                total+=1
            assert abs(rayleigh(r,B,v)-gap)<1.e-10*(1+gap)
            total+=1
            for _ in range(12):
                trial=[rng.uniform(-2,2) for _ in range(M)]
                assert rayleigh(r,B,trial)>=gap-1.e-9*(1+gap)
                total+=1
        # Derived critical scale; a finite check does not prove the limit.
        M=2500
        gap,_,_=sharp_gap(r,B,M)
        predicted=B*r*(1+r)/(1-r)**3 *pi*pi/(M+(1+r)/(1-r))**2
        assert abs(gap-predicted)/predicted < .0001
        total+=1
    # Angular perturbation on the single shell |x|_2=1:
    # function +1 on 1+4Z_2, -1 on 3+4Z_2; radial reference +1.
    # Its Hardy mass is 1/2. Cross-coset pair distance is 1/2,
    # and the extra quotient is C*2**order (for p=2, dim=1).
    r,B,C=parameters(2,1,.5)
    base,_,_=sharp_gap(r,B,1)
    shell_measure=1/4
    cross_sum=2*shell_measure**2 * (2**(1+.5)) * (1-(-1))**2
    extra_quotient = (C/2*cross_sum)/(2*shell_measure)
    assert abs(extra_quotient-C*2**.5)<1e-12
    assert extra_quotient>0
    total+=2
    print('PASS', total, 'finite algebraic/numerical diagnostics')


if __name__ == '__main__':
    diagnostics()
