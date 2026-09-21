import sympy as sp

x, y, z, alpha, gamma = sp.symbols("x y z alpha gamma", real=True)
fx = y * (z - 1 + x**2) + gamma * x
fy = x * (3*z + 1 - x**2) + gamma * y
fz = -2*z * (alpha + x*y)

R = x**2 + y**2
W = R + 4*z

def lie(F):
    return sp.expand(sp.diff(F, x)*fx + sp.diff(F, y)*fy + sp.diff(F, z)*fz)

assert sp.simplify(lie(R) - (2*gamma*R + 8*x*y*z)) == 0
assert sp.simplify(lie(W) - (2*gamma*R - 8*alpha*z)) == 0

Sdot_on_S0 = sp.factor((fx + fy).subs(y, -x))
assert sp.simplify(Sdot_on_S0 - 2*x*(z + 1 - x**2)) == 0

N = z - x**2 + 1
Ndot_on = sp.factor(lie(N).subs({y: -x, z: x**2 - 1}))
expected = 2*(3*x**4 - (alpha + gamma + 3)*x**2 + alpha)
assert sp.simplify(Ndot_on - expected) == 0

q = 1 + gamma/2
r = sp.sqrt(q)
special = {alpha: q, x: r, y: -r, z: gamma/2}
assert all(sp.simplify(F.subs(special)) == 0 for F in (fx, fy, fz))

ratio_identity = z*(x+y)**2/R - (z + 2*x*y*z/R)
assert sp.simplify(ratio_identity) == 0

print("all symbolic identities verified")
