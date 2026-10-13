"""Exact-rational checks of an extreme-order-statistic rank-concordance identity.

Run with Python 3 (standard library only): python verify.py
Finite checks complement, but do not replace, the analytic proof.
"""
from fractions import Fraction as Q
from itertools import product
from random import Random


def exact_tau(rates):
    """Finite subset-sum formula for positive integer or rational rates."""
    rates = tuple(map(Q, rates))
    n = len(rates)
    if n < 2 or min(rates) <= 0:
        raise ValueError('At least two strictly positive rates are required')
    total = sum(rates)
    terms = []
    for mask in range(1, (1 << n) - 1):
        subset_rate = sum(rate for k, rate in enumerate(rates) if mask & (1 << k))
        parity = 1 if mask.bit_count() % 2 else -1
        coefficient = Q(parity) * (total - subset_rate) / total
        terms.append((subset_rate, coefficient))
    ans = Q(0)
    for s, a in terms:
        for t, b in terms:
            ans += (a * b * s * t / (s + t)
                    * (Q(1) / (total + s) + Q(1) / (total + t)))
    return ans


def two_rate_tau(a, b):
    a, b = Q(a), Q(b)
    return 2 * a * b * (a*a + 4*a*b + b*b) / ((a+b)**2 * (a+2*b) * (2*a+b))


def direct_two_component_tau(a, b):
    """Independent derivation from the two competing-race winner cases."""
    a, b = Q(a), Q(b)
    z = a+b
    mixture = ((b, a/z), (a, b/z))
    return sum((w*v*(s*t/(s+t))*(Q(1)/(z+s)+Q(1)/(z+t))
                for s,w in mixture for t,v in mixture), Q(0))


def main():
    two_trials = 0
    for a,b in product(range(1, 13), repeat=2):
        actual = exact_tau([a,b])
        assert actual == two_rate_tau(a,b)
        assert actual == direct_two_component_tau(a,b)
        contrast = Q((a-b)**2, (a+b)**2)
        assert actual == (1-contrast)*(3-contrast)/(9-contrast)
        assert actual <= Q(1,3)
        assert actual == exact_tau([b,a])
        assert actual == exact_tau([7*a,7*b])
        two_trials += 1

    symmetric_trials = 0
    for n in range(2,7):
        assert exact_tau([1]*n) == Q(1, 2*n-1)
        symmetric_trials += 1

    multirate_trials = 0
    for n in (3,4,5):
        for j in range(1, 18):
            rates = [1+((j+k*k+3*k) % 9) for k in range(n)]
            exact = exact_tau(rates)
            assert Q(0) < exact <= Q(1,2*n-1)
            assert exact_tau(rates[::-1]) == exact
            assert exact_tau([3*x for x in rates]) == exact
            multirate_trials += 1

    references = {(1,2,3):Q(1549,10395),
                  (1,2,4,8):Q(637623361,10447471125),
                  (1,1,1,5):Q(9103,120120)}
    for rates, expected in references.items():
        assert exact_tau(rates) == expected

    # Separate stochastic diagnostic, fixed seed; not used as mathematical proof.
    rng = Random(744223)
    simulation_cases = 0
    for rates in ((1,2,3), (1,2,4,8), (1,1,1,5)):
        concordance = 0
        count = 150000
        for _ in range(count):
            first = [rng.expovariate(rate) for rate in rates]
            second = [rng.expovariate(rate) for rate in rates]
            concordance += 1 if ((min(first)-min(second))
                                 * (max(first)-max(second)) > 0) else -1
        empirical = concordance / count
        assert abs(empirical - float(exact_tau(rates))) < 0.014
        simulation_cases += 1

    print('VERIFY_OK two_rate=%d symmetric=%d multirate=%d '
          'known_values=%d mc=%d' %
          (two_trials, symmetric_trials, multirate_trials,
           len(references), simulation_cases))


if __name__ == '__main__':
    main()
