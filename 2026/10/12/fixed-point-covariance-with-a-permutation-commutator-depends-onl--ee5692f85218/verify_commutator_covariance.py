"""Reproduce finite cases for the fixed-point/commutator covariance identity.

Run with Python 3: python verify_commutator_covariance.py
Uses exact integer averages, no external packages.
"""
from itertools import permutations
from fractions import Fraction
from math import factorial


def statistics(eta, pi):
    n = len(eta)
    fixed = sum(pi[i] == i for i in range(n))
    commuting_points = sum(pi[eta[i]] == eta[pi[i]] for i in range(n))
    return fixed, commuting_points


def case(eta, all_pi):
    n = len(eta)
    f = sum(eta[i] == i for i in range(n))
    sum_f = sum_c = sum_fc = 0
    for pi in all_pi:
        z, w = statistics(eta, pi)
        sum_f += z
        sum_c += w
        sum_fc += z * w
    total = len(all_pi)
    mean_f = Fraction(sum_f, total)
    mean_c = Fraction(sum_c, total)
    cov = Fraction(sum_fc, total) - mean_f * mean_c
    expected = Fraction(f * (n-f), (n-1) * (n-2))
    assert mean_f == 1, (n, eta, mean_f)
    assert mean_c == 1 + Fraction((f-1)**2, n-1), (n, eta, mean_c)
    assert cov == expected, (n, eta, cov, expected)
    return total


def main():
    checks = 0
    individual = 0
    for n in range(3, 7):
        all_pi = list(permutations(range(n)))
        for eta in all_pi:
            individual += case(eta, all_pi)
            checks += 1
    for n in (7, 8):
        all_pi = list(permutations(range(n)))
        identity = tuple(range(n))
        cycle = tuple((i+1) % n for i in range(n))
        two_cycle = (1,0) + tuple(range(2,n))
        for eta in (identity, cycle, two_cycle):
            individual += case(eta, all_pi)
            checks += 1
    # Sharp bound follows from f(n-f)<=floor(n^2/4), f=n-1 impossible.
    for n in range(3, 200):
        feasible = [f for f in range(n+1) if f != n-1]
        best = max(f*(n-f) for f in feasible)
        assert best == (n*n)//4
    # For n=3 and a full cycle, zero covariance does not imply independence.
    eta = (1,2,0)
    vals = [statistics(eta, pi) for pi in permutations(range(3))]
    assert (3,3) in vals and (1,0) in vals
    assert Fraction(sum(z*w for z,w in vals),6) == Fraction(3,2)
    print(f"PASS: {checks} exact permutation-pair distribution cases, {individual} individual pairs; "
          "mean, covariance, maximum, and nonindependence checks")


if __name__ == '__main__':
    main()
