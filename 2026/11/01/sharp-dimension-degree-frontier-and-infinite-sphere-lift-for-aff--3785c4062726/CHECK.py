"""Exact rational checks for the affine Bernstein spherical frontier.

Requires Python 3.10+ and SymPy. These are finite consistency checks,
not a substitute for the universal proof in RESULT.md.
"""
from itertools import product
from math import comb
import sympy as S

x = S.symbols('x')
checks = 0


def bernstein(poly, n):
    return S.Poly(S.expand(sum(
        S.binomial(n, j) * poly.subs(x, -1 + S.Rational(2*j, n))
        * ((1+x)/2)**j * ((1-x)/2)**(n-j)
        for j in range(n+1))), x)


def normalized_gegenbauer(m, d):
    lam = S.Rational(d-1, 2)
    poly = S.gegenbauer(m, lam, x)
    return S.cancel(poly/S.gegenbauer(m, lam, 1))


# Compute the complete Walsh spectrum of a spherical restriction and verify
# that its nonnegative layer sums are the monomial Bernstein coefficients.
for d in range(2, 7):
    for n in range(1, min(d+2, 6)):
        patterns = list(product((-1, 1), repeat=n))
        for m in range(0, 13):
            f = normalized_gegenbauer(m, d)
            bpoly = bernstein(f, n)
            samples = [f.subs(x, S.Rational(sum(e), n)) for e in patterns]
            for k in range(n+1):
                selected = tuple(range(k))
                hat = sum(v * S.prod(e[i] for i in selected)
                          for e,v in zip(patterns,samples))/2**n
                layer = comb(n,k)*hat
                assert S.cancel(layer-bpoly.nth(k)) == 0, (d,n,m,k,'layer')
                checks += 1
                assert layer >= 0, (d,n,m,k,'positivity')
                checks += 1

# Verify the symbolic closed obstruction coefficient against the actual
# Gegenbauer leading coefficient of the Bernstein image in many dimensions.
for d in range(2,9):
    lam = S.Rational(d-1,2)
    for n in range(1,11):
        f=normalized_gegenbauer(n+2,d)
        q=normalized_gegenbauer(n,d)
        top=bernstein(f,n).nth(n)/S.Poly(q,x).nth(n)
        formula=(S.factorial(n)/S.Integer(n)**n *
                 (n+lam)*(d+1-n)/(3*n) *
                 S.Rational((n+1)*(n+2),(n+d-1)*(n+d)))
        assert S.cancel(top-formula)==0, (d,n,'coefficient')
        checks+=1
        assert S.sign(formula)==S.sign(d+1-n), (d,n,'sign')
        checks+=1

print(f'PASS: {checks} exact rational assertions')
