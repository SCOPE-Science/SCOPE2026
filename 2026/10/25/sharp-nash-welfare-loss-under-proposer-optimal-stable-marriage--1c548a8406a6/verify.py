"""Exact checks of sharp Nash-welfare loss in rank-based stable marriage.

Run: python verify.py
Only Python's standard library is required.
"""

from collections import Counter
from fractions import Fraction
from itertools import permutations, product
from math import prod


def inverse(matching):
    return tuple(matching.index(j) for j in range(len(matching)))


def is_stable(rank_m, rank_w, matching):
    n = len(matching)
    inv = inverse(matching)
    for i in range(n):
        for j in range(n):
            if rank_m[i][j] < rank_m[i][matching[i]] and rank_w[j][i] < rank_w[j][inv[j]]:
                return False
    return True


def gale_shapley(rank_m, rank_w):
    n = len(rank_m)
    order = [tuple(sorted(range(n), key=lambda j: rank_m[i][j])) for i in range(n)]
    next_proposal = [0] * n
    receiver_partner = [-1] * n
    free = list(range(n))
    while free:
        man = free.pop()
        assert next_proposal[man] < n
        j = order[man][next_proposal[man]]
        next_proposal[man] += 1
        incumbent = receiver_partner[j]
        if incumbent == -1:
            receiver_partner[j] = man
        elif rank_w[j][man] < rank_w[j][incumbent]:
            receiver_partner[j] = man
            free.append(incumbent)
        else:
            free.append(man)
    match = [-1] * n
    for j, i in enumerate(receiver_partner):
        match[i] = j
    return tuple(match)


def nash_product(rank_m, rank_w, matching):
    n = len(matching)
    inv = inverse(matching)
    return prod(n - rank_m[i][matching[i]] for i in range(n)) * prod(
        n - rank_w[j][inv[j]] for j in range(n)
    )


def ranked(preferences):
    return [tuple(pref.index(x) for x in range(len(pref))) for pref in preferences]


def cycle_witness(n, moved):
    assert 2 <= moved <= n
    men = []
    women = []
    for i in range(n):
        if i < moved:
            j = (i + 1) % moved
            men.append((i, j) + tuple(x for x in range(n) if x not in (i, j)))
        else:
            men.append((i,) + tuple(x for x in range(n) if x != i))
    for j in range(n):
        if j < moved:
            prev = (j - 1) % moved
            women.append((prev,) + tuple(x for x in range(n) if x not in (prev, j)) + (j,))
        else:
            women.append((j,) + tuple(x for x in range(n) if x != j))
    r_m, r_w = ranked(men), ranked(women)
    A = tuple(range(n))
    B = tuple((i + 1) % moved if i < moved else i for i in range(n))
    assert is_stable(r_m, r_w, A)
    assert is_stable(r_m, r_w, B)
    assert gale_shapley(r_m, r_w) == A
    assert nash_product(r_m, r_w, B) == (n - 1) ** moved * nash_product(r_m, r_w, A)
    return True


def exhaustive(n):
    perm = tuple(permutations(range(n)))
    ranks = [tuple(p.index(j) for j in range(n)) for p in perm]
    dist = Counter()
    max_ratio = Fraction(1)
    n_wrong = 0
    extremal = 0
    profiles = 0
    for inds in product(range(len(perm)), repeat=2*n):
        men, women = [ranks[inds[i]] for i in range(n)], [ranks[inds[n+j]] for j in range(n)]
        male = gale_shapley(men, women)
        assert is_stable(men, women, male)
        pmale = nash_product(men, women, male)
        stable = [p for p in perm if is_stable(men, women, p)]
        assert male in stable
        for m in stable:
            # Independent confirmation that Gale-Shapley is best for every man.
            assert all(men[i][male[i]] <= men[i][m[i]] for i in range(n))
            k = sum(m[i] != male[i] for i in range(n))
            assert nash_product(men, women, m) <= pmale * (n - 1) ** k
            if nash_product(men, women, m) == pmale * (n - 1) ** k and k:
                assert all(men[i][male[i]] == 0 and men[i][m[i]] == 1 for i in range(n) if m[i] != male[i])
                inmale, inm = inverse(male), inverse(m)
                assert all(women[j][inmale[j]] == n-1 and women[j][inm[j]] == 0
                           for j in range(n) if inm[j] != inmale[j])
        popt = max(nash_product(men, women, m) for m in stable)
        ratio = Fraction(popt, pmale)
        max_ratio = max(max_ratio, ratio)
        n_wrong += ratio > 1
        dist[str(ratio)] += 1
        extremal += ratio == (n-1) ** n
        profiles += 1
    assert max_ratio == (n - 1) ** n
    return {'n':n, 'total':profiles, 'strict_loss_profiles':n_wrong,
            'maximum_product_ratio':str(max_ratio), 'maximizer_profiles':extremal,
            'ratio_histogram':dict(sorted(dist.items()))}


def main():
    for n in (2,3):
        ans = exhaustive(n)
        if n == 2:
            assert ans['total'] == 16 and ans['strict_loss_profiles'] == 0
        if n == 3:
            assert ans['total'] == 46656 and ans['strict_loss_profiles'] == 5424
            assert ans['maximum_product_ratio'] == '8' and ans['maximizer_profiles'] == 12
        print(ans)
    for n in range(2,15):
        for moved in range(2,n+1):
            assert cycle_witness(n,moved)
    print('EXACT CHECKS PASSED: n=2,3 complete profiles; n=2..14 sharp cyclic constructions')


if __name__ == '__main__':
    main()
