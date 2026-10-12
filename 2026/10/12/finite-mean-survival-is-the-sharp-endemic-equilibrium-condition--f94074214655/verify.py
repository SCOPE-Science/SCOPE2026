#!/usr/bin/env python3
"""Exact algebra checks for a finite-mean age-survival stationary criterion.

The analytic infinite-age proof and conditional convolution limit are in RESULT.md.
This small checker verifies identities and rational witnesses only.
"""
from fractions import Fraction as F


def equilibrium(psi, sigma):
    # All constant rates (other than recruitment psi) are set equal to 1.
    d = F(1) + F(1, 2)
    reproduction = psi * sigma / d
    assert reproduction > 1
    T = psi / reproduction
    V = reproduction - 1
    A = V
    L = A / 2
    J = T * V
    assert psi - T - J == 0
    assert J * sigma - (2 * A - L) == 0
    assert A - 2 * L == 0
    assert A - V == 0
    assert J == psi * (1 - 1 / reproduction)
    return reproduction, T, A, L, V, J


def power_law_mean(k):
    # The exact improper integral of (1+a)^(-k).
    return F(1, 1) / (k - 1) if k > 1 else None


def main():
    # Source-admissible positive bounded integrable hazard s=(log 2)*exp(-a).
    # Its total cumulative hazard is log 2 and sigma=1-exp(-log 2)=1/2.
    assert equilibrium(F(6), F(1, 2)) == (F(2), F(3), F(1), F(1, 2), F(1), F(3))
    # For s=k/(1+a), every k>0 has sigma=1, but only k>1 has finite mean.
    assert equilibrium(F(3), F(1)) == (F(2), F(3, 2), F(1), F(1, 2), F(1), F(3, 2))
    assert power_law_mean(F(1, 2)) is None
    assert power_law_mean(F(1)) is None
    assert power_law_mean(F(2)) == 1
    assert power_law_mean(F(3, 2)) == 2
    assert F(3, 2) * power_law_mean(F(3, 2)) == 3
    # At k>1, the same reproduction number carries a finite mass 3/[2(k-1)].
    for k in (F(5, 4), F(3, 2), F(2), F(3)):
        assert F(3, 2) * power_law_mean(k) == F(3, 2) / (k - 1)
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
