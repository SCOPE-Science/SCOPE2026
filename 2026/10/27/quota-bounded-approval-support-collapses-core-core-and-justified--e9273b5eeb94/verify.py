"""Exact finite regression tests for quota-capped approval elections.

The mathematical statement for arbitrary electorate sizes is proved separately;
these finite tests do not certify its unbounded quantifiers.
"""
from fractions import Fraction
from itertools import combinations, product


def support(profile, c):
    return frozenset(i for i, mask in enumerate(profile) if mask & (1 << c))


def utility(mask, W):
    return sum(bool(mask & (1 << c)) for c in W)


def jr(profile, m, k, W):
    q = Fraction(len(profile), k)
    covered = {i for i, mask in enumerate(profile) if utility(mask, W)}
    for c in range(m):
        if c not in W and len(support(profile, c)) >= q:
            if not (support(profile, c) & covered):
                return False
    return True


def core(profile, m, k, W):
    q = Fraction(len(profile), k)
    base = [utility(mask, W) for mask in profile]
    for r in range(1, k + 1):
        for T in combinations(range(m), r):
            gainers = sum(utility(mask, T) > base[i]
                          for i, mask in enumerate(profile))
            if gainers >= q * r:
                return False
    return True


def greedy(profile, m, k):
    q = Fraction(len(profile), k)
    if q.denominator != 1:
        return tuple(range(k))
    selected, occupied = [], set()
    for c in range(m):
        sc = support(profile, c)
        if len(sc) == q and not (occupied & sc):
            selected.append(c)
            occupied.update(sc)
    assert len(selected) <= k
    for c in range(m):
        if len(selected) == k:
            break
        if c not in selected:
            selected.append(c)
    return tuple(selected)


def exhaustive():
    committee_cases = 0
    profile_cases = 0
    for n, m in ((2, 3), (3, 3), (4, 3), (3, 4)):
        for k in range(1, m + 1):
            q = Fraction(n, k)
            for profile in product(range(1 << m), repeat=n):
                if any(len(support(profile, c)) > q for c in range(m)):
                    continue
                profile_cases += 1
                Wg = greedy(profile, m, k)
                assert jr(profile, m, k, Wg)
                assert core(profile, m, k, Wg)
                for W in combinations(range(m), k):
                    assert jr(profile, m, k, W) == core(profile, m, k, W)
                    committee_cases += 1
    return profile_cases, committee_cases


def exceptional(q):
    assert isinstance(q, int) and q >= 1
    n, m, k = 2 * q, 3, 2
    a, b, c = 0, 1, 2
    profile = [(1 << a)] * q + [1 << b] + [1 << c] * (q - 1)
    profile[0] |= 1 << c
    profile[q] |= 1 << c
    W = (a, b)
    assert sorted(len(support(profile, j)) for j in range(m)) == [1, q, q + 1]
    assert core(profile, m, k, W) and jr(profile, m, k, W)
    # Explicit feasible fractional blocking variables. Only the losing
    # candidate c receives positive z and x variables.
    y = [Fraction(0)] * n
    x = [[Fraction(0)] * m for _ in range(n)]
    z = [Fraction(0)] * m
    z[c] = Fraction(1)
    y[0] = y[q] = Fraction(1, 2)
    for i in range(q + 1, n):
        y[i] = Fraction(1)
    for i in support(profile, c):
        x[i][c] = Fraction(1)
    for i in range(n):
        for j in range(m):
            assert Fraction(0) <= x[i][j] <= 1
            if x[i][j]:
                assert profile[i] & (1 << j)
            assert x[i][j] <= z[j]
            if j in W:
                assert x[i][j] <= y[i]
        assert sum(x[i]) >= (utility(profile[i], W) + 1) * y[i]
    assert sum(y) == Fraction(n, k) * sum(z)
    assert sum(y) > 0
    return True


if __name__ == '__main__':
    profiles, committees = exhaustive()
    for q in range(1, 51):
        exceptional(q)
    print('PASS capped-profile complete regression:', profiles, 'profiles;', committees, 'committees')
    print('PASS exact fractional obstruction and core stability: quotas 1..50')
