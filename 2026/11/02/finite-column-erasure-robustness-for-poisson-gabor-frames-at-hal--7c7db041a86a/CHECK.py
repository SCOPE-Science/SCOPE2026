#!/usr/bin/env python3
"""Supplementary checks of the rational Poisson transfer identities.

Run: python3 CHECK.py
The tests are finite; the all-order frame proof is analytical.
"""
from fractions import Fraction
import cmath
import math

checks = 0
for nr in (1, 2, 3, 5, 7):
    r = Fraction(nr, 11)
    for nz in (13, 17, 19, 23, 29):
        z = Fraction(nz, 31)
        a = 1 / (1 - r*z)
        b = r / (z-r)
        aa = 1 / (1 + r*z)
        bb = -r / (z+r)
        computed = a*bb - aa*b
        formula = -2*r*z*(1-r*r) / ((1-r*z)*(1+r*z)*(z-r)*(z+r))
        assert computed == formula
        checks += 1

for w in (0.2, 1.0, 2.5):
    for t in (0.0, 0.34, 1.25):
        z = cmath.exp(1j*math.pi*t)
        r = math.exp(-math.pi*w)
        a = 1/(1-r*z)
        b = r/(z-r)
        aa = 1/(1+r*z)
        bb = -r/(z+r)
        det = a*bb-aa*b
        assert abs(det) > 0.0000001 * abs(a*bb)
        checks += 1
        for theta in (0.4, 1.4, 3.9):
            direct = sum(cmath.exp(1j*j*theta)/((t-2*j)**2+w*w)
                         for j in range(-6000,6001))
            predicted = (math.pi/(2*w))*cmath.exp(1j*t*theta/2)*(
                a*math.exp(-w*theta/2)+b*math.exp(w*theta/2))
            assert abs(direct-predicted) < 3e-8
            checks += 1

# A half-line of entire translation columns has vanishing analysis energy
# on test functions escaping to the right, in the predicted cubic order.
for w in (0.4, 1.0):
    for R in (10, 20, 40):
        energy_upper = 2*sum(1/((R-k)**2+w*w)**2 for k in range(-8000,1))
        assert energy_upper < 2.01/(3*(R-1)**3)
        checks += 1

print(f'CHECK_OK assertions={checks}')
