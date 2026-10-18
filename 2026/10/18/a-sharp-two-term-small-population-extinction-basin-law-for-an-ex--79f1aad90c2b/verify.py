#!/usr/bin/env python3
"""Reproduce the two deterministic small-population basin coefficients.

No external libraries; finite numerical trajectories are not proofs.
"""
from math import exp


def bisect(fun, lo, hi, iterations=90):
    flo, fhi = fun(lo), fun(hi)
    assert flo * fhi < 0
    for _ in range(iterations):
        mid = (lo + hi) / 2
        fm = fun(mid)
        if (fm > 0) == (flo > 0):
            lo, flo = mid, fm
        else:
            hi, fhi = mid, fm
    return (lo + hi) / 2


def coefficients(a, b, d, alpha):
    def F(z):
        return (b + a*z)*exp(-alpha*z) - (d+1)
    zm = 1/alpha - b/a
    assert zm > 0 and F(0) < 0 < F(zm)
    hi = 2*zm + 1
    while F(hi) > 0:
        hi *= 2
    low = bisect(F, 0, zm)
    high = bisect(F, zm, hi)
    q = exp(-alpha*low)
    lu = b*q-d
    lz = low*q*(a-alpha*(b+a*low))
    k = low/(lu-lz)
    assert lu < 0 < lz and k < 0
    fp = q*(a-alpha*(b+a*low))
    fpp = q*(-2*alpha*a+alpha*alpha*(b+a*low))
    ap = -a*q*(1-alpha*low)
    eta = (k*(fp*k+2) + (0.5*low*fpp-ap)*k*k)/(2*lu-lz)
    if low <= 1:
        p0, p1 = 1-low/2, -k/3
    else:
        p0, p1 = 1/(2*low), -k/(3*low**3)
    return low, high, k, eta, p0, p1


def trajectory(a, b, d, alpha, u, z, dt=0.02, horizon=140):
    def f(u, z):
        q = exp(-alpha*z)
        return (u*(1-u-a*z*q), z*((b+a*z)*q-(d+1)+u))
    for _ in range(round(horizon/dt)):
        p, r = f(u, z)
        p2, r2 = f(u+dt*p/2, z+dt*r/2)
        p3, r3 = f(u+dt*p2/2, z+dt*r2/2)
        p4, r4 = f(u+dt*p3, z+dt*r3)
        u += dt*(p+2*p2+2*p3+p4)/6
        z += dt*(r+2*r2+2*r3+r4)/6
        assert u >= 0 and z >= 0
    return u, u*z


if __name__ == '__main__':
    for parameters in [(6, 0.5, 1, 1), (1.5, 0.5, 1, 0.2)]:
        a,b,d,alpha=parameters
        low, high, k, eta, p0, p1=coefficients(*parameters)
        print('parameters',parameters)
        print('roots',low,high,'curvature',k,'quadratic slope',eta)
        print('P(eps)=',p0,'+',p1,'* eps + O(eps^2)')
        for delta in (-0.003, 0.003):
            u0=0.002
            z0=low+k*u0+eta*u0*u0+delta
            outcome=trajectory(a,b,d,alpha,u0,z0)
            print('  delta',delta,'terminal (u,v)',outcome)
            assert outcome[0] > 0.99 if delta < 0 else outcome[0] < 1e-10
