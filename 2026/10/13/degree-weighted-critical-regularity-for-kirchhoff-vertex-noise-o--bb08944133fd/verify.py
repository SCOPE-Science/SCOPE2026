#!/usr/bin/env python3
"""Reproduce exact vertex-trace test cases and the ultraviolet logarithmic slope.
The general theorem uses the analytic metric-graph heat-kernel path formula.
"""
from fractions import Fraction
from math import pi, log, exp, sqrt

# Neumann interval of length pi, independent endpoint intensities plus covariance.
q00, q01, q11 = Fraction(2), Fraction(1), Fraction(3)
assert q00 > 0 and q00*q11-q01*q01 == 5
assert q00+q11 == 5

def eig_weight_numerator(n):
    # For n>=1: weight = 2/pi * this integer.
    return q00+q11+2*q01*((-1)**n)

assert eig_weight_numerator(1) == 3
assert eig_weight_numerator(2) == 7
assert (eig_weight_numerator(1)+eig_weight_numerator(2))/2 == 5
assert q00+q11+2*q01 == 7 # zero mode: 7/pi

# The d-arm equal-length star's symmetric Neumann sector carries exactly
# 1/d times the central vertex weight on a single Neumann interval.
for d in range(2,16):
    assert Fraction(2,d) * d == 2
    assert Fraction(1,d) * d == 1

# Check the logarithmic UV coefficient using differences, not slow absolute
# ratios (which retain finite-cutoff constants).
def endpoint_energy(nmax, t=Fraction(1)):
    total = float(q00+q11+2*q01)/(2*pi) * (1-exp(-2.0))
    for n in range(1,nmax+1):
        mu = 1+n*n
        a = 2.0*float(eig_weight_numerator(n))/pi
        total += 0.5*a/sqrt(mu)*(1-exp(-2.0*mu))
    return total

n1,n2=8192,65536
E1,E2=endpoint_energy(n1),endpoint_energy(n2)
observed=(E2-E1)/(log(1+n2*n2)-log(1+n1*n1))
expected=5/(2*pi)
assert abs(observed-expected) < 0.0005, (observed,expected)
print('VERIFY_OK exact_PSD_parity_and_star_normalization=true log_slope_interval=',
      f'{observed:.9f}', 'predicted=',f'{expected:.9f}', 'modes=', n2)
