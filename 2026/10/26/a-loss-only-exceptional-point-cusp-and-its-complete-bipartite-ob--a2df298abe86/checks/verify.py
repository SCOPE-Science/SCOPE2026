#!/usr/bin/env python3
"""Reproduce the exact discriminant and bright-block algebra.

Requires SymPy >= 1.12. Run: python checks/verify.py
All identities tested are exact; numerical samples are supplementary only.
"""
import sympy as s

a,b,g,z,X=s.symbols('a b gamma z X', positive=True, real=True)
A,B=s.symbols('A B', positive=True, real=True)
H=s.Matrix([[-s.I*g,a,0],[a,0,b],[0,b,0]])
p=s.expand((z*s.eye(3)-H).det())
expect=z**3+s.I*g*z**2-(a*a+b*b)*z-s.I*g*b*b
assert s.simplify(p-expect)==0
Delta=s.expand(s.discriminant(p,z))
D=4*b*b*g**4+(8*b**4-20*a*a*b*b-a**4)*g*g+4*(a*a+b*b)**3
assert s.expand(Delta-D)==0
Q=4*B*X**2+(8*B**2-20*A*B-A**2)*X+4*(A+B)**3
assert s.factor(s.discriminant(Q,X))==A*(A-8*B)**3
assert s.simplify(Q.subs(A,8*B)-4*B*(X-27*B)**2)==0
assert s.expand(p.subs({a:2*s.sqrt(2)*b,g:3*s.sqrt(3)*b})-(z+s.I*s.sqrt(3)*b)**3)==0
# Parameter test: a=3,b=1 gives exactly two positive gamma-square thresholds.
assert s.solve(Q.subs({A:9,B:1}),X)==[s.Rational(125,4),s.Integer(32)]
# Positive definite spectral region lies strictly between thresholds.
assert Q.subs({A:9,B:1,X:s.Rational(253,8)})<0
assert Q.subs({A:9,B:1,X:s.Rational(123,4)})>0
assert Q.subs({A:9,B:1,X:33})>0
# At the triple coalescence, geometric multiplicity is one.
M=H.subs({a:2*s.sqrt(2),b:1,g:3*s.sqrt(3)})+s.I*s.sqrt(3)*s.eye(3)
assert M.rank()==2 and M**3==s.zeros(3) and M**2!=s.zeros(3)
# For every integer bipartite block size m>=2, a^2/b^2<8.
for m in range(2,15):
 for n in range(1,15):
  assert s.Rational(n,n*(m-1))<8
  HM=H.subs({a:s.sqrt(n),b:s.sqrt(n*(m-1)),g:s.Rational(3,2)})
  assert s.expand(HM.det())!=0
# The only bright block in the star-center case is a dissipative dimer.
for n in range(1,20):
 G=s.sqrt(n)
 E=s.symbols('E')
 M2=s.Matrix([[-s.I*g,G],[G,0]])
 assert s.expand((E*s.eye(2)-M2).det()-(E**2+s.I*g*E-n))==0
 assert s.discriminant((E*s.eye(2)-M2).det(),E)==4*n-g*g
print('VERIFY_OK: characteristic polynomial, discriminants, EP3 Jordan chain, two EP2 roots, K_mn bright blocks and star-center EP2')
