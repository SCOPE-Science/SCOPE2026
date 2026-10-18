#!/usr/bin/env python3
"""Exact series and numerical checks for a planar Euclidean ball-hull profile."""
from sympy import (symbols, sqrt, sin, cos, asin, acos, series, factor, simplify,
                   Rational, pi, diff, limit)
import mpmath as mp

b,k=symbols('b k', positive=True, real=True)
q=1-k
# Scale the containing-ball radius to one.
s=sqrt(k*k+2*q*(1-cos(b)))
phi=asin(q*sin(b)/s)
D=(1-k*k)*b-q*sin(b)-k*k*phi
sc=series(s,b,0,6).removeO().expand()
dc=series(D,b,0,7).removeO().expand()
S2=factor(sc.coeff(b,2));S4=factor(sc.coeff(b,4))
D3=factor(dc.coeff(b,3));D5=factor(dc.coeff(b,5))
assert simplify(S2-q/(2*k))==0
assert simplify(S4-(k-1)*(k*k-3*k+3)/(24*k**3))==0
assert simplify(D3-q/(3*k))==0
assert simplify(D5-(k-1)*(7*k*k-18*k+12)/(60*k**3))==0
A=simplify(D3/(S2**Rational(3,2)))
B=simplify((D5/D3-Rational(3,2)*S4/S2)/S2)
C=factor(1-Rational(4,3)*k*B)
assert simplify(A-(2*sqrt(2*k)/(3*sqrt(1-k))))==0
assert simplify(B-3*(3*k*k-7*k+3)/(20*k*(k-1)))==0
assert simplify(C-(3*k*k-12*k+8)/(5*(1-k)))==0
mp.mp.dps=65
for ratio in [mp.mpf('0.2'),mp.mpf('0.5'),mp.mpf('0.9')]:
 Q=1-ratio
 alpha=2*mp.sqrt(2*ratio)/(3*mp.sqrt(1-ratio))
 corr=3*(3*ratio**2-7*ratio+3)/(20*ratio*(ratio-1))
 for z in [mp.mpf('1e-3'),mp.mpf('1e-4')]:
  distance=ratio+z
  angle=mp.acos((1+Q**2-distance**2)/(2*Q))
  theta=mp.acos((1-Q**2-distance**2)/(2*distance*Q))
  area=angle-Q*mp.sin(angle)-ratio**2*theta
  approximation=alpha*z**mp.mpf('1.5')*(1+corr*z)
  assert abs(area/approximation-1)<mp.mpf('0.00008')
 ratio=ratio
# At the ball-convexity loss radius s=R.
for ratio in [mp.mpf('0.3'),mp.mpf('0.8')]:
 Q=1-ratio
 ang=mp.acos(Q/2)
 t=mp.acos((1-Q**2-1)/(2*Q))
 assert abs(t-(mp.pi-ang))<mp.mpf('1e-55')
 f=ang-Q*mp.sin(ang)-ratio**2*t
 threshold=(1+ratio**2)*ang-Q*mp.sqrt(1-Q**2/4)-mp.pi*ratio**2
 assert abs(f-threshold)<mp.mpf('1e-55')
print('VERIFY_OK symbolic_series=4 asymptotics=6 threshold=2')
