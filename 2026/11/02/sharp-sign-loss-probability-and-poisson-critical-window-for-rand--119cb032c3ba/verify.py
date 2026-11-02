"""Reproducible tests for a randomized two-stage implicit Runge--Kutta positivity law.

Requires Python 3.10+ and SymPy 1.10+. Run `python verify.py`.
The finite checks supplement, rather than replace, the analytical proof.
"""
from fractions import Fraction as F
from math import sqrt, log, exp
from random import Random
import sympy as s

x, z = s.symbols('x z', real=True)
r = s.symbols('r', positive=True)
A = s.Matrix([[x, 0], [1 - 2*x, x]])
weights = s.Matrix([[s.Rational(1,2), s.Rational(1,2)]])
R = s.factor(1 + z*(weights*(s.eye(2)-z*A).inv()*s.ones(2,1))[0])
num = 2+(4*x-2)*r+(2*x*x-4*x+1)*r*r
assert s.simplify(R.subs(z,-r) - num/(2*(1+x*r)**2)) == 0
assert s.simplify(num.subs(x,s.Rational(1,2))-(2-r*r/2)) == 0
assert s.simplify(num.subs(x,1)-(2+2*r-r*r)) == 0
assert s.simplify(num.subs(x,1-1/r)+r*(r-2)) == 0
assert s.simplify(s.discriminant(num,x)-8*r**3*(r-2)) == 0
assert s.simplify(s.diff(num,x,2)-4*r*r) == 0
assert s.factor(s.diff(num,x).subs({r:2,x:s.Rational(1,2)})) == 0
assert s.simplify(num.subs({r:2,x:s.Rational(1,2)})) == 0
assert s.simplify(num.subs({r:1+s.sqrt(3), x:1})) == 0
mean = s.simplify(2*s.integrate(R.subs(z,-r),(x,s.Rational(1,2),1)))
formula_mean = 2-1/(1+r)+4*s.log((2+r)/(2*(1+r)))
assert s.simplify(s.logcombine(s.expand_log(mean-formula_mean, force=True),force=True)) == 0
assert s.simplify(s.diff(formula_mean,r)+(3*r+2)/((r+1)**2*(r+2))) == 0
assert s.simplify(formula_mean.subs(r,0)-1)==0

# Exact rational stage equations versus rational amplification formula.
checks=0
for rr in [F(0),F(1,2),F(1),F(3,2),F(2),F(21,10),F(5,2),F(3),F(5),F(12)]:
 for k in range(0,101):
  xx=F(1,2)+F(k,200)
  # Linear test f(y)=-lambda*y, lambda*h=rr, with initial value 1.
  first=F(1,1)/(1+xx*rr)
  second=(1-rr*(1-2*xx)*first)/(1+xx*rr)
  result=1-rr*(first+second)/2
  direct=(2+(4*xx-2)*rr+(2*xx*xx-4*xx+1)*rr*rr)/(2*(1+xx*rr)**2)
  assert result==direct
  assert abs(result)<=1
  if rr<=2 and xx>F(1,2) or rr<2:
   assert direct>0
  if rr>=3:
   assert direct<0
  checks+=1

# Closed-form probability checked by integration over a dense deterministic grid.
def probability(t):
 if t<=2: return 0.
 if t>=1+sqrt(3): return 1.
 return 1-2/t+sqrt(2-4/t)

for tt in [2.000001,2.001,2.01,2.1,2.2,2.5,2.7,1+sqrt(3),3.0,5.0]:
 count=0
 n=20000
 for j in range(n):
  xx=.5 + (j+.5)/(2*n)
  q=2+(4*xx-2)*tt+(2*xx*xx-4*xx+1)*tt*tt
  count+=(q<0)
 assert abs(count/n-probability(tt))<=2/n, (tt,count/n,probability(tt))
 checks+=1

# Critical n^{-2} window, Poisson count and parity formulas at several sizes.
for c in [0.,.25,1.,4.,9.]:
 for n in [100,1000,10000]:
  pp=probability(2+c/(n*n))
  assert abs(n*pp-sqrt(c))< max(.1,5*sqrt(c)/n)
  no_flip=(1-pp)**n
  parity=(1+(1-2*pp)**n)/2
  assert abs(no_flip-exp(-sqrt(c)))< max(.05,4*sqrt(c)/n)
  assert abs(parity-(1+exp(-2*sqrt(c)))/2) < max(.05,8*sqrt(c)/n)
  checks+=1

# Seeded sampling checks a genuine independent two-stage simulation.
rng=Random(20260721)
for tt in [1.5,2.01,2.2,2.5,2.72,3.]:
 count=0
 trials=50000
 for i in range(trials):
  xx=.5+.5*rng.random()
  q=2+(4*xx-2)*tt+(2*xx*xx-4*xx+1)*tt*tt
  count+=(q<0)
 phat=count/trials
 pp=probability(tt)
 assert abs(phat-pp) < .014, (tt,phat,pp)
 checks+=1
print('PASS:', checks, 'stage/probability/critical-window checks, and 12 symbolic assertions.')
print('Mean multiplier sign-crossing:', s.nsolve(formula_mean, 2.2))
