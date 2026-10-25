#!/usr/bin/env python3
"""Independent finite checks for the signohedron support and fluctuation formulas.
This program supplies finite diagnostics; it is not a substitute for an asymptotic proof.
Requires NumPy and SciPy. Usage: python verify.py
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq, linprog
from scipy.stats import norm

RNG = np.random.default_rng(20261018)

def analytic_support_and_rank(g):
    y = np.sort(np.abs(g))[::-1]
    v = np.cumsum(y) / np.arange(2, len(y) + 2)
    k = int(np.argmax(v)) + 1
    return float(v[k - 1]), k

def independent_linear_program(g):
    d = len(g)
    # decision variables x[0:d], t[d:2d], m[2d];
    # t_i >= |x_i|, m >= |x_i|, sum(t_i)+m <= 1.
    constraints = []
    rhs = []
    for i in range(d):
        for variable, sign in ((d+i, 1.0), (2*d, 1.0)):
            row = np.zeros(2*d + 1)
            row[i] = 1.0
            row[variable] = -sign
            constraints.append(row)
            rhs.append(0.0)
            row = np.zeros(2*d + 1)
            row[i] = -1.0
            row[variable] = -sign
            constraints.append(row)
            rhs.append(0.0)
    row = np.zeros(2*d + 1)
    row[d:] = 1.0
    constraints.append(row)
    rhs.append(1.0)
    objective = np.zeros(2*d + 1)
    objective[:d] = -np.asarray(g)
    result = linprog(objective, A_ub=np.array(constraints), b_ub=np.array(rhs),
                     bounds=[(None, None)]*d + [(0, None)]*(d+1), method='highs')
    assert result.success, result.message
    return -float(result.fun)

def root_t(d):
    return brentq(lambda t: 2*d*(norm.pdf(t) - t*norm.sf(t)) - t, 0.01, max(8, 2*math.sqrt(math.log(d))))

def main():
    lp_checks = 0
    fixed_point_checks = 0
    rank_checks = 0
    for d in range(2, 9):
        for _ in range(15):
            g = RNG.normal(size=d)
            h, k = analytic_support_and_rank(g)
            hp = independent_linear_program(g)
            assert abs(h-hp) < 1.0e-9, (d,h,hp)
            lp_checks += 1
            residual = np.maximum(np.abs(g)-h, 0).sum()-h
            assert abs(residual) < 1.0e-9, (d,residual)
            fixed_point_checks += 1
            assert k == int(np.count_nonzero(np.abs(g)>h)), (d,k,h)
            rank_checks += 1
    quadratures = 0
    for t in [0.5, 1.0, 2.0, 3.0, 4.0]:
        m1 = 2*(norm.pdf(t)-t*norm.sf(t))
        m2 = 2*((1+t*t)*norm.sf(t)-t*norm.pdf(t))
        for power, reference in [(1,m1),(2,m2)]:
            integral = quad(lambda y:2*norm.pdf(y)*(y-t)**power,t,np.inf,epsabs=2e-13)[0]
            assert abs(integral-reference) <= 5e-11, (t,power,integral,reference)
            quadratures += 1
    exact_identity_checks = 0
    for d in [100, 1000, 10000, 100000, 1000000]:
        t = root_t(d)
        p = 2*norm.sf(t)
        m2 = 2*((1+t*t)*norm.sf(t)-t*norm.pdf(t))
        assert abs(d*m2-(d*p-t*t)) < 2e-7
        exact_identity_checks += 1
    # The finite-dimensional CLT covariance is not the limiting covariance.
    # Report, rather than assert, the empirical distributional diagnostics.
    obs = []
    for _ in range(1000):
        d = 10000
        g = RNG.normal(size=d)
        h,k = analytic_support_and_rank(g)
        t = root_t(d)
        obs.append((t*t*(h-t), (k-t*t)/t))
    arr = np.asarray(obs)
    mu = np.mean(arr,axis=0)
    cov = np.cov(arr,rowvar=False)
    assert np.isfinite(cov).all() and cov[0,1]<0
    print('VERIFY_OK lp=',lp_checks,'fixed_points=',fixed_point_checks,
          'exposed_ranks=',rank_checks,'quadratures=',quadratures,
          'moment_identities=',exact_identity_checks)
    print('FINITE_DIAGNOSTIC d=10000 replicates=1000 mean=',np.round(mu,3),
          'covariance=',np.round(cov,3).tolist())
    print('ASYMPTOTIC_TARGET_COVARIANCE=[[2,-1],[-1,1]] (not a finite exact identity)')

if __name__ == '__main__':
    main()
