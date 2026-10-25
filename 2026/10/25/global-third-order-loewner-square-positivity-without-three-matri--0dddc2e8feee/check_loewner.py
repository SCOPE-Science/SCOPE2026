"""Exact rational certificate for a three-node Loewner-square separation.

Requires Python 3 and sympy. All determinant, coefficient and inequality
checks use rational arithmetic, including the boundary of the node cube.
"""
import sympy as sp

x, y, z = sp.symbols('x y z')
t, u, v = sp.symbols('t u v')
C = sp.Rational(1, 100)


def kernel(a, b):
    return (1 + (a*a + a*b + b*b)/3
            + sp.Rational(2, 25)*sum(a**(4-j)*b**j for j in range(5)))


def diagonal(a):
    return 1 + a*a + sp.Rational(2, 5)*a**4


def coefficient_poly(expr, vars):
    return sp.Poly(sp.expand(expr), *vars, domain=sp.QQ)


def sorted_quotient(matrix):
    determinant = sp.factor(matrix.det(method='domain-ge'))
    vandermonde_sq = (x-y)**2 * (y-z)**2 * (x-z)**2
    quotient = sp.cancel(determinant / vandermonde_sq)
    assert sp.denom(quotient) == 1, 'Vandermonde quotient not polynomial'
    poly = coefficient_poly(quotient.subs({x:t, y:t+u, z:t+u+v}), (t,u,v))
    return poly


pair = sp.cancel((diagonal(x)*diagonal(y)-kernel(x,y)**2) / (x-y)**2)
assert sp.denom(pair) == 1
P2 = coefficient_poly(pair.subs({x:t, y:t+u}), (t,u))
assert len(P2.terms()) == 16
assert P2.coeff_monomial(1) == sp.Rational(1,3)
# Valid when t,u are each between 0 and 1/100.
negative_abs_bound = sum(-co*C**sum(powers) for powers,co in P2.terms() if co < 0)
assert negative_abs_bound < sp.Rational(1,12)

nodes = [x,y,z]
L = sp.Matrix([[diagonal(a) if i == j else kernel(a,b)
                for j,b in enumerate(nodes)] for i,a in enumerate(nodes)])
P3 = sorted_quotient(L)
assert len(P3.terms()) == 44
assert P3.coeff_monomial(1) == -sp.Rational(7,675)
assert all(co < 0 for _,co in P3.terms())

K = L.multiply_elementwise(L)
P3sq = sorted_quotient(K)
assert len(P3sq.terms()) == 681
assert P3sq.coeff_monomial(1) == sp.Rational(22,675)
assert sum(1 for _,co in P3sq.terms() if co > 0) == 1
assert sum(1 for _,co in P3sq.terms() if co < 0) == 680
# For nonnegative 0 <= t,u,v <= C, all nonconstant monomials
# have negative coefficients, hence the quotient is >= P3sq(C,C,C).
lower_bound = P3sq.eval({t:C, u:C, v:C})
assert lower_bound > sp.Rational(3,100)

# Need t+u+v < C, so above cube is deliberately larger
# than necessary; there is no unverified numerical step.
# Explicit distinct triple demonstrates negative Loewner determinant.
triple = [sp.Rational(j, 400) for j in (1,2,3)]
witness = sp.Matrix([[diagonal(a) if i==j else kernel(a,b)
                     for j,b in enumerate(triple)] for i,a in enumerate(triple)])
assert witness.det() < 0
assert witness.multiply_elementwise(witness).det() > 0
print('PASS: pair quotient 16 terms; negative-tail bound < 1/12; 44 negative Loewner triple coefficients')
print('PASS: squared Loewner triple 681 terms, exactly 680 negative, strictly positive constant')
print('PASS: exact squared-kernel quotient lower bound > 3/100; explicit triple determinant separation')
print('Lower bound (exact):', lower_bound)
