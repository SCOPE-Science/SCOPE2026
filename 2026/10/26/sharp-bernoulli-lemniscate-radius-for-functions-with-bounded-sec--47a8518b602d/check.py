"""Exact-algebra checks for a sharp Bernoulli-lemniscate radius.

The proof is analytic; this script verifies the finite algebraic identities
and explores representative boundary values, not the Schwarz--Pick step.
"""
from fractions import Fraction
import math
import sympy as sp

x, c, a, w = sp.symbols('x c a w', real=True)
P=(1+2*a*w)/(1+a*w)
assert sp.factor((P**2-1)*(1+a*w)**2-a*w*(2+3*a*w)) == 0
Q=sp.expand((1+2*a*c+a**2)**2-a**2*(4+12*a*c+9*a**2))
assert sp.simplify(Q-((1-2*a*a+2*a*c)**2+2*a*a*(1-6*a*a))) == 0
astar=1/sp.sqrt(6)
cstar=-sp.sqrt(sp.Rational(2,3))
assert sp.simplify(Q.subs({a:astar,c:cstar}))==0
assert sp.simplify(sp.diff(Q,c).subs({a:astar,c:cstar}))==0
assert -1<float(cstar)<1
# Spectral/tangency quantification: at the transition two boundary points
# have the same modulus 1, and a larger a fails near these points.
for mm in [0.20, 0.58, 0.8, math.sqrt(2/3), 0.84]:
 aa=mm/2
 co=max(-1,min(1,(2*aa*aa-1)/(2*aa)))
 vals=[]
 for theta in [math.acos(co), 0.0, math.pi]:
  z=complex(math.cos(theta),math.sin(theta))
  p=(1+mm*z)/(1+(mm/2)*z)
  vals.append(abs(p*p-1))
 print('m=',round(mm,12),'max_checks=',[round(q,12) for q in vals])
assert float(sp.sqrt(sp.Rational(2,3)))>2-math.sqrt(2)
print('symbolic algebra and threshold checks: PASS')
