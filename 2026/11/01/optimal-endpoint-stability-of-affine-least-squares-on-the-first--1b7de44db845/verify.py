"""Exact-rational verification for affine least-squares projection on two Hamming layers.

Run with Python 3 and SymPy: python verify.py
The test enumerates complete finite sample spaces and forms the weighted
normal-equation projector independently of the closed kernel calculation.
"""
from itertools import combinations
from fractions import Fraction
from math import comb
import sympy as sp


def closed_rows(n, t):
    t = sp.Rational(t)
    h = n-1+(n-3)*t
    a = sp.Rational(4*(n-1)*(n-2), n)/h
    r = sp.Rational((n-2)*(n-3), n*(n-1))
    r1 = 1+t*a
    r2 = 1+(1-t)*a+2*r*max(sp.S.Zero, 4*(n-1)*t/h-1)
    return sp.factor(r1), sp.factor(r2)


def direct_rows(n, t):
    t = sp.Rational(t)
    points = [set(c) for r in (1, 2) for c in combinations(range(n), r)]
    masses = [(1-t)/n if len(x)==1 else t/sp.binomial(n, 2) for x in points]
    vectors = [sp.Matrix([1]+[int(j in x) for j in range(n)]) for x in points]
    gram = sp.zeros(n+1)
    for v, w in zip(vectors, masses):
        gram += w * (v * v.T)
    inv = gram.inv()
    rows = [sp.factor(sum(w*abs((v.T*inv*u)[0]) for u, w in zip(vectors, masses))) for v in vectors]
    assert len(set(rows[:n])) == 1
    assert len(set(rows[n:])) == 1
    return rows[0], rows[n]


def symbolic_checks():
    n, t = sp.symbols('n t', positive=True)
    h = n-1+(n-3)*t
    a = 4*(n-1)*(n-2)/(n*h)
    r = (n-2)*(n-3)/(n*(n-1))
    r1 = 1+t*a
    r2_low = 1+(1-t)*a
    r2_high = r2_low+2*r*(4*(n-1)*t/h-1)
    optimal = (n-1)/(n+1)
    target = 3-4/n
    assert sp.simplify(r1.subs(t,optimal)-target)==0
    assert sp.simplify(r2_high.subs(t,optimal)-target)==0
    assert sp.simplify(sp.diff(r1,t) - 4*(n-1)**2*(n-2)/(n*h**2)) == 0
    assert sp.simplify(sp.diff(r2_low,t) + 8*(n-1)*(n-2)**2/(n*h**2)) == 0
    assert sp.simplify(sp.diff(r2_high,t) + 8*(n-1)*(n-2)/(n*h**2)) == 0
    determinant_profile = t*(1-t)*h**(n-1)
    derivative_of_log = 1/t-1/(1-t)+(n-1)*(n-3)/h
    assert sp.simplify(derivative_of_log.subs(t,optimal))==0
    assert sp.simplify(sp.diff(sp.log(t*(1-t)),t,2) + (n-1)*sp.diff(sp.log(h),t,2) + 1/t**2+1/(1-t)**2+(n-1)*(n-3)**2/h**2)==0
    print('PASS symbolic extremum, monotonicity and determinant-design comparisons')


def run():
    symbolic_checks()
    profiles = 0
    rows_checked = 0
    for n in range(3, 10):
        for t in sorted(set([sp.Rational(1, 7), sp.Rational(1, 3),
                             sp.Rational(1, 2), sp.Rational(2, 3),
                             sp.Rational(4, 5), sp.Rational(9, 10),
                             sp.Rational(n-1, n+1)])):
            expected = closed_rows(n, t)
            actual = direct_rows(n, t)
            assert actual == expected, (n,t,actual,expected)
            profiles += 1
            rows_checked += n+comb(n,2)
        optimum = sp.Rational(n-1, n+1)
        assert max(closed_rows(n,optimum)) == sp.Rational(3*n-4,n)
        left, right = closed_rows(n, optimum)
        assert left == right
        for probe in [sp.Rational(1,100), sp.Rational(1,2), sp.Rational(7,8), sp.Rational(99,100)]:
            assert max(closed_rows(n, probe)) >= sp.Rational(3*n-4, n)
    print('PASS exact weighted-Gram inversions:', profiles, 'profiles;', rows_checked, 'row instances')
    print('PASS optimal-t equalization and benchmark for n=3..9')

if __name__ == '__main__':
    run()
