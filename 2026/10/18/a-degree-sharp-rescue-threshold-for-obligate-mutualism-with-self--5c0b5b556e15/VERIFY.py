from fractions import Fraction as Q
from math import sqrt
import sympy as s
x,a,b,c,k,n=s.symbols('x a b c k n', positive=True)
R=c*(n-1)-b
F=-a+R*x-k*x**3
sc=s.Rational(3,2)*a/R
kc=4*R**3/(27*a*a)
assert s.simplify(F.subs({x:sc,k:kc}))==0
assert s.simplify(s.diff(F,x).subs({x:sc,k:kc}))==0
assert s.factor(F.subs(k,kc)+kc*(x-sc)**2*(x+2*sc))==0
assert s.simplify(((-a+c*n*x-(b+c)*x-k*x**3))-F)==0
assert s.simplify(((c*(n-1)-b)-3*k*sc**2).subs(k,kc))==0
# Four-species n=4, all parameters 1: positive equilibrium polynomial roots
f=s.factor(F.subs({n:4,a:1,b:1,c:1,k:1}))
assert s.expand(f)==-1+2*x-x**3
assert s.simplify(f+(x-1)*(x*x+x-1))==0
lo=(-1+s.sqrt(5))/2
assert s.simplify(f.subs(x,lo))==0
assert s.simplify(f.subs(x,1))==0
assert s.simplify((x*s.diff(f,x)).subs(x,1))==-1
assert (s.simplify((-x*(b+c+3*k*x*x)).subs({x:1,b:1,c:1,k:1}))==-5)
assert float((x*s.diff(f,x)).subs(x,lo))>0
for nv in range(2,10):
 for av,bv,cv,kv in [(1,1,1,1),(3,2,1,0.3),(2,3,5,1)]:
  rr=cv*(nv-1)-bv
  if rr<=0: continue
  kk=4*rr**3/(27*av*av)
  # sign of scalar critical drift at sample points
  xstar=3*av/(2*rr)
  for xv in [0.1*xstar,0.9*xstar,xstar,1.01*xstar,2*xstar]:
   fv=-av+rr*xv-kk*xv**3
   assert fv<1e-9
print('symbolic and sample parameter checks passed')
# Critical saddle-node coefficient and graph spectral separation.
d=s.symbols('d',integer=True,positive=True)
rr=c*d-b
xs=s.Rational(3,2)*a/rr
kt=4*rr**3/(27*a*a)
ff=-a+rr*x-kt*x**3
assert s.simplify(s.diff(x*ff,x,2).subs(x,xs)/2+rr)==0
assert s.simplify(-c*xs*(d-(d-1))+c*xs)==0
# Same parameter set, two connected regular four-species graphs.
assert s.simplify(4*(c*3-b)**3/(27*a*a)).subs({a:1,b:1,c:1})==s.Rational(32,27)
assert s.simplify(4*(c*2-b)**3/(27*a*a)).subs({a:1,b:1,c:1})==s.Rational(4,27)
# For K4 at upper equilibrium 1, J=A-4I with spectrum -1,-5,-5,-5.
A=s.ones(4,4)-s.eye(4)
J=A-4*s.eye(4)
assert J.eigenvals()=={-1:1,-5:3}
assert (s.eye(4)*3/4*(A-3*s.eye(4))).eigenvals()=={0:1,-3:3}
print('critical coefficient and graph eigenvalue checks passed')
