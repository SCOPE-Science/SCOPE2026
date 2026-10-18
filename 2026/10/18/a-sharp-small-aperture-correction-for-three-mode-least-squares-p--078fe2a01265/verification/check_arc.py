#!/usr/bin/env python3
"""Reproduce exact symbolic coefficients and independent finite-aperture checks.
Requires Python 3, sympy and mpmath. These finite checks are not a universal proof.
"""
import sympy as s
import mpmath as m

y,h,x=s.symbols('y h x', real=True)
q=3*x*x-1
K0=1+3*x*y+s.Rational(5,4)*q*(3*y*y-1)
rminus=(-1-s.sqrt(6))/5
rplus=(-1+s.sqrt(6))/5
K2=-(175*y**4+140*y**3-90*y**2-28*y-5)/280
c0=1+12*s.sqrt(6)/25
c2=-387*s.sqrt(6)/21875
checks=0
def check(cond,label):
 global checks
 assert cond,label
 checks+=1

check(s.simplify(K0.subs(x,1)-s.Rational(3,2)*(5*y*y+2*y-1))==0,'Legendre endpoint kernel')
check(s.simplify(K0.subs({x:1,y:rminus}))==0,'first root')
check(s.simplify(K0.subs({x:1,y:rplus}))==0,'second root')
check(s.simplify(1-s.integrate(K0.subs(x,1),(y,rminus,rplus))-c0)==0,'leading constant')
check(s.simplify(-s.integrate(K2,(y,rminus,rplus))-c2)==0,'quadratic correction')
check(s.integrate(K2,(y,-1,1))==0,'kernel normalization correction')

# Derive the C^1-limiting monotonicity formula rather than assume it.
a=s.Rational(15,4)*q
bb=3*x
cc=1-s.Rational(5,4)*q
center=-bb/(2*a)
d2=s.factor(center**2-cc/a)
mean_deriv=s.factor(3*center+s.Rational(15,2)*x*(3*center**2+d2-1))
formula=-9*x*(5*x*x-2*x-1)*(5*x*x+2*x-1)/(5*q*q)
check(s.factor(mean_deriv-formula)==0,'monotonicity formula')
check(s.N((1+3*x*x+s.Rational(5,4)*(3*x*x-1)**2).subs(x,s.Rational(21,25)),40)<s.N(c0*c0,40),'Cauchy strict barrier')

# Confirm the even-order expansion from exact trigonometric moments.
A=s.sin(h)/h
B=(1+s.sin(2*h)/(2*h))/2
C=(1-s.sin(2*h)/(2*h))/2
ca=s.series(s.cos(h)-A,h,0,9).removeO()
cb=s.series(s.cos(h*y)-A,h,0,9).removeO()
var=s.series(B-A*A,h,0,9).removeO()
sv=s.series(s.sin(h)*s.sin(h*y),h,0,7).removeO()
cv=s.series(C,h,0,7).removeO()
actual=s.series(1+ca*cb/var+sv/cv,h,0,4).removeO().expand()
check(s.factor(actual.coeff(h,0)-K0.subs(x,1))==0,'constant term of exact kernel')
check(s.factor(actual.coeff(h,2)-K2)==0,'quadratic term of exact kernel')

m.mp.dps=75
C0=m.mpf(str(s.N(c0,75))); C2=m.mpf(str(s.N(c2,75)))
for hh in ['0.5','0.2','0.1','0.05','0.02']:
 hh=m.mpf(hh)
 aa=m.sin(hh)/hh; bb=(1+m.sin(2*hh)/(2*hh))/2
 cc=(1-m.sin(2*hh)/(2*hh))/2
 coeffA=(m.cos(hh)-aa)/(bb-aa*aa); coeffB=m.sin(hh)/cc
 fun=lambda yy:1+coeffA*(m.cos(hh*yy)-aa)+coeffB*m.sin(hh*yy)
 z0=m.findroot(fun,(-m.mpf('0.8'),-m.mpf('0.6')))
 z1=m.findroot(fun,(m.mpf('0.2'),m.mpf('0.35')))
 check(-1<z0<z1<1,'two simple roots')
 check(fun(0)<0 and fun(-1)>0 and fun(1)>0,'kernel sign pattern')
 norm=1-m.quad(fun,[z0,z1])
 err=abs(norm-C0-C2*hh**2)
 check(err< m.mpf('0.01')*hh**4,'fourth-order residual bound on sampled aperture')
 print(f'aperture={m.nstr(hh,5)}, exact endpoint norm={m.nstr(norm,22)}, remainder/h^4={m.nstr((norm-C0-C2*hh**2)/hh**4,16)}')
print('PASS:', checks, 'independent symbolic/numeric assertions')
