import sympy as sp

m, a = sp.symbols("m a", positive=True)
A = sp.symbols("A", positive=True)

# Exact scalar reduction of the b=1, k=2 source system after x1=A and x2*x3=A**2.
reduced = sp.expand(m * (a + m**2) - (a * m**2 + 1))
expected = sp.expand((m - 1) * (m**2 + (1 - a) * m + 1))
assert sp.expand(reduced - expected) == 0
assert sp.factor(sp.discriminant(m**2 + (1-a)*m + 1, m)) == (a - 3) * (a + 1)

mp = ((a - 1) + sp.sqrt((a - 3) * (a + 1))) / 2
mm = ((a - 1) - sp.sqrt((a - 3) * (a + 1))) / 2
assert sp.simplify(mp * mm - 1) == 0

# Exact counterexample to the printed mt=1 implication.
av = sp.Rational(7, 2)
A0 = sp.sqrt(av)
for m0 in (sp.Rational(2), sp.Rational(1, 2)):
    t0 = 1 / m0
    x1, x2, x3 = A0, A0*m0, A0*t0
    e1 = sp.simplify(x1 - A0*(x3**2 + 1)/(x3**2 + 1))
    e2 = sp.simplify(x2 - A0*((x2**2 + 1)*x3**2)/((x3**2 + 1)*x1**2))
    e3 = sp.simplify(x3 - A0*((x3**2 + 1)*x1**2)/((x2**2 + 1)*x3**2))
    assert e1 == e2 == e3 == 0
    assert sp.simplify(m0*t0 - 1) == 0 and m0 != 1 and t0 != 1

print("VERIFY_OK factorization=exact threshold=3 counterexample=a=7/2")
