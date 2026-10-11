#!/usr/bin/env python3
"""Reproduce exact four-eigenvalue numerical-radius example with stdlib only.

Finite quadrature is a sanity check; the analytic proof is in RESULT.md.
"""
import math


def defect_closed(epsilon):
    return (epsilon + (epsilon*epsilon-1.0)*math.atan(epsilon))/math.pi


def defect_quadrature(epsilon, n=65536):
    assert n % 4 == 0
    total = 0.0
    for k in range(n):
        angle = (k+0.5)*2.0*math.pi/n
        support = max(abs(math.cos(angle)), epsilon*abs(math.sin(angle)))
        total += support*support
    return total/n-0.5


def distance_exact(epsilon):
    return epsilon/math.sqrt(1.0+epsilon*epsilon)


def main():
    for e in (0.01, 0.05, 0.1, 0.3, 0.8, 1.0):
        exact = defect_closed(e)
        approx = defect_quadrature(e)
        assert abs(approx-exact)<3.0e-8, (e,exact,approx)
        assert exact+1.0e-14 >= distance_exact(e)**3/(2.0*math.pi)
        print('epsilon',e,'defect',exact,'norm_distance',distance_exact(e))
    e=1.0e-4
    assert abs(defect_closed(e)/(e**3)-4/(3*math.pi))<2.0e-4
    print('EXPLICIT_EXAMPLE_OK')


if __name__=='__main__':
    main()
