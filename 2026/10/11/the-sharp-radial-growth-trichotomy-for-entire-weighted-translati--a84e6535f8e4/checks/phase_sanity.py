#!/usr/bin/env python3
"""Independent finite consistency checks of two algebraic identities."""
from fractions import Fraction as F
import cmath

def cabs2(z):
    return z.real*z.real+z.imag*z.imag

a = complex(0,1)
b = complex(2,-1)
alpha = F(3,2)
z = complex(3,-2)
left = cabs2(a*z+b)-cabs2(z)
right = cabs2(b)+2*(a*z*b.conjugate()).real
assert left == right
# For m=4 and real b, the circle average of |R exp(i theta)+b|^4-R^4
# equals 4 R^2 b^2 + b^4. Check via coefficient algebra in real R,b.
from math import comb
# (R^2+b^2+2Rb cos theta)^2: average cos = 0, cos^2 = 1/2.
for R in [1, 2, 7, 16]:
    for b0 in [1, 3, 5]:
        average=(R*R+b0*b0)**2+2*R*R*b0*b0
        assert average-R**4==4*R*R*b0*b0+b0**4
print("RADIAL_FOCK_PHASE_GAUSSIAN_AND_QUARTIC_IDENTITIES_OK")
