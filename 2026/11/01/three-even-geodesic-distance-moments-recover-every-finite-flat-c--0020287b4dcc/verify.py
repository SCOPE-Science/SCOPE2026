import sympy as s
from fractions import Fraction
import math, random
u,v,x,y,t=s.symbols('u v x y t',real=True)
m2=u/s.Integer(3)+v/s.Integer(6)
m4=u**2/s.Integer(5)+u*v/s.Integer(9)+v**2/s.Integer(15)
m6=u**3/s.Integer(7)+u*u*v/s.Integer(10)+u*v*v/s.Integer(15)+v**3/s.Integer(28)
for moment,expect in [(m2,1/s.Integer(6)),(m4,(11*x*x-7*x+3)/45),(m6,(-32*x**3+110*x*x-62*x+15)/420)]:
 assert s.factor(moment.subs({u:x,v:1-2*x})-expect)==0
print('EXACT_MOMENT_POLYNOMIALS_PASSED')
f4=(11*x*x-7*x+3)/45
f6=(-32*x**3+110*x*x-62*x+15)/420
assert s.factor((f4-f4.subs(x,y))/(x-y)-(11*(x+y)-7)/45)==0
expr=s.factor((f6-f6.subs(x,y))/(x-y))
sum_condition=s.Rational(7,11)
assert s.factor(expr.subs(y,sum_condition-x)+2*(484*(x-s.Rational(7,22))**2+26)/12705)==0
assert s.factor(s.diff(f6,x).subs(x,s.Rational(7,22))+s.Rational(52,12705))==0
x1=s.Rational(1,4);x2=s.Rational(17,44)
assert x1!=x2 and 0<x1<s.Rational(1,2) and 0<x2<s.Rational(1,2)
assert s.factor(f4.subs(x,x1)-f4.subs(x,x2))==0
assert s.factor(f6.subs(x,x1)-f6.subs(x,x2))!=0
print('SHARP_TWO_MOMENT_FOLD_AND_THIRD_MOMENT_SEPARATION_PASSED')
# exact numerical checks by 2D integration independent of moments. quadrature scipy quad 2D transformed:
from scipy.integrate import quad
for C,H in [(1,1),(1,0.3),(1,2.5),(math.sqrt(17/11), math.sqrt(5/22)),(2,2)]:
 Q=C/2
 def integrate_moment(k):
  # x uniformly [0,Q], vertical difference Y triangular 2(H-y)/H^2
  return quad(lambda xx:quad(lambda yy:(xx*xx+yy*yy)**k*2*(H-yy)/H**2,0,H,epsabs=1e-11)[0]/Q,0,Q,epsabs=1e-11)[0]
 U=Q**2; V=H**2
 expected=(U/3+V/6,U**2/5+U*V/9+V**2/15,U**3/7+U**2*V/10+U*V**2/15+V**3/28)
 for k, want in enumerate(expected,1):
  actual=integrate_moment(k)
  assert abs(actual-want)<3e-10*max(1,abs(want)),(C,H,k,actual,want)
print('INDEPENDENT_TWO_COORDINATE_QUADRATURE_PASSED')
print('ALL_CHECKS_PASSED')
