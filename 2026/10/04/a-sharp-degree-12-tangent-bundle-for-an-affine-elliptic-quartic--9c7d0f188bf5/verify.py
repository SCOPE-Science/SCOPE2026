import sympy as sp

x, y, z, u, v, w = sp.symbols("x y z u v w")

f = 1 + x**2 + y**2 + z**2
g = 1 + 2*x**2 + 3*y**2 + 4*z**2
t1 = x*u + y*v + z*w
t2 = 2*x*u + 3*y*v + 4*z*w

L1 = -2*x + y + 3*z + 3*u + 3*v - 3*w - 1
L2 = -3*x + 3*z + 2*w

G = sp.groebner(
    [f, g, t1, t2, L1, L2],
    x, y, z, u, v, w,
    order="lex",
    domain=sp.QQ,
)

assert G.is_zero_dimensional
assert len(G.polys) == 6

# The reduced lex basis has leading monomials
# x, y, z, u, v, w^12.  Hence the quotient has basis
# 1,w,...,w^11 and length 12.
expected_lms = [
    x, y, z, u, v, w**12
]
actual_lms = [p.LM(order=G.order).as_expr() for p in G.polys]
assert actual_lms == expected_lms

univariate = [
    p.as_expr() for p in G.polys
    if p.as_expr().free_symbols <= {w}
]
assert len(univariate) == 1
h = sp.Poly(univariate[0], w, domain=sp.QQ)
assert h.degree() == 12
assert sp.gcd(h, h.diff()).degree() == 0

primitive = sp.primitive(sp.together(h.as_expr()))[1]
num, den = sp.fraction(primitive)
num = sp.Poly(num, w, domain=sp.ZZ)
assert num.degree() == 12

# Independent arithmetic for the projective curve:
# a smooth (2,2) complete intersection has degree 4 and genus 1.
D = 2 * 2
two_g_minus_two = (2 + 2 - 4) * D
assert D == 4
assert two_g_minus_two == 0
genus = 1 + two_g_minus_two // 2
assert genus == 1

# A general plane projection of a smooth nondegenerate space curve
# has delta = p_a(plane degree D) - g ordinary nodes.
mu = (D - 1) * (D - 2) // 2 - genus
assert mu == 2

# Lanciano's secant-corrected bound in this case.
upper = D**2 - 2 * mu * 1
assert upper == 12

print("groebner_leading_monomials=x,y,z,u,v,w^12")
print("section_length=12")
print("section_reduced=true")
print("degree_V=4")
print("genus_X=1")
print("general_secant_count=2")
print("secant_corrected_upper_bound=12")
print("eliminant_integer_polynomial=" + str(num.as_expr()))
print("VERIFY_OK")
