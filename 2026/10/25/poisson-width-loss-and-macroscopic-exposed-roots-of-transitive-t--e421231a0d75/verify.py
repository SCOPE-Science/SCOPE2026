"""Finite algebraic and stochastic diagnostics for positive-root directional widths.

The asymptotic conclusions require the mathematical proof; this file only
checks exact finite identities and explores their distributional scaling.
"""
import math
import random
import statistics

RNG = random.Random(20261018)


def optimized(g):
    """Return two directed support values and corresponding ordered pairs."""
    best_plus = (-math.inf, -1, -1)
    best_minus = (-math.inf, -1, -1)
    ix_max = ix_min = 0
    for j in range(1, len(g)):
        if g[ix_max] - g[j] > best_plus[0]:
            best_plus = (g[ix_max] - g[j], ix_max, j)
        if g[j] - g[ix_min] > best_minus[0]:
            best_minus = (g[j] - g[ix_min], ix_min, j)
        if g[j] > g[ix_max]:
            ix_max = j
        if g[j] < g[ix_min]:
            ix_min = j
    return best_plus, best_minus


def exhaustive(g):
    n = len(g)
    return (
        max((g[i] - g[j], i, j) for i in range(n) for j in range(i + 1, n)),
        max((g[j] - g[i], i, j) for i in range(n) for j in range(i + 1, n)),
    )


def pp_trial(B):
    """Independent spatial marked Poisson processes restricted to mark>=-B."""
    limit = math.exp(B)
    def cloud():
        z = 0.0
        points = []
        while True:
            z += RNG.expovariate(1.0)
            if z >= limit:
                break
            points.append((RNG.random(), -math.log(z)))
        return points
    high, low = cloud(), cloud()
    if not high or not low:
        return None
    events = sorted([(t, x, 0) for t, x in high] +
                    [(t, x, 1) for t, x in low])
    max_high = (-math.inf, 0.0)
    max_low = (-math.inf, 0.0)
    forward = (-math.inf, 0.0, 0.0)
    reverse = (-math.inf, 0.0, 0.0)
    for t, x, kind in events:
        if kind == 0:
            if x + max_low[0] > reverse[0]:
                reverse = (x + max_low[0], max_low[1], t)
            if x > max_high[0]:
                max_high = (x, t)
        else:
            if x + max_high[0] > forward[0]:
                forward = (x + max_high[0], max_high[1], t)
            if x > max_low[0]:
                max_low = (x, t)
    top = max(x for _, x in high) + max(y for _, y in low)
    loss = 2.0 * top - forward[0] - reverse[0]
    return loss, forward, reverse, high, low


checks = 0
for n in (3, 4, 7, 13, 24):
    for _ in range(180):
        g = [RNG.gauss(0, 1) for _ in range(n)]
        a, b = optimized(g)
        a2, b2 = exhaustive(g)
        assert abs(a[0] - a2[0]) < 1e-12
        assert abs(b[0] - b2[0]) < 1e-12
        full = max(g) - min(g)
        assert abs(max(a[0], b[0]) - full) < 1e-12
        assert min(a[0], b[0]) < full
        mean = sum(g) / n
        r = math.sqrt(sum((x - mean) ** 2 for x in g))
        u = [(x - mean) / r for x in g]
        au, bu = optimized(u)
        assert abs((au[0] + bu[0]) * r - (a[0] + b[0])) < 1e-11
        assert abs(2 * (max(u) - min(u)) * r - 2 * full) < 1e-11
        checks += 1

point_checks = 0
for _ in range(45):
    trial = pp_trial(2.5)
    if trial is None:
        continue
    loss, forward, reverse, high, low = trial
    f2 = max((x + y, t, s) for t, x in high for s, y in low if t < s)
    r2 = max((x + y, s, t) for t, x in high for s, y in low if t > s)
    assert abs(f2[0] - forward[0]) < 1e-12
    assert abs(r2[0] - reverse[0]) < 1e-12
    assert abs(max(forward[0], reverse[0]) -
               (max(x for _, x in high) + max(y for _, y in low))) < 1e-12
    assert loss >= -1e-12
    point_checks += 1

for n in (500, 4000):
    samples = []
    spans = []
    scale = math.sqrt(2 * math.log(n))
    for _ in range(500):
        g = [RNG.gauss(0, 1) for _ in range(n)]
        a, b = optimized(g)
        samples.append(scale * (2 * (max(g) - min(g)) - a[0] - b[0]))
        spans.append((a[2] - a[1]) / n)
    print('Gaussian', n, 'scaled_loss_mean=', round(statistics.mean(samples), 4),
          'exposed_gap_mean=', round(statistics.mean(spans), 4))

for B in (4.0, 6.0):
    samples = []
    spans = []
    for _ in range(500):
        trial = pp_trial(B)
        if trial is None:
            continue
        loss, forward, _, _, _ = trial
        samples.append(loss)
        spans.append(forward[2] - forward[1])
    print('Poisson_cutoff', B, 'scaled_loss_mean=', round(statistics.mean(samples), 4),
          'exposed_gap_mean=', round(statistics.mean(spans), 4))

print('VERIFY_OK exact_support=', checks, 'poisson_brute=', point_checks)
