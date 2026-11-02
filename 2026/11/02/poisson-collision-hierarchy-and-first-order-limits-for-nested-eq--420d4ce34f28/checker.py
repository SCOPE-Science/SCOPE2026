"""Exact finite tests of nested-equivalence rare-profile identities.

Only Python standard library is required. The asymptotic theorem is proved
mathematically in RESULT.md; bounded tests are not infinite proofs.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb, factorial, exp, log1p


def q_profile(s, r, j, ell):
    """Exact probability of j all-blue, ell all-red E-blocks in an F-block."""
    if j < 0 or ell < 0 or j + ell > s:
        return Fraction(0)
    p = Fraction(1, 2**r)
    return (comb(s, j) * comb(s - j, ell)
            * p ** (j + ell) * (1 - 2 * p) ** (s - j - ell))


def rare_vector_from_colors(bits, m, s, r, h):
    v = [0] * (h + 1)
    for outer in range(m):
        blue = red = 0
        for inner in range(s):
            begin = (outer * s + inner) * r
            block = bits[begin:begin + r]
            if not any(block):
                blue += 1
            elif all(block):
                red += 1
        if blue + red == h:
            v[blue] += 1
    return tuple(v)


def exact_derived_distribution(m, s, r, h):
    profiles = [(j, ell, q_profile(s, r, j, ell))
                for j in range(s + 1) for ell in range(s + 1 - j)]
    dist = Counter()
    for indices in product(range(len(profiles)), repeat=m):
        out = [0] * (h + 1)
        weight = Fraction(1)
        for idx in indices:
            j, ell, p = profiles[idx]
            weight *= p
            if j + ell == h:
                out[j] += 1
        dist[tuple(out)] += weight
    return dist


def test_exact():
    total_assignments = 0
    for m, s, r, h in [(2, 2, 2, 2), (2, 3, 2, 2), (2, 2, 3, 2), (2, 3, 3, 2)]:
        dist = Counter()
        for bits in product((0, 1), repeat=m * s * r):
            dist[rare_vector_from_colors(bits, m, s, r, h)] += 1
            total_assignments += 1
        observed = {k: Fraction(v, 2 ** (m * s * r)) for k, v in dist.items()}
        computed = exact_derived_distribution(m, s, r, h)
        assert sum(observed.values()) == 1
        assert sum(computed.values()) == 1
        assert all(computed[k] == v for k, v in observed.items())
        assert all(observed.get(k, 0) == v for k, v in computed.items())
    assert total_assignments == 256 + 4096 + 4096 + 262144
    return total_assignments


def test_mixed_factorial_moments():
    # E[ X_{2,0} X_{1,1} ] = (m)_2 q_{2,0} q_{1,1}.
    # E[ (X_{0,2})_2 ] = (m)_2 q_{0,2}^2.
    deviations = []
    for n in range(3, 10):
        s, r, m = 2 ** n, 2 * n, 2 ** (2 * n)
        a, b, c = [float(q_profile(s, r, j, 2 - j)) for j in range(3)]
        mixed = m * (m - 1) * b * c
        twice = m * (m - 1) * a * a
        assert 0 < mixed < 1
        assert 0 < twice < 1
        deviations.append(abs(mixed - Fraction(1, 2)))
        # Under lambda=1, limits are (1/1!1!)(1/2!0!)=1/2,
        # and (1/2!)^2=1/4 respectively.
        assert abs(twice - 0.25) < 0.13
    assert deviations[-1] < deviations[0]
    return len(deviations)


def test_alternating_counterexample():
    # Constant h=2 critical examples with lambda in {1,2}.
    # Exactly two all-blue E-classes are, with high probability,
    # the only obstruction; probability of >=2 uses binomial tail.
    values = {1: [], 2: []}
    for n in range(3, 11):
        s, r = 2 ** n, 2 * n
        p = 2.0 ** (-r)
        q = 1 - (1 - p) ** s - s * p * (1 - p) ** (s - 1)
        assert q > 0
        for lam in (1, 2):
            m = lam * 2 ** (2 * n)
            event = -__import__('math').expm1(m * log1p(-q))
            values[lam].append(event)
    for lam in (1, 2):
        limit = 1 - exp(-lam / 2)
        assert abs(values[lam][-1] - limit) < 0.002
    assert values[2][-1] - values[1][-1] > 0.2
    return len(values[1]) * 2


if __name__ == '__main__':
    a = test_exact()
    b = test_mixed_factorial_moments()
    c = test_alternating_counterexample()
    print(f'ALL_CHECKS_OK assignments={a} factorial_moment_cases={b} threshold_cases={c}')
