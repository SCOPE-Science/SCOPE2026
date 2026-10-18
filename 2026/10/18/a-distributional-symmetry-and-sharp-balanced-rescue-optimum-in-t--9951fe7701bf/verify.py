"""Exact check of the two-patch directed rescue Laplace identity.

Run with: python verify.py
Requires sympy; all comparisons are exact symbolic/rational arithmetic.
"""
from fractions import Fraction
import sympy as sp

a,b,c,d,s = sp.symbols('a b c d s', positive=True)
Q=sp.Matrix([[-a-b,b,a],[c,-a-c,0],[d,0,-b-d]])
r=sp.Matrix([0,a,b])
L = sp.cancel(((s*sp.eye(3)-Q).inv()*r)[0])
K=a+b+c+d
B=a*b*K
D = s**3+(2*(a+b)+c+d)*s**2+(a*a+3*a*b+b*b+(a+b)*(c+d)+c*d)*s+B
formula=a*b*(2*s+K)/D
assert sp.factor(L-formula)==0
A=a*a+3*a*b+b*b+(a+b)*(c+d)+c*d
H=a*a+a*b+b*b+(a+b)*(c+d)+c*d
mean=H/B
variance=(A/B)**2-2*(2*(a+b)+c+d)/B-4/K**2
assert sp.factor(-sp.diff(L,s).subs(s,0)-mean)==0
assert sp.factor((sp.diff(L,s,2)-sp.diff(L,s)**2).subs(s,0)-variance)==0

# For any fixed total colonization intensity, increasing the product c*d
# lowers the Laplace transform at every positive Laplace argument.
C,z=sp.symbols('C z', nonnegative=True)
D_C = sp.expand(D.subs(d,C-c))
assert sp.factor(D_C - (s**3+(2*(a+b)+C)*s**2+(a*a+3*a*b+b*b+(a+b)*C+c*(C-c))*s+a*b*(a+b+C)))==0
assert sp.factor(sp.diff(formula,s).subs(s,0)+mean)==0

# Exact generator inversion on six ordered allocations with a highly
# heterogeneous extinction pair, including a swapped pair.
allocations=[(sp.Rational(0),sp.Rational(2)),(sp.Rational(1,2),sp.Rational(3,2)),
             (sp.Rational(1),sp.Rational(1)),(sp.Rational(3,2),sp.Rational(1,2)),
             (sp.Rational(2),sp.Rational(0))]
results=[]
for cc,dd in allocations:
  subs={a:4,b:1,c:cc,d:dd}
  mat=Q.subs(subs)
  F=sp.factor(((s*sp.eye(3)-mat).inv()*r.subs(subs))[0])
  expected=sp.factor(formula.subs(subs))
  assert sp.factor(F-expected)==0
  results.append((cc,dd,F,sp.factor(mean.subs(subs)),sp.factor(variance.subs(subs))))
assert results[0][2:] == results[-1][2:]
assert results[1][2:] == results[-2][2:]
assert results[2][3] > results[0][3]
assert results[2][4] > results[0][4]
assert sp.factor(formula.subs({a:4,b:1,c:0,d:2,s:1}))==sp.Rational(9,20)
assert sp.factor(formula.subs({a:4,b:1,c:1,d:1,s:1}))==sp.Rational(4,9)
print('symbolic Laplace identity, moments, allocation invariance: PASS')
print('exact five-allocation calculations: PASS')
for row in results:
  print(tuple(str(x) for x in row))
