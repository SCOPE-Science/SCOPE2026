"""Independent finite-state checks for collision-lineage probability identities.

Usage: python birthday_lineage_verification.py
Only standard Python plus scipy (optional for quadrature) are used.
"""
from fractions import Fraction
from functools import lru_cache
from math import factorial, gamma


def exact_marginal(m, s):
    """Exact E T_s and P(T_s >= k) by finite states before the first s-fold hit."""
    law = {(0,) * m: Fraction(1)}
    survival = {1: Fraction(1)}
    expectation = Fraction(0)
    for k in range(1, (s - 1) * m + 2):
        # law holds after k-1 draws, conditional on no s-fold hit.
        mass = sum(law.values(), Fraction(0))
        assert mass == survival[k]
        expectation += mass
        nxt = {}
        for state, prob in law.items():
            for i in range(m):
                counts = list(state)
                counts[i] += 1
                if counts[i] == s:
                    continue
                nxt_state = tuple(counts)
                nxt[nxt_state] = nxt.get(nxt_state, Fraction(0)) + prob / m
        law = nxt
        survival[k + 1] = sum(law.values(), Fraction(0))
    assert not law
    return expectation, survival


def exact_joint(m, r):
    """Probability of the same winner at r and r+1, by an independent marked-state DP."""
    state_probs = {((0,) * m, -1): Fraction(1)}
    event_pmf = {}
    for k in range(1, r * m + 2):
        nxt = {}
        hit_mass = Fraction(0)
        for (counts, first), weight in state_probs.items():
            for i in range(m):
                new_counts = list(counts)
                new_counts[i] += 1
                new_first = i if first == -1 and new_counts[i] == r else first
                if new_counts[i] == r + 1:
                    if i == new_first:
                        hit_mass += weight / m
                else:
                    new_state = (tuple(new_counts), new_first)
                    nxt[new_state] = nxt.get(new_state, Fraction(0)) + weight / m
        event_pmf[k] = hit_mass
        state_probs = nxt
    assert not state_probs
    return event_pmf


def run():
    identities = 0
    for m in range(1, 6):
        for r in range(2, 5):
            er, sr = exact_marginal(m, r)
            er1, sr1 = exact_marginal(m, r + 1)
            event = exact_joint(m, r)
            assert sum(event.values()) == (er1 - er) / m
            identities += 1
            for k, actual in event.items():
                predicted = (sr1.get(k, 0) - sr.get(k, 0)) / m
                assert actual == predicted, (m, r, k, actual, predicted)
                identities += 1
    # Independent Poisson/gamma quadrature for finite-size probabilities.
    from scipy.integrate import quad
    import math
    def Q(s, x):
        return math.exp(-x) * sum(x**j / factorial(j) for j in range(s))
    quadratures = 0
    for m in [2, 3, 4, 5]:
        for r in [2, 3, 4]:
            er, _ = exact_marginal(m, r)
            er1, _ = exact_marginal(m, r + 1)
            value = quad(lambda x: Q(r+1, x)**m - Q(r,x)**m, 0, 40,
                         epsabs=2e-12)[0]
            assert abs(value - float((er1-er)/m)) < 2e-10
            quadratures += 1
    # Sharp leading and two-scale asymptotics tested without simulation.
    numerical_asymptotics = 0
    for r in [2, 3, 4]:
        c = lambda s: factorial(s)**(1/s) * gamma(1+1/s)
        for m in [10_000, 1_000_000]:
            def Ez(s):
                scale=m**(1/s)
                return quad(lambda u: Q(s, u / scale)**m, 0, 70,
                            epsabs=3e-11)[0]/scale
            actual=Ez(r+1)-Ez(r)
            leading=c(r+1)*m**(-1/(r+1))
            second=leading-c(r)*m**(-1/r)
            assert abs(actual-second) < 7*m**(-2/(r+1)), (r,m,actual,second)
            numerical_asymptotics+=1
    print(f'PASS exact finite-state identities: {identities}')
    print(f'PASS independent gamma-integral comparisons: {quadratures}')
    print(f'PASS sharp two-scale asymptotic checks: {numerical_asymptotics}')

if __name__ == '__main__':
    run()
