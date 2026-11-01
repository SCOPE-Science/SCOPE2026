#!/usr/bin/env python3
"""Deterministic corroboration of the explicit sharpness witnesses."""
import cmath
import math

checks = 0
for r in (0.13, 0.37, 0.63, 0.91):
    for d in range(3, 22):
        A = math.sqrt((1-r**(2*d)) / (r**2-r**(2*d-2)))
        for j in range(53):
            t = 2 * math.pi * (j + 0.123) / 53
            z = cmath.exp(1j*t)
            f = 1 + A*z**(d-1)
            g = A*z + z**d
            assert abs(abs(f)**2-abs(g)**2) < 1e-8
            checks += 1
            z = r*z
            f = 1 + A*z**(d-1)
            g = A*z + z**d
            predicted = 2*A*r**(d-1)*(1-r*r)*math.cos((d-1)*t)
            assert abs((abs(f)**2-abs(g)**2)-predicted) < 1e-8
            checks += 1
        for j in range(2*d-2):
            t = math.pi*(j+0.5)/(d-1)
            z = r*cmath.exp(1j*t)
            assert abs(abs(1+A*z**(d-1))**2-abs(A*z+z**d)**2)<1e-8
            checks += 1
    for c in (0.3, 1.1):
        for j in range(53):
            t = 2*math.pi*(j + 0.123)/53
            z = r*cmath.exp(1j*t)
            f = 1+1j*c*z+z*z
            g = 1-1j*c*z+z*z
            assert abs(abs(f)**2-abs(g)**2+4*c*r*(1-r*r)*math.sin(t))<1e-8
            checks += 1
        for t in (0,math.pi):
            z = r*cmath.exp(1j*t)
            assert abs(abs(1+1j*c*z+z*z)**2-abs(1-1j*c*z+z*z)**2)<1e-8
            checks += 1
print(f"PASS: {checks} deterministic witness checks")
