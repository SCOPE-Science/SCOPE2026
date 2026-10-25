"""Finite numeric cross-checks for the reflected Gaussian-particle matching law.

Requires only Python 3 standard library. This script checks representative cases,
not universally quantified statements; those follow from the written proof.
"""
import itertools
import math


def g(tau, d):
    return (tau * math.sqrt(2 / math.pi) *
            math.exp(-0.5 * (d / tau) ** 2) +
            d * math.erf(d / (math.sqrt(2) * tau)))


def g_tail(tau, d):
    x = abs(d)
    return (tau * math.sqrt(2 / math.pi) * math.exp(-0.5 * (x / tau) ** 2) -
            x * math.erfc(x / (math.sqrt(2) * tau)))


def w(r, sigma, d):
    return g_tail(sigma * math.sqrt(2 * (r + 1)), d) - g_tail(sigma * math.sqrt(2 * r), d)


def w2(r, sigma, d):
    tp = sigma * math.sqrt(2 * (r + 1))
    tm = sigma * math.sqrt(2 * r)
    return math.sqrt(2 / math.pi) * (math.exp(-d * d / (2 * tp * tp)) / tp -
                                       math.exp(-d * d / (2 * tm * tm)) / tm)


def threshold(r, sigma):
    return sigma * math.sqrt(2 * r * (r + 1) * math.log1p(1 / r))


def scores(r, sigma, a, b):
    return [(sum(w(r, sigma, x - b[p]) for x, p in zip(a, perm)), perm)
            for perm in itertools.permutations(range(len(b)))]


def check():
    count = 0
    for r in (1, 2, 5, 10):
        for sigma in (0.4, 1.0, 2.3):
            t = threshold(r, sigma)
            assert abs(w2(r, sigma, t)) < 1e-13 / sigma
            assert w2(r, sigma, 0.25 * t) < 0 < w2(r, sigma, 1.6 * t)
            for n in (2, 3, 4):
                span = 0.15 * t
                a = tuple(span * i / n for i in range(n))
                b = tuple(0.03 * t + span * i / n for i in range(n))
                vals = sorted(scores(r, sigma, a, b), reverse=True)
                assert vals[0][1] == tuple(range(n))
                assert vals[0][0] - vals[1][0] > 1e-10 * sigma
                # All cross distances exceed the positive curvature radius.
                b_far = tuple(4.0 * t + span * i / n for i in range(n))
                vals = sorted(scores(r, sigma, a, b_far), reverse=True)
                assert vals[0][1] == tuple(reversed(range(n)))
                assert vals[0][0] - vals[1][0] > 1e-14 * sigma
                count += 2
            for delta in (0.02 * sigma, 0.05 * sigma, 0.1 * sigma):
                def gap(d):
                    return w(r, sigma, d - delta) + w(r, sigma, d + delta) - 2 * w(r, sigma, d)
                lo = t - delta
                hi = t + delta
                assert gap(lo) < 0 < gap(hi)
                for _ in range(55):
                    mid = (lo + hi) / 2
                    if gap(mid) > 0:
                        hi = mid
                    else:
                        lo = mid
                root = (lo + hi) / 2
                coeff = ((2 * r + 1) * math.log1p(1 / r) - 1) / (12 * t)
                assert abs((root - t) / delta ** 2 - coeff) < 0.008 / sigma
                count += 1
            D = 3 * t
            # Check positive gains and superiority of reverse matching.
            Wd, W2d, W3d = (w(r, sigma, z) for z in (D, 2 * D, 3 * D))
            assert Wd + W3d > 2 * W2d > 0
            count += 1
    # Fixed stage r=1, dimensionless asymptotic at moderately large separation.
    r, sigma, D = 1, 1.0, 10.0
    exact = (w(r, sigma, D) + w(r, sigma, 3 * D)) / (2 * w(r, sigma, 2 * D))
    predicted = 2 * math.exp(3 * D * D / (4 * (r + 1) * sigma * sigma))
    assert 0.80 < exact / predicted < 1.10
    print(f"PASS: {count} curvature/assignment/crossover/gain configurations and asymptotic comparison")


if __name__ == "__main__":
    check()
