"""Exact symbolic checks for the real period-two locus of the Bogdanov map.

Requires only SymPy. These checks supplement, but do not replace, the
algebraic equivalence proof in RESULT.md.
"""
import sympy as sp

x, y, k, mu, eps = sp.symbols('x y k mu eps', real=True)
u, v, S, d = sp.symbols('u v S d', real=True)


def step(X, Y, kk, mm, ee):
    new_y = sp.expand((1 + ee + mm * X) * Y + kk * X * (X - 1))
    return sp.expand(X + new_y), new_y


def check(condition, label):
    if not condition:
        raise AssertionError(label)
    print('OK', label)

# The two equations for a prime-two pair are the original update at both points.
E1 = sp.expand(d * (2 + eps + mu * u) - k * u * (u - 1))
E2 = sp.expand(-d * (2 + eps + mu * v) - k * v * (v - 1))
sub = {u: (S - d) / 2, v: (S + d) / 2}
P1 = sp.expand((E1 - E2).subs(sub))
P2 = sp.expand((E1 + E2).subs(sub))
constraint_sum = sp.expand(d * ((k + mu) * S - (k - 4 - 2 * eps)))
constraint_quad = sp.expand((k + 2 * mu) * d**2 - k * S * (2 - S))
check(sp.simplify(P1 - constraint_sum) == 0, 'sum constraint exact')
check(sp.simplify(P2 + constraint_quad / 2) == 0, 'quadratic constraint exact')

# Each exceptional branch has its announced prime-two locus.
branches = [
    ('reflection-through-origin', -k / 2, (k - 4) / 2, 2*x-y),
    ('reflection-through-one', -k / 2, -2, 2*x-y-2),
    ('mobius-hyperbola', -k, (k - 4) / 2, 2*x*x-2*x*y-2*x+y),
]
for name, mm, ee, invariant in branches:
    X, Y = step(x, y, k, mm, ee)
    X2, Y2 = step(X, Y, k, mm, ee)
    poly = sp.Poly(invariant, y)
    if poly.degree() == 1:
        on_curve_y = sp.solve(invariant, y)[0]
        check(sp.simplify((X2-x).subs(y, on_curve_y)) == 0,
              name+' two-step x')
        check(sp.simplify((Y2-y).subs(y, on_curve_y)) == 0,
              name+' two-step y')
    else:
        raise AssertionError('unexpected curve type')
    # For a point on each branch the original relation holds identically;
    # the second-step fixed locus contains its smooth one-dimensional curve.

# Representative exact 2-cycles, including points on the three continua.
for name, kk, mm, ee, xx, yy in [
    ('line S=0', sp.Rational(2), sp.Rational(-1), sp.Rational(-1), sp.Rational(2), sp.Rational(4)),
    ('line S=2', sp.Rational(2), sp.Rational(-1), sp.Rational(-2), sp.Rational(3), sp.Rational(4)),
    ('hyperbola', sp.Rational(2), sp.Rational(-2), sp.Rational(-1), sp.Rational(2), sp.Rational(4,3)),
    ('isolated generic', sp.Rational(5), sp.Rational(0), sp.Rational(0), sp.Rational(2,5), sp.Rational(3,5)),
    ('whole-plane involution', sp.Rational(0), sp.Rational(0), sp.Rational(-2), sp.Rational(7), sp.Rational(2)),
]:
    X,Y = step(xx, yy, kk, mm, ee)
    X2,Y2 = step(X,Y,kk,mm,ee)
    check((sp.simplify(X2-xx),sp.simplify(Y2-yy)) == (0,0) and (X,Y)!=(xx,yy), name+' prime-two')

# On the codimension-three meeting point, F^2 is the identity globally.
X,Y = step(x,y,0,0,-2)
X2,Y2 = step(X,Y,0,0,-2)
check(sp.simplify(X2-x)==0 and sp.simplify(Y2-y)==0,
      'global involution')

# Generic negative discriminant gives no real two-cycle.
ss = sp.Rational(2-4,2)
rr = sp.simplify(2*ss*(2-ss)/(2+0))
check(rr < 0, 'generic empty example')
print('All exact symbolic checks passed.')
