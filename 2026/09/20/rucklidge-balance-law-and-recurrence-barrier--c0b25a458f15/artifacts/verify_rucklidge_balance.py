#!/usr/bin/env python3
"""Exact symbolic checks for the published Rucklidge/Shimizu-Morioka identities."""
import sympy as sp

x, y, z, a, b = sp.symbols("x y z a b")
xd = -a*x + b*y - y*z
yd = x
zd = y**2 - z
F = sp.Rational(1, 2)*x**2 - sp.Rational(1, 2)*b*y**2 + sp.Rational(1, 2)*y**2*z - sp.Rational(1, 4)*z**2
LF = sp.diff(F, x)*xd + sp.diff(F, y)*yd + sp.diff(F, z)*zd
rucklidge_residual = sp.factor(sp.expand(LF - (-a*x**2 + sp.Rational(1, 2)*zd**2)))

u, v, w, lam, alpha = sp.symbols("u v w lam alpha")
ud = v
vd = u - lam*v - u*w
wd = u**2 - alpha*w
G = sp.Rational(1, 2)*v**2 - sp.Rational(1, 2)*u**2 + sp.Rational(1, 2)*u**2*w - sp.Rational(1, 4)*alpha*w**2
LG = sp.diff(G, u)*ud + sp.diff(G, v)*vd + sp.diff(G, w)*wd
shimizu_morioka_residual = sp.factor(sp.expand(LG - (-lam*v**2 + sp.Rational(1, 2)*wd**2)))

# Generator identities used for stationary moments.
H_y2 = y**2 / 2
H_z = z
H_z2 = z**2 / 2
H_xy = x*y

def L(H):
    return sp.factor(sp.expand(sp.diff(H, x)*xd + sp.diff(H, y)*yd + sp.diff(H, z)*zd))

print("Rucklidge balance residual:", rucklidge_residual)
print("Shimizu-Morioka balance residual:", shimizu_morioka_residual)
print("L(y^2/2) =", L(H_y2))
print("L(z) =", L(H_z))
print("L(z^2/2) =", L(H_z2))
print("L(x y) =", L(H_xy))

assert rucklidge_residual == 0
assert shimizu_morioka_residual == 0
