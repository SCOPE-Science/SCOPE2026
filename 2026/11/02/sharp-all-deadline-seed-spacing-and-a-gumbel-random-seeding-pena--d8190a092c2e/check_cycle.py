"""Exact finite-state cross-checks for seeded SI flooding on a cycle.

No simulation is used to certify the identities: the two Laplace transforms
are computed independently using rational arithmetic.
"""
from fractions import Fraction
from math import comb, factorial
from collections import defaultdict
import mpmath as mp


def cyclic_gaps(n, seeds):
    seeds = sorted(seeds)
    k = len(seeds)
    return [(seeds[(i + 1) % k] - seeds[i] - 1) % n
            for i in range(k)]


def infection_laplace(n, s):
    """Laplace transforms at every nonempty infected mask by CTMC recursion."""
    full = (1 << n) - 1
    f = {full: Fraction(1)}
    for count in range(n - 1, 0, -1):
        for mask in range(1, full):
            if mask.bit_count() != count:
                continue
            transitions = []
            for v in range(n):
                if not (mask >> v) & 1:
                    rate = ((mask >> ((v - 1) % n)) & 1) + ((mask >> ((v + 1) % n)) & 1)
                    if rate:
                        transitions.append((mask | (1 << v), rate))
            total = sum(rate for _, rate in transitions)
            f[mask] = sum((rate * f[new] for new, rate in transitions), Fraction(0)) / (s + total)
    return f


def poly_mul(a, b):
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def gamma_max_laplace(gaps, s):
    """Exact LST from product of Erlang CDFs (not a state recursion)."""
    groups = {0: [Fraction(1)]}
    for ell in gaps:
        if ell == 0:
            continue
        p = [Fraction(2 ** j, factorial(j)) for j in range(ell)]
        updated = {r: values[:] for r, values in groups.items()}
        for r, values in groups.items():
            new = poly_mul(values, p)
            key = r + 1
            old = updated.get(key, [Fraction(0)] * len(new))
            if len(old) < len(new):
                old += [Fraction(0)] * (len(new) - len(old))
            for j, coeff in enumerate(new):
                old[j] -= coeff
            updated[key] = old
        groups = updated
    return s * sum((coeff * Fraction(factorial(j), (s + 2 * r) ** (j + 1))
                    for r, poly in groups.items() for j, coeff in enumerate(poly)), Fraction(0))


def erlang_cdf(ell, t):
    if ell == 0:
        return mp.mpf(1)
    return 1 - mp.exp(-2 * t) * sum(((2*t)**j / mp.factorial(j)
                                      for j in range(ell)), mp.mpf(0))


def check():
    assertions = 0
    for n in range(3, 10):
        for s in (1, 2, 3):
            f = infection_laplace(n, s)
            for mask in range(1, 1 << n):
                seeds = [i for i in range(n) if (mask >> i) & 1]
                gaps = cyclic_gaps(n, seeds)
                expected = gamma_max_laplace(gaps, s)
                assert f[mask] == expected, (n, s, mask, gaps, f[mask], expected)
                assertions += 1
    mp.mp.dps = 60
    for n in range(3, 12):
        for k in range(1, n):
            q, r = divmod(n - k, k)
            balanced = [q + 1] * r + [q] * (k - r)
            for t in map(mp.mpf, ('0.3', '1.0', '3.0')):
                best = mp.fprod(erlang_cdf(x, t) for x in balanced)
                for mask in range(1, 1 << n):
                    if mask.bit_count() != k:
                        continue
                    gaps = cyclic_gaps(n, [i for i in range(n) if mask >> i & 1])
                    observed = mp.fprod(erlang_cdf(x, t) for x in gaps)
                    assert observed <= best + mp.mpf('1e-50'), (n, k, gaps, t)
                    if sorted(gaps) != sorted(balanced):
                        assert observed < best - mp.mpf('1e-55'), (n, k, gaps, t)
                    assertions += 1
    # Independent exact inclusion-exclusion and brute uniform compositions
    from itertools import combinations
    for n in range(3, 13):
        for k in range(1, n):
            for m in range(1, n):
                lhs = Fraction(sum(max(cyclic_gaps(n, seeds)) < m for seeds in combinations(range(n), k)), comb(n, k))
                rhs = sum((Fraction((-1)**j * comb(k, j) * comb(n-1-j*m, k-1), comb(n-1, k-1))
                           for j in range(k+1) if n-1-j*m >= k-1), Fraction(0))
                assert lhs == rhs, (n,k,m,lhs,rhs)
                assertions += 1
    print('PASS exact CTMC/LST, all-site balanced stochastic comparison, and random-gap inclusion-exclusion:', assertions, 'assertions')

if __name__ == '__main__':
    check()
