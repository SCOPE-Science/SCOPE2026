#!/usr/bin/env python3
"""Self-contained finite checks for the directed p-Rips/Cho equality.
All matrices below record p-th powers of edge dissimilarities, so the
checks use integers without rounding. No external dependencies.
"""
from itertools import combinations, product
from random import Random


def rips_power(a):
    """Compute the Rips threshold to the p-th power by raw subsequences."""
    n = len(a) - 1
    best = 0
    for k in range(2, n + 2):
        for idx in combinations(range(n + 1), k):
            score = sum(a[idx[z]][idx[z+1]] for z in range(k-1))
            best = max(best, score)
    return best


def certificate(a):
    n = len(a) - 1
    D = [0] * (n + 1)
    for j in range(1, n + 1):
        D[j] = max(D[i] + a[i][j] for i in range(j))
    b = [D[j] - D[j - 1] for j in range(1, n + 1)]
    return D[-1], b


def is_cho_certificate(a, b):
    n = len(a) - 1
    return len(b) == n and all(v >= 0 for v in b) and all(
        a[i][j] <= sum(b[i:j])
        for i in range(n + 1) for j in range(i + 1, n + 1)
    )


def independent_integer_optimum(a, upper):
    """Exhaustively minimize a Cho certificate's sum of p-th powers."""
    n = len(a) - 1
    for total in range(upper + 1):
        # Enumerate every nonnegative integer composition of total.
        for cuts in combinations(range(total + n - 1), n - 1):
            ends = (-1,) + cuts + (total + n - 1,)
            b = [ends[j+1] - ends[j] - 1 for j in range(n)]
            if is_cho_certificate(a, b):
                return total
    raise AssertionError('no integer Cho certificate below Rips optimum')


def check_matrix(a, brute_cho=False):
    r = rips_power(a)
    c, b = certificate(a)
    assert r == c == sum(b), (a, r, c, b)
    assert is_cho_certificate(a, b), (a, b)
    if brute_cho:
        q = independent_integer_optimum(a, c)
        assert q == r, (a, q, r)


def make_matrix(n, vals):
    a = [[0] * (n+1) for _ in range(n+1)]
    pairs = list(combinations(range(n+1), 2))
    for (i, j), val in zip(pairs, vals):
        a[i][j] = val
    return a


def main():
    cases = 0
    for n in (1, 2, 3):
        pairs = n * (n+1) // 2
        for vals in product((0, 1, 2), repeat=pairs):
            check_matrix(make_matrix(n, vals), brute_cho=True)
            cases += 1
    rng = Random(261023)
    for n in (4, 5, 6):
        for j in range(250):
            vals = [rng.randrange(7) for _ in range(n*(n+1)//2)]
            check_matrix(make_matrix(n, vals), brute_cho=(n == 4 and j < 30))
            cases += 1
    # Journal example 3.6, with all missing reverse edges infinite.
    a = make_matrix(3, [1, 9, 16, 9, 9, 1])
    check_matrix(a, brute_cho=True)
    assert is_cho_certificate(a, [1, 9, 6])
    assert sum([1, 9, 6]) == rips_power(a) == 16
    print(f'PASS: {cases + 1} directed upper-triangular dissimilarity matrices,')
    print('including exhaustive integer Cho optima and journal counterexample.')
    print('Journal example: radius-4 Cho certificate (1, 3, sqrt(6)).')


if __name__ == '__main__':
    main()
