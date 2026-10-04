import sympy as sp

A, B = sp.symbols("A B", positive=True)
t = sp.symbols("t", real=True)
a = A**3
b = B**3
S = A**2 + B**2
L = S**sp.Rational(3, 2)
kappa = A*B/S
t0 = sp.atan(B/A)

G = a/sp.cos(t) + b/sp.sin(t)
H = 1/(sp.sin(t)*sp.cos(t))

G0 = sp.trigsimp(G.subs(t, t0))
H0 = sp.trigsimp(H.subs(t, t0))
Gp0 = sp.trigsimp(sp.diff(G, t).subs(t, t0))
Gpp0 = sp.trigsimp(sp.diff(G, t, 2).subs(t, t0))
Hp0 = sp.trigsimp(sp.diff(H, t).subs(t, t0))

assert sp.simplify(G0 - L) == 0
assert sp.simplify(H0 - 1/kappa) == 0
assert sp.simplify(Gp0) == 0
assert sp.simplify(Gpp0 - 3*S**sp.Rational(3, 2)) == 0
assert sp.simplify(Hp0 + (A**2-B**2)*S/(A**2*B**2)) == 0

n2 = sp.simplify(-Hp0**2/Gpp0)
expected_n2 = -(A**2-B**2)**2*sp.sqrt(S)/(3*A**4*B**4)
assert sp.simplify(n2 - expected_n2) == 0

mu = (A**2-B**2)**2*sp.sqrt(S)/(6*A**4*B**4)
assert sp.simplify(-n2/2 - mu) == 0

print("VERIFY_OK")
