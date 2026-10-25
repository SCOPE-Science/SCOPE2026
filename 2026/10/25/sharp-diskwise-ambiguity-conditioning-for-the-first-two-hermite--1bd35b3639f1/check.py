"""Numerical corroboration for two Hermite-window ambiguity coverage.

Python 3 standard library; scientific proof is independent of these tests.
"""
import math
import random


def envelope(s, w):
    return math.exp(-s) * (1.0 + w * s * (s - 2.0))


def minimum_on_disk(R, w):
    nodes = [0.0, R]
    if w > 0.5:
        u = math.sqrt(2.0 - 1.0 / w)
        nodes.extend(x for x in (2.0 - u, 2.0 + u) if 0.0 <= x <= R)
    return min(envelope(s, w) for s in nodes)


def optimal_weight(R):
    if R < 2.0:
        return 0.0
    if R == 2.0:
        return 0.5
    def equation(u):
        return 2.0 * (1.0 - u) * math.exp(R - 2.0 + u) - ((R - 1.0)**2 + 1.0 - u*u)
    lo, hi = 0.0, 1.0
    assert equation(lo) > 0.0 and equation(hi) < 0.0
    for _ in range(80):
        mid = (lo + hi) / 2.0
        if equation(mid) > 0.0:
            lo = mid
        else:
            hi = mid
    u = (lo + hi) / 2.0
    return 1.0 / (2.0 - u*u)


def run():
    rng = random.Random(137)
    count = 0
    for R in [0.1, 0.8, 1.5, 2.0, 2.1, 2.5, 3.0, 4.0, 6.0, 10.0, 20.0]:
        wstar = optimal_weight(R)
        val = minimum_on_disk(R, wstar)
        assert val > 0.0
        if R < 2.0:
            assert wstar == 0.0
            assert abs(val - math.exp(-R)) < 1.0e-13
        elif R == 2.0:
            assert abs(val - math.exp(-2.0)) < 1.0e-13
        else:
            u = math.sqrt(2.0 - 1.0 / wstar)
            inner = envelope(2.0 - u, wstar)
            outer = envelope(R, wstar)
            assert 0.5 < wstar < 1.0
            assert abs(inner - outer) < 5.0e-13
            assert val >= math.exp(-R) * (1.0 + 1.0e-9)
            count += 4
        for i in range(101):
            w = i / 100.0
            got = minimum_on_disk(R, w)
            assert got <= val + 1.0e-12, (R, w, got, val)
            if i % 10 == 0:
                sampled = min(envelope(R * j / 2000.0, w) for j in range(2001))
                assert sampled >= got - 1.0e-12
                assert sampled <= got + 3.0e-5
                count += 2
            count += 1
    for _ in range(150):
        R = rng.uniform(0.05, 18.0)
        w = rng.uniform(0.0, 1.0)
        exact = minimum_on_disk(R, w)
        grid = min(envelope(R * j / 3000.0, w) for j in range(3001))
        assert exact <= grid + 1.0e-12
        assert grid <= exact + 8.0e-5
        count += 2
    prev = 0.5
    for R in [2.02, 2.05, 2.1, 2.5, 3., 4., 5., 7., 10., 16., 20.]:
        w = optimal_weight(R)
        assert w > prev
        prev = w
        count += 1
    for t in [0.02, 0.04, 0.08]:
        v = (optimal_weight(2.0+t)-0.5) / (t*t)
        assert 0.045 < v < 0.064
        count += 1
    for R in [12., 16., 20.]:
        w = optimal_weight(R)
        gain = minimum_on_disk(R, w) / math.exp(-R)
        assert abs(gain / ((R-1.0)**2) - 1.0) < 0.05
        count += 1
    print('PASS:',count,'numerical assertions')
    for R in [2.1, 3., 4., 6., 10.]:
        w=optimal_weight(R)
        print(f'R={R:4.1f}  weight={w:.12f}  minimum={minimum_on_disk(R,w):.12g}  gain={minimum_on_disk(R,w)/math.exp(-R):.8g}')

if __name__ == '__main__':
    run()
