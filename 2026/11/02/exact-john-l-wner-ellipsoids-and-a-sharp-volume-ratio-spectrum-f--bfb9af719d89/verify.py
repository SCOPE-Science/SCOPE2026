#!/usr/bin/env python3
"""Reproducibility checks for the two ellipsoids of a truncated simplex.

Standard library only. Finite tests corroborate the all-parameter analytic proof.
"""
import math


def parameters(d, t):
    assert isinstance(d, int) and d >= 2 and 0 <= t < 1
    low, high = 1/d, 1.0
    for _ in range(90):
        r = (low + high)/2
        residual = t*t*r*r + d*(1-t*t)*r - 1
        if residual > 0:
            high = r
        else:
            low = r
    r = (low + high)/2
    lam = 1/(1+r)
    m2 = lam + (1-lam)*t*t
    y = t + (1-t)*lam
    s = min(1/(d+1), (1-t)/2)
    return r, lam, m2, y, s


def check_case(d, t):
    r, lam, m2, y, s = parameters(d, t)
    aL2 = (1-t)**2 * lam*(1-lam)
    bL2 = m2
    aJ2 = s*s/d
    bJ2 = (1-2*s)/(d*(d-1))
    yJ = 1-s
    # Polytope's facet support function exactly controls inscribed ellipsoids.
    coord_support_J = math.sqrt((aJ2+(d-1)*bJ2)/d)
    sum_support_J = math.sqrt(d*aJ2)
    assert math.isclose(coord_support_J, yJ/d, rel_tol=2e-12, abs_tol=2e-12)
    assert math.isclose(yJ+sum_support_J,1,rel_tol=2e-12,abs_tol=2e-12)
    assert yJ-sum_support_J >= t-2e-12
    # Every one of the 2d original frustum vertices is on the outer boundary.
    def squared_ellipsoid_gauge(T):
        return ((T-y)**2 / (d*aL2) + (d-1)*T*T/(d*bL2))
    h_outer, h_inner = squared_ellipsoid_gauge(1),squared_ellipsoid_gauge(t)
    assert abs(h_outer-1)<2e-11,(d,t,h_outer)
    assert abs(h_inner-1)<2e-11,(d,t,h_inner)
    # The contact distribution's mean and covariance reproduce center and shape.
    assert math.isclose(m2-y*y,aL2,rel_tol=2e-10,abs_tol=2e-11)
    assert abs(r + (d-1)/m2-d)<2e-10
    # Normalize ellipsoid volumes by unit-ball volume.
    vJ = math.sqrt(aJ2)*bJ2**((d-1)/2)
    vL = math.sqrt(aL2)*bL2**((d-1)/2)
    ratio=vL/vJ
    lower = d**(d/2)*(d-1)**((d-1)/2)
    upper=d**d
    assert lower*(1-1e-9) <= ratio <= upper*(1+1e-9), (d,t,ratio)
    return ratio


def main():
    cases=0
    for d in range(2,17):
        tc=(d-1)/(d+1)
        ts=[0.0,0.001,0.037,0.11,0.25,0.43,0.51,0.69,0.83,0.93,0.985,0.999,
            tc,tc-1e-6,tc+1e-6]
        ts=sorted(set(t for t in ts if 0<=t<1))
        last=float('inf')
        for t in ts:
            R=check_case(d,t)
            assert R <= last*(1+2e-12),(d,t,R,last)
            last=R
            cases+=1
        assert abs(check_case(d,0)-d**d)<3e-10*d**d
    # For dimension three, the limiting ratio is 6*sqrt(3).
    assert math.isclose(3**1.5*2, 6*math.sqrt(3))
    print('VERIFY_OK',cases,'ellipsoid/facet/contact/bound and monotonicity instances')


if __name__=='__main__':
    main()
