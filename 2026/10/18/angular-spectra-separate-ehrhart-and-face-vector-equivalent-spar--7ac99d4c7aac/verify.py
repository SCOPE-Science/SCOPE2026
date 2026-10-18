"""Exact checks for angular spectra of sparse-paving matroid base polytopes.

Uses only the Python standard library. Finite tests supplement the proofs.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations
from math import comb, factorial

STAR = tuple(map(frozenset, ((1, 2, 3), (1, 4, 5), (1, 6, 7))))
TRIANGLE = tuple(map(frozenset, ((1, 2, 3), (1, 4, 5), (2, 4, 6))))


def data(n, deleted):
    rank = 3
    N, d = comb(n, rank), rank * (n - rank)
    ground = range(1, n + 1)
    all_sets = [frozenset(s) for s in combinations(ground, rank)]
    deleted = set(deleted)
    assert all(len(h & g) <= rank - 2 for h, g in combinations(deleted, 2))
    remaining = [s for s in all_sets if s not in deleted]
    t = {s: sum(len(s & h) == rank - 1 for h in deleted) for s in remaining}
    q = sum(len(h & g) == rank - 2 for h, g in combinations(deleted, 2))
    triple = sum(comb(z, 3) for z in t.values())
    histogram = Counter(t.values())
    assert sum(histogram.values()) == N - len(deleted)
    assert sum(t.values()) == len(deleted) * d
    assert sum(comb(z, 2) for z in t.values()) == 4 * q
    angle = {s: Fraction(d + t[s], N * d) for s in remaining}
    assert sum(angle.values()) == 1
    moment = lambda j: sum(p**j for p in angle.values())
    c2 = Fraction(N + len(deleted), N * N)
    c2 += Fraction(len(deleted), N * N * d)
    c2 += Fraction(8 * q, N * N * d * d)
    assert moment(2) == c2
    return N, d, remaining, t, q, triple, histogram, angle, moment


def check_basis_exchange(remaining):
    bases = set(remaining)
    for left in remaining:
        for right in remaining:
            for out in left - right:
                assert any((left - {out}) | {incoming} in bases
                           for incoming in right - left)


def tutte_counts(n, remaining):
    rank = 3
    counts = Counter()
    for size in range(n + 1):
        for selected in combinations(range(1, n + 1), size):
            subset = frozenset(selected)
            subset_rank = max(len(subset & B) for B in remaining)
            counts[(rank - subset_rank, size - subset_rank)] += 1
    return counts


def verify_full_rankings(n, remaining, t, N, d):
    # Powers of two make every competing subset-sum distinct.
    counts = Counter()
    for ordering in permutations(range(1, n + 1)):
        weights = {vertex: 1 << (n - place - 1)
                   for place, vertex in enumerate(ordering)}
        optimal = max(remaining, key=lambda B: sum(weights[i] for i in B))
        counts[optimal] += 1
    for B in remaining:
        expected = Fraction(factorial(n) * (d + t[B]), N * d)
        assert counts[B] == expected
    assert sum(counts.values()) == factorial(n)


def main():
    for n in range(7, 12):
        N, d, base_s, t_s, q_s, z_s, a_s, angle_s, moment_s = data(n, STAR)
        _, _, base_t, t_t, q_t, z_t, a_t, angle_t, moment_t = data(n, TRIANGLE)
        assert q_s == q_t == 3
        assert z_s == 0 and z_t == 1
        assert [a_s[j] for j in range(4)] == [N - 3*d + 9, 3*d - 24, 12, 0]
        assert [a_t[j] for j in range(4)] == [N - 3*d + 8, 3*d - 21, 9, 1]
        for j in (1, 2):
            assert moment_t(j) == moment_s(j)
        for j in (3, 4, 5):
            expected_delta = Fraction((d + 3)**j - 3*(d + 2)**j
                                      + 3*(d + 1)**j - d**j, (N*d)**j)
            assert moment_t(j) - moment_s(j) == expected_delta > 0
        assert moment_t(3) - moment_s(3) == Fraction(6, N**3 * d**3)
        print('Exact spectra and collision moments:', n, 'PASS')
        if n <= 8:
            for label, remaining, t in (('star', base_s, t_s),
                                        ('triangle', base_t, t_t)):
                check_basis_exchange(remaining)
                verify_full_rankings(n, remaining, t, N, d)
                print('  Complete permutation exposure:', label, factorial(n), 'PASS')
            assert tutte_counts(n, base_s) == tutte_counts(n, base_t)
            print('  Exact rank-based Tutte coefficients:', n, 'PASS')
    print('ALL CHECKS PASSED; finite verification does not certify arbitrary n.')


if __name__ == '__main__':
    main()
