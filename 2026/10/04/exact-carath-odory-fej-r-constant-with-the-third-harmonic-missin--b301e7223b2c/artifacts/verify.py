#!/usr/bin/env python3
from fractions import Fraction as F
import math

# General two-point upper certificate.  Represent coefficients of
# (constant, lambda, b, c).
T_half = (F(1), F(-1), F(1), F(1))
T_third = (F(1), F(-1,2), F(-1,2), F(-1,2))
cert = tuple(T_half[i] + 2*T_third[i] for i in range(4))
assert cert == (F(3), F(-2), F(0), F(0))

# Extremal coefficients.
lam = F(3,2)
b = F(7,12)
c = F(-1,12)

# Q(x)=1+lam*x+b*(2*x^2-1)+c*(8*x^4-8*x^2+1).
# Coefficients from x^0 through x^4.
q = [F(1)-b+c, lam, 2*b-8*c, F(0), 8*c]

# Expand ((2-x)(x+1)(2x+1)^2)/6 exactly.
def mul(a,d):
    z=[F(0)]*(len(a)+len(d)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(d): z[i+j]+=x*y
    return z
fact = mul(mul([F(2),F(-1)],[F(1),F(1)]),[F(1),F(4),F(4)])
fact = [z/F(6) for z in fact]
assert q == fact
assert q == [F(1,3),F(3,2),F(11,6),F(0),F(-2,3)]

# Equality certificate forces b+c=1/2.  Stationarity at x=-1/2 gives
# 3/2 - 2b + 4c = 0.  Verify the unique solution.
assert b+c == F(1,2)
assert lam-2*b+4*c == 0
# Eliminate b=1/2-c: 3/2-1+2c+4c=0.
c_solved = -F(1,2)/6
b_solved = F(1,2)-c_solved
assert (b_solved,c_solved)==(b,c)

# Positive-definite sequence normalization.
assert lam/2 == F(3,4)
assert b/2 == F(7,24)
assert c/2 == F(-1,24)

# Numerical sign sanity check (corroborative only).
def T(t):
    return 1.0 + float(lam)*math.cos(2*math.pi*t) + float(b)*math.cos(4*math.pi*t) + float(c)*math.cos(8*math.pi*t)
mn=10.0
arg=None
for j in range(200001):
    t=j/200000.0
    v=T(t)
    if v<mn: mn,arg=v,t
assert mn > -2e-14
assert abs(T(0.5)) < 2e-14
assert abs(T(1/3)) < 2e-14
print('exact_certificate=', cert)
print('exact_factor_coefficients=', q)
print('dense_minimum=', format(mn,'.17g'), 'at', format(arg,'.17g'))
print('VERIFY_OK')
