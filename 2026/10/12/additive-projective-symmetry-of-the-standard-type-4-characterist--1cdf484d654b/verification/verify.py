import sympy as sp

# Exact symbolic verification over characteristic 2.
u, v, t = sp.symbols("u v t")
x, y, z = sp.symbols("x y z")
a, b, c, d = sp.symbols("a b c d")
lam, mu = sp.symbols("lam mu")


def zero_mod2(expr, *gens):
    return sp.Poly(sp.expand(expr), *gens, modulus=2).is_zero


# Curve and normalization.
F = y**4 + x*z**3 + x**3*z
Xn = u**4
Yn = u*v*(u + v)**2
Zn = v**4
assert zero_mod2(F.subs({x: Xn, y: Yn, z: Zn}), u, v)

# Dense-chart rational inverse t = Y(1+Z)/(1+Z+Y^2).
Yt = t*(1 + t)**2
Zt = t**4
assert zero_mod2(Yt*(1 + Zt) - t*(1 + Zt + Yt**2), t)

# Singular-point derivative identities.
Fx, Fy, Fz = [sp.diff(F, q) for q in (x, y, z)]
assert zero_mod2(Fx - z*(x + z)**2, x, y, z)
assert zero_mod2(Fy, x, y, z)
assert zero_mod2(Fz - x*(x + z)**2, x, y, z)

# Linear-series preservation under a general PGL_2 matrix.
U = a*u + b*v
V = c*u + d*v
W = sp.expand(U*V*(U + V)**2)
Pw = sp.Poly(W, u, v)
c31 = Pw.coeff_monomial(u**3*v)
c22 = Pw.coeff_monomial(u**2*v**2)
c13 = Pw.coeff_monomial(u*v**3)
Delta = a*d + b*c
assert zero_mod2(c22 - Delta*(a*b + c*d), a, b, c, d)
# Fixing q=[1:1] gives d=a+b+c; then the mixed odd coefficients agree.
assert zero_mod2((c31 - c13).subs(d, a + b + c), a, b, c)
# The remaining condition factors exactly.
assert zero_mod2((a*b + c*d).subs(d, a + b + c) - (a + c)*(b + c), a, b, c)
# The factor a+c=0 would force a=c,d=b and determinant zero.
assert zero_mod2(Delta.subs({c: a, d: b}), a, b)
# Therefore b=c,d=a; determinant is (a+b)^2.
assert zero_mod2(Delta.subs({c: b, d: a}) - (a + b)**2, a, b)

# Normalized additive matrices on P^1.
Ulam = (1 + lam)*u + lam*v
Vlam = lam*u + (1 + lam)*v
assert zero_mod2(Ulam + Vlam - (u + v), u, v, lam)
assert zero_mod2(Vlam - (v + lam*(u + v)), u, v, lam)

# Induced transformation on plane coordinates.
Xp = (1 + lam**4)*x + lam**4*z
Yp = y + (lam + lam**2)*(x + z)
Zp = lam**4*x + (1 + lam**4)*z
assert zero_mod2(Ulam**4 - Xp.subs({x: u**4, y: Yn, z: v**4}), u, v, lam)
assert zero_mod2(Vlam**4 - Zp.subs({x: u**4, y: Yn, z: v**4}), u, v, lam)
assert zero_mod2(Ulam*Vlam*(Ulam + Vlam)**2 - Yp.subs({x: u**4, y: Yn, z: v**4}), u, v, lam)

# Preservation of the quartic equation.
assert zero_mod2(F.xreplace({x: Xp, y: Yp, z: Zp}) - F, x, y, z, lam)

# Matrix form and additive composition law.
def T(q):
    return sp.Matrix([
        [1 + q**4, 0, q**4],
        [q + q**2, 1, q + q**2],
        [q**4, 0, 1 + q**4],
    ])

M = T(lam)*T(mu) - T(lam + mu)
for entry in M:
    assert zero_mod2(entry, lam, mu)
assert zero_mod2(T(lam).det() - 1, lam)

# Both the singular point [1:0:1] and strange point [0:1:0] are fixed exactly.
pvec = sp.Matrix([1, 0, 1])
nvec = sp.Matrix([0, 1, 0])
for vec in (T(lam)*pvec - pvec, T(lam)*nvec - nvec):
    for entry in vec:
        assert zero_mod2(entry, lam)

print("VERIFY_OK stabilizer=Ga smooth_orbit=simple_transitive characteristic=2")
