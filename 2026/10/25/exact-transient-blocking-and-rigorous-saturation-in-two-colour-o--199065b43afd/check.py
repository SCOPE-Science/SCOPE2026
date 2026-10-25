"""Reproducible checks of a two-colour nearest-neighbour deposition law.

Pure standard-library Python 3.10+; run: python check.py
Analytic derivation and proof are in RESULT.md. Simulation is not a proof.
"""
import math
import random
from functools import lru_cache
from fractions import Fraction


def cavity_survival(t):
    return math.exp(-t / 2 - (1 - math.exp(-t)) / 2)


def cavity_weight(t):
    u = -math.expm1(-t)
    return u * math.exp(-u / 2)


def blocked_probability(t):
    return cavity_weight(t) ** 2 / 2


def exact_finite_ring_blocked(n):
    @lru_cache(maxsize=None)
    def expected_vacancies(state):
        candidates = []
        for i, v in enumerate(state):
            if v:
                continue
            left = state[(i - 1) % n]
            right = state[(i + 1) % n]
            for species in (1, 2):
                if left in (0, species) and right in (0, species):
                    changed = list(state)
                    changed[i] = species
                    candidates.append(tuple(changed))
        if not candidates:
            return Fraction(state.count(0), 1)
        return sum((expected_vacancies(c) for c in candidates), Fraction()) / len(candidates)

    return expected_vacancies((0,) * n) / n


def simulate(n=1500, repeats=450, times=(0.25, 0.5, 1, 2, 4, 8), seed=410041):
    random_source = random.Random(seed)
    observations = [[0.0, 0.0] for _ in times]
    for _ in range(repeats):
        state = bytearray(n)
        now = 0.0
        for j, cutoff in enumerate(times):
            # Independent homogeneous proposals at total rate n.
            while True:
                dtime = random_source.expovariate(n)
                if now + dtime > cutoff:
                    now = cutoff
                    break
                now += dtime
                site = random_source.randrange(n)
                species = 1 + random_source.randrange(2)
                if (state[site] == 0 and
                    state[(site - 1) % n] != 3 - species and
                    state[(site + 1) % n] != 3 - species):
                    state[site] = species
            blocked = 0
            for i, s in enumerate(state):
                if not s and state[(i - 1) % n] * state[(i + 1) % n] == 2:
                    blocked += 1
            fraction = blocked / n
            observations[j][0] += fraction
            observations[j][1] += fraction * fraction

    report = []
    for t, (summation, squares) in zip(times, observations):
        sample_mean = summation / repeats
        var = max(0.0, squares / repeats - sample_mean * sample_mean)
        se = math.sqrt(var / repeats)
        formula = blocked_probability(t)
        z = abs(sample_mean - formula) / se
        assert z < 5.0, (t, sample_mean, formula, se, z)
        report.append((t, sample_mean, se, formula, z))
    return report


def main():
    tests = 0
    # Functional identities implied by the analytic cavity equations.
    for t in (0.0, 0.01, 0.2, 1.0, 3.0, 10.0):
        g = cavity_survival(t)
        h = math.exp(t / 2) * g
        assert abs(h - math.exp(-(-math.expm1(-t)) / 2)) < 2e-14
        tests += 1
        assert 0 <= blocked_probability(t) <= 1/(2*math.e) + 1e-14
        tests += 1
    assert abs(blocked_probability(100) - 1/(2*math.e)) < 1e-14
    tests += 1
    assert cavity_weight(0) == 0
    tests += 1
    # Independent exact generator recursion on small periodic lattices.
    for n in range(4, 13):
        exact = exact_finite_ring_blocked(n)
        alternating = sum((Fraction((-1)**k, math.factorial(k))
                           for k in range(n+1)), Fraction())
        # The earlier finite-ring identity is used ONLY as a check, not claimed as proved.
        prior_expression = alternating/2 - Fraction(n-1, 2*math.factorial(n))
        assert exact == prior_expression, (n, exact, prior_expression)
        tests += 1
    print(f"Deterministic functional/exact-rational checks: {tests} passed")
    print(f"Infinite-volume blocked limit: {1/(2*math.e):.15f}")
    print("Finite-time independent Poisson simulations: t estimate standard-error formula abs-z")
    report = simulate()
    for r in report:
        print(f"{r[0]:4g} {r[1]:.9f} {r[2]:.9f} {r[3]:.9f} {r[4]:.3f}")
    print(f"Simulation comparisons: {len(report)} passed (5-standard-error tolerance)")


if __name__ == '__main__':
    main()
