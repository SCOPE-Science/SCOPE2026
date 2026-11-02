"""Exact verification for asynchronous push-pull dissemination on double stars.

No external dependencies. Uses rational arithmetic for independent finite-state
Markov recurrences and algebraically derived exponential-max formulas.
"""
from fractions import Fraction as F
from math import comb, factorial, log, exp
from functools import lru_cache
import random


def harmonic(n):
    return sum((F(1, j) for j in range(1, n + 1)), F(0))


def analytic(a, b):
    """Return exact mean and probability the final informed leaf is on first side."""
    ra = F(a + 2, a + 1)
    rb = F(b + 2, b + 1)
    c = F(1, a + 1) + F(1, b + 1)
    delta = F(0)
    p = F(0)
    for i in range(1, a + 1):
        s = i * ra
        laplace = c / (c + s)
        for j in range(1, b + 1):
            laplace *= j * rb / (s + j * rb)
        term = (-1 if i % 2 == 0 else 1) * comb(a, i) * laplace
        p += term
        delta += term / s
    return 1 / c + harmonic(b) / rb + delta, p


def direct_ctmc(a, b):
    """Independent exact recursion on all reachable infection-count states."""
    ra = F(a + 2, a + 1)
    rb = F(b + 2, b + 1)
    c = F(1, a + 1) + F(1, b + 1)

    @lru_cache(None)
    def solve(i, j, infected_second):
        if infected_second and i == a and j == b:
            return F(0), F(0)
        edges = []
        if i < a:
            edges.append(((i + 1, j, infected_second), (a - i) * ra, bool(infected_second and i + 1 == a and j == b)))
        if not infected_second:
            edges.append(((i, 0, True), c, False))
        elif j < b:
            edges.append(((i, j + 1, True), (b - j) * rb, False))
        total = sum((r for _, r, _ in edges), F(0))
        mean = F(1, 1) / total
        mark = F(0)
        for dest, rate, won_a in edges:
            em, pm = solve(*dest)
            weight = rate / total
            mean += weight * em
            mark += weight * (int(won_a) if dest[0] == a and dest[1] == b and dest[2] else pm)
        return mean, mark
    return solve(0, 0, False)


def source_order_diagnostic():
    """Independent-clock CDF comparisons, not the analytic ordering proof."""
    def cdf(a, b, t):
        ra = (a + 2) / (a + 1)
        rb = (b + 2) / (b + 1)
        rate = 1 / (a + 1) + 1 / (b + 1)
        def integrand(s):
            return rate * exp(-rate * s) * (1 - exp(-rb * (t - s))) ** b
        n = 128
        step = t / n
        total = integrand(0) + integrand(t)
        for k in range(1, n):
            total += (4 if k % 2 else 2) * integrand(k * step)
        return (1 - exp(-ra * t)) ** a * total * step / 3

    for a in range(1, 12):
        for b in range(1, a + 1):
            for t in (0.25, 0.5, 1, 2, 4, 8, 15):
                assert cdf(a, b, t) + 1e-11 >= cdf(b, a, t), (a, b, t)


def asymptotic_stress_check():
    # This is a diagnostic, not a proof of convergence.
    rng = random.Random(20201030)
    for a in (10000, 1000000):
        for rho in (0.3, 1.0, 2.0):
            b = max(1, round(rho * log(a)))
            rate_a = (a + 2) / (a + 1)
            rate_b = (b + 2) / (b + 1)
            c = 1 / (a + 1) + 1 / (b + 1)
            vals = []
            marks = []
            for _ in range(2000):
                # Maximum of iid exponentials via inverse CDF, O(1) each.
                u1, u2 = rng.random(), rng.random()
                la = -log(1 - u1 ** (1 / a)) / rate_a
                lb = -log(1 - u2 ** (1 / b)) / rate_b
                bridge = rng.expovariate(c)
                vals.append(max(la, bridge + lb) / log(a))
                marks.append(int(la > bridge + lb))
            # Loose finite-size checks, mainly to guard normalization errors.
            empirical_mean = sum(vals) / len(vals)
            target = 1 + rho * exp(-1 / rho)
            assert abs(empirical_mean - target) < 0.55, (a, rho, empirical_mean, target)
            assert 0 <= sum(marks) <= len(marks)


def run():
    count = 0
    for a in range(1, 10):
        for b in range(1, 10):
            explicit = analytic(a, b)
            independent = direct_ctmc(a, b)
            assert explicit == independent, (a, b, explicit, independent)
            count += 2
            assert F(0) < explicit[1] < F(1)
            count += 1
            assert explicit[0] >= 1 / (F(1, a + 1) + F(1, b + 1))
            count += 1
    for a in range(1, 10):
        for b in range(1, a + 1):
            assert analytic(a, b)[0] <= analytic(b, a)[0]
            count += 1
    source_order_diagnostic()
    asymptotic_stress_check()
    print(f'PASS: {count} exact comparisons and bounds; CDF source-order and scaling diagnostics passed')

if __name__ == '__main__':
    run()
