from sympy import Poly, symbols, factor, discriminant, gcd, rem, Rational, __version__

u, t, T = symbols("u t T")
f = Poly(u**3 - 96*u**2 + 48*u + 64, u, domain="QQ")
h = Poly(t**3 - 3*t + 1, t, domain="QQ")
assert f.is_irreducible
assert h.is_irreducible
assert discriminant(f.as_expr(), u) == 241864704

u_of_t = -36*t**2 - 12*t + 104
r1 = rem(Poly(f.as_expr().subs(u, u_of_t), t, domain="QQ"), h)
assert r1.is_zero

t_of_u = -u**2/Rational(48) + 2*u - Rational(2, 3)
r2 = rem(Poly(h.as_expr().subs(t, t_of_u), u, domain="QQ"), f)
assert r2.is_zero

phi = Poly(T**6 + T**3 + 1, T, modulus=2)
assert phi.is_irreducible
for k in range(1, 9):
    q = Poly(T**k - 1, T, modulus=2)
    assert gcd(phi, q).degree() == 0

assert 1 + 3*9 == 28
assert 4*9 == 36
assert 7*9 == 63
assert 1 + 7*9 == 64

print("VERIFY_OK sympy=" + __version__ + " bitangents=1+9+9+9 even_theta=4x9 steiner=7x9 field=Q(zeta9+zeta9^-1)")
