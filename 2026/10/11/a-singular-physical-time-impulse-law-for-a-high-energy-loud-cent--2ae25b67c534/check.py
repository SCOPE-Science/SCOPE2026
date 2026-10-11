"""Optional finite checks for the exact quadratures in the accompanying result.

Requires only Python 3.10+ standard library. Numerical convergence is not proof.
"""
import math


def simpson(fun, lo, hi, n=4000):
    assert n > 0 and n % 2 == 0
    h = (hi - lo) / n
    accum = fun(lo) + fun(hi)
    for j in range(1, n):
        accum += (4 if j % 2 else 2) * fun(lo + j * h)
    return accum * h / 3


def turning_points(E):
    left, right = E, E + 1
    for _ in range(90):
        a = (left + right) / 2
        if a + math.exp(-a) - 1 < E:
            left = a
        else:
            right = a
    a = (left + right) / 2
    left, right = 0.0, math.log(E + 1) + 2
    for _ in range(90):
        r = (left + right) / 2
        if math.exp(r) - r - 1 < E:
            left = r
        else:
            right = r
    return a, (left + right) / 2


def times(E):
    a, r = turning_points(E)
    c = math.exp(-a)
    def pos(u):
        if u == 0:
            return math.sqrt(2 / (1 - c))
        w = u * u
        return math.sqrt(2) / math.sqrt(1 - c * math.expm1(w) / w)
    z = math.exp(r)
    def neg(u):
        if u == 0:
            return math.sqrt(2 / (z - 1))
        w = u * u
        return math.sqrt(2) * u / math.sqrt(z * (-math.expm1(-w)) - w)
    tp = simpson(pos, 0, math.sqrt(a))
    tn = simpson(neg, 0, math.sqrt(r))
    return a, r, tp, tn


def run():
    for q, p in [(0.2, -1.1), (2.5, 0.9), (-1.0, -0.3)]:
        x, y = 1 - math.exp(-q), -p
        qdot, pdot = p, math.exp(-q) - 1
        assert abs(math.exp(-q) * qdot + y * (1 - x)) < 1e-13
        assert abs(-pdot - x) < 1e-13
        assert abs(p * pdot + (1 - math.exp(-q)) * qdot) < 1e-13
    ratios = []
    negative_fractions = []
    for E in [16, 64, 256]:
        a, r, tp, tn = times(E)
        assert abs(a + math.exp(-a) - 1 - E) < 1e-10
        assert abs(math.exp(r) - r - 1 - E) < 1e-10
        period = 2 * (tp + tn)
        ratios.append(period / (2 * math.sqrt(2 * E)))
        negative_fractions.append(tn / (tp + tn))
    assert 1 < ratios[2] < ratios[1] < ratios[0] < 1.2, ratios
    assert 0 < negative_fractions[2] < negative_fractions[1] < negative_fractions[0] < 0.2
    # These limits are mathematical assertions proved in RESULT.md, not established by the finite checks.
    print('CHECK_OK', 'period_ratios=', [round(z, 6) for z in ratios],
          'negative_phase_fractions=', [round(z, 6) for z in negative_fractions])

if __name__ == '__main__':
    run()
