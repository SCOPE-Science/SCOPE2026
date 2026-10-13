"""Independent exact checks for steered complete-bipartite cover laws.

Run: python verify_steered_biclique.py
No external packages, credentials or network calls are required.
"""
from fractions import Fraction
from functools import lru_cache
from math import gamma, exp, log, sqrt

checks = 0

for m in range(2, 7):
    for eps in (Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(3, 4), Fraction(1)):
        @lru_cache(None)
        def p(k):
            return eps + (1 - eps) * Fraction(k, m)

        # Distribution of the one-side coupon completion time after j arrivals.
        mass = [Fraction(0)] * (m + 1)
        mass[m] = Fraction(1)
        F = [mass[0]]
        for t in range(1, 4 * m * m + 2):
            nxt = [Fraction(0)] * (m + 1)
            nxt[0] = mass[0]
            for k in range(1, m + 1):
                nxt[k] += mass[k] * (1 - p(k))
                nxt[k - 1] += mass[k] * p(k)
            mass = nxt
            F.append(mass[0])
        assert F[0] == 0 and F[1] == 0 and F[m] > 0
        checks += 1

        # Direct finite-horizon dynamic program, explicitly optimising the
        # controller's two choices. The exact greedy law must attain the max.
        @lru_cache(None)
        def optimal(u, v, at_a, t):
            if u == 0 and v == 0:
                return Fraction(1)
            if t == 0:
                return Fraction(0)
            k = v if at_a else u
            if k == 0:
                return optimal(u, v, not at_a, t - 1)
            next_state = (u, v - 1, False) if at_a else (u - 1, v, True)
            stayed = (u, v, not at_a)
            val_success = optimal(*next_state, t - 1)
            val_failure = optimal(*stayed, t - 1)
            base = (1 - eps) * Fraction(k, m)
            value_avoid = base * val_success + (1 - base) * val_failure
            value_greedy = (base + eps) * val_success + (1 - base - eps) * val_failure
            assert value_greedy >= value_avoid
            return value_greedy

        for j in range(1, 2 * m + 6):
            # Odd horizons 2j-1 and even horizons 2j.
            if 2*j < len(F):
                assert optimal(m - 1, m, True, 2*j - 1) == F[j]*F[j]
                assert optimal(m - 1, m, True, 2*j) == F[j]*F[j+1]
                checks += 2

        # The PGF is a product of independent Geom(p_k) factors.
        @lru_cache(None)
        def coeff(j, k):
            # P(sum_{i=1}^k Geom(p_i) = j)
            if k == 0:
                return Fraction(int(j == 0))
            if j < k:
                return Fraction(0)
            return sum(coeff(j - r, k - 1) * p(k) * (1-p(k))**(r-1)
                       for r in range(1, j-k+2))
        for j in range(m, min(3*m+1, 23)):
            assert sum(coeff(i,m) for i in range(m,j+1)) == F[j]
            checks += 1

# Verify the gamma crossover transform numerically at fixed c and s.
for c in (0.0, 0.5, 1.0, 2.5):
    for s in (0.3, 1.2):
        values = []
        for m in (1000, 4000, 16000):
            eps = c / m
            a = m*eps/(1-eps)
            delta = m * (exp(s/m) - 1)/(1-eps)
            log_laplace = s*log(m) + sum(log((k+a)/(k+a+delta)) for k in range(1,m+1))
            values.append(exp(log_laplace))
        target = gamma(c+s+1)/gamma(c+1)
        assert abs(values[-1] - target) < 0.009*max(1,target), (c,s,values,target)
        assert abs(values[-1] - target) < abs(values[0] - target)
        checks += 2

print(f'PASS {checks} exact finite checks and asymptotic-transform checks')
