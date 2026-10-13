"""Exact symbolic and numerical checks for midpoint phase-mixing theorem.

Dependency: sympy. All infinite-law claims are proved in RESULT.md, not by tests.
"""
import cmath
import math
from sympy import I, Matrix, Rational, Symbol, sqrt, together, cancel, re, im

t=Symbol('t', real=True, nonnegative=True)
R=Matrix([[1-t*t,2*t],[-2*t,1-t*t]])/(1+t*t)
zero=lambda e: cancel(together(e))==0
assert all(zero(e) for e in (R.T*R-Matrix.eye(2)))
Z=(1+I*t)**4/(1+t*t)**2
Re=(1-6*t*t+t**4)/(1+t*t)**2
Im=4*t*(1-t*t)/(1+t*t)**2
assert zero(re(Z)-Re) and zero(im(Z)-Im)
slack=t-(1-Re-Im)/2
cert=t*(t-1)**2*(t*t+2*t+3)/(1+t*t)**2
assert zero(slack-cert)
assert zero(Z.subs(t,0)-1) and zero(Z.subs(t,1)+1)

u=Symbol('u', real=True)
v=(1+u)/(1-u)
R0=R.subs(t,u)
R1=R.subs(t,v)
J=Matrix([[0,1],[-1,0]])
assert all(zero(e) for e in R1-J*R0)
for S in [Matrix([[1,0],[0,0]]),Matrix([[2,1],[1,3]])]:
   avg=(R0*S*R0.T+R1*S*R1.T)/2
   assert all(zero(e) for e in avg-S.trace()*Matrix.eye(2)/2)

m=Symbol('m',positive=True)
s=(m+2-sqrt(m*m+8))/2
assert zero(s*s-(m+2)*s+(m-1))
# If s solves this polynomial, s+(1+s)/(1-s)=m.
assert zero((s+(1+s)/(1-s)-m)*(1-s))
for mm in [1,1.1,2,3,5,50]:
    x=float(s.subs(m,mm)); y=(1+x)/(1-x)
    assert x>=0 and y>=1 and math.isclose(x+y,mm,abs_tol=1e-10)
    phase=lambda a: cmath.exp(4j*math.atan(a))
    assert abs(phase(x)+phase(y))<1e-10
print('PASS: exact matrix/rotation and dual-deficit identities, two-point cancellation,')
print('      positive examples and one-step isotropic second moments.')
