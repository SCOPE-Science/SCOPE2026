from sympy import Matrix, symbols, exp, factor, simplify, Rational, sqrt, N

lam = symbols('lam')
a,c,d,xi = symbols('a c d xi', positive=True, real=True)
b = 1/c
x1,x2,x3,x4 = symbols('x1 x2 x3 x4', real=True)

f = Matrix([
    a*(x2-x1)+x4,
    b*x1+x2-x1*x3,
    -c*x3+exp(x1*x2),
    d*x2*x3,
])
J = f.jacobian([x1,x2,x3,x4])
E = {x1:xi, x2:0, x3:1/c, x4:a*xi}
assert all(simplify(v.subs(E)) == 0 for v in f)

char = factor(J.subs(E).charpoly(lam).as_expr())
expected = lam*(lam+a)*(lam**2+(c-1)*lam+xi**2-c)
assert simplify(char-expected) == 0

# Published parameter slice a=2, c=8/3, b=3/8, d=1/10.
subs0 = {a:2, c:Rational(8,3), d:Rational(1,10), xi:0}
char0 = factor(char.subs(subs0))
assert char0 == lam*(lam-1)*(lam+2)*(3*lam+8)/3
paper_cond0 = simplify((2*a+2*c-a*c-xi**2-1).subs(subs0))
assert paper_cond0 == 3  # Source Eq. (7) would accept xi=0.

# Reported limiting equilibrium coordinates in the source both fall in xi^2>c.
for q in [Rational(20070,10000), Rational(16385,10000)]:
    assert q*q > Rational(8,3)

# The first reported limit xi≈2.007 violates the source's Eq. (7).
q = Rational(20070,10000)
paper_cond_first = simplify((2*a+2*c-a*c-xi**2-1).subs({a:2,c:Rational(8,3),xi:q}))
assert paper_cond_first < 0

print('characteristic_factor =', char)
print('source_slice_xi0_spectrum = {0, -2, 1, -8/3}')
print('source_eq7_value_at_xi0 =', paper_cond0)
print('source_eq7_value_at_xi_2.007 =', N(paper_cond_first, 12))
print('actual_transverse_stability = c>1 and xi^2>c (for a>0)')
print('VERIFY_OK')
