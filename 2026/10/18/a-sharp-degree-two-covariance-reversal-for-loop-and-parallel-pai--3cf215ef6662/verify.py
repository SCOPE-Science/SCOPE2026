"""Direct exact enumeration for loop--parallel-pair dependence in a random configuration.

Run with Python 3; uses only the standard library. All assertions are exact
rational equalities unless explicitly described as numerical asymptotics.
"""
from fractions import Fraction
from itertools import combinations
from math import comb


def matchings(stubs):
    if not stubs:
        yield ()
        return
    first = stubs[0]
    for k in range(1, len(stubs)):
        other = stubs[k]
        for remainder in matchings(stubs[1:k] + stubs[k + 1:]):
            yield ((first, other),) + remainder


def exact_covariance(degrees):
    N = sum(degrees)
    if N < 6 or N % 2:
        raise ValueError('The general formula requires an even N of at least six')
    S = sum(comb(d, 2) for d in degrees)
    pairs = [(u, v) for u, v in combinations(degrees, 2)]
    B = 2 * sum(comb(u, 2) * comb(v, 2) for u, v in pairs)
    T = 4 * sum(comb(u, 2) * comb(v, 2) * (u + v - 3) for u, v in pairs)
    return Fraction(4 * S * B - (N - 1) * T, (N - 1) ** 2 * (N - 3) * (N - 5))


def enumerated_covariance(degrees):
    labels = [v for v, deg in enumerate(degrees) for _ in range(deg)]
    N = len(labels)
    total = sum_l = sum_p = sum_lp = 0
    for pairing in matchings(tuple(range(N))):
        total += 1
        loops, multiplicities = 0, {}
        for a, b in pairing:
            i, j = labels[a], labels[b]
            if i == j:
                loops += 1
            else:
                ij = tuple(sorted((i, j)))
                multiplicities[ij] = multiplicities.get(ij, 0) + 1
        parallel_pairs = sum(comb(v, 2) for v in multiplicities.values())
        sum_l += loops
        sum_p += parallel_pairs
        sum_lp += loops * parallel_pairs
    return Fraction(sum_lp, total) - Fraction(sum_l * sum_p, total * total)


def regular_covariance(n, d):
    N = n * d
    if N < 6 or N % 2:
        raise ValueError('Need at least six stubs, and even total degree')
    a = comb(d, 2)
    return Fraction(2 * n * (n - 1) * a * a * (N * (2 - d) + 2 * d - 3),
                    (N - 1) ** 2 * (N - 3) * (N - 5))


def run():
    cases = [(2, 2, 2), (2, 2, 2, 2), (2, 2, 2, 2, 2),
             (3, 3), (3, 3, 3, 3), (4, 4), (1, 2, 3),
             (1, 1, 2, 2), (2, 3, 3), (2, 2, 4),
             (1, 1, 1, 1, 2, 2), (1, 1, 4), (1, 2, 2, 3),
             (2, 2, 3, 3), (3, 3, 4), (1, 1, 1, 1, 1, 1)]
    checked = 0
    for ds in cases:
        if sum(ds) >= 6 and sum(ds) % 2 == 0:
            assert exact_covariance(ds) == enumerated_covariance(ds), ds
            checked += 1
    for n in range(2, 61):
        for d in range(2, 26):
            if n * d < 6 or n * d % 2:
                continue
            value = regular_covariance(n, d)
            assert value == exact_covariance((d,) * n), (n, d)
            assert (value > 0 if d == 2 else value < 0), (n, d)
            checked += 2
    assert Fraction(-4, 9) == (Fraction(0) - Fraction(2, 3) * Fraction(2, 3))
    checked += 1
    for n in range(3, 70):
        val = regular_covariance(n, 2)
        assert val == Fraction(2 * n * (n - 1), (2 * n - 1) ** 2 * (2 * n - 3) * (2 * n - 5))
        checked += 1
    for d in range(3, 15):
        coeff = Fraction(-(d - 1) ** 2 * (d - 2), 2 * d)
        approx = 400000 * regular_covariance(400000, d)
        assert abs(approx - coeff) < Fraction(1, 2000)
        checked += 1
    print('PASS', checked, 'exact or explicitly bounded asymptotic assertions')

if __name__ == '__main__':
    run()
