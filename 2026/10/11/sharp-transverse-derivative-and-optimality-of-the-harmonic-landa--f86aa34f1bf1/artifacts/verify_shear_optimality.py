#!/usr/bin/env python3
import sympy as sp
import mpmath as mp

r, x, rho = sp.symbols("r x rho", positive=True, real=True)
t = sp.symbols("t", real=True)

# Kernel identity.
z = sp.exp(sp.I*t)
series_closed = sp.im(z / (1-r*z)**2).expand(complex=True)
target_kernel = (1-r**2)*sp.sin(t)/(1-2*r*sp.cos(t)+r**2)**2
assert sp.simplify(sp.trigsimp(series_closed - target_kernel)) == 0

# Exact extremal integral after x=cos(t).
H = (1-r**2)/(1-2*r*x+r**2)**2
A = sp.integrate(H, (x, 0, 1)) - sp.integrate(H, (x, -1, 0))
sharp = sp.simplify(2*A/sp.pi)
assert sp.simplify(sharp - 8*r/(sp.pi*(1-r**4))) == 0

# Source derivative from the explicit real-coordinate formula.
y = sp.symbols("y", real=True)
u = -sp.Rational(2,1)/sp.pi * sp.atan(
    4*x*y/(1-(x**2+y**2)**2)
)
uy_axis = sp.simplify(sp.diff(u, y).subs(y, 0))
assert sp.simplify(uy_axis + 8*x/(sp.pi*(1-x**4))) == 0

# Threshold factorization.
eq = sp.expand(
    8*rho
    + sp.pi*(1-rho**4)
    - 4*(1+rho**2)
)
Q = sp.pi*rho**3 + sp.pi*rho**2 + (sp.pi+4)*rho + sp.pi - 4
assert sp.simplify(eq + (rho-1)*Q) == 0

# Q is strictly increasing on rho>0.
Qp = sp.diff(Q, rho)
assert sp.expand(Qp) == 3*sp.pi*rho**2 + 2*sp.pi*rho + sp.pi + 4

mp.mp.dps = 80
def q(v):
    return mp.pi*v**3 + mp.pi*v**2 + (mp.pi+4)*v + mp.pi - 4

root = mp.findroot(q, (mp.mpf("0.11"), mp.mpf("0.12")))
M = (1+root**2)/(2*root)

assert mp.mpf("0.11384751816255312") < root < mp.mpf("0.11384751816255314")
assert mp.mpf("4.4487630197851664") < M < mp.mpf("4.4487630197851665")

print("VERIFY_OK")
print("rho_star =", mp.nstr(root, 60))
print("M_shear =", mp.nstr(M, 60))
print("sharp_derivative =", "8r/(pi(1-r^4))")
