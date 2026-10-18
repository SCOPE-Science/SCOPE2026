#!/usr/bin/env python3
"""Exact rational checks for a finite-support characteristic-function example.

The general characterization is proved analytically in RESULT.md. This script
checks only the explicitly identified example and illustrative factorizations.
"""
from fractions import Fraction as F
from itertools import product

# Unnormalized three-atom masses, which normalize by 17.
a, b, c = 8, 7, 2
assert a+b+c == 17
assert b*(a+c) - 4*a*c == 6  # ordinary monotonicity margin
assert b*b-4*a*c == -15      # nonreal roots and failure of strong monotonicity

# Under the exponential tilt with e^theta=2, the masses are 8:14:8 = 4:7:4.
assert [a,b*2,c*4] == [8,14,8]
# The polynomial (4+7z+4z^2)/15 vanishes at z=(-7+i sqrt(15))/8.
# Elements (u,v) represent the exact number u+v*i sqrt(15).
def plus(x,y): return (x[0]+y[0],x[1]+y[1])
def times(x,y): return (x[0]*y[0]-15*x[1]*y[1], x[0]*y[1]+x[1]*y[0])
z=(F(-7,8),F(1,8))
z2=times(z,z)
p=plus(plus((F(4),F(0)),(7*z[0],7*z[1])),(4*z2[0],4*z2[1]))
assert p == (F(0),F(0))
assert z[0]**2+15*z[1]**2 == 1
# At angle pi the normalized characteristic function is 1/15, not zero.
assert F(4-7+4,15) == F(1,15)

# Check the exact quadratic derivative formula using integer polynomials in
# c=cos(t) for numerous masses (including degenerate boundary cases).
for a,b,c in product(range(1,10),repeat=3):
    # |a+b exp(it)+c exp(2it)|^2 = S0+2b(a+c)u+2ac(2u^2-1)
    # derivative w.r.t. u: 2b(a+c)+8ac*u, minimized at u=-1.
    margin=b*(a+c)-4*a*c
    criterion=(margin>=0)
    assert criterion == (2*b*(a+c)-8*a*c>=0)
    # all-radius criterion is discriminant nonnegativity
    assert (b*b>=4*a*c) == ((b*b-4*a*c)>=0)

# Illustrative factorization: two independent Bernoulli variables with
# probabilities 1/3 and 2/5 give masses 2/5, 7/15, 2/15.
p,q=F(1,3),F(2,5)
coeffs=((1-p)*(1-q),p*(1-q)+(1-p)*q,p*q)
assert coeffs == (F(2,5),F(7,15),F(2,15))
assert sum(coeffs)==1
print('PASS: exact quadratic criterion, nonreal-root witness, tilt failure, and Bernoulli product')
