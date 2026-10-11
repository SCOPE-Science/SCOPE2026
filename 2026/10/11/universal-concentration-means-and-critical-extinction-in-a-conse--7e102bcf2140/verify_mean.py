"""Symbolic checks for the homogenized Wilhelm--Heinrich mass-action model.

Run with Python 3 and SymPy 1.10 or later: python verify_mean.py
The identities supplement, and do not replace, the analytical proof.
"""
import sympy as sp
x,y,z,w,p,q,r,s,C=sp.symbols('x y z w p q r s C',positive=True)
X=x*w-r*x-p*x*y
Y=s*z-q*y
Z=r*x-s*z
W=p*x*y+q*y-x*w
alpha=(1+p)/q
beta=alpha+1/s
D=1+r*beta
delta=C-r
assert sp.simplify(X+Y+Z+W)==0
phi_dot=sp.cancel(X/x-alpha*Y-beta*Z)
assert sp.simplify(phi_dot-(delta-D*x).subs(C,x+y+z+w))==0
assert sp.simplify((Y+Z)-(r*x-q*y))==0
assert sp.simplify(Z-(r*x-s*z))==0
xstar=delta/D
ystar=r*xstar/q
zstar=r*xstar/s
wstar=r+p*r*xstar/q
for expr in (X,Y,Z,W):
    assert sp.simplify(expr.subs({x:xstar,y:ystar,z:zstar,w:wstar}))==0
assert sp.simplify(xstar+ystar+zstar+wstar-C)==0
# At the critical total mass C=r, the formal asymptotic profile is
# (x,y,z)~(1,r/q,r/s)/(D*t); the identities check its consistency.
assert sp.simplify((1+(1+p)*r/q+r/s)-D)==0
print('CHECK_OK: conservation, exact logarithmic coboundary, integrated balances, equilibrium, critical coefficient')
