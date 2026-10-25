"""Exact finite checks of nearest-neighbor default-delegation loss."""
from fractions import Fraction
from itertools import product, combinations
from math import comb


def orbit(delegate, start):
    seen = set()
    current = start
    while current not in seen:
        seen.add(current)
        current = delegate[current]
    return frozenset(seen)


def all_profiles(n):
    return product(*(tuple(j for j in (i - 1, i, i + 1)
                           if 0 <= j < n) for i in range(n)))


def a_fixed_absent(n, t):
    return [Fraction(comb(t, s), comb(n, s)) if s <= t
            else Fraction(0) for s in range(n + 1)]


def loss_from_orbit_sizes(prof, a):
    return sum((a[len(orbit(prof, i))] for i in range(len(prof))),
               Fraction(0))


def lost_ballots_for_absent(prof, absent):
    return sum(orbit(prof, v) <= absent for v in range(len(prof)))


def brute_turnout_loss(prof, n, t):
    total = sum(lost_ballots_for_absent(prof, frozenset(c))
                for c in combinations(range(n), t))
    return Fraction(total, comb(n, t))


def verify():
    checked = 0
    checked_turnout = 0
    for n in range(2, 10):
        profs = list(all_profiles(n))
        assert len(profs) == 4 * 3 ** max(n-2, 0)
        for t in range(n + 1):
            a = a_fixed_absent(n, t)
            optimum = 2*a[2] + sum(a[3:], Fraction(0))
            min_seen = min(loss_from_orbit_sizes(p, a) for p in profs)
            assert min_seen == optimum, (n, t, min_seen, optimum)
            checked += len(profs)
            if n <= 6:
                for prof in profs:
                    direct = brute_turnout_loss(prof, n, t)
                    formula = loss_from_orbit_sizes(prof, a)
                    assert direct == formula, (n, t, prof, direct, formula)
                    checked_turnout += 1
        # Exact boundary profiles are optimal for every fixed turnout count.
        for pair in (0, n-2):
            p = tuple(i + 1 if i <= pair else i - 1 for i in range(n))
            for t in range(n + 1):
                a = a_fixed_absent(n, t)
                assert loss_from_orbit_sizes(p, a) == (2*a[2] + sum(a[3:], Fraction(0)))
        # Test strict characterization for independent abstentions q=1/2.
        q = Fraction(1, 2)
        aq = [q ** s for s in range(n+1)]
        vals = [(loss_from_orbit_sizes(p, aq), p) for p in profs]
        target = 2*q*q + sum((q ** s for s in range(3, n+1)), Fraction(0))
        winners = [p for val, p in vals if val == target]
        boundaries = set(tuple(i + 1 if i <= pair else i - 1 for i in range(n))
                         for pair in (0, n-2))
        assert min(x[0] for x in vals) == target
        assert set(winners) == boundaries, (n, winners, boundaries)
    print('PASS: fixed-count exchangeable laws, n=2..9,',checked,'profile/count cases')
    print('PASS: direct turnout subsets, n=2..6,',checked_turnout,'profile/count cases')
    print('PASS: strict i.i.d. q=1/2 optimal-profile classification, n=2..9')


if __name__ == '__main__':
    verify()
