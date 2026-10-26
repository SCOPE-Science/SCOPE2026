"""Independent numerical checks for the Green-Ampt intensity-order theorem.

The mathematical proof does not depend on this program. Uses continuous-
segment solutions with a monotone root, not time-stepping discretization.
"""
from math import isclose, log1p
from random import Random


def primitive(f, B):
    return f - B * log1p(f / B)


def segment(F, rate, duration, K=1.0, B=1.0):
    assert F >= 0 and rate > 0 and duration >= 0 and K > 0 and B > 0
    if not duration:
        return F
    if rate <= K:
        return F + rate * duration
    threshold = K * B / (rate - K)
    if F < threshold:
        t_to_capacity = (threshold - F) / rate
        if duration <= t_to_capacity:
            return F + rate * duration
        F, duration = threshold, duration - t_to_capacity
    target = primitive(F, B) + K * duration
    lo = F
    hi = F + rate * duration + 1
    while primitive(hi, B) < target:
        hi *= 2
    for _ in range(100):
        mid = (lo + hi) / 2
        if primitive(mid, B) < target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def compare(K, B, F0, lo, hi, dlo, dhi):
    descending = segment(segment(F0, hi, dhi, K, B), lo, dlo, K, B)
    ascending = segment(segment(F0, lo, dlo, K, B), hi, dhi, K, B)
    upper_cut = K * B / (hi - K) if hi > K else float('inf')
    lower_cut = K * B / (lo - K) if lo > K else float('inf')
    strict = (F0 < lower_cut and F0 + hi * dhi + lo * dlo > upper_cut)
    return descending, ascending, strict


def main():
    K, B, F0, low, high, tl, th = 1.0, 1.0, 0.25, 1.5, 3.0, 0.2, 0.2
    a, b, strict = compare(K, B, F0, low, high, tl, th)
    print('two-block example: descending=', format(a, '.12f'),
          ' ascending=', format(b, '.12f'), ' difference=', format(a - b, '.12f'))
    assert strict and a - b > 1e-3

    # Representative equality regimes: rainfall below initial capacity;
    # both rates below conductivity; initial wetting front beyond lower
    # capacity threshold.
    for cfg in [
        (1.0, 1.0, 0.25, 0.5, 0.7, 1.0, 1.0),
        (1.0, 1.0, 0.25, 0.7, 2.0, 0.5, 0.1),
        (1.0, 1.0, 3.0, 1.5, 3.0, 0.2, 0.2),
    ]:
        u, v, expect = compare(*cfg)
        assert not expect and isclose(u, v, rel_tol=2e-11, abs_tol=2e-11)

    r = Random(1978)
    for _ in range(3000):
        K = 10 ** r.uniform(-0.5, 0.5)
        B = 10 ** r.uniform(-0.5, 0.5)
        F0 = 10 ** r.uniform(-1, 1)
        low = K * 10 ** r.uniform(-0.6, 0.3)
        high = low * 10 ** r.uniform(0.1, 0.8)
        tl = 10 ** r.uniform(-1, 0.5)
        th = 10 ** r.uniform(-1, 0.5)
        descending, ascending, strict = compare(K, B, F0, low, high, tl, th)
        assert descending >= ascending - 3e-10 * max(1, descending)
        if not strict:
            assert isclose(descending, ascending, abs_tol=3e-10,
                           rel_tol=3e-10)
    print('3000 deterministic randomized parameter checks passed.')


if __name__ == '__main__':
    main()
