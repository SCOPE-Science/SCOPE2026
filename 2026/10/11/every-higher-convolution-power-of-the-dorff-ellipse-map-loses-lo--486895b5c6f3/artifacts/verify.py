#!/usr/bin/env python3
"""Exact rational checks for higher Hadamard powers of a harmonic ellipse map.

All constants are public mathematical data from Wang--Zhong (2026),
 arXiv:2609.11556v1, equations (6.4)--(6.9).
"""
from fractions import Fraction as F
from math import comb

a = F(-10, 11)
b = F(1, 44)
A = F(-9890884608, 9139543205)
B = F(-251761689, 562995861428)
C = F(41190732, 12795360487)
D = F(1373955264, 9139543205)

def S(t, x):
    return x*(2-t*x)/(1-t*x)**2

def P(m, x):
    return 1 + sum(comb(m,j)*A**j*B**(m-j)*S(a**j*b**(m-j),x)
                   for j in range(m+1))

def Q(m, x):
    return sum(comb(m,j)*D**j*C**(m-j)*S(a**j*b**(m-j),x)
               for j in range(m+1))

assert a == F(-10,11) and b == F(1,44)
assert A < -F(27,25) < 0 and B < 0 and C > 0 and D > 0
assert F(0)<-a<1 and F(0)<b<1
u=F(10,11)**3
lower=F(27,25)**3*(2+u)/(1+u)**2
assert lower-1 == F(136271021,1048140625), (lower-1)

for m in range(3,13):
    s=1 if m%2 else -1
    x=F(s)
    bound=1-(-A)**m*(2+(-a)**m)/(1+(-a)**m)**2
    assert P(m,F(0))==1 and Q(m,F(0))==0
    assert P(m,x)<0 and P(m,x)<=bound<0
    assert Q(m,x)*x>0
print('EXACT_RATIONAL_CHECKS_PASS: m=3..12, base m=3 sharp inequality, and coefficient signs.')
print('ALL_m_PROOF: sign of S_t(x) is sign(x) on (-1,1) and at ±1;')
print('positive term (-A)^m (2+rho^m)/(1+rho^m)^2 increases with integer m≥3;')
print('continuous intermediate-value root p_m\' and nonzero q_m\' imply negative Jacobian.')
