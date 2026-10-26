#!/usr/bin/env python3
"""Numerical regression tests for exact quadrupole concentration identities."""
import math
from scipy.special import beta
from scipy.integrate import quad


def eigenvalues(d, t):
    b = beta(0.5, (d - 1) / 2)
    # Substitute u=v*v to remove the removable endpoint sqrt singularity.
    def integ(fn):
        return quad(lambda v: 2 * (1 - v*v) ** ((d-3)/2) * fn(v*v),
                    math.sqrt(t), 1, epsabs=1e-12, epsrel=1e-12)[0] / b
    z = (d+2)/(2*(d-1)) * integ(lambda u:(d*u-1)**2)
    m = d*(d+2)/(d-1) * integ(lambda u:u*(1-u))
    e = d*(d+2)/((d-1)*(d+1)) * integ(lambda u:(1-u)**2)
    return z,m,e


def verify():
    for d in (3, 4, 5, 12, 20):
        b=beta(0.5, (d-1)/2)
        for t in (0.2/d, 0.7/d, 1/d, 1.4/d, 0.9):
            z,m,e = eigenvalues(d,t)
            zm=(d+2)/((d-1)*b)*(d*t-1)*math.sqrt(t)*(1-t)**((d-1)/2)
            me=2*d*(d+2)/((d-1)*(d+1)*b)*math.sqrt(t)*(1-t)**((d+1)/2)
            assert abs((z-m)-zm)<3e-10, (d,t,z,m,zm)
            assert abs((m-e)-me)<3e-10, (d,t,m,e,me)
            assert me>0
            if t<1/d: assert m>z and m>e
            if t>1/d: assert z>m and m>e
            if t==1/d: assert abs(z-m)<3e-10 and m>e
    print('Quadrupole beta integrals and exact gaps: PASS')

if __name__=='__main__':
    verify()
