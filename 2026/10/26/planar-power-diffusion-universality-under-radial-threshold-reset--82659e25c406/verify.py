#!/usr/bin/env python3
"""Standalone symbolic and numerical checks for the radial reset theorem."""
import sympy as s
import mpmath as mp
r,L,alpha,d,u,b=s.symbols('r L alpha d u b',positive=True)
gamma=alpha+2
h=(r/L)**gamma
D=s.simplify(r**(-alpha)*(s.diff(h,r,2)+(d-1)*s.diff(h,r)/r))
Q=s.simplify(r**(-alpha)*s.diff(h,r)**2)
assert s.simplify(D-gamma*(alpha+d)/L**gamma)==0
assert s.simplify(Q-gamma**2*h/L**gamma)==0
p=b/(b-1)*(1-u**(b-1))
assert s.simplify(s.diff(u*p,u,2)-b*s.diff(p,u))==0
assert s.simplify(b/(b-1)*(1-1/b)-1)==0  # exact normalization
assert s.simplify(s.limit(p,b,1)+s.log(u))==0
m1=1-u
m2=s.Rational(3,2)-2*u+u**2/2
B=lambda f:s.simplify(u*s.diff(f,u,2)+s.diff(f,u))
assert B(m1)==-1 and s.simplify(B(m2)+2*m1)==0
assert m1.subs(u,1)==m2.subs(u,1)==0
assert m1.subs(u,0)==1 and m2.subs(u,0)==s.Rational(3,2)
assert all(abs(mp.quad(lambda x:x**k*(-mp.log(x)),[0,1])-1/(k+1)**2)<1e-11 for k in range(20))
mp.mp.dps=30
for di in (1,2,3,4,5,8):
 for a in (0,0.5,1,2,7/3):
  g=a+2; bb=(a+di)/g
  if di==1: f=lambda z:(a+1)*g*z**a*(1-z)
  elif di==2: f=lambda z:g*g*z**(a+1)*mp.log(1/z)
  else: f=lambda z:g*(a+di)/(di-2)*z**(a+1)*(1-z**(di-2))
  assert abs(mp.quad(f,[0,1])-1)<mp.mpf('1e-11'),(di,a)
  z=mp.mpf('.4321')
  pu=-mp.log(z**g) if di==2 else bb/(bb-1)*(1-(z**g)**(bb-1))
  assert abs(f(z)-g*z**(g-1)*pu)<mp.mpf('1e-12'),(di,a)
z=s.symbols('z')
series=s.series(1/s.hyper([], [1],z),z,0,4).removeO()
assert s.simplify(series-(1-z+s.Rational(3,4)*z**2-s.Rational(19,36)*z**3))==0
print('PASS: conjugacy coefficients, stationarity equation, exact normalization, planar exit moments and Laplace series; 20 stationary moments and 30 full radial density cases.')
