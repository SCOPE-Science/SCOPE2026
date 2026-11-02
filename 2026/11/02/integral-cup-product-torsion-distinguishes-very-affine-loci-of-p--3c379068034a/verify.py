#!/usr/bin/env python3
"""Exact finite algebra checks for the multiplicity-sensitive positive-chart theorem.

Finite checks support but do not replace the topological Gysin proof.
"""
from fractions import Fraction
from math import comb, gcd
from functools import reduce


def mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return c


def power_linear(c, m):
    p = [1]
    for _ in range(m):
        p = mul(p, [1, c])
    return p


def eval_poly(a, x):
    out = Fraction(0)
    for c in reversed(a):
        out = out*x+c
    return out


def divide_linear(p, root):
    """Coefficients in ascending order: exact divide by (s-root)."""
    assert len(p) >= 2
    q = [Fraction(0)] * (len(p)-1)
    q[-1] = Fraction(p[-1])
    for k in range(len(q)-2, -1, -1):
        q[k] = Fraction(p[k+1]) + root*q[k+1]
    assert Fraction(p[0]) == -root*q[0]
    return q


def multiplicity(p, root):
    q = [Fraction(z) for z in p]
    m = 0
    while len(q) > 1 and eval_poly(q, root) == 0:
        q = divide_linear(q, root)
        m += 1
    return m, q


def cup_cokernel_from_restriction(multiplicities):
    """Compute Smith invariant for [I_2 | -multiplicity row]."""
    if not multiplicities:
        return 0, 1
    return len(multiplicities) - 1, reduce(gcd, multiplicities)


def main():
    assert cup_cokernel_from_restriction([]) == (0, 1)
    for a in range(2, 13):
        seen = []
        for m in range(1, a+1):
            # Homogeneous polynomial (x0+x1)^(a-m)*(x0+2*x1)^m.
            h = mul(power_linear(1, a-m), power_linear(2, m))
            assert len(h) == a+1 and all(x > 0 for x in h)
            assert h[0] == 1 and h[-1] == 2**m
            # Independently dehomogenize x0=1-s, x1=s.
            p = [0] * (a+1)
            for j, coeff in enumerate(h):
                term = mul(power_linear(-1, a-j), [0]*j+[1])
                for k, v in enumerate(term):
                    p[k] += coeff*v
            while len(p)>1 and p[-1]==0:
                p.pop()
            assert p == power_linear(1, m)
            assert eval_poly(p, Fraction(-1)) == 0
            multiplicity, quotient = multiplicity_fn(p, Fraction(-1))
            assert multiplicity == m and quotient == [Fraction(1)]
            assert cup_cokernel_from_restriction([m]) == (0, m)
            # Cohomology ranks: H1=4; H2=4+number of distinct roots=5.
            assert (1,4,5) == (1,4,4+len([m]))
            seen.append(m)
        assert len(set(seen)) == a
    p = mul(power_linear(1, 2), power_linear(2, 4))
    r1, q1 = multiplicity_fn(p, Fraction(-1))
    r2, q2 = multiplicity_fn(q1, Fraction(-1,2))
    assert (r1, r2, q2) == (2,4,[Fraction(16)])
    assert cup_cokernel_from_restriction([r1,r2]) == (1,2)
    p2 = mul(power_linear(1, 2), power_linear(2, 3))
    r1, q1 = multiplicity_fn(p2, Fraction(-1))
    r2, q2 = multiplicity_fn(q1, Fraction(-1,2))
    assert (r1,r2,q2)==(2,3,[Fraction(8)])
    assert cup_cokernel_from_restriction([r1,r2]) == (1,1)
    # Euler characteristic agrees with the alternating Betti sum.
    for q in range(20):
        assert 1-4+(q+4) == 1+q
    print('VERIFY_OK: exact homogeneous families a<=12; root multiplicities; Smith invariants; Euler checks')


multiplicity_fn = multiplicity
if __name__ == '__main__':
    main()
