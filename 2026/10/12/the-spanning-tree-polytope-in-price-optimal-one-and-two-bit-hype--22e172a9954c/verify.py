#!/usr/bin/env python3
"""Exact arithmetic checks for priced single- and double-bit hypercube mixing."""
from fractions import Fraction as F
from itertools import combinations
from random import Random


def subsets(d):
    return range(1, 1 << d)


def pairs(d):
    return list(combinations(range(d), 2))


def optimal_gap(d, t):
    n = 1 << d
    return F(8, n * (2 + (d - 1) * t)) if t < 2 else F(4, d * n)


def walsh_spectrum(d, b, a):
    """Exact nonzero eigenvalues of a translation-invariant bit-flip generator."""
    ans = []
    for mask in subsets(d):
        value = 2 * sum(b[i] for i in range(d) if mask >> i & 1)
        value += 2 * sum(a[i, j] for i, j in pairs(d)
                         if bool(mask >> i & 1) != bool(mask >> j & 1))
        ans.append(value)
    return ans


def conductance_cost(d, t, b, a):
    return F(1 << d, 2) * (sum(b) + t * sum(a.values()))


def from_fractional_forest(d, t, z):
    n = 1 << d
    q = F(4, n * (2 + (d - 1) * t)) if t < 2 else F(2, d * n)
    a = {ij: q * z.get(ij, 0) / 2 for ij in pairs(d)}
    b = [q - sum(a[i, j] if i < j else a[j, i]
                 for j in range(d) if j != i) for i in range(d)]
    return q, b, a


def forest_constraints(d, z, tree):
    assert all(z.get(ij, 0) >= 0 for ij in pairs(d))
    for mask in subsets(d):
        k = mask.bit_count()
        mass = sum(z.get((i, j), 0) for i, j in pairs(d)
                   if mask >> i & 1 and mask >> j & 1)
        assert mass <= k - 1
    if tree:
        assert sum(z.values()) == d - 1
    else:
        assert sum(z.values()) <= d - 1


def check_full_laplacian(d, b, a):
    """Check every Walsh eigen-equation against the full explicit Laplacian."""
    n = 1 << d
    spec = [0] + walsh_spectrum(d, b, a)
    count = 0
    moves = [(1 << i, b[i]) for i in range(d)]
    moves += [((1 << i) | (1 << j), a[i, j]) for i, j in pairs(d)]
    for mask in range(n):
        for x in range(n):
            chi = (-1) ** ((x & mask).bit_count())
            lhs = sum(w * (chi - (-1) ** (((x ^ v) & mask).bit_count()))
                      for v, w in moves)
            assert lhs == spec[mask] * chi
            count += 1
    return count


def check_random_irregular(d, t, rng):
    """Arbitrary individual edges: exact global Rayleigh upper certificates."""
    n = 1 << d
    w1 = w2 = 0
    for x in range(n):
        for i in range(d):
            v = x ^ (1 << i)
            if x < v:
                w1 += rng.randrange(0, 21)
        for i, j in pairs(d):
            v = x ^ (1 << i) ^ (1 << j)
            if x < v:
                w2 += rng.randrange(0, 21)
    budget = w1 + t * w2
    assert budget > 0
    w1, w2 = F(w1, budget), F(w2, budget)
    bound = min(F(4 * w1, n), F(4 * (w1 + 2 * w2), d * n))
    assert bound <= optimal_gap(d, t)


def main():
    rng = Random(20261010)
    verify_modes = 0
    optimizers = 0
    random_bounds = 0
    for d in range(3, 9):
        n = 1 << d
        for t in [F(1, 4), F(1, 2), F(1), F(3, 2), F(2), F(5, 2), F(4), F(11)]:
            expected = optimal_gap(d, t)
            if t < 2:
                z = {ij: F(2, d) for ij in pairs(d)}
                forest_constraints(d, z, True)
                q, b, a = from_fractional_forest(d, t, z)
                assert q * 2 == expected
                assert all(v == b[0] for v in b)
                assert all(v == b[0] for v in a.values())
                assert conductance_cost(d, t, b, a) == 1
                assert min(walsh_spectrum(d, b, a)) == expected
                optimizers += 1
                # A path on coordinate indices is a sparse optimal generator family.
                z = {(i, i + 1): F(1) for i in range(d - 1)}
                forest_constraints(d, z, True)
                q, b, a = from_fractional_forest(d, t, z)
                assert all(v >= 0 for v in b)
                assert sum(v > 0 for v in b) + sum(v > 0 for v in a.values()) == d + 1
                assert conductance_cost(d, t, b, a) == 1
                assert min(walsh_spectrum(d, b, a)) == expected
                optimizers += 1
            elif t == 2:
                for z in ({}, {(i, i + 1): F(1) for i in range(d - 1)},
                          {ij: F(2, d) for ij in pairs(d)}):
                    forest_constraints(d, z, False)
                    q, b, a = from_fractional_forest(d, t, z)
                    assert 2 * q == expected
                    assert all(v >= 0 for v in b)
                    assert conductance_cost(d, t, b, a) == 1
                    assert min(walsh_spectrum(d, b, a)) == expected
                    optimizers += 1
            else:
                b = [F(2, d * n)] * d
                a = {ij: F(0) for ij in pairs(d)}
                assert conductance_cost(d, t, b, a) == 1
                assert min(walsh_spectrum(d, b, a)) == expected
                optimizers += 1
            if d <= 5:
                verify_modes += check_full_laplacian(d, b, a)
            for _ in range(30):
                check_random_irregular(d, t, rng)
                random_bounds += 1
    assert optimizers == 84
    assert random_bounds == 1440
    print(f"VERIFY_OK {optimizers} exact optimal designs; {verify_modes} Walsh-Laplacian equations; {random_bounds} irregular Rayleigh upper bounds")


if __name__ == '__main__':
    main()
