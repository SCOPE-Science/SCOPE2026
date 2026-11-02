#!/usr/bin/env python3
"""Exact polynomial verification of the stationary centered-third-moment identity."""
import sympy as sp
A,B,W=sp.symbols('A B W')
m1=B*W/(A+B)
m2=B*(A*B*W**2+A+B+1)/((A+1)*(A+B)*(A+B+1))
m3=B*W*(A**2*B**2*W**2+3*A**2*B+2*A**2+3*A*B**2+9*A*B+6*A+2*B**2+6*B+4)/((A+1)*(A+2)*(A+B)*(A+B+1)*(A+B+2))
P=A*(A+1)*(A+2)*(A-B)-(1-W**2)*B**2*(7*A**2+12*A+4+(7*A+6)*B+2*B**2)
target=2*B*W*P/((A+1)*(A+2)*(A+B)**3*(A+B+1)*(A+B+2))
num=sp.together(m3-3*m1*m2+2*m1**3-target).as_numer_denom()[0]
assert sp.Poly(sp.expand(num),A,B,W).is_zero
print('PASS: exact symbolic centered-third-moment polynomial identity')
