"""Exact tests for neighborhood lower-median filtering on complete bipartite graphs.
Run with Python 3; no third-party dependencies are required.
"""
from itertools import product
from fractions import Fraction
from random import Random


def lower_median(values):
    return sorted(values)[(len(values) - 1) // 2]


def cut_cost(bits_x, bits_y, weights):
    return sum(weights[i][j] * (bits_x[i] != bits_y[j])
               for i in range(len(bits_x)) for j in range(len(bits_y)))


def weighted_variation(x, y, weights):
    return sum(weights[i][j] * abs(x[i] - y[j])
               for i in range(len(x)) for j in range(len(y)))


def optimum_binary_cut(weights):
    p, q = len(weights), len(weights[0])
    best = None
    best_config = None
    for bits in product((0, 1), repeat=p + q):
        a, b = bits[:p], bits[p:]
        if lower_median(a) == lower_median(b):
            continue
        cost = cut_cost(a, b, weights)
        if best is None or cost < best:
            best = cost
            best_config = (a, b)
    assert best is not None and best > 0
    return best, best_config


def unweighted_constant(p, q):
    if p % 2 == 1 and q % 2 == 1:
        return Fraction(2*p*q, p*q + 1)
    return Fraction(2)


def median_step(x, y):
    return ([lower_median(y)] * len(x), [lower_median(x)] * len(y))


def run():
    checks = {'unweighted_binary': 0, 'weighted_binary': 0,
              'real_signal': 0, 'dynamics': 0, 'witness': 0}
    # Unweighted checks cover all binary configurations for part sizes through 7.
    for p in range(1, 8):
        for q in range(1, 8):
            weights = [[1] * q for _ in range(p)]
            c, witness = optimum_binary_cut(weights)
            assert Fraction(p*q, c) == unweighted_constant(p, q)
            bx, by = witness
            assert weighted_variation(*median_step(bx, by), weights) == p*q
            assert weighted_variation(bx, by, weights) == c
            checks['witness'] += 1
            for bits in product((0, 1), repeat=p + q):
                x, y = bits[:p], bits[p:]
                after = median_step(x, y)
                assert weighted_variation(*after, weights) * c <= p*q * cut_cost(x, y, weights)
                checks['unweighted_binary'] += 1
    rng = Random(17031)
    # Positive integer edge weights test the independently weighted cut formula.
    for p in range(1, 6):
        for q in range(1, 6):
            for _ in range(7):
                weights = [[rng.randint(1, 19) for _ in range(q)] for _ in range(p)]
                W = sum(map(sum, weights))
                best, witness = optimum_binary_cut(weights)
                x0, y0 = witness
                assert weighted_variation(x0, y0, weights) == best
                assert weighted_variation(*median_step(x0, y0), weights) == W
                checks['witness'] += 1
                for bits in product((0, 1), repeat=p + q):
                    x, y = bits[:p], bits[p:]
                    c = cut_cost(x, y, weights)
                    v = weighted_variation(*median_step(x, y), weights)
                    assert best * v <= W * c
                    checks['weighted_binary'] += 1
                for _ in range(70):
                    x = [rng.randint(-30, 30) for _ in range(p)]
                    y = [rng.randint(-30, 30) for _ in range(q)]
                    v = weighted_variation(x, y, weights)
                    a, b = median_step(x, y)
                    assert best * weighted_variation(a, b, weights) <= W * v
                    checks['real_signal'] += 1
                    c, d = median_step(a, b)
                    e, f = median_step(c, d)
                    assert (e, f) == (a, b)
                    assert weighted_variation(c, d, weights) == weighted_variation(a, b, weights)
                    checks['dynamics'] += 1
    print('PASS', checks)
    return checks


if __name__ == '__main__':
    run()
