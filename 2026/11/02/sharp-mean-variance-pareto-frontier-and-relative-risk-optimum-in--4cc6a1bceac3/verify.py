#!/usr/bin/env python3
"""Exact rational checks for the sticky run-and-tumble escape-time formulas.

Run: python3 verify.py
Uses Python's standard library only. These finite checks complement, not
replace, the all-parameter proof given in RESULT.md.
"""
from fractions import Fraction as F
from math import factorial


def add(a, b):
    n = max(len(a), len(b))
    return [(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)]


def mul(a, b, n=None):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out[:n] if n is not None else out


def scale(a, c):
    return [c * x for x in a]


def deriv(a):
    return [(i + 1) * a[i + 1] for i in range(len(a) - 1)]


def evaluate(a, x):
    z = F(0)
    for c in reversed(a):
        z = z * x + c
    return z


def subtract(a, b):
    return add(a, scale(b, -1))


def check_zero(a):
    assert all(v == 0 for v in a), a


def moments(b):
    # Solutions of the two backward generator boundary-value problems.
    one_plus = [F(3, 2)*b + 2, -b-2, -b/2]
    one_minus = [F(3, 2)*b + 4 + 2/b, -b, -b/2]
    two_plus = [
        F(19, 4)*b*b + F(46, 3)*b + 13 + 4/b,
        -F(11, 3)*b*b - 14*b - 14 - 4/b,
        -F(3, 2)*b*b - 2*b + 1,
        b*b/3 + 2*b/3,
        b*b/12,
    ]
    two_minus = [
        F(19, 4)*b*b + F(68, 3)*b + 35 + 24/b + 8/(b*b),
        -F(11, 3)*b*b - 8*b - 2,
        -F(3, 2)*b*b - 4*b - 1,
        b*b/3,
        b*b/12,
    ]
    return one_plus, one_minus, two_plus, two_minus


def generator_check(b):
    p1, m1, p2, m2 = moments(b)
    # L f_+ = f'_+ + b(f_- - f_+)/2;
    # L f_- = -f'_- + b(f_+ - f_-)/2.
    for n, p, m, prevp, prevm in [(1,p1,m1,[F(1)],[F(1)]),
                                    (2,p2,m2,p1,m1)]:
        check_zero(add(add(deriv(p), scale(subtract(m, p), b/2)), scale(prevp, n)))
        check_zero(add(add(scale(deriv(m), -1), scale(subtract(p, m), b/2)), scale(prevm, n)))
        assert evaluate(p, 1) == 0
        if n == 1:
            assert evaluate(m, -1) - evaluate(p, -1) == 2/b
        else:
            assert evaluate(m, -1) - evaluate(p, -1) == 4*evaluate(p1, -1)/b + 8/(b*b)
    expected_mean = (3*b*b + 6*b + 2)/(2*b)
    expected_m2 = (19*b**4 + 76*b**3 + 96*b*b + 56*b + 16)/(4*b*b)
    expected_var = (5*b**4 + 20*b**3 + 24*b*b + 16*b + 6)/(2*b*b)
    mean = (p1[0] + m1[0])/2
    second = (p2[0] + m2[0])/2
    assert mean == expected_mean
    assert second == expected_m2
    assert second - mean*mean == expected_var
    assert expected_var/(mean*mean) == 2*(5*b**4+20*b**3+24*b*b+16*b+6)/(3*b*b+6*b+2)**2
    return mean, second


def laplace_check(b, expected_mean, expected_m2):
    # Independent Taylor expansion of the published exact first-passage
    # transform: (s+b)(cosh k+(s/k)sinh k) /
    # [(2s+b)cosh(2k)+2k sinh(2k)], where k^2=s(s+b).
    q = [F(0), b, F(1)]
    q2 = mul(q, q, 3)
    ch = add(add([F(1)], scale(q, F(1, 2))), scale(q2, F(1,24)))
    sh_over_k = add([F(1)], scale(q, F(1,6)))
    left = mul([b,F(1)], add(ch,mul([F(0),F(1)],sh_over_k,3)),3)
    ch2 = add(add([F(1)],scale(q,2)),scale(q2,F(2,3)))
    two_k_sh2k = add(scale(q,4),scale(q2,F(8,3)))
    right = add(mul([b,F(2)],ch2,3),two_k_sh2k)
    assert left[0] == right[0] == b
    c0 = left[0]/right[0]
    c1 = (left[1] - c0*right[1])/right[0]
    c2 = (left[2] - c0*right[2] - c1*right[1])/right[0]
    assert c0 == 1 and c1 == -expected_mean and 2*c2 == expected_m2


def analytic_optima_check():
    # Sign certificates and strict ordering of the three critical points.
    def p(b): return 5*b**4 + 10*b**3 - 8*b - 6
    def q(b): return 2*b**3 - 3*b*b - 9*b - 5
    assert p(F(0)) < 0 and p(F(1)) > 0
    assert q(F(3)) < 0 and q(F(4)) > 0
    # Both polynomials have exactly one positive root by Descartes' rule:
    # coefficients (+,+,0,-,-) and (+,-,-,-), respectively.
    # Numerically isolate each root within rational brackets of width 1e-9.
    def bisect(f, lo, hi, times=60):
        assert f(lo) < 0 < f(hi)
        for _ in range(times):
            mid = (lo+hi)/2
            if f(mid) > 0: hi = mid
            else: lo = mid
        return lo, hi
    v0,v1=bisect(p,F(0),F(1))
    c0,c1=bisect(q,F(3),F(4))
    assert v1-v0 < F(1,10**9) and c1-c0 < F(1,10**9)
    # Comparison m_min=sqrt(2/3) < v_min, since p(m_min)<0.
    from math import sqrt
    assert sqrt(2/3) < float(v0) < 1 < 3 < float(c0) and v0 < v1 and c0 < c1
    # Check exact candidate first-order signs at rational probes.
    for b in [F(1,2), F(4,5), F(9,10),F(1),F(3),F(7,2),F(4)]:
        cv_slope_num = q(b)
        variance_slope_num = p(b)
        assert (cv_slope_num < 0) == (b<c0)
        assert (variance_slope_num < 0) == (b<v0)
    return float((v0+v1)/2), float((c0+c1)/2)


def main():
    tests=[F(1,7),F(1,3),F(1,2),F(2,3),F(4,5),F(9,10),F(1),
           F(11,10),F(4,3),F(3,2),F(2),F(3),F(4),F(5),F(7),F(10)]
    for b in tests:
        mean,second=generator_check(b)
        laplace_check(b,mean,second)
    v,c=analytic_optima_check()
    print('VERIFY_OK: %d exact-rational independent parameter checks; %.12f %.12f' % (len(tests),v,c))


if __name__=='__main__': main()
