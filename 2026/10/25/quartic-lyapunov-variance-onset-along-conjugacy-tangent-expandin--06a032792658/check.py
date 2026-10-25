#!/usr/bin/env python3
"""Standalone rational Fourier certificate and finite near-conjugacy checks."""
from fractions import Fraction
from math import sin, cos, pi, log

# The second-order logarithmic derivative has Fourier cosine coefficients.
c={1:Fraction(-1,2),3:Fraction(3,2),4:Fraction(-1,1)}
def covariance(j):
    return sum((v*c.get(k*2**j, Fraction(0)) for k,v in c.items()),Fraction(0))/2
assert covariance(0)==Fraction(7,4)
assert covariance(1)==0
assert covariance(2)==Fraction(1,4)
assert all(covariance(j)==0 for j in range(3,20))
variance=covariance(0)+2*sum((covariance(j) for j in range(1,20)),Fraction(0))
assert variance==Fraction(9,4)

def u(x): return -sin(2*pi*x)/(2*pi)
def up(x): return -cos(2*pi*x)
def v(x): return 2*u(x)-u(2*x)
def vp(x): return 2*up(x)-2*up(2*x)
def H(x,e): return x+e*u(x)
def Hp(x,e): return 1+e*up(x)
def f(x,e): return 2*x+e*v(x)
def fp(x,e): return 2+e*vp(x)
def invH(y,e):
    z=y
    for _ in range(10): z-=(H(z,e)-y)/Hp(z,e)
    assert abs(H(z,e)-y)<1e-13
    return z
def g(y,e):
    z=invH(y,e)
    return H(f(z,e),e)
def gp(y,e):
    z=invH(y,e)
    return Hp(f(z,e),e)*fp(z,e)/Hp(z,e)
def w(y): return up(2*y)*v(y)
def phi(y): return Fraction(3,2)*cos(6*pi*y)-Fraction(1,2)*cos(2*pi*y)-cos(8*pi*y)
xs=[(k+.371)/137 for k in range(137)]
errs2=[]; errs3=[]
for e in (0.08,0.04,0.02,0.01):
    assert min(fp(x,e) for x in xs)>1
    delta=max(abs((g(x,e)-2*x)/e**2-w(x)) for x in xs)
    delta_phi=max(abs((log(gp(x,e))-log(2))/e**2-phi(x)) for x in xs)
    errs2.append(delta); errs3.append(delta_phi)
    print(f'eps={e:.5f} map_second_order_error={delta:.7e} log_derivative_error={delta_phi:.7e}')
assert all(errs2[i+1]<0.66*errs2[i] for i in range(3))
assert all(errs3[i+1]<0.66*errs3[i] for i in range(3))
print(f'EXACT_CORRELATIONS c0={covariance(0)} c1={covariance(1)} c2={covariance(2)} c>=3=0')
print(f'EXACT_VARIANCE={variance}')
print('CHECKS_PASS')
