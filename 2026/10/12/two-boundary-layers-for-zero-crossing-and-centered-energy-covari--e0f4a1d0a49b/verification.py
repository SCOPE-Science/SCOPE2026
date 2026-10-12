#!/usr/bin/env python3
"""Exact checks for Gaussian AR(1) crossing / centered-energy covariance.

Only the Python standard library is needed. Finite computations check identities;
they do not prove the asymptotic assertions in the accompanying text.
"""
from fractions import Fraction as F
from math import isclose


def centered_polynomial(n, r):
    """Direct projected covariance-vector formula, exact for rational r."""
    assert n >= 2
    columns = [[r ** abs(i - j) for j in range(n)] for i in range(n)]
    projected = [[v - sum(col) / n for v in col] for col in columns]
    return sum(
        r * (sum(v*v for v in projected[i])
             + sum(v*v for v in projected[i+1]))
        - 2 * sum(x*y for x, y in zip(projected[i], projected[i+1]))
        for i in range(n-1)
    )


def decomposition(n, r):
    """Independently expand into raw energy and squared-sum terms."""
    t = -2*r*(1-r*r)*sum((n-1-k)*r**(2*k) for k in range(n-1))
    b = [sum(r**abs(i-j) for j in range(n)) for i in range(n)]
    u = sum(r*(b[i]**2+b[i+1]**2)-2*b[i]*b[i+1]
            for i in range(n-1))
    return t-u/n, t, u


def d_moment(n, i):
    vals = [abs(j-i) for j in range(1, n+1)]
    return sum(v*v for v in vals)-F(sum(vals)**2, n)


def main():
    count = 0
    for n in range(2, 15):
        for r in [F(-1,2), F(0), F(1,4), F(1,2), F(3,4)]:
            f = centered_polynomial(n, r)
            alternative, _, _ = decomposition(n, r)
            assert f == alternative, (n, r, f, alternative)
            assert centered_polynomial(n, F(0)) == F(2*(n-1),n)
            count += 1
    for n, expected in {7:F(-4311,14336),
                        8:F(-115161,131072),
                        9:F(-75563,49152)}.items():
        assert centered_polynomial(n,F(1,2)) == expected
    for n in range(2,25):
        q = sum(F(4*i*(n-i), n) for i in range(1,n))
        s = sum(d_moment(n,i)+d_moment(n,i+1) for i in range(1,n))
        assert q == F(2*(n*n-1),3)
        assert s == F((n*n-1)*(3*n*n-5*n+8),30)
    assert centered_polynomial(2,F(1,2)) == F(3,8)
    # Diagnostic finite-n checks of the proven limiting scales.
    rows=[]
    for n in (80,160,320):
        small = centered_polynomial(n,1.0/n)
        high = n*n*centered_polynomial(n,1.0-4.0/n**2)
        rows.append((n, small, high))
    assert abs(rows[-1][1]) < abs(rows[0][1])
    assert abs(rows[-1][2]-4.0**2*(2/3-4/10)) < abs(rows[0][2]-4.0**2*(2/3-4/10))
    print('PASS:',count,'exact projected/decomposition comparisons; 3 exact n=7..9 signs;')
    print('23 exact geometric-moment identities; boundary-layer diagnostics:')
    for row in rows:print(row)

if __name__ == '__main__':main()
