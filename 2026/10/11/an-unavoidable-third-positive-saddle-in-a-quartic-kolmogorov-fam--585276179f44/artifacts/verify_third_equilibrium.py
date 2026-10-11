from sympy import Matrix, Rational, factor, simplify, sqrt, symbols

x, y = symbols('x y', real=True)
a, b, A10, B10 = symbols('a b A10 B10', real=True)

P = Rational(1, 6) * x * (y - 1) * (
    x**2 - 24*a*y - 6*A10*x + 6*A10*x*y - 7*y**2 + 30*a*y**2 - 6*a
)
Q = Rational(1, 3) * y * (
    3*b + 3*B10*x - x**2 + 6*x**3 + 9*b*y - 6*B10*x*y
    - 26*x**2*y - 2*y**2 - 27*b*y**2 + 39*x*y**2
    + 3*B10*x*y**2 - 16*y**3 + 15*b*y**3
)

assert simplify(P.subs(y, 1)) == 0
q_line = factor(Q.subs(y, 1))
assert q_line == (x - 1)*(x - 2)*(2*x - 3)

J = Matrix([P, Q]).jacobian([x, y])
J1 = simplify(J.subs({x: 1, y: 1}))
Jm = simplify(J.subs({x: Rational(3,2), y: 1}))
J2 = simplify(J.subs({x: 2, y: 1}))
assert J1 == Matrix([[0, -1], [1, 0]])
assert J2 == Matrix([[0, -1], [1, 0]])
assert Jm == Matrix([[0, -Rational(19,16)], [-Rational(1,2), Rational(13,6)]])
assert factor(Jm.det()) == -Rational(19,32)
assert Jm.trace() == Rational(13,6)
lam = symbols('lam')
char = factor(Jm.charpoly(lam).as_expr())
assert simplify(char - (lam**2 - Rational(13,6)*lam - Rational(19,32))) == 0
roots = [(Rational(26) - sqrt(1018))/24, (Rational(26) + sqrt(1018))/24]
for r in roots:
    assert simplify(char.subs(lam, r)) == 0
assert roots[0] < 0 < roots[1]

print('Q(x,1) =', q_line)
print('J(1,1) =', J1)
print('J(3/2,1) =', Jm)
print('J(2,1) =', J2)
print('det J(3/2,1) =', Jm.det())
print('trace J(3/2,1) =', Jm.trace())
print('eigenvalues = (26-sqrt(1018))/24, (26+sqrt(1018))/24')
print('VERIFY_OK')
