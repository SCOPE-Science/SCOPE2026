"""Reproduce exact finite-cohort seed-bank allocation checks.

Only Python's standard library is required. The general theorem rests on
its analytic proof; these finite tests are auxiliary checks.
"""
from fractions import Fraction as Q
from itertools import product
from math import exp, log


def excess(n, k, a, b, q10, q01, q11):
    return q10 * a**k + q01 * b**(n-k) + q11 * a**k * b**(n-k)


def direct_failure(n, k, a, b, q00, q10, q01, q11):
    total = Q(0)
    joint = {(0, 0): q00, (1, 0): q10,
             (0, 1): q01, (1, 1): q11}
    for (g1, g2), weight in joint.items():
        probs = [g1 * (1-a)] * k + [g2 * (1-b)] * (n-k)
        for outcomes in product((0, 1), repeat=n):
            term = weight
            for outcome, prob in zip(outcomes, probs):
                term *= prob if outcome else (1-prob)
            if not any(outcomes):
                total += term
    return total


def run():
    profiles = convexities = windows = direct = boundaries = 0
    for a, b, q10, q01, q11 in product(
            (Q(1, 4), Q(1, 2), Q(3, 4)),
            (Q(1, 3), Q(2, 3), Q(4, 5)),
            (Q(1, 10), Q(1, 4)),
            (Q(1, 10), Q(1, 5)),
            (Q(0), Q(1, 8), Q(1, 3))):
        q00 = Q(1)-q10-q01-q11
        assert q00 >= 0
        A, B = -log(float(a)), -log(float(b))
        share = B / (A+B)
        rate = A*B / (A+B)
        bound_constant = (float(q10)*exp(A/2) + float(q01)*exp(B/2)
                          + float(q11)*exp(abs(A-B)/2))
        for n in range(1, 25):
            values = [excess(n, k, a, b, q10, q01, q11)
                      for k in range(n+1)]
            least = min(values)
            winners = [k for k, value in enumerate(values)
                       if value == least]
            profiles += 1
            assert len(winners) <= 2
            assert winners[-1]-winners[0] <= 1
            for k in range(1, n):
                assert values[k-1] - 2*values[k] + values[k+1] > 0
                convexities += 1
            for k in winners:
                assert k + 1e-10 >= (share*n
                    - log(bound_constant / float(q10))/A)
                assert k - 1e-10 <= (share*n
                    + log(bound_constant / float(q01))/B)
                windows += 1
            lo = float(min(q10, q01))*exp(-rate*n)
            hi = bound_constant*exp(-rate*n)
            assert float(least) + 1e-13 >= lo
            assert float(least) <= hi + 1e-13
            if n <= 5 and q11 == Q(1, 8):
                for k in range(n+1):
                    assert direct_failure(n,k,a,b,q00,q10,q01,q11) == q00 + values[k]
                    direct += 1
    # On the support boundary one good season occurs only jointly,
    # and the optimal number assigned to that season is bounded.
    for a, b, q01, q11 in product(
            (Q(1,4),Q(1,2)), (Q(1,3),Q(3,4)),
            (Q(1,10),Q(1,4)), (Q(0),Q(1,4))):
        nmax = 100
        g = [b**(-k) * (q01 + q11*a**k) for k in range(nmax+1)]
        imin = min(range(nmax+1), key=lambda k:g[k])
        for n in range(1, nmax+1):
            vals=[excess(n,k,a,b,Q(0),q01,q11) for k in range(n+1)]
            best=min(range(n+1),key=lambda k:vals[k])
            assert best <= imin
            boundaries += 1
    print('VERIFY_OK', 'exact_profiles=',profiles,
          'strict_convexity_cases=',convexities,
          'optimal_windows=',windows,
          'direct_outcome_expansions=',direct,
          'support_boundary_cases=',boundaries)

if __name__ == '__main__':
    run()
