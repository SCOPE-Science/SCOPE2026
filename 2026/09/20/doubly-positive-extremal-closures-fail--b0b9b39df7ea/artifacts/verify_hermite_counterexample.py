# Symbolic checks for the explicit Hermite counterexample.
# Requires SymPy 1.14 or compatible.
import sympy as sp

X, U, xi = sp.symbols("X U xi", real=True)
s = sp.sqrt(6)
a = (2 - s) / 8
b = sp.Rational(1, 8)

P = 1 + 2*a + 3*b - 2*(a + 3*b)*X + b*X**2
Phat = 1 - 2*a + 3*b - 2*(-a + 3*b)*X + b*X**2

Q = X**2 + (2*s - 10)*X + 15 - 2*s
R = (X - (1 + s))**2

assert sp.simplify((-a + 2*b)**2 + 2*(b - sp.Rational(1, 4))**2) == sp.Rational(1, 8)
assert sp.expand(8*P - Q) == 0
assert sp.expand(8*Phat - R) == 0

disc_Q = sp.factor(sp.discriminant(Q, X))
assert sp.simplify(disc_Q - 32*(2 - s)) == 0
assert float(disc_Q) < 0

x = sp.symbols("x", real=True)
pi = sp.pi
Qx = (4*pi*x**2)**2 + (2*s - 10)*(4*pi*x**2) + 15 - 2*s
Gpoly = sp.expand(Qx**2)
basehat = sp.exp(-pi*xi**2/2) / sp.sqrt(2)

Ghat = 0
for (n,), coeff in sp.Poly(Gpoly, x).terms():
    assert n % 2 == 0
    k = n // 2
    Ghat += coeff * ((-1)**k / (2*pi)**(2*k)) * sp.diff(basehat, xi, 2*k)

T = U**4 - (8 + 4*s)*U**3 + (64 + 16*s)*U**2 - (96 + 16*s)*U + 168 - 32*s
expected = sp.exp(-pi*xi**2/2) / sp.sqrt(2) * T.subs(U, pi*xi**2)
assert sp.simplify(sp.expand(Ghat - expected)) == 0

Tpoly = sp.Poly(T, U, extension=s)
assert Tpoly.count_roots(-sp.oo, sp.oo) == 0
assert sp.simplify(T.subs(U, 0)) > 0

print("boundary identity:", sp.simplify((-a + 2*b)**2 + 2*(b-sp.Rational(1,4))**2))
print("8 P(X):", sp.expand(Q))
print("disc(8 P):", disc_Q)
print("8 Phat(X):", sp.factor(R))
print("Fourier polynomial for F^2:", sp.expand(T))
print("real roots of that polynomial:", Tpoly.count_roots(-sp.oo, sp.oo))
