"""Reproducibility checks for a four-periodic weighted-shift test-vector maximum.

The accompanying proof establishes the infinite parameter range using inequalities;
this program checks polynomial identities symbolically and samples parameters.
"""
from random import Random
import sympy as sp

z,y,q,s,t=sp.symbols('z y q s t', positive=True)
x,u,v=sp.symbols('x u v', positive=True)
P=1+s*q*z+q**2*z**2+t*q**3*z**3
R=1-q**4*z**4
B=sp.expand((P*(1-3*z)+2*z*(1-z)*sp.diff(P,z))*R + 2*z*(1-z)*P*(4*q**4*z**3))
assert sp.degree(B,z)==8
G=sp.expand((1+y)**8*B.subs(z,y/(1+y))).cancel()
C=[sp.factor(sp.Poly(G,y).nth(i)) for i in range(9)]
EXPECTED=[
 1,5+3*x,7+16*x+5*u,
 -7+33*x+23*u+7*v,
 -35+30*x+40*u+26*v+7*u**2,
 -49+(5+5*u**2)*x+30*u+34*v+23*u**2,
 -35+(12*u**2-12)*x+5*u+16*v+27*u**2+3*u**3,
 -(1-u**2)*(13+9*x+5*u+v),
 -2*(1-u**2)*(1+x+u+v)]
for i,(actual,desired) in enumerate(zip(C, EXPECTED)):
 assert sp.simplify(actual-sp.sympify(desired).subs({x:q*s,u:q*q,v:q**3*t}))==0, i
c3,c4,c5,c6=EXPECTED[3:7]
assert sp.expand(c4-5*c3)==-135*x-75*u-9*v+7*u**2
assert sp.simplify(5*(c5-sp.Rational(7,5)*c4)-((-185+25*u**2)*x-130*u-12*v+66*u**2))==0
assert sp.simplify(7*(c6-sp.Rational(5,7)*c5)-((59*u**2-109)*x-115*u-58*v+74*u**2+21*u**3))==0
# The latter polynomials are strictly negative for 0<u<1 and x,v>0.
rng=Random(177)
for _ in range(256):
 Q=rng.uniform(0.01,0.999)
 S=10**rng.uniform(-4,4)
 T=10**rng.uniform(-4,4)
 seq=[float(c.subs({q:Q,s:S,t:T})) for c in C]
 signs=[1 if a>0 else -1 for a in seq if abs(a)>1e-10]
 assert sum(signs[i]!=signs[i-1] for i in range(1,len(signs)))==1
print('PASS: transform, inequalities, and parameter samples')
