"""Reproduce the exact two-patch periodic-dispersal identities and examples.
Requires Python 3 and SymPy. No external data or network access.
"""
import sympy as S

m,a,b,s=S.symbols('m a b s', real=True, positive=True)
J=S.Matrix([[0,1],[1,0]])
D=S.Matrix([[1-m,s*m],[s*m,1-m]])
A=S.diag(a,b)
B=S.diag(b,a)
T=J*D*A
P=D*B*D*A
assert S.simplify(P-T*T)==S.zeros(2)
tr=S.trace(T)
det=T.det()
assert S.factor(tr-s*m*(a+b))==0
assert S.factor(det-a*b*(s*s*m*m-(1-m)**2))==0
rad=S.factor(tr*tr-4*det)
assert S.simplify(rad-s*s*(a-b)**2*m*m-4*a*b*(1-m)**2)==0
R=(tr+S.sqrt(rad))/2
u=s*(a-b);v=2*S.sqrt(a*b)
h=S.sqrt(u*u*m*m+v*v*(1-m)**2)
assert S.simplify(S.diff(h,m,2)-u*u*v*v/h**3)==0
assert S.simplify(S.diff(R,m).subs(m,0)-(s*(a+b)/2-S.sqrt(a*b)))==0
assert S.simplify((S.diff(R,m).subs(m,1)-s*a).subs(a,b+S.Symbol('delta',positive=True)))==0
assert S.simplify(R.subs(m,0)-S.sqrt(a*b))==0
assert S.simplify((R.subs(m,1)-s*a).subs(a,b+S.Symbol('delta',positive=True)))==0
# Exact rescue example, isolated patches decline but full switching grows.
A0=S.Rational(4);B0=S.Rational(1,5);S0=S.Rational(3,10)
r=S.simplify(R.subs({a:A0,b:B0,s:S0}))
assert S.simplify(r.subs(m,S.Rational(1,10))-S.Rational(87,100))==0
assert S.simplify(r.subs(m,0)**2-S.Rational(4,5))==0
assert S.simplify(r.subs(m,1)-S.Rational(6,5))==0
mstar=(85+5*S.sqrt(1745))/364
assert S.simplify(r.subs(m,mstar)-1)==0
assert 0<float(mstar)<1
# Independent direct-matrix checks at a rational grid, with exact characteristic polynomial.
for av,bv,sv in [(S.Rational(4),S.Rational(1,5),S.Rational(3,10)),(S.Rational(3),S.Rational(1,2),S.Rational(4,5))]:
 for i in range(1,20):
  mv=S.Rational(i,20)
  mat=P.subs({a:av,b:bv,s:sv,m:mv})
  rv=R.subs({a:av,b:bv,s:sv,m:mv})
  assert S.simplify(mat.det()-S.factor(det.subs({a:av,b:bv,s:sv,m:mv}))**2)==0
  assert S.simplify(mat.charpoly().as_expr().subs(mat.charpoly().gen,rv**2))==0
print('PASS: 11 identities, exact rescue threshold and 38 matrix characteristic checks')
