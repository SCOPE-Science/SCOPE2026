#!/usr/bin/env python3
"""Numerical cross-checks for the two-deme Poisson branching survival theorem.

Uses elementary arithmetic only. These checks do not replace the analytical proof.
"""
import math


def survival(lam, s, d, tol=3e-14):
    assert lam > 1 and 0 < s < 2 and abs(d) < min(s, 2-s)
    a, b = (s-d)/2, (s+d)/2
    x = y = 1.0
    for _ in range(300000):
        xn = -math.expm1(-lam*((1-a)*x+b*y))
        yn = -math.expm1(-lam*(a*x+(1-b)*y))
        if max(abs(xn-x), abs(yn-y)) < tol:
            return xn, yn
        x, y = xn, yn
    raise AssertionError('Fixed point iteration did not converge')


def derivative(lam, s, d):
    x, y = survival(lam, s, d)
    a, b = (s-d)/2, (s+d)/2
    D1, D2 = 1-x, 1-y
    A11, A12 = 1-lam*D1*(1-a), -lam*D1*b
    A21, A22 = -lam*D2*a, 1-lam*D2*(1-b)
    det = A11*A22-A12*A21
    assert det > 0
    mean_der = lam*(x+y)*(y-x)/(4*det)
    first_der = lam*(x+y)*D1*(1-lam*D2)/(2*det)
    return mean_der, first_der


def test():
    count = 0
    for lam in (1.2, 1.5, 2., 4.):
        for s in (.15, .6, 1., 1.5):
            limit = min(s, 2-s)
            for j in range(1, 10):
                d = limit*j/10
                x, y = survival(lam, s, d)
                assert 0 < y < x < 1
                z, w = survival(lam, s, -d)
                assert abs(x-w) < 3e-12 and abs(y-z) < 3e-12
                m0 = sum(survival(lam, s, d - 1.e-5))/2
                m1 = sum(survival(lam, s, d + 1.e-5))/2
                observed = (m1-m0)/(2.e-5)
                predicted, _ = derivative(lam, s, d)
                assert predicted < 0
                assert abs(observed-predicted) < 5.e-7, (lam, s, d, observed, predicted)
                count += 1
    # Independent implicit scalar optimum equation for the fully redistributed case.
    for lam in (1.2, 1.5, 2., 4.):
        lo, hi = math.log(lam), 2*lam + math.log(lam) + 2
        def f(x): return x + lam*math.exp(-x) - (2*lam-1-math.log(lam))
        assert f(lo) < 0 < f(hi)
        for _ in range(100):
            mid = (lo+hi)/2
            if f(mid) < 0: lo = mid
            else: hi = mid
        x = (lo+hi)/2
        d = (x-math.log(lam))/(x+math.log(lam))
        q1,q2 = survival(lam, 1., d)
        assert abs(q2-(1-1/lam)) < 2e-12
        assert abs(q1-(1-math.exp(-x))) < 2e-12
        _, dq1 = derivative(lam, 1., d)
        assert abs(dq1) < 2e-11
        for eps in (.01,.02):
            assert survival(lam, 1., d-eps)[0] < q1
            assert survival(lam, 1., d+eps)[0] < q1
        count += 1
    # Quadratic curvature about symmetric migration, computed independently.
    lam,s = 2.,1.
    p = 1-survival(lam,s,0)[0]
    q = 1-p
    z = lam*p
    C = lam**2*q**2*p/(2*(1-z)*(1-z*(1-s))**2)
    h=0.001
    empirical = (q-sum(survival(lam,s,h))/2)/h**2
    assert abs(empirical-C) < 0.0002
    print('CHECK_OK', count)

if __name__ == '__main__':
    test()
