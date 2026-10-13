#!/usr/bin/env python3
"""Exact finite parameter checks illustrating the analytic final-size theorem.

The infinite-time statements are proved by comparison in RESULT.md,
not by this finite test. Requires Python 3 standard library only.
"""
from fractions import Fraction as F
from math import log, pi


def bounded_root(s0, i0, beta):
    s0 = float(s0)
    i0 = float(i0)
    beta = float(beta)
    def g(x):
        return log(s0 / x) - beta * (s0 + i0 - x)
    lo, hi = s0 / 10**15, s0
    assert g(lo) > 0 and g(hi) < 0
    for _ in range(200):
        m = (lo + hi) / 2
        if g(m) > 0:
            lo = m
        else:
            hi = m
    return (lo + hi) / 2, g


def main():
    k, mu, D, hypoth_smin, interval_low, interval_width = (
        F(2), F(1), F(1), F(1,10), F(40), F(1)
    )
    # The Archimedean bound pi < 22/7 and exact (22/7)^2 < 10 give a certified lower
    # bound on the principal Dirichlet growth exponent.
    assert F(22,7)**2 < F(10)  # exact; classical Archimedes bound pi < 22/7
    assert pi < float(F(22,7))  # floating sanity check, not the proof of pi bound
    rational_lower = k*hypoth_smin*interval_low-mu-D*F(10,2*interval_width**2)
    assert rational_lower == 2
    exact_eigen_growth = float(k*hypoth_smin*interval_low-mu)-float(D)*pi*pi/(2*float(interval_width)**2)
    assert exact_eigen_growth > float(rational_lower) > 0
    print('Dirichlet sample: growth >', rational_lower)
    s0, i0, beta = F(99,100), F(1,100), F(2)
    root, g = bounded_root(s0, i0, beta)
    assert 0 < root < float(s0)
    assert abs(g(root)) < 2e-14
    assert g(root*.5) > 0
    assert g((root+float(s0))/2) < 0
    crude_lower = float(s0)*__import__('math').exp(-float(beta)*(float(s0)+float(i0)))
    assert crude_lower < root
    print('Bounded-domain final-size root:', format(root,'.15f'))
    print('CHECK: sharp-root inequalities and growth witness consistent')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
