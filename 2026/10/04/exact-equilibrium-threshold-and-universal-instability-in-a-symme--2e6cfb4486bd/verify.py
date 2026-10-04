#!/usr/bin/env python3
import sympy as sp
import numpy as np

x, y, z, nu, t, lam = sp.symbols('x y z nu t lam', real=True)
f = sp.Matrix([
    y - 2*x*z,
    -x + sp.Rational(1,2)*(1-x**2)*y - sp.Rational(1,2)*y*z,
    sp.Rational(1,10)*x*y + nu*x**2 - sp.Rational(4,5),
])

r2 = 1 + t + 1/t
nu_t = sp.factor(t*(t**2+t+5)/(5*(t**2+t+1)))
r = sp.sqrt(r2)
E = {x:r, y:-2*t*r, z:-t, nu:nu_t}
assert all(sp.factor(sp.simplify(v.subs(E))) == 0 for v in f)

X2 = 1 - z - 1/z
nu_from_z = sp.factor(sp.Rational(4,5)/X2 - z/5)
assert sp.factor(nu_from_z.subs(z,-t) - nu_t) == 0

P = t**4 + 2*t**3 - t**2 + 2*t + 5
assert sp.factor(sp.diff(nu_t,t) - P/(5*(t**2+t+1)**2)) == 0

J = f.jacobian([x,y,z])
JE = sp.simplify(J.subs(E))
a1 = (1-4*t**2)/(2*t)
a2 = (15-17*t-17*t**2)/10
a3 = 2*P/(5*t)
expected = sp.expand(lam**3 + a1*lam**2 + a2*lam + a3)
actual = sp.expand((lam*sp.eye(3)-JE).det())
assert sp.factor(actual-expected) == 0

N = 60*t**4 + 52*t**3 - 69*t**2 - 33*t - 25
assert sp.factor(a1*a2-a3 - N/(20*t)) == 0

# The source's two displayed equilibrium relations do not by themselves
# annihilate the second component of the vector field.
y_src = 8/x - 10*nu*x
z_src = 4/x**2 - 5*nu
residual = sp.factor(sp.together(f[1].subs({y:y_src,z:z_src})))
assert residual != 0

# Numerical replay at a published chaotic parameter value.
poly = sp.Poly(t**3-(5*nu-1)*t**2+(5-5*nu)*t-5*nu, t)
poly_021 = sp.Poly(poly.as_expr().subs(nu,sp.Rational(21,100)), t)
roots = [complex(v) for v in sp.nroots(poly_021)]
pos_t = [v.real for v in roots if abs(v.imag) < 1e-12 and v.real > 0]
assert len(pos_t) == 1
T = pos_t[0]
Jn = np.array(JE.subs(t,T).evalf(), dtype=float)
eigs = np.linalg.eigvals(Jn)
assert sum(ev.real > 1e-9 for ev in eigs) == 2
assert sum(ev.real < -1e-9 for ev in eigs) == 1

print('nu_0.21_t=', format(T,'.15g'))
print('nu_0.21_eigenvalues=', [complex(ev) for ev in eigs])
print('VERIFY_OK')
