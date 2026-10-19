#!/usr/bin/env python3
"""Symbolic reproduction of a nonlinear Runge--Kutta squared-radius law."""
import sympy as s
from fractions import Fraction
x,q,h = s.symbols('x q h', real=True)
w2=1+q*x**2/4
x3=1-x**2*w2/2
y3=-x*w2
w3=1+q*(x3*x3+y3*y3-1)
xx=1-x**2*w2*(1+w3)/4
yy=-x*(1+2*w2+w3*x3)/4
Q=s.Poly(s.expand(xx*xx+yy*yy),x)
assert all(Q.nth(j)==0 for j in (1,2,3,4,5))
assert all(Q.nth(j)==0 for j in range(1,Q.degree()+1,2))
assert s.factor(Q.nth(6))==(q+1)**2/64
assert s.factor(Q.nth(8))==-q*(q+1)*(2*q+1)/128
assert s.factor(Q.nth(10))==q*(9*q+8)/1024
assert s.factor(Q.nth(12))==q**2*(2*q**3+8*q**2+13*q+8)/1024
critical=s.factor(Q.as_expr().subs(q,-1)-1)
assert s.limit(critical/x**10,x,0)==s.Rational(1,1024)
# frequency 2-r, dimensionless r=1+h^2*y, q=-r/(2-r), x=h*(2-r)
y=s.symbols('y',real=True)
r=1+h**2*y
p=s.factor(Q.as_expr().subs({q:-r/(2-r),x:h*(2-r)}, simultaneous=True)*r-r)
L=s.factor(s.limit(p/h**10,h,0))
assert s.simplify(L-(8*y+1)**2/s.Integer(1024))==0
# Two independent exact numerical evaluations: Cartesian stages and scalar radial polynomial.
def f(z):
    a,b=z
    om=Fraction(2)-a*a-b*b
    return (om*b,-om*a)
def step(z,dt):
    k1=f(z)
    s2=tuple(z[i]+dt*k1[i]/2 for i in range(2))
    k2=f(s2)
    s3=tuple(z[i]+dt*k2[i] for i in range(2))
    k3=f(s3)
    return tuple(z[i]+dt*(k1[i]+2*k2[i]+k3[i])/4 for i in range(2))
def radius(z):return z[0]*z[0]+z[1]*z[1]
for z in [(Fraction(1),Fraction(0)), (Fraction(2,3),Fraction(1,4)), (Fraction(0),Fraction(3,5)),(Fraction(1,3),Fraction(0))]:
    for dt in [Fraction(1,10),Fraction(1,4),Fraction(2,5)]:
        rv=radius(z); om=2-rv
        if om==0:continue
        qt=-rv/om; xt=dt*om
        scalar=rv*Q.as_expr().subs({x:xt,q:qt})
        direct=radius(step(z,dt))
        assert scalar==direct,(z,dt,s.factor(scalar-direct))
# Independent double-precision long-step integrations illustrate the proven limit.
def scalar_integrate(dt, tau):
    rv=1.0
    for _ in range(round(tau/dt**8)):
        t=dt*(2-rv)
        qq=-rv/(2-rv)
        bb=1+qq*t*t/4
        xx3=1-t*t*bb/2
        yy3=-t*bb
        cc=1+qq*(xx3*xx3+yy3*yy3-1)
        xout=1-t*t*bb*(1+cc)/4
        yout=-t*(1+2*bb+cc*xx3)/4
        rv*=xout*xout+yout*yout
    return (rv-1)/dt**2
limit_value=8/(1024-8*8)
approximations=[scalar_integrate(dt,8) for dt in (0.4,0.3,0.25)]
assert all(approximations[j]>approximations[j+1]>limit_value for j in (0,1))
print('PASS: degree', Q.degree(), 'critical order10, Riccati coefficient', L,
      '12 exact Cartesian checks, 3 long-step convergence comparisons')
