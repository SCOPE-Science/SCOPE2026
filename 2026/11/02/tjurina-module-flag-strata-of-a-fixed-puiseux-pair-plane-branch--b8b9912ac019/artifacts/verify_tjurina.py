"""Exact finite checks for Tjurina strata of a semiquasihomogeneous plane-branch pencil.

Run: python3 artifacts/verify_tjurina.py
Requires: SymPy. These checks supplement, not replace, the proof for all m,q.
"""
from itertools import product
import sympy as sp

X, Y = sp.symbols('x y')


def quotient_dimension(G, m, n):
    """Count standard monomials within an independently justified rectangle."""
    lead = [p.LM().exponents for p in G.polys]
    if (m - 1, 0) not in lead or not any(a == 0 and b <= n for a,b in lead):
        raise AssertionError(('unexpected leading terms', lead))
    return sum(
        all(not (y_power >= a and x_power >= b) for a, b in lead)
        for y_power, x_power in product(range(m - 1), range(n))
    ), lead


def test_case(m, q, coeffs):
    n = m * q + 1
    h = sum(sp.Integer(a) * X**((m-1)*q+j)
            for j, a in enumerate(coeffs, 1))
    f = Y**m - X**n + Y*h
    basis = sp.groebner((f, sp.diff(f, X), sp.diff(f, Y)), Y, X,
                       order='lex', domain=sp.QQ)
    tau, leading = quotient_dimension(basis, m, n)
    if all(c == 0 for c in coeffs):
        expected = (m - 1)*(n - 1)
        expected_lead = {(m - 1, 0), (0, n - 1)}
    else:
        j = next(j for j, c in enumerate(coeffs, 1) if c)
        v = (m-1)*q+j
        expected = n + (m-2)*(v-1)
        expected_lead = {(m-1, 0), (1, v-1), (0, n)}
        # A polynomial identity in the ideal, independent of Groebner output.
        euler = sp.expand(m*X*sp.diff(f, X)
                          + n*Y*sp.diff(f, Y) - m*n*f)
        assert sp.expand(euler - Y*(m*X*sp.diff(h, X)-n*(m-1)*h)) == 0
        lowest = sp.Poly(m*X*sp.diff(h, X)-n*(m-1)*h, X).nth(v)
        assert lowest == (m*(j-1)+1)*coeffs[j-1]
    assert tau == expected, (m,q,coeffs,tau,expected,leading)
    assert set(leading) == expected_lead, (m,q,coeffs,leading,expected_lead)
    return tau


def main():
    count = 0
    for m, q in [(5, 2), (5, 3), (6, 2), (7, 2), (8, 2)]:
        for j in range(1, q+1):
            for first in (1, 3):
                coeffs = [0]*(j-1)+[first]+[2]*(q-j)
                test_case(m, q, coeffs)
                count += 1
            # Independent tail-sparse example.
            coeffs = [0]*(j-1)+[1]+[0]*(q-j)
            test_case(m, q, coeffs)
            count += 1
        test_case(m, q, [0]*q)
        count += 1
    print(f'VERIFY_OK: {count} exact Gröbner quotient checks')


if __name__ == '__main__':
    main()
