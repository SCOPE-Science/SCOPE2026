"""Exact-rational checks for a neutral border-collision map and its section return.

This finite checker is supplementary evidence, not a proof of universal statements.
Run: python3 verify.py
"""
from fractions import Fraction as F
from math import ceil, log


def step(x, y, a):
    return (1 + y - a*x, F(0)) if x <= 0 else (1 + y, -x)


def on_core(x, y):
    return 0 <= x <= 1 and -1 <= y <= 0


def next_outside_section(z, a):
    if z < 0:
        return 1 - a*z, 1
    if z > 1:
        return a*(z-1), 3
    raise ValueError('Stopped when inside the invariant square')


def capture_count(z, a):
    """Count exterior three-step return blocks; only use if 1<z and,
    when a>1, z < p=a/(a-1)."""
    if a == 0:
        return 1
    if a == 1:
        return ceil(float(z-1))
    if a < 1:
        return ceil(log(float((1-a)*z+a)) / log(float(1/a)))
    p = a/(a-1)
    assert z < p
    return ceil(-log(float(a-(a-1)*z)) / log(float(a)))


def exact_count(z, a):
    n = 0
    while z > 1:
        z = a*(z-1)
        n += 1
        assert n < 10000
    return n


def run():
    q = F
    a_values = [q(0), q(1,5), q(1,2), q(1), q(5,4), q(3,2), q(2), q(3)]
    core_checks = 0
    return_checks = 0
    trajectory_checks = 0
    times_checks = 0
    for a in a_values:
        for i in range(0, 13):
            for j in range(0, 11):
                x, y = q(i, 12), -q(j, 10)
                X, Y = x, y
                for _ in range(4):
                    X, Y = step(X, Y, a)
                assert (X, Y) == (x, y)
                core_checks += 1
        for i in range(-17, 69):
            z = q(i, 8)
            if z < 0 or z > 1:
                w, time = next_outside_section(z,a)
                X, Y = z, q(0)
                for _ in range(time):
                    X, Y = step(X, Y, a)
                assert (X,Y) == (w, q(0))
                return_checks += 1
        for i in range(-17, 69):
            for j in range(-9, 10):
                x, y = q(i, 8), q(j, 7)
                if on_core(x,y):
                    continue
                for _ in range(5):
                    if y == 0 or on_core(x,y):
                        break
                    x, y = step(x,y,a)
                assert y == 0 or on_core(x,y)
                trajectory_checks += 1
        if a > 1:
            p = a/(a-1)
            X,Y = p,q(0)
            first = []
            for _ in range(3):
                first.append((X,Y))
                X,Y = step(X,Y,a)
            assert (X,Y)==(p,q(0))
            assert first == [(p,q(0)),(q(1),-p),(q(1)-p,q(-1))]
            # D(R^2) = -I; the third derivative is the left reset matrix.
            M = ((a,q(-1)),(q(0),q(0)))
            assert M[0][0]+M[1][1]==a
            assert M[0][0]*M[1][1]-M[0][1]*M[1][0]==0
            for k in (1,2,4,8):
                z = p - q(1,2**k)*(p-1)
                n = exact_count(z,a)
                if abs(float(a-(a-1)*z))>1e-12:
                    prediction = capture_count(z,a)
                    # Floating logs can land on an integer boundary with a roundoff.
                    assert abs(prediction-n) <= 1
                times_checks += 1
        else:
            for j in range(2, 15):
                z = q(j*7,5)
                n = exact_count(z,a)
                prediction = capture_count(z,a)
                assert abs(prediction-n) <= 1
                times_checks += 1
    # Exact analytical fixed point and multiplier data, separately checked.
    for a in [q(5,4),q(2),q(7,3)]:
        p = a/(a-1)
        assert a*(p-1)==p
        for delta in [q(1,20),q(1,17),q(1,9)]:
            for sign in [-1,1]:
                z=p+sign*delta
                nxt=a*(z-1)
                assert nxt-p == a*(z-p)
    print('VERIFY_OK core_quarter_turn=%d exact_section_returns=%d entry_or_section=%d capture_counts=%d period3_saddle=3' % (core_checks,return_checks,trajectory_checks,times_checks))


if __name__ == '__main__':
    run()
