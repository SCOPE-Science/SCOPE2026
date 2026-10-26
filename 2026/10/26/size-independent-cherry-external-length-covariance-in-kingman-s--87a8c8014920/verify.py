"""Exact finite checks for the cherry-count/external-length covariance theorem.

Uses only the Python standard library. Finite tests supplement, not replace,
the all-size induction given in RESULT.md.
"""
from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations

@lru_cache(None)
def moments(b, r):
    """(mean cherry count, mean external length, mixed first moment).

    Initially b singleton ancestral lineages and r already-internal lineages.
    Pairwise merger rate is one for every unordered pair.
    """
    k = b + r
    if k <= 1:
        return Q(0), Q(0), Q(0)
    denominator = k * (k - 1)
    choices = []
    if b >= 2:
        choices.append((Q(b * (b - 1), denominator), b - 2, r + 1, 1))
    if b and r:
        choices.append((Q(2 * b * r, denominator), b - 1, r, 0))
    if r >= 2:
        choices.append((Q(r * (r - 1), denominator), b, r - 1, 0))
    mu_c = mu_e = mu_ce = Q(0)
    for p, nb, nr, mark in choices:
        c, e, ce = moments(nb, nr)
        interval_external = Q(2 * b, denominator)
        mu_c += p * (mark + c)
        mu_e += p * (interval_external + e)
        mu_ce += p * (interval_external * (mark + c) + mark * e + ce)
    return mu_c, mu_e, mu_ce


def target_cov(b, k):
    return Q(-2 * b * (b - 1) * (3 * k - 2 * b - 2),
             9 * k * (k - 1) * (k - 2))


def check_dynamic(max_k=65):
    checks = 0
    for k in range(4, max_k + 1):
        for b in range(k + 1):
            c, e, ce = moments(b, k-b)
            assert c == Q(b * (b-1), 3 * (k-1)), (b, k, 'C')
            assert e == Q(2*b, k), (b, k, 'E')
            assert ce - c*e == target_cov(b, k), (b, k, 'Cov')
            checks += 1
        assert moments(k, 0)[2] - moments(k, 0)[0] * moments(k, 0)[1] == Q(-2,9)
    assert moments(3, 0)[2] - moments(3, 0)[0] * moments(3, 0)[1] == 0
    assert moments(2, 0)[2] - moments(2, 0)[0] * moments(2, 0)[1] == 0
    return checks


def exhaustive_histories(n):
    """Enumerate actual labeled merger histories, independent of state DP.

    Each complete history is equiprobable (the number of possible merges at
    stage k depends only on k). Conditional on a history, mean external
    branch length is the sum of singleton counts divided by merger rates.
    """
    total_histories = 0
    sum_c = sum_e = sum_ce = Q(0)

    def descend(lineages, cherries, conditional_external_mean):
        nonlocal total_histories, sum_c, sum_e, sum_ce
        k = len(lineages)
        if k == 1:
            total_histories += 1
            sum_c += cherries
            sum_e += conditional_external_mean
            sum_ce += cherries * conditional_external_mean
            return
        b = sum(len(x) == 1 for x in lineages)
        weight = Q(b, k*(k-1)//2)
        for a, z in combinations(range(k), 2):
            ca, cb = lineages[a], lineages[z]
            new_lineages = tuple(lineages[j] for j in range(k) if j not in (a, z)) + (ca | cb,)
            descend(new_lineages, cherries + int(len(ca)==1 and len(cb)==1),
                    conditional_external_mean + weight)

    descend(tuple(frozenset((i,)) for i in range(n)), 0, Q(0))
    c = sum_c / total_histories
    e = sum_e / total_histories
    cov = sum_ce / total_histories - c*e
    return total_histories, c, e, cov

if __name__ == '__main__':
    state_checks = check_dynamic()
    print('Exact state-moment comparisons:', state_checks)
    for n in range(2, 8):
        histories, c, e, cov = exhaustive_histories(n)
        assert c == (Q(1) if n <= 3 else Q(n, 3))
        assert e == Q(2)
        assert cov == (Q(0) if n <= 3 else Q(-2, 9))
        print('n=',n,'histories=',histories,'mean_cherries=',c,
              'mean_external=',e,'covariance=',cov)
    print('All exact finite checks passed; analytical induction needed for all sizes.')
