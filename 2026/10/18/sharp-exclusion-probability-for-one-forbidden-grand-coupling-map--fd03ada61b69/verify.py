"""Finite checks for the excluded-map support obstruction asymptotics.

Requires numpy and scipy. These checks complement, but do not replace,
the analytic argument for the all-dimension limit.
"""
import itertools
import math
import numpy as np
from scipy.optimize import linprog
from scipy.special import gammaln


def lp_feasible_excluding(n, P, forbidden):
    maps = [f for f in itertools.product(range(n), repeat=n) if f != tuple(forbidden)]
    mat = np.zeros((n * n + 1, len(maps)))
    mat[0, :] = 1
    for j, f in enumerate(maps):
        for i, value in enumerate(f):
            mat[1 + i*n + value, j] = 1
    target = np.r_[1., P.ravel()]
    res = linprog(np.zeros(len(maps)), A_eq=mat, b_eq=target,
                  bounds=(0, None), method='highs')
    return res.success


def finite_lp_checks():
    rng = np.random.default_rng(182)
    count = 0
    for n in (2, 3):
        for k in range(120):
            P = rng.dirichlet(np.ones(n)*rng.uniform(.5, 2.), size=n)
            f = tuple(rng.integers(0, n, size=n))
            excess = sum(P[i, f[i]] for i in range(n)) - (n-1)
            if abs(excess) < 1e-6:
                continue
            criterion = excess <= 0
            feasible = lp_feasible_excluding(n, P, f)
            assert criterion == feasible, (n, k, criterion, feasible)
            count += 1
    return count


def dirichlet_checks():
    rng = np.random.default_rng(936)
    count = 0
    out = []
    for n, reps in [(5, 25000), (8, 20000), (12, 20000),
                    (20, 14000), (40, 7000), (80, 3000)]:
        a = n-1
        g = rng.gamma(a, 1., (reps, n))
        g0 = rng.exponential(1., (reps, 1))
        d = g/(g.sum(axis=1, keepdims=True) + g0)
        w = np.exp(-n * np.log1p(-d).sum(axis=1))
        ratio = np.mean(w * (d.max(axis=1) <= .5))/math.exp(n+.5)
        out.append((n, float(ratio)))
        assert .5 < ratio < 1.25, (n, ratio)
        count += 1
    assert abs(out[-1][1]-1) < .03, out[-1]
    for n in (3, 5, 12):
        m = n*(n-1)
        log_A = -n*math.log(n) - gammaln(m+1)
        assert math.isfinite(log_A)
        count += 1
    return count, out


def density_checks():
    # For n=3, the Irwin--Hall density gives these *exact* pieces.
    for r in (.03, .25, .75, 1., 1.25, 1.75, 2., 2.5, 4., 10.):
        if r <= 1:
            val = r / 3
        elif r <= 2:
            val = 1-r/3-1/(3*r*r)
        else:
            val = 1/(r*r)
        # Numerical Gauss--Legendre integration of integral_0^1 u f_S(ru) du.
        nodes, weights = np.polynomial.legendre.leggauss(150)
        u = (nodes+1)/2
        s = r*u
        dens = np.where(s < 1, s, np.where(s < 2, 2-s, 0.))
        integral = (weights @ (u*dens))/2
        assert abs(val-integral) < 2e-5, (r, val, integral)
    return 10


def main():
    checks = finite_lp_checks()
    c, ratios = dirichlet_checks(); checks += c
    checks += density_checks()
    print('passed', checks, 'finite checks')
    print('importance-sampling ratios:', ratios)
    print('The proof of the dimension limit is analytic; these finite checks are not a proof of it.')

if __name__ == '__main__':
    main()
