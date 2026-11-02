"""Exact Laurent-identity verification for the torus chart of a quartic complement."""
import sympy as sp

A, Y, W = sp.symbols('A Y W', nonzero=True)
I = sp.I
B = (W + Y**2 + 1)/A
Z = (A - B)/(2*I)
T = (A + B - 1 + Z**2)/Y
F = (T*Y + 1 - Z**2)**2 - 4*(1 + Y**2 - Z**2)
U = (T*Y + 1 - Z**2)/2
assert sp.cancel(F - 4*W) == 0
assert sp.cancel(U + I*Z - A) == 0
assert sp.cancel(U - I*Z - B) == 0
assert sp.cancel((U + I*Z)*(U - I*Z) - Y**2 - 1 - W) == 0

# Verify the reverse composition symbolically on the original affine coordinates.
t, y, z = sp.symbols('t y z', nonzero=True)
f = (t*y + 1 - z**2)**2 - 4*(1 + y**2 - z**2)
u = (t*y + 1 - z**2)/2
a = u + I*z
w = f/4
br = (w + y**2 + 1)/a
zr = (a - br)/(2*I)
tr = (a + br - 1 + zr**2)/y
assert sp.cancel(zr-z) == 0
assert sp.cancel(tr-t) == 0
print('VERIFY_OK: forward and inverse formulas are mutual rational identities; F=4W')
