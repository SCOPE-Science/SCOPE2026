"""Exact finite checks for binomial quantile-share phase-boundary formulas.

All fractions use integer arithmetic. Finite checks supplement, and do not
replace, the all-parameter argument in RESULT.md.
"""
from fractions import Fraction
from math import comb
from itertools import product


def pmf(trials, probability, value):
    if not 0 <= value <= trials:
        return Fraction(0)
    return Fraction(comb(trials, value)) * probability**value * (1 - probability)**(trials - value)


def tail(n, t, p):
    return sum((pmf(n * t - 1, p, j) for j in range(t)), Fraction(0))


def step_decomposition(n, t, p):
    old = [pmf(n * t - 1, p, j) for j in range(t + 1)]
    added = [pmf(n, p, j) for j in range(n + 1)]
    gain = added[0] * old[t]
    loss = sum((added[j] * sum((old[t - h] if t - h >= 0 else Fraction(0)
                                 for h in range(1, j)), Fraction(0))
                for j in range(2, n + 1)), Fraction(0))
    return gain - loss


def h_polynomial(n, p):
    z = p / (1 - p)
    return sum((Fraction(comb(n, j)) * sum((z**(j-h) / (n-1)**h
               for h in range(1, j)), Fraction(0))
               for j in range(2, n+1)), Fraction(0))


def exact_binomial_checks():
    checks = 0
    for n in range(2, 15):
        critical = Fraction(1, n)
        probabilities = sorted(set([critical, critical / 4, critical / 2,
                                    critical * Fraction(3, 4),
                                    critical * Fraction(9, 10),
                                    critical * Fraction(11, 10),
                                    min(Fraction(19, 20), critical * Fraction(3, 2))]))
        for p in probabilities:
            previous = None
            for t in range(1, 35):
                f = tail(n, t, p)
                if t == 1:
                    assert f == (1-p)**(n-1)
                if previous is not None:
                    delta = f - previous
                    assert delta == step_decomposition(n, t-1, p)
                    if p <= critical:
                        lower = pmf(n*(t-1)-1, p, t-1) * (1-p)**n * (1-h_polynomial(n, p))
                        assert delta >= lower
                        assert delta >= 0
                        if p < critical or n >= 3:
                            assert delta > 0
                        else:
                            assert delta == 0
                    checks += 1
                previous = f
            if p <= critical:
                assert h_polynomial(n, p) <= 1
                if p < critical:
                    assert h_polynomial(n, p) < 1
                else:
                    assert h_polynomial(n, p) == 1
                checks += 1
    return checks


def uniform_rank_allocation_checks():
    checks = 0
    for n, max_m in [(2, 6), (3, 5), (4, 4)]:
        p = Fraction(1, n)
        q = (1-p)**(n-1)
        for m in range(max_m + 1):
            rank_choices = range(m + 1)
            # A utility of a bundle equals min(bundle cardinality, rank cap).
            for caps in product(rank_choices, repeat=n):
                threshold = []
                for cap in caps:
                    threshold.append(next((k for k in range(cap+1)
                                           if sum((pmf(m,p,j) for j in range(m+1)
                                                   if min(j,cap)<=k),Fraction(0)) >= q), cap))
                feasible = False
                for choices in product(range(n), repeat=m):
                    counts = [choices.count(i) for i in range(n)]
                    if all(min(counts[i],caps[i]) >= threshold[i] for i in range(n)):
                        feasible=True
                        break
                assert feasible, (n,m,caps,threshold)
                checks += 1
    return checks

if __name__ == '__main__':
    a = exact_binomial_checks()
    b = uniform_rank_allocation_checks()
    print(f'PASS: {a} exact binomial identities/monotonicity checks; {b} exhaustive uniform-rank profiles.')
