import itertools
import math
import random

rng = random.Random(350060)

def fval(a, x):
    return 0.5 * sum(ai * xi * xi for ai, xi in zip(a, x))

def qsgd_exact_expectation(a, x, eta):
    g = [ai * xi for ai, xi in zip(a, x)]
    ng = math.sqrt(sum(gi * gi for gi in g))
    if ng == 0.0:
        return fval(a, x)
    return (
        fval(a, x)
        - eta * ng * ng
        + 0.5 * eta * eta * ng * sum(ai * abs(gi) for ai, gi in zip(a, g))
    )

def qsgd_enumeration(a, x, eta):
    g = [ai * xi for ai, xi in zip(a, x)]
    ng = math.sqrt(sum(gi * gi for gi in g))
    if ng == 0.0:
        return fval(a, x)
    p = [abs(gi) / ng for gi in g]
    ans = 0.0
    d = len(a)
    for bits in itertools.product((0, 1), repeat=d):
        prob = 1.0
        q = []
        for gi, pi, bi in zip(g, p, bits):
            prob *= pi if bi else (1.0 - pi)
            sg = 0.0 if gi == 0.0 else (1.0 if gi > 0.0 else -1.0)
            q.append(ng * sg * bi)
        xp = [xi - eta * qi for xi, qi in zip(x, q)]
        ans += prob * fval(a, xp)
    return ans

# Exhaustive distribution replay for random diagonal quadratics.
for d in range(1, 9):
    for _ in range(30):
        a = [10 ** rng.uniform(-1.0, 1.0) for _ in range(d)]
        x = [rng.uniform(-2.0, 2.0) for _ in range(d)]
        if sum(xi*xi for xi in x) < 1e-16:
            continue
        eta = 0.2 / math.sqrt(sum(ai*ai for ai in a))
        exact = qsgd_exact_expectation(a, x, eta)
        enum = qsgd_enumeration(a, x, eta)
        assert abs(exact - enum) < 2e-10 * max(1.0, abs(exact))

# Sharp curvature-profile threshold and attaining direction.
for d in range(1, 12):
    for _ in range(50):
        a = [10 ** rng.uniform(-2.0, 2.0) for _ in range(d)]
        anorm = math.sqrt(sum(ai*ai for ai in a))
        threshold = 2.0 / anorm
        x = [1.0 if rng.random() < 0.5 else -1.0 for _ in range(d)]
        f0 = fval(a, x)

        at = qsgd_exact_expectation(a, x, threshold)
        assert abs(at - f0) < 2e-10 * max(1.0, f0)

        below = qsgd_exact_expectation(a, x, 0.99 * threshold)
        above = qsgd_exact_expectation(a, x, 1.01 * threshold)
        assert below < f0
        assert above > f0

        for _j in range(20):
            y = [rng.uniform(-3.0, 3.0) for _ in range(d)]
            if sum(yi*yi for yi in y) < 1e-18:
                continue
            assert qsgd_exact_expectation(a, y, 0.95 * threshold) < fval(a, y) + 1e-12

# Isotropic exact worst factor.
for d in range(1, 30):
    L = 1.7
    h = 1.0 / math.sqrt(d)
    eta = h / L
    x = [1.0] * d
    factor = qsgd_exact_expectation([L]*d, x, eta) / fval([L]*d, x)
    target = 1.0 - 1.0 / math.sqrt(d)
    assert abs(factor - target) < 2e-12

    h1 = 1.0
    factor1 = qsgd_exact_expectation([L]*d, x, h1/L) / fval([L]*d, x)
    assert abs(factor1 - (math.sqrt(d)-1.0)) < 2e-12

assert abs((math.sqrt(4)-1.0)-1.0) < 1e-15
assert math.sqrt(5)-1.0 > 1.0

print("verification passed")
