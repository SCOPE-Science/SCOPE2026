"""Reproducible numerical checks for the exact symmetric two-ball-lens ellipsoid formulas.

Standard-library computation. The accompanying analytic proof certifies all dimensions;
finite tests here are diagnostics, not proof of an infinite family.
"""
import math
import random


def parameters(d, h):
    assert d >= 2 and 0 <= h < 1
    k = (d + 1) * h / math.sqrt(d)
    a = (2 * (1 - h * h)) / (math.sqrt(k * k + 4 * (1 - h * h)) + k)
    b2 = a * a + h * a * math.sqrt(d)
    return a, math.sqrt(b2)


def log_volume_ratio(d, h):
    a, b = parameters(d, h)
    return math.log(a) + (d - 1) * math.log(b)


def critical_limit(t):
    a = 2 / (math.sqrt(t * t + 4) + t)
    return a * math.exp(-t * (a + t) / 2)


def main():
    rng = random.Random(20261024)
    diagnostics = 0
    for d in (2, 3, 4, 5, 8, 13, 25, 60):
        for h in (0.0001, 0.0125, 0.1, 0.25, 0.49, 0.8, 0.99):
            a, b = parameters(d, h)
            assert a > 0 and b > 0
            assert abs(a*a + (d+1)/math.sqrt(d)*h*a + h*h - 1) < 4e-12
            assert abs(b*b-a*a-h*a*math.sqrt(d)) < 4e-12
            diagnostics += 2
            for k in range(250):
                q = rng.random()
                gap = 1 - ((h + a*q)**2 + b*b*(1-q*q))
                expected = h*a*math.sqrt(d)*(q-1/math.sqrt(d))**2
                assert gap > -1e-12
                assert abs(gap-expected) < 4e-12
                diagnostics += 2
            # Each of the 4(d-1) normalized signed contact points has weight d/(4(d-1)).
            # Evaluate the entire second-moment matrix directly.
            size = d
            gram = [[0.0 for _ in range(size)] for _ in range(size)]
            mean = [0.0 for _ in range(size)]
            weight = d/(4*(d-1))
            for j in range(1, d):
                for e in (-1, 1):
                    for s in (-1, 1):
                        v = [0.0 for _ in range(d)]
                        v[0] = e / math.sqrt(d)
                        v[j] = s * math.sqrt((d-1)/d)
                        assert abs(sum(z*z for z in v)-1) < 1e-12
                        for i in range(d):
                            mean[i] += weight*v[i]
                            for t in range(d):
                                gram[i][t] += weight*v[i]*v[t]
            assert max(abs(z) for z in mean) < 1e-11
            assert max(abs(gram[i][j]-(1.0 if i==j else 0.0)) for i in range(d) for j in range(d)) < 1e-10
            diagnostics += 3
    for t in (0.15, 0.7, 1.0, 2.5, 5):
        target = critical_limit(t)
        for d in (500, 3000, 20000):
            h = t/math.sqrt(d)
            assert h < 1
            actual = math.exp(log_volume_ratio(d, h))
            if d == 20000:
                assert abs(actual/target-1) < 0.01
            diagnostics += 1
    for h in (0.15, 0.4, 0.7, 0.9):
        for d in (500, 3000, 20000):
            actual_log = log_volume_ratio(d, h)
            target_log = -.5 + ((d+1)/2)*math.log1p(-h*h)-math.log(h)-math.log(d)/2
            if d == 20000:
                assert abs(actual_log-target_log) < .002
            diagnostics += 1
    print('SUCCESS:', diagnostics, 'independent numeric identities, inclusions, contact moments, asymptotic checks')


if __name__ == '__main__':
    main()
