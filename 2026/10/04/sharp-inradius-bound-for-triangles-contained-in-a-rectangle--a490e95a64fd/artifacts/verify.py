#!/usr/bin/env python3
from fractions import Fraction
from math import sqrt, hypot


def q(h,x,y):
    A=h-x*y
    P=hypot(1.0,y)+hypot(x,h)+hypot(1.0-x,h-y)
    return A/P

# Exact rational replay of the Cauchy--Schwarz step A^2 <= v^2 w^2.
for hi in range(1,41):
    h=Fraction(hi,40)
    for xi in range(1,40):
        x=Fraction(xi,40)
        for yi in range(1,hi):
            y=Fraction(yi,40)
            A=h-x*y
            lhs=A*A
            rhs=(x*x+h*h)*((1-x)*(1-x)+(h-y)*(h-y))
            assert lhs <= rhs

# Exact rational inequalities sufficient for the two radical boundary comparisons.
# sqrt(4+h^2) <= 2+h and sqrt(1+4h^2) <= 1+2h.
for hi in range(1,1001):
    h=Fraction(hi,1000)
    assert 4+h*h <= (2+h)*(2+h)
    assert 1+4*h*h <= (1+2*h)*(1+2*h)
    # sqrt(1+h^2) >= h, used for the right-side boundary.
    assert 1+h*h >= h*h

# Deterministic stress test of the complete normalized corner quotient.
max_excess=-1e100
arg=None
for hi in range(1,101):
    h=hi/100.0
    target=h/(1.0+sqrt(1.0+4.0*h*h))
    for xi in range(0,201):
        x=xi/200.0
        for yi in range(0,201):
            y=h*yi/200.0
            val=q(h,x,y)
            excess=val-target
            if excess>max_excess:
                max_excess=excess; arg=(h,x,y,val,target)
            assert excess <= 2e-14

# Verify the stated extremizer exactly at sampled aspect ratios.
for hi in range(1,1001):
    h=hi/1000.0
    target=h/(1.0+sqrt(1.0+4.0*h*h))
    val=q(h,0.5,0.0)
    assert abs(val-target) < 2e-15

print('VERIFY_OK')
print('max_excess', format(max_excess,'.3e'))
print('arg', arg)
