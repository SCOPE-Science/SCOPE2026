#!/usr/bin/env python3
"""Standalone numerical and symbolic checks for a telegraph-modulated diffusion inverse law.
This code provides finite checks; analytic claims rely on the proof in RESULT.md.
"""
import sympy as sp
import mpmath as mp

x,p=sp.symbols('x p', positive=True)
f=x-1+sp.exp(-x)
I=x/sp.Integer(2)-sp.Rational(5,4)+(x+1)*sp.exp(-x)+sp.exp(-2*x)/4
num=sp.expand(sp.diff(I,x)*f-2*I*sp.diff(f,x))
P=2*sp.exp(2*x)*num
assert sp.simplify(P-((4-x)*sp.exp(2*x)-(2*x**2+8)*sp.exp(x)+(x+4)))==0
coeff=lambda n:sp.simplify(sp.diff(P,x,n).subs(x,0))
assert all(coeff(n)==0 for n in range(6))
assert all(coeff(n)<0 for n in range(6,21))
assert sp.simplify(sp.inverse_laplace_transform(1/(p**2*(p+1)**2*(p+2)),p,x)-I)==0
assert sp.limit(140*I/f**2,x,0,dir='+')==sp.Rational(70,3)
assert sp.limit(140*I/f**2,x,sp.oo)==0
mp.mp.dps=70
for t,k,mu,a in [(1,.2,1,.4),(.7,.8,2,.5),(2,.35,1.3,.2),(3,2,3,1)]:
 t,k,mu,a=map(mp.mpf, map(str,(t,k,mu,a)))
 lam=2*k; xx=lam*t
 ff=xx-1+mp.exp(-xx)
 ii=xx/2-mp.mpf(5)/4+(xx+1)*mp.exp(-xx)+mp.exp(-2*xx)/4
 def logmoment(u):
  h=mp.sqrt(k*k+a*a*u*u)
  return (mu*u-k)*t+mp.log(mp.cosh(h*t)+(k/h)*mp.sinh(h*t))
 c=mp.taylor(logmoment,0,4)
 assert mp.almosteq(c[1],mu*t, rel_eps=mp.mpf('1e-48'))
 assert mp.almosteq(c[2],a*a*ff/(lam*lam), rel_eps=mp.mpf('1e-48'))
 assert abs(c[3]) < mp.mpf('1e-45')
 assert mp.almosteq(c[4],-2*a**4*ii/lam**4, rel_eps=mp.mpf('1e-43'))
 C=mp.factorial(4)*c[2]; E=mp.factorial(8)*c[4]; V=2*mu*t
 assert mp.almosteq(-E/C**2,140*ii/ff**2,rel_eps=mp.mpf('1e-43'))
 inv_k=mp.findroot(lambda z:140*(z/2-mp.mpf(5)/4+(z+1)*mp.exp(-z)+mp.exp(-2*z)/4)/(z-1+mp.exp(-z))**2+E/C**2,(xx*.8,xx*1.2))
 inv_a=inv_k/t*mp.sqrt(C/(24*(inv_k-1+mp.exp(-inv_k))))
 assert mp.almosteq(inv_k,xx,rel_eps=mp.mpf('1e-33'))
 assert mp.almosteq(inv_a,a,rel_eps=mp.mpf('1e-33'))
 assert mp.almosteq(V/(2*t),mu,rel_eps=mp.mpf('1e-33'))
 print('CHECK',float(t),float(k),'C=',mp.nstr(C,11),'E=',mp.nstr(E,11),'Q=',mp.nstr(-E/C**2,11))
print('All symbolic and independent matrix-exponential cumulant checks passed.')
