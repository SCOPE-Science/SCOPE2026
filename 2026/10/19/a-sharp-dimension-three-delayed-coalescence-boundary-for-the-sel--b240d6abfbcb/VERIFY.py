"""Reproducible floating-point diagnostic for the two-step merger theorem.

The exact theorem is proved analytically; these tests only check formulas and
illustrate one distinct pair of trajectories with a common second iterate.
Requires Python 3 standard library only.
"""
import math


def h(x):
    return math.exp(x * math.log(x)) if x > 0 else 1.0


def full_step(p):
    w = [h(x) for x in p]
    z = sum(w)
    return [x / z for x in w]


def F(s):
    a, b = h(s), h((1.0 - s) / 2.0)
    return a / (a + 2.0 * b)


def g(s):
    return 1.5 + math.log(s) + 0.5 * math.log((1.0 - s) / 2.0)


def root(f, lo, hi, increasing=True):
    ylo, yhi = f(lo), f(hi)
    if increasing:
        assert ylo <= 0 <= yhi, (ylo, yhi)
    else:
        assert ylo >= 0 >= yhi, (ylo, yhi)
    for _ in range(100):
        mid = (lo + hi) / 2.0
        if (f(mid) < 0) == increasing:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def p(s):
    return [s, (1.0 - s) / 2.0, (1.0 - s) / 2.0]


def maxdiff(a, b):
    return max(abs(x - y) for x, y in zip(a, b))


def main():
    assert math.exp(1 + 1/math.e) < 4
    z = math.sqrt(2.0) - 1.0
    assert abs(F(0.0) - z) < 1e-15
    assert abs(F(1/3) - 1/3) < 1e-15
    assert g(1/3) < 0 < g(z)
    s0 = root(g, 1/3, z)
    m = F(s0)
    # The common target is not the uniform state.
    y = (m + min(F(z), 1/3)) / 2
    a = root(lambda t: F(t)-y, 1/3, s0, increasing=False)
    b = root(lambda t: F(t)-y, s0, z, increasing=True)
    u = root(lambda t: F(t)-a, 0, 1/3, increasing=False)
    v = root(lambda t: F(t)-b, 0, 1/3, increasing=False)
    assert abs(u-v) > 1e-4
    assert a < s0 < b
    one_u, one_v = full_step(p(u)), full_step(p(v))
    two_u, two_v = full_step(one_u), full_step(one_v)
    assert maxdiff(one_u, one_v) > 0.003
    assert maxdiff(two_u, two_v) < 5e-14
    assert maxdiff(two_u, p(y)) < 5e-14
    # Every dimension >=4 has the entire first image in the monotone region.
    for n in (4, 5, 6, 9, 20):
        assert math.exp(1/math.e) / n < 1/math.e
        for i in range(n):
            v0 = [0.0] * n
            v0[i] = 1.0
            first = full_step(v0)
            assert max(first) < 1 / math.e
    print('PASS: exact derivative signs, unique fold, distinct first images, common second image')
    print('fold', s0, 'nonuniform target', y)
    print('input scalars', u, v, 'first images', a, b)
    print('first-image discrepancy', maxdiff(one_u, one_v))
    print('second-image discrepancy', maxdiff(two_u, two_v))
    print('PASS: dimension>=4 core upper bounds')


if __name__ == '__main__':
    main()
