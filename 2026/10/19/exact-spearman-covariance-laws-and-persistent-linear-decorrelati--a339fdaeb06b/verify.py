#!/usr/bin/env python3
"""Exact rational finite-case checks for a shuffled full-branch interval map."""
from fractions import Fraction as F
from itertools import product, permutations


def integrated_covariance(m, signs, permutation):
    """Integrate (x-1/2)*(g(x)-1/2) on each affine composition segment."""
    n = len(permutation)
    accum = F(0)
    for j, sign in enumerate(signs, 1):
        for i, destination in enumerate(permutation, 1):
            lo, hi = F(i-1, n), F(i, n)
            # x on inverse branch is a + slope * y, and the output permutation is y + shift.
            a = F(j-1, m) - F(1, 2) if sign == 1 else F(j, m) - F(1, 2)
            slope = F(sign, m)
            offset = F(destination-i, n) - F(1, 2)
            # Integral of (a+slope*y)*(y+offset), multiplied by inverse branch Jacobian 1/m.
            accum += (a*offset*(hi-lo)
                      + (a+slope*offset)*(hi*hi-lo*lo)/2
                      + slope*(hi**3-lo**3)/3) / m
    return accum


def predicted_covariance(m, signs, permutation):
    n = len(permutation)
    q = sum((F(i)-F(n+1, 2))*(F(permutation[i-1])-F(n+1, 2))
            for i in range(1, n+1))
    return F(sum(signs), m*m)*(F(1, 12*n*n)+q/n**3)


def moments(m, signs, n):
    vals = [integrated_covariance(m, signs, p)
            for p in permutations(range(1, n+1))]
    mean = sum(vals, F(0))/len(vals)
    variance = sum((z-mean)**2 for z in vals)/len(vals)
    s = sum(signs)
    expected_mean = F(s, 12*m*m*n*n)
    expected_var = F(s*s*(n*n-1)**2, 144*m**4*n**4*(n-1))
    assert mean == expected_mean and variance == expected_var, (m, signs, n)
    counts = {}
    for z in vals:
        counts[z] = counts.get(z, 0) + 1
    assert all(counts.get(2*mean-z, 0) == v for z, v in counts.items())
    if s == 0:
        assert all(z == 0 for z in vals)


def main():
    checked = 0
    for m, n in [(2,2),(2,3),(3,3),(3,4),(4,4),(4,5)]:
        for signs in product((1,-1), repeat=m):
            for permutation in permutations(range(1, n+1)):
                actual = integrated_covariance(m, signs, permutation)
                predicted = predicted_covariance(m, signs, permutation)
                assert actual == predicted, (m, signs, permutation, actual, predicted)
                checked += 1
            moments(m, signs, n)
    assert checked == 2576, checked
    print('VERIFY_OK', checked)


if __name__ == '__main__':
    main()
