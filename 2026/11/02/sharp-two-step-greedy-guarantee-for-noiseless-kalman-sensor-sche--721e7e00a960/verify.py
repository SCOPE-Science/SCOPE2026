"""Reproducible exact-arithmetic checks for two-time Kalman sensor scheduling."""
from fractions import Fraction as F
from random import Random


def schedule_costs(p, q, a):
    """Exhaustive trace costs after observing one exact coordinate at each time."""
    out = {}
    for first in (0, 1):
        v1 = [p[0], p[1]]
        v1[first] = 0
        prior = [a[i] * a[i] * v1[i] + q[i] for i in range(2)]
        for second in (0, 1):
            v2 = prior.copy()
            v2[second] = 0
            out[first, second] = sum(v1) + sum(v2)
    return out


def myopic_cost(cost, p, q, a):
    first = 0 if p[0] >= p[1] else 1
    unobserved = 1 - first
    time2_prior = [q[0], q[1]]
    time2_prior[unobserved] += a[unobserved] ** 2 * p[unobserved]
    second = 0 if time2_prior[0] >= time2_prior[1] else 1
    return cost[first, second]


def noisy_cost(p, q, a, path, noise):
    var = list(map(float, p))
    total = 0.
    for k, observed in enumerate(path):
        if k:
            var = [a[i] ** 2 * var[i] + q[i] for i in range(2)]
        var[observed] = var[observed] * noise / (var[observed] + noise)
        total += sum(var)
    return total


def noisy_greedy(p, q, a, noise):
    var = list(map(float, p))
    decisions = []
    total = 0.
    for k in range(2):
        if k:
            var = [a[i] ** 2 * var[i] + q[i] for i in range(2)]
        observed = 0 if var[0] >= var[1] else 1
        decisions.append(observed)
        var[observed] = var[observed] * noise / (var[observed] + noise)
        total += sum(var)
    return tuple(decisions), total


def verify():
    rng = Random(20231027)
    for _ in range(20000):
        p = [F(rng.randint(1, 30), rng.randint(1, 12)) for i in range(2)]
        q = [F(rng.randint(1, 30), rng.randint(1, 12)) for i in range(2)]
        a = [F(rng.randint(-8, 8), rng.randint(1, 8)) for i in range(2)]
        cost = schedule_costs(p, q, a)
        G = myopic_cost(cost, p, q, a)
        O = min(cost.values())
        assert G >= O > 0
        assert G / O <= 1 + max(v * v for v in a)
        assert cost[0, 0] == (1 + a[1] ** 2) * p[1] + q[1]
        assert cost[0, 1] == p[1] + q[0]
        assert cost[1, 0] == p[0] + q[1]
        assert cost[1, 1] == (1 + a[0] ** 2) * p[0] + q[0]
        if p[0] >= p[1]:
            predicted = p[1] + min(q[0], a[1] ** 2 * p[1] + q[1])
            assert G == predicted and O == min(G, p[0] + q[1])
            assert (G > O) == (p[0] - p[1] < min(q[0] - q[1], a[1] ** 2 * p[1]))
        else:
            predicted = p[0] + min(q[1], a[0] ** 2 * p[0] + q[0])
            assert G == predicted and O == min(G, p[1] + q[0])
            assert (G > O) == (p[1] - p[0] < min(q[1] - q[0], a[0] ** 2 * p[0]))
    for R in (F(1, 4), F(1), F(9), F(100)):
        delta = min(R, F(1)) / 100000
        p = [1 + delta, F(1)]
        q = [R + 2, delta]
        a = [F(0), F(int(R.numerator**0.5)) if R.denominator == 1 else F(1, 2)]
        assert a[1] ** 2 == R
        cost = schedule_costs(p, q, a)
        greedy = myopic_cost(cost, p, q, a)
        optimal = min(cost.values())
        assert greedy == 1 + R + delta
        assert optimal == 1 + 2 * delta
        assert cost[1, 0] == optimal
        assert 0 < (1 + R) - greedy / optimal < F(3, 100)
        print('growth_squared=', R, 'ratio=', float(greedy / optimal), 'limit=', float(1 + R))
    p = [F(11, 10), F(1)]
    q = [F(3), F(1, 10)]
    a = [F(0), F(1)]
    schedule, greedy = noisy_greedy(p, q, a, 0.000001)
    costs = {ij: noisy_cost(p, q, a, ij, 0.000001) for ij in ((0, 0), (0, 1), (1, 0), (1, 1))}
    assert schedule == (0, 0)
    assert costs[(1, 0)] < greedy and costs[(1, 0)] == min(costs.values())
    print('VERIFY_OK 20000 exact rational schedule instances, 4 sharpness families, positive-noise robustness')


if __name__ == '__main__':
    verify()
