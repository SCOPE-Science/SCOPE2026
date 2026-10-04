import sympy as sp

q, lam, X, Y = sp.symbols("q lam X Y")

N1 = 3563201
N2 = 6112121
r1 = sp.sqrt(N1)
r2 = sp.sqrt(N2)

ell1 = -1601*X + 1000*Y + sp.Rational(134133, 500)
ell2 = -2261*X + 1000*Y + sp.Rational(1788717, 1000)

Q = sp.Matrix([
    [20, 0, 0],
    [0, -5, 0],
    [0, 0, 1],
])

def cubic_discriminant(expr):
    p = sp.Poly(sp.expand(expr), lam, domain="EX")
    a, b, c, d = p.all_coeffs()
    return sp.expand(
        b*b*c*c - 4*a*c**3 - 4*b**3*d
        - 27*a*a*d*d + 18*a*b*c*d
    )

def branch(sign):
    sol = sp.solve(
        [
            sp.Eq(ell1, q*r1),
            sp.Eq(ell2, sign*q*r2),
        ],
        [X, Y],
        dict=True,
    )[0]
    cx = sp.simplify(sol[X])
    cy = sp.simplify(sol[Y])

    # q is the signed Euclidean distance to ell1=0, hence q^2 is
    # the squared radius.  The conic below is the corresponding circle.
    C = sp.Matrix([
        [1, 0, -cx],
        [0, 1, -cy],
        [-cx, -cy, cx**2 + cy**2 - q**2],
    ])

    pencil = sp.expand((Q + lam*C).det())
    disc = cubic_discriminant(pencil)
    p = sp.Poly(disc, q, extension=[r1 + r2])

    assert p.degree() == 8
    assert sp.Poly(sp.sqf_part(p.as_expr()), q, extension=[r1 + r2]).degree() == 8
    real_count = p.count_roots(-sp.oo, sp.oo)

    # q=0 would be a zero-radius circle; it is not a root on either branch.
    assert p.eval(0) != 0

    return p, int(real_count)

p_plus, c_plus = branch(+1)
p_minus, c_minus = branch(-1)

assert c_plus == 8
assert c_minus == 6
assert c_plus + c_minus == 14

print("field=Q(sqrt(3563201)+sqrt(6112121))")
print("plus_degree=", p_plus.degree(), sep="")
print("plus_real_roots=", c_plus, sep="")
print("minus_degree=", p_minus.degree(), sep="")
print("minus_real_roots=", c_minus, sep="")
print("total_real_parameter_roots=", c_plus + c_minus, sep="")
print("VERIFY_OK")
