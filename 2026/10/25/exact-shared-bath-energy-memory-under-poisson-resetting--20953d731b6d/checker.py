#!/usr/bin/env python3
"""Reproduce stationary energy-covariance identities for a reset diffusing-diffusivity model."""
import sympy as s
from fractions import Fraction
z=s.symbols('z',nonnegative=True)
d=s.symbols('d',integer=True,positive=True)
a,L=s.symbols('a L', positive=True)
# Independent moment calculation from the polynomial Markov generator.
w2=2*L**2/a
w4=s.simplify(12*L**2*w2/a)
x2=s.simplify(2*w2/a)
x2w2=s.simplify((2*w4+2*L**2*x2)/a)
x2x2=s.simplify(4*x2w2/a)
x4=s.simplify(12*x2w2/a)
assert s.simplify(w2-2*L**2/a)==0
assert s.simplify(w4-24*L**4/a**2)==0
assert s.simplify(x2-4*L**2/a**2)==0
assert s.simplify(x2w2-56*L**4/a**3)==0
assert s.simplify(x2x2-224*L**4/a**4)==0
assert s.simplify(x4-672*L**4/a**4)==0
cross0=s.factor(x2x2-x2**2)
auto0=s.factor(x4-x2**2)
mode=s.factor(x2w2-x2*w2)
assert s.simplify(cross0-208*L**4/a**4)==0
assert s.simplify(auto0-656*L**4/a**4)==0
assert s.simplify(mode-48*L**4/a**3)==0
Ccross=s.exp(-a*z)*(cross0+2*z*mode)
Cauto=s.exp(-a*z)*(auto0+2*z*mode)
for C,k in [(Ccross,13),(Cauto,41)]:
    assert s.simplify(C-16*L**4/a**4*(k+6*a*z)*s.exp(-a*z))==0
Cenergy=s.simplify(d*Cauto+d*(d-1)*Ccross)
assert s.simplify(Cenergy-16*L**4/a**4*d*(13*d+28+6*d*a*z)*s.exp(-a*z))==0
integrated=s.integrate(Cenergy,(z,0,s.oo))
assert s.simplify(2*integrated-32*L**4/a**5*d*(19*d+28))==0
mean= d*x2
assert s.simplify(2*integrated/mean**2-2*(19+28/d)/a)==0
# Check independent-environment comparator and positive finite-d gap.
independent_coeff=32*L**4/a**5*47*d
assert s.simplify(independent_coeff/(d*x2)**2-94/(a*d))==0
assert s.factor(2*integrated-independent_coeff)==32*L**4*d*(d-1)*19/a**5
# Additional independent stationary-age integration of Brownian diffusivity functionals.
t=s.symbols('t',positive=True)
# E[ \int_0^t omega_u^2 du ] = L^2 t^2; conditional variance of X_i = 2L^2 t^2
ageMoment=lambda n:s.factorial(n)/a**n
assert s.simplify(2*L**2*ageMoment(2)-x2)==0
# E[(integral omega_u^2 du)^2 |age=t] = (7/3)L^4 t^4;
# E[X_i^2 X_j^2 |age=t] =4*(7/3)L^4 t^4.
assert s.simplify(s.Rational(28,3)*L**4*ageMoment(4)-x2x2)==0
# For i=j, conditional Gaussian fourth moment yields factor 3.
assert s.simplify(3*s.Rational(28,3)*L**4*ageMoment(4)-x4)==0
# Covariance numerical quadrature checks (independent from symbolic integrator).
import scipy.integrate as it
for dimension in (1,2,3,6,12):
    for rate,lam in ((1.,1.),(.8,1.7),(2.3,.5)):
        f=lambda tau:16*lam**4/rate**4*dimension*(13*dimension+28+6*dimension*rate*tau)*s.exp(-rate*tau)
        num=2*it.quad(lambda tau:float(f(tau)),0,150/rate,epsabs=1.e-9)[0]
        exact=32*lam**4/rate**5*dimension*(19*dimension+28)
        assert abs(num-exact)/exact<5e-11
print('PASS: 16 exact symbolic assertions; 15 independent numerical Green-Kubo quadratures; stationarity and comparator identities checked.')
