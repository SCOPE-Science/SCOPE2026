#!/usr/bin/env python3
"""Symbolic checks for the Rabinovich--Fabrikant balance identities."""

import sympy as sp

x, y, z, alpha, gamma = sp.symbols("x y z alpha gamma", real=True)
f1 = y * (z - 1 + x**2) + gamma * x
f2 = x * (3*z + 1 - x**2) + gamma * y
f3 = -2*z * (alpha + x*y)

q = x**2 + y**2
W = q + 4*z

def lie(expr):
    return sp.expand(sp.diff(expr, x)*f1 + sp.diff(expr, y)*f2 + sp.diff(expr, z)*f3)

checks = {
    "W_balance": sp.simplify(lie(W) - (2*gamma*q - 8*alpha*z)),
    "plane_q_balance": sp.simplify(lie(q).subs(z, 0) - 2*gamma*q),
    "sum_derivative_on_y_minus_x": sp.factor((f1 + f2).subs(y, -x) + 2*x*(x**2-z-1)),
}

r, theta = sp.symbols("r theta", positive=True, real=True)
xp = r*sp.cos(theta)
yp = r*sp.sin(theta)
g1 = yp*(xp**2 - 1)
g2 = xp*(1 - xp**2)
theta_dot = sp.simplify((xp*g2 - yp*g1)/r**2)
checks["gamma0_plane_theta"] = sp.trigsimp(theta_dot - (1-r**2*sp.cos(theta)**2))

for name, residual in checks.items():
    print(f"{name}: {sp.simplify(residual)}")
    assert sp.simplify(residual) == 0

print("all symbolic residuals vanish")
