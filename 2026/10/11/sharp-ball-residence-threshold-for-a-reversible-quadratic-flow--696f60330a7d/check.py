"""Symbolic consistency checks for the Li–Sprott constant-forced quadratic flow.
This is a finite symbolic algebra verifier, not a proof of global dynamical statements.
"""
import sympy as s
x,y,z,a=s.symbols('x y z a',real=True)
F=s.Matrix([1+y*z,-x*z,y*y+a*y*z])
Lie=lambda q:s.expand(s.diff(q,x)*F[0]+s.diff(q,y)*F[1]+s.diff(q,z)*F[2])
P=z-a*x
assert s.simplify(Lie(P)-(y*y-a))==0
assert s.simplify(Lie(x)-(1+y*z))==0
assert s.simplify(Lie(z)-y*y-a*y*z)==0
G=(a+1/a)*x-(1-1/a**2)*z
Rstar2=a+1/a
r2=x*x+y*y+z*z
certificate=Rstar2-r2+x*x+(z+y/a)**2
assert s.cancel(Lie(G)-certificate)==0
# Exact decomposition of stationary radial mean square by P and x coboundaries.
Q=r2-Rstar2-x*x-(z+y/a)**2
identity=(1-1/a**2)*(y*y-a)-(2/a)*(1+y*z)
assert s.cancel(Q-identity)==0
for v in (s.Rational(1,4),s.Rational(1,2),s.Rational(1),s.Rational(2),s.Rational(9,2)):
 for sign in (-1,1):
  E={x:0,y:sign*s.sqrt(v),z:-sign/s.sqrt(v),a:v}
  assert all(s.simplify(ff.subs(E))==0 for ff in F)
  assert s.simplify(r2.subs(E)-(v+1/v))==0
print('PASS: Lie derivative identities, stationary square decomposition and ten exact equilibria.')
