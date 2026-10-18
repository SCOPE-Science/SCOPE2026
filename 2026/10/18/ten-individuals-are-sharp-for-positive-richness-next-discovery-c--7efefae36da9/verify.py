"""Exact finite-population richness / next-discovery covariance checks.

Requires Python >=3.9; standard library only. Run:
    python finite_discovery_covariance_verifier.py
No network access required.
"""
from fractions import Fraction
from math import comb
from itertools import combinations
from collections import Counter
import json


def partitions(n, low=1):
    if n == 0:
        yield ()
    else:
        for x in range(low, n + 1):
            for rem in partitions(n - x, x):
                yield (x,) + rem


def absent(N, total, m):
    return Fraction(comb(N - total, m), comb(N, m)) if N - total >= m else Fraction(0)


def formula(a, m):
    N = sum(a)
    assert 1 <= m < N
    q = [absent(N, x, m) for x in a]
    weight = sum(x * z for x, z in zip(a, q))
    both = sum(a[i] * absent(N, a[i] + a[j], m)
               for i in range(len(a)) for j in range(len(a)) if i != j)
    return (weight * (sum(q) - 1) - both) / (N - m)


def direct(a, m):
    N = sum(a)
    species = tuple(i for i, count in enumerate(a) for _ in range(count))
    S = set(species)
    K = U = KU = Fraction(0)
    den = comb(N, m)
    for I in combinations(range(N), m):
        seen = {species[i] for i in I}
        k = len(seen)
        # Unseen mass among the unsampled population: exact conditional
        # probability that the next uniformly chosen individual is novel.
        u = Fraction(sum(x for j, x in enumerate(a) if j not in seen), N - m)
        K += Fraction(k, den)
        U += u / den
        KU += k * u / den
    return KU - K * U


def family(t, s):
    N = t + s
    return Fraction(t * (t - 1) * s * (t * (s - 3) - 2 * (s - 1)),
                    N * N * (N - 1) ** 2 * (N - 2))


def main():
    tests = 0
    per_n = {}
    max_value = Fraction(0)
    max_case = None
    for N in range(2, 10):
        n_cases = 0
        for a in partitions(N):
            for m in range(1, N):
                c = formula(a, m)
                assert c == direct(a, m), (N, a, m, c, direct(a, m))
                assert c <= 0, (N, a, m, c)
                n_cases += 1
                if c > max_value:
                    max_value, max_case = c, (a, m)
        per_n[str(N)] = n_cases
        tests += n_cases
    a = (4, 1, 1, 1, 1, 1, 1)
    assert formula(a, 2) == direct(a, 2) == Fraction(1, 450)
    assert formula(a, 9) == direct(a, 9) == Fraction(-6, 25)
    assert [formula(a, m) for m in range(1, 10)] == [
        Fraction(0), Fraction(1, 450), Fraction(-26, 1575),
        Fraction(-409, 7350), Fraction(-46, 441), Fraction(-1327, 8820),
        Fraction(-14, 75), Fraction(-16, 75), Fraction(-6, 25)]
    positive_n10 = []
    for b in partitions(10):
        for m in range(1, 10):
            c = formula(b, m)
            assert c == direct(b, m)
            if c > 0:
                positive_n10.append({'abundances': list(b), 'sample_size': m,
                                     'covariance': f'{c.numerator}/{c.denominator}'})
    assert len(positive_n10) >= 1
    assert {'abundances': [1, 1, 1, 1, 1, 1, 4], 'sample_size': 2,
            'covariance': '1/450'} in positive_n10
    for t in range(2, 13):
        for s in range(2, 28):
            assert formula((t,) + (1,) * s, 2) == family(t, s)
    for s in range(6, 31):
        a = (4,) + (1,) * s
        N = sum(a)
        assert formula(a, 2) == family(4, s) > 0
        assert formula(a, N - 1) == -Fraction(4 * s, N * N)
    data = {
        'method': 'independent hypergeometric-absence formula and labeled-subset enumeration',
        'fully_enumerated_population_sizes': list(range(2, 11)),
        'nonpositive_verified_through_population_size': 9,
        'small_census_profile_depth_checks': tests,
        'small_census_checks_by_population_size': per_n,
        'first_witness': {'abundances': [4, 1, 1, 1, 1, 1, 1], 'N': 10,
                          'm': 2, 'covariance': '1/450',
                          'near_census_covariance': '-6/25'},
        'positive_ten_individual_cases': positive_n10,
        'algebraic_family_checks': 11 * 26,
        'unbounded_family_checks': 25,
        'all_checks': 'passed',
    }
    print(json.dumps(data, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
