#!/usr/bin/env python3
"""Exact finite checks for radial harmonic Bergman commutator blocks.

Only standard-library Python is used. These are reproducible finite checks,
not a substitute for the analytic asymptotic proof.
"""
from fractions import Fraction
from math import comb, factorial, sqrt

def moment(m, exponent):
    """E[(1-t)^exponent] for t ~ Beta(m+1, 1), with integer exponent."""
    return Fraction(factorial(exponent) * factorial(m + 1),
                    factorial(m + exponent + 1))

def variance(m, exponent):
    return moment(m, 2 * exponent) - moment(m, exponent)**2

for exponent in (1, 2, 3):
    for m in range(40):
        direct = (m+1)*sum(
            (Fraction(((-1)**j)*comb(exponent,j),m+j+1)
             for j in range(exponent+1)), Fraction(0))
        assert direct == moment(m, exponent)
        assert variance(m, exponent)>0
    target = factorial(2*exponent)-factorial(exponent)**2
    assert target>0
    at_m=1200
    approximation=(at_m**(2*exponent))*float(variance(at_m,exponent))
    assert abs(approximation/target-1)<0.04

# Four equal-mass radial atoms; the skew commutator A=[diag(u),qq^T]
# has rank two and squared Frobenius norm exactly twice the variance.
u=[Fraction(0),Fraction(1,2),Fraction(1),Fraction(2)]
q=[Fraction(1,2)]*4
A=[[q[i]*q[j]*(u[i]-u[j]) for j in range(4)] for i in range(4)]
mean=sum((x for x in u),Fraction(0))/4
var=sum(((x-mean)**2 for x in u),Fraction(0))/4
assert sum((A[i][j]**2 for i in range(4) for j in range(4)),Fraction(0))==2*var
# An antisymmetric matrix of the form a q^T - q a^T has rank at most two.
for i in range(4):
    for j in range(4):
        assert A[i][j]==-A[j][i]
assert A[0][1]!=0
print('RADIAL_HARMONIC_BERGMAN_BLOCK_IDENTITIES_OK')
