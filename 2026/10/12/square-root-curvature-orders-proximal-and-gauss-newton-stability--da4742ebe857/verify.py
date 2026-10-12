"""Numerical checks for radial NGN/SPP stability-index ordering.

Finite tests supplement, and do not replace, the theorem's analytic proof.
"""
from math import isfinite


def values(p, r, alpha):
    f = r**p / p
    g = r**(p - 1)
    delta_ngn = (alpha * g * g / 2) / (1 + alpha * g * g / (2 * f))
    if p == 1:
        y = max(0., r-alpha)
    else:
        lo, hi = 0., r
        for _ in range(125):
            m = (lo+hi)/2
            if m + alpha * m**(p-1) < r:
                lo = m
            else:
                hi = m
        y = (lo+hi)/2
    min_prox = y**p/p + (r-y)**2/(2*alpha)
    delta_spp = f-min_prox
    return delta_spp, delta_ngn, y


if __name__ == '__main__':
    checks=0
    for p in [1.,1.125,1.25,1.5,1.75,1.9,2.,2.1,2.5,3.,4.,6.,8.]:
        for r in [0.125,0.25,0.5,1.,2.,4.]:
            for alpha in [0.001,0.01,0.1,0.3,1.,3.,10.,100.,1000.]:
                d_spp,d_ngn,y=values(p,r,alpha)
                assert isfinite(d_spp) and isfinite(d_ngn)
                tol=1.e-11 * max(1.,abs(d_spp),abs(d_ngn))
                if p < 2:
                    assert d_spp >= d_ngn-tol, (p,r,alpha,d_spp,d_ngn)
                elif p > 2:
                    assert d_spp <= d_ngn+tol, (p,r,alpha,d_spp,d_ngn)
                else:
                    assert abs(d_spp-d_ngn)<=tol
                checks+=1
    # Exact p=1 instance: f(y)=abs(y), x=1, alpha=1.
    assert values(1.,1.,1.)[:2] == (0.5,1/3)
    print('VERIFY_OK',checks,'cases; exact linear witness')
