"""Reproduce the symbolic coefficient identity and finite numerical diagnostics.
This checker is not a substitute for the all-parameter proof in RESULT.md.
Requires Python 3 and sympy.
"""
import math
import random
import sympy as s
u, eta, y=s.symbols('u eta y',real=True)
def a(n):
    return (1-u)*(sum(u**j for j in range(n))-n*(2*n-1)*u**(n-1))
def c(n):
    return 2*n*(1-(2*n-1)*u**(n-1))
def b(n):
    return a(n)+eta*c(n)
assert s.factor(b(2)-((1-u)*(1-5*u)+4*eta*(1-3*u)))==0
assert s.factor(a(3)*c(2)-a(2)*c(3))==-2*(u-1)**3*(9*u-1)
Q=s.cosh(y)+eta*y*s.sinh(y)-(1+(eta+(1-u)/2)*y*y)*s.cosh(s.sqrt(u)*y)
for n in range(2,7):
    assert s.expand(s.diff(Q,y,2*n).subs(y,0)-b(n))==0
rng=random.Random(7439)
for _ in range(600):
    z=rng.uniform(0.0001,0.9999)
    e=10**rng.uniform(-2,2)
    F=(1-z)*(1-5*z)+4*e*(1-3*z)
    if F>=0:
        t0=e+(1-z)/2
        for yv in (0.05,0.2,0.5,1,3,8):
            tv=(math.cosh(yv)+e*yv*math.sinh(yv)-math.cosh(math.sqrt(z)*yv))/(yv*yv*math.cosh(math.sqrt(z)*yv))
            assert tv>t0-1e-10
print('PASS: six exact symbolic coefficient identities, strict sign factorization, 600 randomized parameter sets')
