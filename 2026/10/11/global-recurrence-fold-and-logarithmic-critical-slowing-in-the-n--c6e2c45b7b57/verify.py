"""Exact polynomial checks for the negative-forcing Sprott M fold.

Requires Python 3 and SymPy. Run: python verify.py
The statements about infinite-time dynamics remain analytic theorems.
"""
import sympy as s

x, y, z, a, b, u, w, h, lam = s.symbols('x y z a b u w h lam', real=True)
f = s.Matrix([-z, -x*x-y, a+b*x+y])
qdot = s.diff(y+z,x)*f[0] + s.diff(y+z,y)*f[1] + s.diff(y+z,z)*f[2]
delta = b*b+4*a
assert s.simplify(qdot-(delta/4-(x-b/2)**2))==0
J = f.jacobian((x,y,z))
r = s.symbols('r', real=True)
chi = s.expand((lam*s.eye(3)-J.subs({x:r,y:-r*r,z:0})).det())
assert s.factor(chi-(lam**3+lam**2+b*lam+b-2*r))==0
# Exact critical coordinate transformation and invariance up to cubic order.
ac = -b*b/4
X = s.Matrix([b/2+u, -b*b/4-b*u+h, w])
fs = f.subs({x:X[0],y:X[1],z:X[2],a:ac})
assert s.simplify(fs[0]+w)==0
assert s.simplify(fs[2]-h)==0
assert s.simplify(fs[1]+b*fs[0]+h+b*w+u*u)==0
W = -u*u/b + 2*u**3/b**3
H = -2*u**3/b**2
assert s.series(s.diff(W,u)*(-W)-H,u,0,4).removeO().expand()==0
assert s.series(s.diff(H,u)*(-W)+H+b*W+u*u,u,0,4).removeO().expand()==0
# u'=-W, and R=-b/u implies R'=b*(-W)/u^2.
assert s.simplify(s.expand(b*(-W)/u**2)-(1-2*u/b**2))==0
print('PASS: global identity, Jacobian, critical coordinate map, cubic invariance, logarithmic coefficient')
