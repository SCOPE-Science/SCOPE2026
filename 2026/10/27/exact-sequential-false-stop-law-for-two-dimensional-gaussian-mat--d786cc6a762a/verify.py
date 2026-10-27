"""Deterministic numerical checks of the two-look-ahead Gaussian QB law.

Run with Python 3: python verify.py. These finite checks supplement the proof;
they do not establish universal identities or historical originality.
"""
import math
import random


def quadrature_probs(a, b, tau, strips=12000):
    if not (a >= b > 0 and 0 < tau < b and strips % 2 == 0):
        raise ValueError('Require a >= b > 0, 0 < tau < b and even strips')
    delta = (math.pi / 2) / strips
    accum0 = accum1 = 0.0
    for k in range(strips + 1):
        theta = k * delta
        d = b * b + (a * a - b * b) * math.cos(theta) ** 2
        p0 = -math.expm1(-tau * tau / (2 * d))
        p1 = math.exp(-tau * tau / (2 * d)) * math.erf(tau * math.sqrt(d) / (math.sqrt(2) * a * b))
        weight = 1 if k in (0, strips) else (4 if k % 2 else 2)
        accum0 += weight * p0
        accum1 += weight * p1
    return (2 / math.pi) * delta / 3 * accum0, (2 / math.pi) * delta / 3 * accum1


def limiting_prob(c, strips=12000):
    delta = (math.pi / 2) / strips
    acc = 0.0
    for k in range(strips + 1):
        theta = k * delta
        term = math.erf(c * math.cos(theta) / math.sqrt(2))
        acc += (1 if k in (0, strips) else (4 if k % 2 else 2)) * term
    return (2 / math.pi) * delta / 3 * acc


def residual_cdf(r, a, b):
    if not a > b > 0:
        raise ValueError('This density is for unequal positive singular values')
    if r <= b:
        return 0.0
    if r >= a:
        return 1.0
    u = (b * b * (a * a - r * r)) / (r * r * (a * a - b * b))
    return 2 * math.acos(math.sqrt(u)) / math.pi


def one_run(a, b, tau, rng):
    x, y = rng.gauss(0, 1), rng.gauss(0, 1)
    u, v = rng.gauss(0, 1), rng.gauss(0, 1)
    Ax, Ay = a * x, b * y
    L = math.hypot(Ax, Ay)
    if L <= tau:
        return 0
    q1, q2 = Ax / L, Ay / L
    # Direct two-sided action of the rank-one orthogonal residual (I-qq^T)A.
    W1, W2 = a * u, b * v
    dot = q1 * W1 + q2 * W2
    W1 -= q1 * dot
    W2 -= q2 * dot
    direct_norm = math.hypot(W1, W2)
    residual2 = (a - q1 * q1 * a) ** 2 + (b - q2 * q2 * b) ** 2
    residual2 += (q1 * q2 * a) ** 2 + (q1 * q2 * b) ** 2
    closed = (a * b) ** 2 * (x * x + y * y) / (a * a * x * x + b * b * y * y)
    assert abs(residual2 - closed) < 2e-10 * max(1, a * a)
    assert b * b * (1 - 1e-12) <= closed <= a * a * (1 + 1e-12)
    return 1 if direct_norm <= tau else 2


def main():
    cases = [(1, 1, 0.5), (4, 1, 0.5), (100, 1, 0.5), (7, 2, 1.4)]
    checks = 0
    for i, (a, b, tau) in enumerate(cases):
        p0, p1 = quadrature_probs(a, b, tau)
        assert 0 < p0 < 1 and 0 < p1 < 1 and p0 + p1 < 1
        rng = random.Random(7300 + i)
        n = 100000
        counts = [0, 0, 0]
        for _ in range(n):
            counts[one_run(a, b, tau, rng)] += 1
        obs = [v / n for v in counts]
        target = [p0, p1, 1 - p0 - p1]
        assert max(abs(x - y) for x, y in zip(obs, target)) < 0.008, (cases[i], obs, target)
        checks += n + 5
        print(f'case a={a}, b={b}, tau={tau}: theory {target}; observed {obs}')
    rng = random.Random(8627)
    a, b = 4.0, 1.0
    thresholds = [1.25, 1.5, 2.0, 3.0]
    tally = [0] * len(thresholds)
    n_resid = 100000
    for _ in range(n_resid):
        x, y = rng.gauss(0, 1), rng.gauss(0, 1)
        residual = a * b * math.hypot(x, y) / math.hypot(a * x, b * y)
        for i, threshold in enumerate(thresholds):
            tally[i] += residual <= threshold
    for t, hit in zip(thresholds, tally):
        assert abs(hit / n_resid - residual_cdf(t, a, b)) < 0.009
    checks += n_resid + len(thresholds)
    p0, p1 = quadrature_probs(1, 1, 0.5)
    assert abs(p0 - (1 - math.exp(-0.5 ** 2 / 2))) < 1e-13
    assert abs(p1 - math.exp(-0.5 ** 2 / 2) * math.erf(0.5 / math.sqrt(2))) < 1e-13
    J = limiting_prob(0.5)
    assert abs(J - 0.24712605614758926) < 2e-12, J
    p0_large, p1_large = quadrature_probs(100000, 1, 0.5)
    assert abs(p0_large) < 1e-5
    assert abs(p1_large - J) < 2e-5
    checks += 5
    print(f'high-conditioning false-stop limit J(0.5)={J:.15f}; at kappa=100000: {p0_large+p1_large:.15f}')
    print(f'PASS numerical suite: {checks} trial/analytic checks (400000 sequential direct trials; 100000 residual-CDF trials)')


if __name__ == '__main__':
    main()
