"""Exact, finite checks for a positive quadratic mass-action flow.

These checks support (but do not replace) the analytic global proof.
"""
from fractions import Fraction as Q
from math import gcd


def check_ratio_slopes():
    cases = [(1, 3, 1), (1, 2, 1), (2, 5, 3), (1, 4, 2),
             (2, 2, 1), (3, 3, 1), (1, 2, 2), (1, 3, 3)]
    count = 0
    for ai, bi, ci in cases:
        a, b, c = map(Q, (ai, bi, ci))
        assert b >= max(a, c) and b > min(a, c)
        for ri in [Q(1, 9), Q(1, 4), Q(1, 2), Q(1), Q(2), Q(4), Q(9)]:
            r = ri
            d = (b-a)+(b-c)*r
            actual = (a-b*r)/(r*d)
            if b>a and b>c:
                e = (b*b-a*c)/((b-a)*(b-c))
                expected = a/((b-a)*r)-e*(b-c)/d
            elif b==a:
                expected = a/(a-c)*(1/(r*r)-1/r)
            else:
                expected = a/((c-a)*r)-c/(c-a)
            assert actual == expected, (ai, bi, ci, r, actual, expected)
            count += 1
    print('EXACT_RATIO_QUADRATURE_IDENTITIES_PASS', count)


def check_original_example():
    import sympy as s
    t = s.symbols('t', real=True)
    R = s.sqrt(t*t+s.Rational(1, 4))
    x = (R-t)/(2*R*R)
    y = (R+t)/(2*R*R)
    assert s.simplify(s.diff(x, t)-(x*x-3*x*y)) == 0
    assert s.simplify(s.diff(y, t)-(3*x*y-y*y)) == 0
    assert s.simplify(x*y/(x+y)**4-s.Rational(1, 16)) == 0
    assert x.subs(t, 0) == y.subs(t, 0) == 1
    print('EXACT_SOURCE_EXAMPLE_TIME_SOLUTION_PASS 4')


def check_endpoint_signs():
    count = 0
    for ai in range(1, 5):
        for ci in range(1, 5):
            for bi in range(1, 7):
                a, b, c = map(Q, (ai, bi, ci))
                if b>=max(a,c) and b>min(a,c):
                    d0, dinf = b-a, b-c
                    assert (d0>0 or dinf>0) and d0>=0 and dinf>=0
                    if d0 and dinf:
                        assert a/d0>0 and -b/dinf < -1 and -c/dinf<0
                    elif not d0:
                        assert c < b == a
                    elif not dinf:
                        assert a < b == c
                    count += 1
    print('EXACT_PARAMETER_ENDPOINT_SIGN_CHECKS_PASS', count)


if __name__ == '__main__':
    check_ratio_slopes()
    check_original_example()
    check_endpoint_signs()
    print('GLOBAL_COMPACTNESS_AND_LOG_ASYMPTOTICS_REQUIRE_ANALYTIC_PROOF')
