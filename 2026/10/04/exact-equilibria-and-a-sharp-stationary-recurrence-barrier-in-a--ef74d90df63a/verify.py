#!/usr/bin/env python3
import sympy as sp

a = sp.symbols('a', real=True)
b, c = sp.symbols('b c', positive=True)
d = sp.symbols('d', real=True, nonzero=True)
x, y, z, w = sp.symbols('x y z w', real=True)
sig = sp.symbols('sig', real=True)

f = sp.Matrix([a*x-y*z+w, x*z-b*y, x*y-c*z, -y+d])

# d != 0 equilibria; sig^2 = 1.
r = sp.sqrt(b*c)
q = sp.sqrt(b/c)
E = {x:sig*r, y:d, z:sig*d*q, w:sig*r*(d**2/c-a)}
vals = [sp.simplify(expr.subs(E)).subs(sig**2,1) for expr in f]
assert all(sp.simplify(v)==0 for v in vals), vals

# d = 0 equilibrium line.
xi = sp.symbols('xi', real=True)
f0 = sp.Matrix([a*x-y*z+w, x*z-b*y, x*y-c*z, -y])
assert all(sp.simplify(v)==0 for v in f0.subs({x:xi,y:0,z:0,w:-a*xi}))

# Sign conjugacy T f_d = f_-d T.
Tq = sp.Matrix([-x,-y,z,-w])
DT = sp.diag(-1,-1,1,-1)
f_minus_at_T = sp.Matrix([
    a*Tq[0]-Tq[1]*Tq[2]+Tq[3],
    Tq[0]*Tq[2]-b*Tq[1],
    Tq[0]*Tq[1]-c*Tq[2],
    -Tq[1]-d
])
assert sp.simplify(f_minus_at_T - DT*f) == sp.zeros(4,1)

# Generator identities.
Lf_w = f[3]
Lf_y2_minus_z2 = sp.expand(2*y*f[1]-2*z*f[2])
assert sp.expand(Lf_w - (-y+d)) == 0
assert sp.expand(Lf_y2_minus_z2 - (-2*b*y**2+2*c*z**2)) == 0

# Equality-case quartic from y=d, x*z=b*d, w constant.
# Differentiate x*z and clear the denominator after z=b*d/x.
expr = sp.expand((a*x-d*z+w)*z + x*(d*x-c*z))
cleared = sp.factor((expr.subs(z,b*d/x) / d) * x**2)
quartic = x**4 + (a-c)*b*x**2 + b*w*x - b**2*d**2
assert sp.expand(cleared-quartic) == 0

# Source Eq. (4) branch: s^2 = b*d^2/c, x=(c/d)s, y=d, z=s,
# w=(1-a*c/d)s. The first component residual is (1-d)s.
s = sp.symbols('s', real=True)
source_residual = sp.expand(a*(c/d)*s - d*s + (1-a*c/d)*s)
assert sp.expand(source_residual-(1-d)*s) == 0

# Baseline numerical values from the source.
A=sp.Rational(8); B=sp.Rational(40); C=sp.Rational(15); D=sp.Rational(-1,10)
S=sp.sqrt(B*D**2/C)
X=C/D*S
Z=S
W_source=(1-A*C/D)*S
W_true=-A*X+D*Z
res=sp.simplify(A*X-D*Z+W_source)
assert sp.simplify(res-(1-D)*S)==0
assert sp.simplify(A*X-D*Z+W_true)==0
print('baseline_corrected=', [sp.N(X,13), sp.N(D,13), sp.N(Z,13), sp.N(W_true,13)])
print('baseline_source_w=', sp.N(W_source,13))
print('baseline_source_residual=', sp.N(res,13))
print('VERIFY_OK')
