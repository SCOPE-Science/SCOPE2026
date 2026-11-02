"""Reproducible finite checks of the forward-nonzero waiting identities.

All exact checks use fractions. Asymptotic/infinite claims require the
analytic arguments in RESULT.md and cannot be certified by finite code.
Run: python CHECK.py (Python standard library only).
"""
from fractions import Fraction
from itertools import product
from math import gamma, log

count = 0


def verify(value, label):
    global count
    assert value, label
    count += 1


def count_law(n, alpha):
    law = {1: Fraction(1)}
    for t in range(1, n):
        next_law = {}
        for k, prob in law.items():
            h = alpha * k / t
            next_law[k] = next_law.get(k, Fraction(0)) + prob * (1-h)
            next_law[k+1] = next_law.get(k+1, Fraction(0)) + prob*h
        law = next_law
    return law


def conditional_survival(n, k, m, alpha):
    v = Fraction(1)
    for t in range(n, n+m):
        v *= 1-alpha*k/t
    return v


def path_survival(n, m, alpha):
    result = Fraction(0)
    for binary_path in product((0, 1), repeat=n-1):
        k = 1
        weight = Fraction(1)
        for t, step in enumerate(binary_path, start=1):
            h = alpha*k/t
            weight *= h if step else (1-h)
            k += step
        result += weight * conditional_survival(n, k, m, alpha)
    return result


for alpha in (Fraction(1, 5), Fraction(1, 2), Fraction(3, 4)):
    for n in range(1, 10):
        law = count_law(n, alpha)
        verify(sum(law.values()) == 1, 'mass normalization')
        verify(all(x >= 0 for x in law.values()), 'nonnegative masses')
        one = Fraction(1)
        for j in range(1, n):
            one *= 1-alpha/j
        verify(law[1] == one, 'one-active-step probability')
        for m in range(0, 9):
            law_method = sum((p*conditional_survival(n, k, m, alpha)
                              for k, p in law.items()), Fraction(0))
            verify(law_method == path_survival(n, m, alpha),
                   'independent full-path enumeration')
            if m:
                prev = sum((p*conditional_survival(n, k, m-1, alpha)
                            for k, p in law.items()), Fraction(0))
                verify(law_method < prev, 'strict survival decrease')
        # The constants are a finite mixture of gamma-ratio leading terms.
        # Only their identities, not limiting assertions, are checked.
        a = float(alpha)
        c1 = float(law[1])*gamma(n)/gamma(n-a)
        verify(abs(c1-1/gamma(1-a)) < 2e-12, 'universal leading constant')
        if n > 1:
            c2_from_law = float(law[2])*gamma(n)/gamma(n-2*a)
            c2_from_sum = a/gamma(1-a)*sum(
                gamma(j-a)/gamma(j+1-2*a) for j in range(1, n))
            verify(abs(c2_from_law-c2_from_sum) < 2e-12,
                   'second-order constant')

# Large-sample checks of the CONDITIONAL law with a deterministic activity
# count of the predicted order; this is not a test of the limit theorem.
for alpha in (0.25, 0.5, 0.75):
    for n in (100_000, 1_000_000):
        for scale in (0.5, 1.0, 1.5):
            k = max(1, int(scale*n**alpha))
            m = int(n**(1-alpha))
            logtail = sum(log(1-alpha*k/t) for t in range(n, n+m))
            approximation = -alpha*k*m/n
            verify(abs(logtail-approximation) < 0.18,
                   'conditional exponential approximation')
print('PASS:', count, 'finite checks')
