#!/usr/bin/env python3
"""Exact rational-function checks for rank-two sparse Hankel projection degrees."""
from sympy import Symbol, Rational, cancel, fraction, Poly, expand

def check(A, B, C):
    S = Symbol('S')
    delta = A * A * C - B ** 3
    assert A != 0 and B != 0 and delta != 0
    P = (B * S ** 2 - C) / (A * S + B)
    a = [Rational(A), Rational(B)]
    a.append(cancel(S * a[1] - P * a[0]))
    a.append(cancel(S * a[2] - P * a[1]))
    assert cancel(a[3] - C) == 0
    for n in range(5, 19):
        a.append(cancel(S * a[-1] - P * a[-2]))
        t = n - 1
        f = cancel(a[t])
        num, den = fraction(f)
        num = Poly(num, S)
        den = Poly(den, S)
        pole = t // 2
        root = -Rational(B, A)
        assert den.degree() == pole, (n, num, den)
        assert den.eval(root) == 0
        # After cancellation the entire finite denominator is supported at S=-B/A.
        assert Poly(den.as_expr(), S) == Poly(den.LC() * (S - root) ** pole, S)
        assert num.eval(root) != 0
        assert num.degree() - den.degree() == n - 4
        assert max(num.degree(), den.degree()) == (n - 4) + pole
        assert max(num.degree(), den.degree()) == (3 * (n - 3)) // 2

if __name__ == '__main__':
    check(2, 3, 5)
    check(3, 4, 7)
    print('VERIFY_OK')
