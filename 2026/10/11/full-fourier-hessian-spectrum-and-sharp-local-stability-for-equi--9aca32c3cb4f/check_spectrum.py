#!/usr/bin/env python3
"""Finite-dimensional consistency checks of the analytic Hessian-spectrum formulas.

Python standard library only. These finite checks are not a proof for all N.
"""
import cmath
import math


def curvature(theta):
    z = cmath.exp(1j * theta)
    return -1.0 - 2.0 * (z.conjugate() * cmath.log(1.0 - z)).real


def pair_potential(theta):
    z = cmath.exp(1j * theta)
    return 2.0 * (1.0 + (z.conjugate() - 1.0) * cmath.log(1.0-z)).real


def eigen_from_hessian(n, s):
    return 2.0 * sum(
        curvature(2.0 * math.pi * r/n) *
        (1.0 - math.cos(2.0 * math.pi * s * r/n))
        for r in range(1, n)
    )


def eigen_from_poisson(n, s, intervals=8192):
    # Simpson quadrature, inclusive endpoints; at t=1 the continuous limit is 0.
    def integrand(t):
        if t == 1.0:
            return 0.0
        return (1.0-t**s)*(1.0-t**(n-s))/(1.0-t**n)
    h = 1.0/intervals
    accum = integrand(0.0)+integrand(1.0)
    for k in range(1, intervals):
        accum += (4 if k%2 else 2)*integrand(k*h)
    return 2.0*n*accum*h/3.0


def energy(angles):
    n=len(angles)
    return 2.0*n+2.0*sum(
        pair_potential(angles[j]-angles[i])
        for i in range(n) for j in range(i+1,n)
    )


def test():
    for n in (2,3,4,5,8,12,23):
        ev=[]
        for s in range(1,n):
            direct=eigen_from_hessian(n,s)
            integral=eigen_from_poisson(n,s)
            assert abs(direct-integral)<2e-7,(n,s,direct,integral)
            assert direct>0
            ev.append(direct)
        # The exact smallest and largest Fourier modes.
        assert abs(min(ev)-eigen_from_hessian(n,1))<1e-10
        assert abs(max(ev)-eigen_from_hessian(n,n//2))<1e-10

    for n,s in ((2,1),(3,1),(5,1),(8,1),(9,2)):
        angles=[2.0*math.pi*j/n for j in range(n)]
        direction=[math.cos(2.0*math.pi*s*j/n) for j in range(n)]
        avg=sum(direction)/n
        direction=[v-avg for v in direction]
        norm2=sum(v*v for v in direction)
        t=0.0005
        ep=energy([a+t*v for a,v in zip(angles,direction)])
        em=energy([a-t*v for a,v in zip(angles,direction)])
        e0=energy(angles)
        observed=(ep+em-2.0*e0)/(t*t*norm2)
        claimed=eigen_from_hessian(n,s)
        assert abs(observed-claimed)<2e-5,(n,s,observed,claimed)
    print('PASS: Poisson integral, direct Hessian, modal extrema, finite differences')


if __name__=='__main__':
    test()
