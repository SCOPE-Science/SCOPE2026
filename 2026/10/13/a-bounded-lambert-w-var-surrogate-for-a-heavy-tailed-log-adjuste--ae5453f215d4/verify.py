"""Independent numerical checks of the LAPFr quantile-surrogate theorem.

Requires Python 3 standard library only. No input files or network.
"""
import math

LOG2 = math.log(2.0)


def cdf_generator(t, beta):
    return math.log1p(t) * math.exp(beta * (t - 1.0)) / LOG2


def surrogate_generator(t, beta):
    return t * math.exp(beta * (t - 1.0)) / LOG2


def inverse_in_unit_interval(function, q, beta):
    assert 0.0 < q < 1.0
    lo, hi = 0.0, 1.0
    for _ in range(130):
        mid = (lo + hi) / 2.0
        if function(mid, beta) < q:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def frechet_inverse(z, alpha=1.0, theta=1.0):
    return alpha * (-math.log(z)) ** (-1.0 / theta)


def test():
    endpoint_ceiling = math.log1p(LOG2) / LOG2
    assert 0.7597 < endpoint_ceiling < 0.7598
    for beta in (0.001, 0.1, 1.0, 5.0, 20.0):
        for q in (1e-8, 0.01, 0.5, 0.9, 0.99, 0.999):
            surrogate_g = inverse_in_unit_interval(surrogate_generator, q, beta)
            true_g = inverse_in_unit_interval(cdf_generator, q, beta)
            achieved = cdf_generator(surrogate_g, beta)
            assert 0.0 < surrogate_g < true_g < 1.0
            assert achieved < q
            assert abs(achieved - q * math.log1p(surrogate_g) / surrogate_g) < 2e-13
            assert abs(cdf_generator(true_g, beta) - q) < 2e-13
            assert frechet_inverse(surrogate_g) < frechet_inverse(true_g)
        # The published Lambert-W formula corresponds to this surrogate equation.
        gstar = inverse_in_unit_interval(surrogate_generator, 1.0 - 1e-14, beta)
        coverage_cap = math.log1p(gstar) / gstar
        assert LOG2 < coverage_cap < endpoint_ceiling
    beta = 1.0
    q = 0.99
    gs = inverse_in_unit_interval(surrogate_generator, q, beta)
    gt = inverse_in_unit_interval(cdf_generator, q, beta)
    apparent = frechet_inverse(gs)
    actual = frechet_inverse(gt)
    achieved = cdf_generator(gs, beta)
    assert abs(apparent - 5.0654970551013) < 1e-10
    assert abs(actual - 171.02874649653) < 1e-7
    assert abs(achieved - 0.72279985243172) < 1e-12
    print('CHECKS_PASS')
    print('universal_coverage_ceiling = %.15f' % endpoint_ceiling)
    print('nominal_coverage = %.5f' % q)
    print('surrogate_VaR = %.12f' % apparent)
    print('true_VaR = %.12f' % actual)
    print('actual_surrogate_coverage = %.12f' % achieved)


if __name__ == '__main__':
    test()
