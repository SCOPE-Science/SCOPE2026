#!/usr/bin/env python3
"""Exact symbolic check of the Fourier polynomial in the quartic response.

Requires sympy. This checks algebra only; the all-parameter dynamical
statement uses the analytic transfer-operator proof in RESULT.md.
"""
import sympy as s

a,b = s.symbols('a b', real=True)
I=s.I
Z=(b-I*a)**2
c1=-(a*a+b*b)/8
c2=Z/4
c3=-3*Z/8
squared=lambda z: s.expand(z*s.conjugate(z))
variance=s.expand(2*(squared(c1+c2)+squared(c3)))
expected=(a*a+b*b)*(9*a*a+5*b*b)/16
assert s.simplify(variance-expected)==0
assert s.simplify(variance/8-(a*a+b*b)*(9*a*a+5*b*b)/128)==0
for A,B,coefficient in [(1,0,s.Rational(9,128)),(0,1,s.Rational(5,128)),(1,1,s.Rational(7,32)),(0,0,0)]:
  assert s.simplify((variance/8).subs({a:A,b:B})-coefficient)==0

# For the four-dimensional real degree <=2 trigonometric space, the
# doubling-map variance is zero exactly if the two complex Fourier
# coefficients sum to zero. A nonzero single-harmonic polynomial does
# not lie in this kernel.
x,y,z,w=s.symbols('x y z w', real=True)
positive_mode_1=x+I*y
positive_mode_2=z+I*w
kernel_variance=s.expand(2*squared(positive_mode_1+positive_mode_2))
assert s.simplify(kernel_variance-2*((x+z)**2+(y+w)**2))==0
print('PASS: exact quartic coefficient, axes, and minimal Fourier kernel')
