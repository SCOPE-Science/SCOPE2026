"""Exact 2x2 and bounded numerical verification for bath-block reset formulas.

Uses only Python's standard library. General-dimension and continuous-parameter
claims are proved analytically in RESULT.md, not by this finite checker.
"""
from fractions import Fraction as F
from math import cos, sin, sqrt, exp, pi

checks = 0
# A real 2x2 fermionic covariance [[a,c],[c,b]] is a positive contraction
# exactly when its two diagonal entries lie in [0,1] and the two determinants
# (for the matrix and its complement) are nonnegative.
values = [F(k, 10) for k in range(11)]
coherences = [F(k, 20) for k in range(-10, 11)]
etas = values
for a in values:
    for b in values:
        for c in coherences:
            if c * c > a * b or c * c > (1-a) * (1-b):
                continue
            for target in values:
                for eta in etas:
                    if eta * eta <= min(target, 1-target):
                        assert eta*eta*c*c <= a*target
                        assert eta*eta*c*c <= (1-a)*(1-target)
                        checks += 2
# Exact rational pure-projector witnesses for every tested violating threshold.
for target in values:
    for eta in etas[1:]:
        q = eta * eta
        if q > target:
            p = (q-target)/(2*q)
            assert F(0) < p < 1
            det = p*(target-q*(1-p))
            assert det < 0
            checks += 1
        if q > 1-target:
            p = 1 - (q-(1-target))/(2*q)
            assert F(0) < p < 1
            det_complement = (1-p)*(1-target-q*p)
            assert det_complement < 0
            checks += 1
# All-time resonant trajectory: eigenvalue formula, endpoints and frontier.
for n in [0, 0.1, 0.25, 0.5, 0.6, 0.9, 1.0]:
    for p in [k/40 for k in range(41)]:
        d = p-n
        predicted = abs(d) <= min(n,1-n) + 1e-12
        valid = True
        for j in range(321):
            theta = 2*pi*j/320
            c=cos(theta)
            discr=sqrt(2-c*c)
            eig1=n+d*(c+discr)/2
            eig2=n+d*(c-discr)/2
            valid &= min(eig1,eig2) >= -1e-10 and max(eig1,eig2) <= 1+1e-10
            checks += 1
        assert valid == predicted,(n,p)
# Fermi--Dirac bath: correct extreme occupations and chemical-potential optimum.
for beta in [0.25,1.0,3.0,6.0]:
    for low, high in [(-2.0,2.0),(-1.0,1.0),(0.1,0.9),(1.0,1.0)]:
        midpoint=(low+high)/2
        def q(mu):
            return 1/(1+exp(beta*max(high-mu,mu-low)))
        center=q(midpoint)
        assert abs(center - 1/(1+exp(beta*(high-low)/2))) < 1e-13
        for j in range(-140,141):
            assert center >= q(midpoint+j/40)-1e-13
            checks += 1
print(f"PASS: {checks} bounded exact-arithmetic and floating-point checks")
