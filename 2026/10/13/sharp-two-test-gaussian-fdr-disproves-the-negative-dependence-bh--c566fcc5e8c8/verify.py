#!/usr/bin/env python3
"""Reproduce rational inequalities and independent Gaussian-threshold diagnostics."""
from fractions import Fraction as F
from statistics import NormalDist
from math import sqrt

alpha = F(1, 20)
rho = -F(99999999, 100000000)
eps = F(1, 200)
var_diff = 2 * (1 + rho)
cheb = var_diff / (eps * eps)
change_bound = eps + cheb
fdr_limit = 3 * alpha / 4
fdr_rigorous_lower = fdr_limit - change_bound
assert var_diff == F(1, 50000000)
assert cheb == F(1, 1250)
assert change_bound == F(29, 5000)
assert fdr_rigorous_lower == F(317, 10000)
# From e < 3 and sqrt(8*pi) > 4, at alpha = 1/20.
s_upper_rational = alpha + 2*alpha**2 + F(9,2)*alpha**3 + F(81,4)*alpha**4/(1-3*alpha)
assert s_upper_rational == F(30307, 544000)
assert fdr_rigorous_lower > s_upper_rational / 2
assert fdr_limit == F(3, 80)

# Check exact normal-CDF threshold relation of the singular extremizer.
phi=NormalDist().cdf
q=NormalDist().inv_cdf
a=float(q(float(alpha/2))+q(float(alpha)))
mu=-a
assert mu>0
cut=float(q(float(alpha/2)))
for z in [-4,-3,-2.1,-2,-1.97,-1.95,-1,0,1,2]:
    U=phi(z)
    V=phi(-z+a)
    assert (V <= float(alpha)) == (U >= float(alpha/2))

# Independent deterministic finite-grid quadrature, diagnostic only.
# Conditional normal expectation for corr rho with Y1=-Z, Y2=rho*(-Z)+noise+mu.
# FDR = alpha/2 + [int_mid P(V<=alpha|U=u) du - int_low P(V<=alpha|U=u) du]/2.
# Use corr=-.99 to keep numerical conditioning modest; the rational witness
# uses rho=-.99999999 and is certified by the analytic probability inequality.
rnum=-0.99
sd=sqrt(1-rnum*rnum)
qalpha=q(float(alpha))
def prob_v_le_alpha(u):
    z=q(u)
    mu_cond= -rnum*z+mu
    return phi((mu_cond+qalpha)/sd)
def midpoint(lo,hi,n=10000):
    step=(hi-lo)/n
    return step*sum(prob_v_le_alpha(lo+(i+0.5)*step) for i in range(n))
low=midpoint(0.,float(alpha/2))
mid=midpoint(float(alpha/2),float(alpha))
fdr_numeric=float(alpha)/2+(mid-low)/2
assert 0.03<fdr_numeric<0.0375
print('OK exact: alpha',alpha,'rho',rho,'mu',mu)
print('OK exact: universal upper',fdr_limit)
print('OK exact: P(disagreement) <',change_bound)
print('OK exact: nonsingular FDR >',fdr_rigorous_lower)
print('OK exact: conjecture RHS <',s_upper_rational/2)
print('OK exact: gap >',fdr_rigorous_lower-s_upper_rational/2)
print('diagnostic FDR at rho=-.99:',round(fdr_numeric,10))
