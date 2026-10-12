#!/usr/bin/env python3
"""Reproduce exact two-curvature Markov switching stability and critical persistence identities."""
import sympy as s
from fractions import Fraction
eta,p=s.symbols('eta p', real=True)
a=(1-eta)**2; b=(1-6*eta)**2
P=s.Matrix([[p,1-p],[1-p,p]])
M=s.diag(a,b)*P
F=s.expand((s.eye(2)-M).det())
C=s.factor(F/eta)
expected=(72*p-36)*eta**3+(84-168*p)*eta**2+(85*p-61)*eta+14*(1-p)
assert s.expand(C-expected)==0
G=23675*p**3-38914*p**2+803*p+36
assert s.expand(s.discriminant(C,eta)+144*(2*p-1)*G)==0
assert s.expand(C.subs(p,0)+36*(eta-s.Rational(1,2))*(eta-s.Rational(2,3))*(eta-s.Rational(7,6)))==0
assert G.subs(p,0)>0 and G.subs(p,s.Rational(1,2))<0
assert s.expand(s.diff(G,p,2)-(142050*p-77828))==0
assert G.subs(p,s.Rational(43,1000))>0 and G.subs(p,s.Rational(44,1000))<0
assert s.factor(F.subs({p:s.Rational(1,50),eta:s.Rational(3,5)}))==-s.Rational(5523,31250)
assert s.factor(F.subs({p:s.Rational(1,50),eta:s.Rational(9,10)}))==s.Rational(53343,125000)
# 26*20 rational comparisons: determinant positivity iff spectral radius below 1 for p<1/2.
checks=0
for j in range(26):
 pp=s.Rational(j,52)
 for i in range(1,21):
  ee=s.Rational(i,17)
  q=M.subs({p:pp,eta:ee})
  tr=s.trace(q); det=s.det(q)
  # Dominant root via exact rational comparison: rho(q)<1 iff tr<2 and det(I-q)>0
  top_below = (tr<2 and (1-tr+det)>0)
  f_positive=F.subs({p:pp,eta:ee})>0
  assert top_below==f_positive, (pp,ee)
  checks+=1
# F function matches transfer for 2-state current-state-conditioned covariance recurrence.
print('VERIFY_OK',checks,'exact rational cases; critical persistence between 0.043 and 0.044')
