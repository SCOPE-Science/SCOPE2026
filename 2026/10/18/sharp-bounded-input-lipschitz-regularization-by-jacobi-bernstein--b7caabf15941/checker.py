"""Deterministic checks for the sharp Jacobi Bernstein--Durrmeyer smoothing theorem.

Requires only Python 3's standard library. Finite checks do not replace proof.
Run: python checker.py
"""
from fractions import Fraction as F
from math import comb, factorial


def point_mass(n, a, b, k):
    """Exact adjacent-beta total variation for integer shape parameters."""
    x = a + k
    y = b + n - k - 1
    s = x + y
    return F(comb(s, x)) * F(x, s)**x * F(y, s)**y


def beta_poly(alpha, beta):
    # Beta(alpha,beta) density: polynomial for integer positive shapes.
    c = F(factorial(alpha + beta - 1),
          factorial(alpha - 1) * factorial(beta - 1))
    out = [F(0)] * (alpha + beta - 1)
    for j in range(beta):
        out[alpha - 1 + j] = c * comb(beta - 1, j) * (-1)**j
    return out


def sub(a, b):
    return [ (a[k] if k < len(a) else F(0)) -
             (b[k] if k < len(b) else F(0))
             for k in range(max(len(a), len(b))) ]


def integrate(poly, c):
    return sum((v * c**(k+1) / (k+1) for k, v in enumerate(poly)), F(0))


def derivative_poly(n, a, b, x):
    p = [beta_poly(a + k, b + n - k) for k in range(n+1)]
    result = [F(0)] * (a + b + n - 1)
    for k in range(n):
        w = n * comb(n-1, k) * x**k * (1-x)**(n-1-k)
        for j, v in enumerate(sub(p[k+1], p[k])):
            result[j] += w * v
    return result


def simpson_abs(poly, steps=4096):
    """Independent approximate absolute integral (not a certificate)."""
    coeff = list(map(float, poly))
    total = 0.0
    for j in range(steps+1):
        t = j / steps
        value = 0.0
        for c in reversed(coeff):
            value = value * t + c
        mult = 1 if j == 0 or j == steps else (4 if j % 2 else 2)
        total += mult * abs(value)
    return total / (3*steps)


def run():
    tests = 0
    for a in (1,2,3,4):
        for b in (1,2,3,4):
            for n in range(2,10):
                vals = [point_mass(n,a,b,k) for k in range(n)]
                peak = max(vals[0], vals[-1])
                assert all(v <= peak for v in vals)
                tests += n
                if n >= 3:
                    assert all(v < peak for v in vals[1:-1])
                    tests += n-2
                if a < b: assert vals[0] > vals[-1]
                if a > b: assert vals[-1] > vals[0]
                if a == b: assert vals[0] == vals[-1]
                tests += 1
                # Evaluate each adjacent signed beta-density integral exactly.
                for k in range(n):
                    alpha, beta = a+k, b+n-k
                    c = F(alpha, alpha+beta-1)
                    signed = sub(beta_poly(alpha+1,beta-1),
                                 beta_poly(alpha,beta))
                    assert integrate(signed,F(1)) == 0
                    abs_int = 2*(integrate(signed,F(1))-integrate(signed,c))
                    assert abs_int == 2*vals[k]
                    tests += 2
                # At the two endpoints the sharp derivative norm is attained.
                for x,expect in ((F(0), vals[0]),(F(1),vals[-1])):
                    deriv = derivative_poly(n,a,b,x)
                    alpha = a if x == 0 else a+n-1
                    cut = F(alpha,a+b+n-1)
                    assert 2*(integrate(deriv,F(1))-integrate(deriv,cut)) == 2*n*expect
                    tests += 1
                # Representative interior evaluation: independent absolute integration.
                if n<=6:
                    for x in (F(1,4),F(1,2),F(3,4)):
                        est = simpson_abs(derivative_poly(n,a,b,x),steps=2048)
                        assert est < float(2*n*peak)+0.0005
                        tests += 1
    for n in range(2,20):
        assert point_mass(n,1,1,0) == F(n,n+1)**n
        tests += 1
    print('PASS: %d exact and numerical finite checks' % tests)


if __name__ == '__main__':
    run()
