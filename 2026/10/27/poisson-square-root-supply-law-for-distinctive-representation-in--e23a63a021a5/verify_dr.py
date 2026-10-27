#!/usr/bin/env python3
"""Reproducible finite checks for exact-quota distinctive representation."""
import itertools
import math
import random


def quota(n, k):
    return (n + k - 1) // k


def jr_direct(supports, committee, n, k):
    """Check every cohesive voter group using its actual defining quantifiers."""
    q = quota(n, k)
    represented = 0
    for j in committee:
        represented |= supports[j]
    for voters in range(1 << n):
        if voters.bit_count() < q:
            continue
        if voters & represented:
            continue
        if any(voters & ~support == 0 for support in supports):
            return False
    return True


def jr_by_uncovered(supports, committee, n, k):
    q = quota(n, k)
    represented = 0
    for j in committee:
        represented |= supports[j]
    uncovered = ((1 << n) - 1) & ~represented
    return all((s & uncovered).bit_count() < q for s in supports)


def exhaustive(n, m=3, k=2):
    profiles = 0
    exact_quota_feasible = 0
    dr_feasible = 0
    differs = 0
    for data in range(1 << (n * m)):
        supports = []
        for j in range(m):
            supports.append(sum(1 << i for i in range(n) if data & (1 << (i * m + j))))
        eligible = [j for j in range(m) if supports[j].bit_count() == quota(n, k)]
        found = False
        for committee in itertools.combinations(range(m), k):
            direct = jr_direct(supports, committee, n, k)
            criterion = jr_by_uncovered(supports, committee, n, k)
            assert direct == criterion, (n, data, committee)
            if direct and all(supports[j].bit_count() == quota(n, k) for j in committee):
                found = True
        predicted_necessary = len(eligible) >= k
        assert not found or predicted_necessary
        profiles += 1
        exact_quota_feasible += int(predicted_necessary)
        dr_feasible += int(found)
        differs += int(predicted_necessary and not found)
    print('exhaustive', n, m, k, 'profiles', profiles,
          'quota_sufficient_in', exact_quota_feasible,
          'DR_exists_in', dr_feasible,
          'exceptions', differs)


def exact_binomial_tail(m, a, k):
    return sum(math.comb(m, j) * a**j * (1-a)**(m-j) for j in range(k, m+1))


def local_probability(n, k, p):
    q = quota(n, k)
    lg = math.lgamma
    return math.exp(lg(n+1)-lg(q+1)-lg(n-q+1)+q*math.log(p)+(n-q)*math.log1p(-p))


def random_test(n=200, k=2, m=50, trials=2400):
    rng = random.Random(19487)
    assert k == 2
    a = local_probability(n, k, .5)
    theoretical = exact_binomial_tail(m, a, k)
    successes = 0
    quota_events = 0
    bad_given_quota = 0
    for _ in range(trials):
        supports = [rng.getrandbits(n) for _ in range(m)]
        eligible = [j for j, s in enumerate(supports) if s.bit_count() == quota(n, k)]
        has_quota = len(eligible) >= k
        quota_events += has_quota
        if has_quota:
            good = jr_by_uncovered(supports, eligible[:k], n, k)
            successes += good
            bad_given_quota += not good
    empirical = quota_events / trials
    print('random sample', 'n', n, 'm', m, 'k', k, 'trials', trials,
          'quota_probability', round(empirical, 6), 'exact_binomial', round(theoretical, 6),
          'quota_without_JR', bad_given_quota, 'verified_DR', successes)
    assert abs(empirical-theoretical) < 0.065
    assert bad_given_quota == 0


def asymptotic_check():
    k = 3
    variance = (k-1)/k**2
    for theta in (0., 0.8):
        coefficient = math.exp(-theta**2/(2*variance))/math.sqrt(2*math.pi*variance)
        for n in (300, 1200, 4800):
            p = 1/k+theta/math.sqrt(n)
            actual = math.sqrt(n)*local_probability(n, k, p)
            assert math.isclose(actual, coefficient, rel_tol=.075)
            print('local_CLT', k, theta, n, round(actual, 7), round(coefficient, 7))


if __name__ == '__main__':
    for n in (3, 4, 5):
        exhaustive(n)
    asymptotic_check()
    random_test()
    print('ALL CHECKS PASSED')
