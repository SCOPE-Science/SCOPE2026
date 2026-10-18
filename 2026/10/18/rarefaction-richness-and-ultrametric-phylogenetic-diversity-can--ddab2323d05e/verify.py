"""Exact finite-sample checks for richness--rooted-PD covariance.

Two copies of taxon 0 and one copy of each of N-2 other taxa occur
at the leaves of a rooted ultrametric tree. The root-to-tip height is H;
the singleton clade has a basal edge H-e and pendant edges e.
Only Python standard-library modules are used.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import comb


def direct_covariance(n, m, height, pendant):
    assert n >= 5 and 1 <= m <= n and 0 < pendant < height
    individuals = [0, 0] + list(range(1, n - 1))
    draws = list(combinations(range(n), m))
    totals = [Q(0), Q(0), Q(0)]
    for indices in draws:
        kinds = {individuals[i] for i in indices}
        fine_richness = len(kinds)
        rare_count = len(kinds - {0})
        rooted_pd = (height if 0 in kinds else Q(0))
        if rare_count:
            rooted_pd += height - pendant + pendant * rare_count
        totals[0] += fine_richness
        totals[1] += rooted_pd
        totals[2] += fine_richness * rooted_pd
    count = len(draws)
    return totals[2] / count - (totals[0] / count) * (totals[1] / count)


def formula_for_interior(n, m, height, pendant):
    assert n >= 5 and 3 <= m <= n - 2
    return Q(m * (m - 1), n * (n - 1)) * Q(n - m, n) * (
        2 * pendant - height * Q(n - m - 1, n - 1)
    )


def main():
    number = 0
    for n in range(5, 13):
        height = Q(1)
        pendant = Q(1, 4 * (n - 1))
        for m in range(1, n + 1):
            actual = direct_covariance(n, m, height, pendant)
            if 3 <= m <= n - 2:
                expect = formula_for_interior(n, m, height, pendant)
                assert actual == expect, (n, m, actual, expect)
                assert actual < 0, (n, m, actual)
            elif m in (1, n):
                assert actual == 0, (n, m, actual)
            else:
                assert actual > 0, (n, m, actual)
            number += 1
    for n, m in ((5, 3), (7, 3), (9, 5), (11, 9)):
        threshold = Q(n - m - 1, 2 * (n - 1))
        actual = direct_covariance(n, m, Q(1), threshold)
        assert actual == 0, (n, m, actual)
        number += 1
    assert direct_covariance(5, 3, Q(1), Q(1, 16)) == -Q(3, 200)
    print('PASS', number, 'exact profile-depth or boundary checks')
    print('N=5, m=3, H=1, e=1/16: covariance = -3/200')
    print('N=5..12: negative at every 3<=m<=N-2, positive at m=2 and m=N-1')
    print('Four analytic phase boundaries have covariance exactly zero')

if __name__ == '__main__':
    main()
