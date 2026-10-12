#!/usr/bin/env python3
"""Reproduce exact algebraic identities and numerical checks for the two-dimensional
one-node Lanczos log-determinant risk law. No third-party packages are required.
Numerical quadrature and finite sampling are corroboration, not infinite proofs.
"""
from fractions import Fraction
from math import cos, cosh, log, pi, sin, sqrt, tanh, asin
from itertools import permutations


def li2(z):
    assert 0 <= z < 1
    if z > 0.70:
        # Numerically stable Euler reflection for z near 1.
        return pi*pi/6-log(z)*log(1-z)-li2(1-z)
    result = 0.0
    power = z
    n = 1
    while True:
        incr = power / (n*n)
        result += incr
        if incr < 1.e-16:
            return result
        power *= z
        n += 1
        assert n < 200000


def exact_theory(kappa):
    assert kappa > 1
    h = log(kappa)/4
    k = tanh(h)
    bias = 4*log(cosh(h))
    return bias, 2*li2(k**4), 4*li2(k**2)


def angular_moments(kappa, n=32768):
    sums = [0., 0., 0., 0., 0.]
    for i in range(n):
        theta = pi*(i+.5)/n
        r = kappa*cos(theta)**2 + sin(theta)**2
        s = kappa*sin(theta)**2 + cos(theta)**2
        log_r, log_s = log(r), log(s)
        t = log_r + log_s
        sums[0] += t
        sums[1] += t*t
        sums[2] += log_r
        sums[3] += log_r*log_r
        sums[4] += log_r*log_s
    means = [x/n for x in sums]
    anti_mean = means[0]
    anti_var = means[1] - anti_mean*anti_mean
    iid_var = 2*(means[3]-means[2]*means[2])
    return anti_mean-log(kappa), anti_var, iid_var


def exact_identity_checks():
    count = 0
    for lam_num in [2, 3, 4, 7, 11]:
        for mu_num in [1, 2, 3]:
            if lam_num <= mu_num:
                continue
            lam, mu = Fraction(lam_num), Fraction(mu_num)
            for p in range(0, 21):
                u = Fraction(p, 20)
                r = lam*u+mu*(1-u)
                s = lam*(1-u)+mu*u
                assert r*s == lam*mu+(lam-mu)**2*u*(1-u)
                count += 1
    return count


def antithetic_discrete_optimality_checks():
    # Exact swap inequality for every permutation of a discrete increasing
    # transformed marginal; finite checks are illustrative only.
    count = 0
    for n in [3, 4, 5, 6]:
        x = [Fraction(1+j, n+1) for j in range(n)]
        opposite = sum(x[i]*x[n-1-i] for i in range(n))
        for pp in permutations(range(n)):
            candidate = sum(x[i]*x[pp[i]] for i in range(n))
            assert candidate >= opposite
            count += 1
    return count


def distribution_checks():
    # The beta(1/2,1/2) CDF transforms exactly into the claimed log-error CDF.
    count = 0
    for kap in [1.1, 2, 4, 10, 100]:
        t = (kap-1)**2/(4*kap)
        for q in [0.01, 0.1, 0.25, .5, .75, .9, .99]:
            w = sin(pi*q/2)**2
            xi = log(1+t*w)
            probability = 2*asin(sqrt((__import__('math').exp(xi)-1)/t))/pi
            assert abs(probability-q) < 5e-10, (kap,q,probability)
            count += 1
    return count


def main():
    nc = exact_identity_checks()
    no = antithetic_discrete_optimality_checks()
    nd = distribution_checks()
    nn = 0
    for kap in [1.001, 1.01, 1.2, 2., 4., 10., 100.]:
        bias, v_anti, v_iid = exact_theory(kap)
        num_bias, num_anti, num_iid = angular_moments(kap)
        assert abs(bias-num_bias) < 1e-10, (kap,bias,num_bias)
        assert abs(v_anti-num_anti) < 1e-10, (kap,v_anti,num_anti)
        assert abs(v_iid-num_iid) < 1e-10, (kap,v_iid,num_iid)
        assert 0 < v_anti < v_iid
        nn += 3
    for t in [0.00001, 0.0001, 0.001]:
        bias,v_anti,v_iid=exact_theory(__import__('math').exp(t))
        assert abs((v_anti+bias*bias)/(t**4)-(3/128))<0.0001
        assert abs((v_iid+bias*bias)/(t*t)-0.25)<0.0001
    print('PASS exact-rational Rayleigh product identities:',nc)
    print('PASS exhaustive finite-grid antithetic rearrangement checks:',no)
    print('PASS transformed arcsine CDF checks:',nd)
    print('PASS independent midpoint quadrature moment comparisons:',nn)
    print('PASS small-contrast leading coefficient checks: 6')
    print('These checks supplement but do not replace the analytic proof.')

if __name__ == '__main__':
    main()
