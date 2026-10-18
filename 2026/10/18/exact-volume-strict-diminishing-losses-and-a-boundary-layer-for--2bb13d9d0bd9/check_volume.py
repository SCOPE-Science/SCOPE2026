#!/usr/bin/env python3
"""Exact independent lattice-point cross-check of two-level hub-metric volumes.

Scales all coordinates by the denominator of the rational distance, enumerates
integer points in the dilated Lipschitz polytope, and extracts the leading
Ehrhart coefficient by finite differences. No floating-point arithmetic.
"""
from fractions import Fraction
from math import comb, factorial


def predicted(n, k, t):
    return 1 + n*(2*t-1) + Fraction(2*(n-k), k+1)*(1-t**(k+1))


def lattice_points(n, k, t, dilate):
    den = t.denominator
    sizes = [int(t*den*dilate)]*k + [den*dilate]*(n-k)
    window = den*dilate
    def count(i, low, high):
        if i == n:
            return 1
        total = 0
        for value in range(-sizes[i],sizes[i]+1):
            newlow = min(low, value)
            newhigh = max(high, value)
            if newhigh-newlow <= window:
                total += count(i+1,newlow,newhigh)
        return total
    return count(0,0,0)


def check(n,k,t):
    data = [lattice_points(n,k,t,dil) for dil in range(n+1)]
    coefficient = Fraction(sum((-1)**(n-i)*comb(n,i)*data[i]
                               for i in range(n+1)), factorial(n)*t.denominator**n)
    expectation = predicted(n,k,t)
    assert coefficient == expectation, (n,k,t,coefficient,expectation)
    return f"n={n}, k={k}, t={t}, volume={expectation}, scaled Ehrhart data={data}"


if __name__ == '__main__':
    cases = [(3,1,Fraction(1,2)),(3,2,Fraction(1,2)),(3,3,Fraction(1,2)),
             (3,2,Fraction(2,3)),(4,1,Fraction(1,2)),(4,2,Fraction(1,2)),
             (4,3,Fraction(1,2)),(4,4,Fraction(1,2)),(4,2,Fraction(2,3)),
             (4,3,Fraction(2,3)),(4,2,Fraction(3,4)),(5,2,Fraction(1,2)),
             (5,3,Fraction(1,2)),(5,4,Fraction(1,2)),(5,5,Fraction(1,2))]
    for case in cases:
        print(check(*case))
    print(f"PASS: {len(cases)} exact Ehrhart-leading-coefficient tests")
