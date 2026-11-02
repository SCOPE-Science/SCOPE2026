#!/usr/bin/env python3
"""Exact algebraic and finite numeric checks for a stationary switching-velocity cumulant."""
import sympy as S
import math

p, r, z, t = S.symbols('p r z t', real=True)
b = p*(1-p)
Pi = S.Matrix([[1-p,p],[1-p,p]])
Id = S.eye(2)
X = S.diag(-p, 1-p)
P = lambda u: Pi + (Id-Pi)*u
v = S.Matrix([[1-p,p]])
one = S.ones(2,1)

def moment(*steps):
    expr=v*X
    for step in steps:
        expr=expr*P(step)*X
    return S.expand((expr*one)[0])

E4 = moment(r,z,t)
E12,E34 = moment(r),moment(t)
E13,E24 = moment(r*z),moment(z*t)
E14,E23 = moment(r*z*t),moment(z)
k4 = S.factor(E4 - E12*E34 - E13*E24 - E14*E23)
assert S.factor(k4 - b*r*z*t*((1-2*p)**2-2*b*z)) == 0

q, x, Delta = S.symbols('q x Delta', positive=True)
A1 = Delta*(1-q)/(q*x)
A4 = Delta*q**3*(1-q)/x
A2 = A1/q
A3 = Delta*q**2*(1-q)/x
assert S.cancel(A1*A4-Delta**2*q**2*(1-q)**2/x**2)==0
assert S.cancel(A2*A3-Delta**2*(1-q)**2/x**2)==0

n=0
for probability in [0.01,0.1,0.2,0.25,0.30,0.4,0.5,0.6,0.7,0.75,0.8,0.9,0.99]:
  bb=probability*(1-probability)
  for xi in [0.0001,0.01,0.1,0.4,1,2,4,8,20,100]:
    H=-math.expm1(-xi)/xi
    bracket=(1-2*probability)**2-2*bb*H**2
    sign = -1 if bracket<0 else (1 if bracket>0 else 0)
    if probability==0.5: assert sign==-1
    elif abs(1-2*probability)>=1/math.sqrt(3): assert sign==1
    else:
      assert math.isfinite(bracket)
    n+=1
print('PASS: four-time cumulant polynomial, exponential integrals,',n,'finite parameter checks')
