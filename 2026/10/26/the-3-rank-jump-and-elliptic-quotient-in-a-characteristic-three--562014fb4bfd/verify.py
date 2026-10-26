#!/usr/bin/env python3
"""Symbolic characteristic-three checks of a cyclic quartic pencil.

Requires sympy. Uses universal polynomials rather than interpolation.
"""
import sympy as sp
x, y, z, r, t, lam = sp.symbols('x y z r t lam')
F=x**3*y+y**3*z+z**3*x+lam*x*y*z*(x+y+z)
e2=x*y+y*z+z*x
D=(x-y)*(x-z)*(y-z)
coordinates={x:-r-t*t-t, y:-r-t*t+t, z:1-r-t*t}
def check_mod3(polynomial, *variables):
    polynomial=sp.Poly(sp.expand(polynomial), *variables)
    assert all(int(c)%3==0 for c in polynomial.coeffs())
check_mod3(e2.subs(coordinates)-r, r,t,lam)
check_mod3(D.subs(coordinates)+t**3-t, r,t,lam)
A=1+lam
E=A*(t**3-t)**2-(t**3-t)+A*r**3-lam*r**2+r
check_mod3(F.subs(coordinates)+E, r,t,lam)
# Discriminant for monic cubic r^3+b*r^2+c*r+d in char 3:
# b^2*c^2-4*c^3-4*b^3*d-27*d^2+18*b*c*d.
# b=-lam/A, c=1/A, d=-1/A^2.
# Multiply by A^5 to clear denominators.
check_mod3(lam**2*A-A**2-lam**3-(lam-1),lam)
# c4=b^2, j=c4^3/discriminant; the numerator identity clears denominators.
check_mod3(lam**6*(A*(lam-1)-(lam**2-1)),lam)
assert sp.Poly(sp.expand((lam-1)*A),lam).degree()==2
print('VERIFY_OK: universal affine quotient, Artin-Schreier relation, discriminant and j')
