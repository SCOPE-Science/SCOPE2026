#!/usr/bin/env python3
"""Exact-rational corroboration for the triangle-strength side-gradient theorem.

This finite checker supplements, but does not replace, the analytic proof in
RESULT.md. It uses only the Python standard library.
"""
from fractions import Fraction as F

THREE_EIGHTHS = F(3, 8)

def side_gradient(x, y, z):
    """Gradient of sigma in (a,b,c), where x=p-a,y=p-b,z=p-c and p=1."""
    assert x > 0 and y > 0 and z > 0 and x + y + z == 1
    X = y*z*(1-2*x)
    Y = x*z*(1-2*y)
    Z = x*y*(1-2*z)
    return ((-X+Y+Z)/2, (X-Y+Z)/2, (X+Y-Z)/2)

def direct_side_gradient(x, y, z):
    """Differentiate xyz/p^2 by chain rule, without using X,Y,Z shortcut."""
    p = x+y+z
    sx = y*z/(p*p) - 2*x*y*z/(p*p*p)
    sy = x*z/(p*p) - 2*x*y*z/(p*p*p)
    sz = x*y/(p*p) - 2*x*y*z/(p*p*p)
    return ((-sx+sy+sz)/2, (sx-sy+sz)/2, (sx+sy-sz)/2)

def norm1(v):
    return sum(abs(t) for t in v)

count = 0
for den in range(3, 81):
    for i in range(1, den-1):
        for j in range(1, den-i):
            k = den-i-j
            if k <= 0:
                continue
            x, y, z = F(i, den), F(j, den), F(k, den)
            g = side_gradient(x, y, z)
            assert g == direct_side_gradient(x, y, z)
            assert norm1(g) <= THREE_EIGHTHS, (x, y, z, g)
            count += 1

for den in (10, 100, 1000, 10000):
    x = F(1, den)
    y = z = (1-x)/2
    value = norm1(side_gradient(x, y, z))
    assert value <= THREE_EIGHTHS
    if den >= 100:
        assert THREE_EIGHTHS - value < F(1, 50)

print(f"exact-rational grid checks passed: {count}")
print(f"boundary-sequence check passed; last gap={float(THREE_EIGHTHS-value):.8g}")
