#!/usr/bin/env python3
"""Exact-arithmetic replay for the sharp affine-detrending inequality."""
from fractions import Fraction as Q


def add(a, b):
    c = [Q(0)] * max(len(a), len(b))
    for j, x in enumerate(a): c[j] += x
    for j, x in enumerate(b): c[j] += x
    return trim(c)


def scale(a, c):
    return trim([Q(c) * x for x in a])


def mult(a, b):
    c = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): c[i+j] += x*y
    return trim(c)


def trim(a):
    while len(a) > 1 and a[-1] == 0: a.pop()
    return a


def deriv(a):
    return trim([j * a[j] for j in range(1, len(a))] or [Q(0)])


def value(a, x):
    y = Q(0)
    for c in a[::-1]: y = y*x + c
    return y


def left_primitive(t, a):
    return (1-a)*t*t/2+a*t*t*t/3


def right_primitive(t, a):
    return -t+(1-a)*t*t/2+a*t*t*t/3


def signed_kernel(x, t):
    return (int(t <= x) + t - 1 - (6*x-3)*t*(1-t))


def exact_row_norm(x):
    x = Q(x)
    if x > Q(1,2):
        return exact_row_norm(1-x)
    a = 6*x-3
    if x <= Q(1,3):
        t0 = -1/a
        assert x < t0 <= 1
        return -2*(right_primitive(t0,a)-right_primitive(x,a))
    return 2*left_primitive(x,a)


def stated_row_norm(x):
    x = min(Q(x), 1-Q(x))
    if x <= Q(1,3):
        return 4*(3*x*x-6*x+2)*(6*x*x-3*x+1)**2/(27*(1-2*x)**2)
    return 4*x*x*(1-x)**2


def main():
    tests = 0
    assert exact_row_norm(0) == Q(8,27); tests += 1
    assert exact_row_norm(Q(1,3)) == Q(16,81); tests += 1
    assert exact_row_norm(Q(1,2)) == Q(1,4); tests += 1
    assert exact_row_norm(1) == Q(8,27); tests += 1

    # Verify polynomial derivative identity globally, not by sampling.
    a = [Q(2),Q(-6),Q(3)]
    b = [Q(1),Q(-3),Q(6)]
    linear = [Q(-1),Q(2)]
    numerator = scale(mult(a,mult(b,b)),4)
    denominator = scale(mult(linear,linear),27)
    derivative_numerator = scale(mult(mult([Q(1),Q(-6),Q(6)],b),[Q(5),Q(-18),Q(12)]),8)
    lhs = add(mult(deriv(numerator),denominator), scale(mult(numerator,deriv(denominator)),-1))
    rhs = scale(mult(derivative_numerator,linear),27)
    assert lhs == rhs; tests += 1

    for j in range(1501):
        x = Q(j,1500)
        assert exact_row_norm(x) == stated_row_norm(x), (j,'row expression')
        assert exact_row_norm(x) <= Q(8,27), (j, 'upper bound')
        tests += 2

    # Exact endpoint extremizing sign: K(0,t)=(1-t)(3t-1).
    # Its negative and positive masses are both 4/27.
    a0 = Q(-3)
    endpoint_negative = right_primitive(Q(1,3),a0)-right_primitive(Q(0),a0)
    endpoint_positive = right_primitive(Q(1),a0)-right_primitive(Q(1,3),a0)
    assert endpoint_negative == Q(-4,27)
    assert endpoint_positive == Q(4,27)
    assert -endpoint_negative+endpoint_positive == Q(8,27)
    tests += 3

    for j in range(100):
        x = Q(j,100)
        for k in range(99):
            t = Q(2*k+1,200)
            # Avoid the diagonal where the indicator has a convention-dependent jump.
            if t == x or 1-t == 1-x:
                continue
            assert signed_kernel(x,t) == -signed_kernel(1-x,1-t)
            tests += 1
    print('PASS', tests, 'exact-rational assertions; analytical monotonicity is proved in RESULT.md')


if __name__ == '__main__':
    main()
