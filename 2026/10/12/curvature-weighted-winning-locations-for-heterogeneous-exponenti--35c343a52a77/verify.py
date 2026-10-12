"""Deterministic checks of finite-n tail sums and winner-mark intensities.

The inequalities at finite n are diagnostics only. The continuum limit is proved
by a separate Laplace expansion and an exact order-statistic density identity.
"""
import math


def rate(t):
    return 1.0 + 100.0 * (t - 0.25) ** 2 * (t - 0.75) ** 2 * (1.0 + 8.0 * t)


def evaluate(n, y=0.0):
    a = [0.25, 0.75]
    curvature = [150.0, 350.0]
    K = sum(math.sqrt(2 * math.pi / v) for v in curvature)
    L = math.log(n)
    b = L - 0.5 * math.log(L) + math.log(K)
    x = b + y
    total = 0.0
    g = [0.0, 0.0]
    product_log = 0.0
    max_q = 0.0
    for i in range(1, n + 1):
        t = i / n
        q = math.exp(-rate(t) * x)
        total += q
        product_log += math.log1p(-q)
        max_q = max(max_q, q)
        g[0 if t < 0.5 else 1] += q
    predicted = [math.sqrt(2 * math.pi / v) / K for v in curvature]
    return {
        'n': n, 'y': y, 'sum_tail': total, 'limit_tail': math.exp(-y),
        'cdf_max': math.exp(product_log),
        'limit_cdf': math.exp(-math.exp(-y)),
        'location_tail_weights': [v / total for v in g],
        'limit_location_weights': predicted,
        'max_single_tail': max_q,
    }


def main():
    for n in (5000, 20000, 100000, 300000):
        row = evaluate(n)
        print(row)
        assert abs(sum(row['location_tail_weights'])-1) < 1e-10
        assert max(row['location_tail_weights']) < 1
        assert row['max_single_tail'] < 1.0 / n**0.5
        assert abs(row['sum_tail'] - 1) < 0.4
    for y in (-1.0, 0.0, 1.0):
        row = evaluate(300000, y)
        assert abs(row['cdf_max'] - row['limit_cdf']) < 0.10
    assert abs(rate(0.25) - 1.0) < 1e-14
    assert abs(rate(0.75) - 1.0) < 1e-14
    h = 1e-5
    for t, c in ((0.25,150),(0.75,350)):
        q = (rate(t+h)+rate(t-h)-2*rate(t))/h**2
        assert abs(q-c) < 1e-3
    print('FINITE_DIAGNOSTICS_OK')


if __name__ == '__main__':
    main()
