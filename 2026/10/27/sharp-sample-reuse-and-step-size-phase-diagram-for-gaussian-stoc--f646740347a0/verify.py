"""Reproduce exact second-moment and sampling-correlation identities for a bilinear stochastic extragradient step.

No third-party packages required. This is a finite collection of algebraic tests,
not a replacement for the analytic proof of universal quantifiers.
"""
from fractions import Fraction as Q
from functools import lru_cache
from math import sqrt
import random


def joint_moment(i, j, v, c):
    """Centered Gaussian moment via the Wick/IBP recurrence; c is covariance."""
    @lru_cache(None)
    def f(i, j):
        if i < 0 or j < 0:
            return Q(0)
        if i == j == 0:
            return Q(1)
        if i:
            return (i - 1) * v * f(i - 2, j) + j * c * f(i - 1, j - 1)
        return (j - 1) * v * f(0, j - 2)
    return f(i, j)


def shifted_moment(i, j, a, v, c):
    from math import comb
    return sum((comb(i, k) * comb(j, l) * a ** (i+j-k-l) *
                joint_moment(k, l, v, c)
                for k in range(i+1) for l in range(j+1)), Q(0))


def factor(a, v, rho, t):
    """t is squared step size, all inputs rational."""
    D = a*a + (2*rho - 1)*v
    H = a**4 + (2 + 4*rho)*a*a*v + (1 + 2*rho*rho)*v*v
    return Q(1) - D*t + H*t*t


def check():
    tests = 0
    for a in [Q(1, 3), Q(1), Q(5, 2)]:
        for v in [Q(1, 7), Q(1), Q(11, 3)]:
            for rho in [Q(0), Q(1, 5), Q(1, 2), Q(4, 5), Q(1)]:
                c = rho*v
                assert joint_moment(2, 2, v, c) == v*v + 2*c*c
                assert shifted_moment(1, 1, a, v, c) == a*a+c
                assert shifted_moment(2, 0, a, v, c) == a*a+v
                H = shifted_moment(2, 2, a, v, c)
                assert H == a**4 + (2+4*rho)*a*a*v + (1+2*rho*rho)*v*v
                tests += 4
                for t in [Q(1, 100), Q(1, 9), Q(4, 3)]:
                    direct = Q(1) - 2*t*shifted_moment(1, 1, a, v, c) + t*t*H + t*shifted_moment(0, 2, a, v, c)
                    assert direct == factor(a, v, rho, t)
                    tests += 1
                for t in [Q(1, 100), Q(1, 9), Q(1, 2)]:
                    D = a*a + (2*rho-1)*v
                    assert (factor(a,v,rho,t) < 1) == (D > 0 and t < D/H)
                    tests += 1

    # Sharp partial reuse minimizer with strictly positive mean-square contraction.
    a, v, t = Q(1), Q(1, 10), Q(12,25)
    best = (Q(1)/(2*t) - a*a)/v
    assert best == Q(5,12)
    assert factor(a,v,best,t) < factor(a,v,Q(0),t)
    assert factor(a,v,best,t) < factor(a,v,Q(1),t)
    assert factor(a,v,best,t) < 1
    tests += 4

    # Correlated minibatches: B same-size batches with k shared entries.
    for B in range(1,9):
        for k in range(B+1):
            for a, tau in [(Q(1),Q(1)),(Q(1,2),Q(3)),(Q(3),Q(1,2))]:
                v = tau*tau/B
                rho = Q(k,B)
                D = a*a + (2*rho-1)*v
                assert D == a*a + Q(2*k-B,B*B)*tau*tau
                assert (D > 0) == (B*B*a*a + (2*k-B)*tau*tau > 0)
                tests += 2

    # Numerically generate correlated normal pairs and independently reconstruct
    # the squared norm of a two-stage step on the bilinear rotation field.
    rng = random.Random(73019)
    a, v, rho, eta = 0.8, 1.5, 0.65, 0.19
    z = [1.3, -0.4]
    total = 0.0
    n = 120000
    for _ in range(n):
        u, w = rng.gauss(0,1), rng.gauss(0,1)
        x = a + sqrt(v)*u
        y = a + sqrt(v)*(rho*u + sqrt(1-rho*rho)*w)
        # J=(0,1;-1,0), J^2=-I; predictor then corrector.
        pu = z[0] - eta*x*z[1]
        pv = z[1] + eta*x*z[0]
        nu = z[0] - eta*y*pv
        nv = z[1] + eta*y*pu
        total += (nu*nu + nv*nv)/(z[0]*z[0]+z[1]*z[1])
    predicted = float(factor(Q(4,5),Q(3,2),Q(13,20),Q(361,10000)))
    assert abs(total/n-predicted) < 0.02, (total/n,predicted)
    tests += 1
    return tests, total/n, predicted

if __name__ == '__main__':
    n, sample, formula = check()
    print(f'PASS {n-1} exact-rational assertions and one seeded Monte Carlo comparison')
    print(f'Empirical amplification {sample:.6f}; analytic amplification {formula:.6f}')
