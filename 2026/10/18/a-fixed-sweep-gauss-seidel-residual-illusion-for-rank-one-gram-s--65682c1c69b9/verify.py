#!/usr/bin/env python3
"""Reproduce the fixed-sweep rank-one Gram example using only Python stdlib."""
import math
from fractions import Fraction


def fgs_sweep(x, a):
    old_total = sum(x)
    prefix = 0.0
    suffix = old_total
    y = []
    for z in x:
        suffix -= z
        v = (1.0 - a * (prefix + suffix)) / (1.0 + a)
        y.append(v)
        prefix += v
    return y


def infinite_gamma(a, sweeps, terms=1200):
    q = 1.0 / (1.0 + a)
    c = a / (1.0 + a)
    return a * sum((q ** j * c ** (sweeps - 1) *
                     math.comb(j + sweeps - 2, sweeps - 1)) ** 2
                    for j in range(1, terms + 1))


def measurements(x, a):
    n = len(x)
    sx = sum(x)
    d = 1.0 - a * sx
    rel_gram_residual = math.sqrt(sum((d-v)**2 for v in x) / n)
    physical_remaining_fraction = d*d + a*sum(v*v for v in x)
    best_possible_fraction = 1.0 / (1.0 + a*n)
    relative_energy_gap = ((physical_remaining_fraction-best_possible_fraction)
                           / (1.0-best_possible_fraction))
    return rel_gram_residual, physical_remaining_fraction, relative_energy_gap


def exact_small_check():
    for n in range(1, 15):
        for a in (Fraction(1, 3), Fraction(1), Fraction(5, 2)):
            q = 1/(1+a)
            previous_sum = Fraction(0)
            solution=[]
            for j in range(1, n+1):
                x=(1-a*previous_sum)/(1+a)
                solution.append(x); previous_sum+=x
                assert x == q**j
            gram_residual=[1-solution[i]-a*sum(solution) for i in range(n)]
            assert gram_residual == [q**n-q**(i+1) for i in range(n)]
    print('exact Fraction checks: all 42 small one-sweep systems passed')


def limits_check():
    for a in (0.2,1.,3.):
        assert abs(infinite_gamma(a,1) - 1/(a+2)) < 1.e-13
        assert abs(infinite_gamma(a,2) - ((a+1)**2+1)/(a+2)**3) < 1.e-12
        n=8192
        x=[0.] * n
        for v in range(1,6):
            x=fgs_sweep(x,a)
            delta, physical, gap=measurements(x,a)
            gamma=infinite_gamma(a,v)
            assert abs(physical-gamma) < 6.e-3, (a,v,physical,gamma)
            assert abs(gap-gamma) < 6.e-3, (a,v,gap,gamma)
            assert abs(n*delta*delta-gamma/a) < 6.e-3, (a,v,n*delta*delta,gamma/a)
            print('a={:.1f} sweeps={} n={} residual={:.6g} outer_fraction={:.6g} limit={:.6g}'.format(a,v,n,delta,physical,gamma))

if __name__ == '__main__':
    exact_small_check()
    limits_check()
    print('ALL_CHECKS_PASSED')
