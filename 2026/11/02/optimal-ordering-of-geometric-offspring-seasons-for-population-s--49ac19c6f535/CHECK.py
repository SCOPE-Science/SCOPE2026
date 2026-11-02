"""Exact arithmetic checks for seasonal geometric-offspring population calendars.

Only the Python standard library is required. This checks rational instances;
all-parameter assertions are established by the accompanying proof.
"""
from fractions import Fraction as Q
from itertools import permutations
from random import Random

CHECKS = 0

def check(test, description):
    global CHECKS
    CHECKS += 1
    if not test:
        raise AssertionError(description)


def pgf(par, s):
    m, a = par
    return 1 - m * (1 - s) / (1 + a * (1 - s))


def total_pgf(calendar, s):
    for pair in reversed(calendar):
        s = pgf(pair, s)
    return s


def stats(calendar):
    m = Q(1)
    for mi, _ in calendar:
        m *= mi
    c = Q(0)
    tail = Q(1)
    for mi, ai in reversed(calendar):
        c += ai * tail
        tail *= mi
    assert tail == m
    return m, c


def survival(calendar):
    m, c = stats(calendar)
    return m / (1 + c)


def lifetime_survival(calendar):
    m, c = stats(calendar)
    return max(Q(0), (m - 1) / c)


def score(par):
    m, a = par
    return (m - 1) / a


def main():
    r = Random(20261029)
    ms = [Q(1, 3), Q(1, 2), Q(3, 4), Q(1), Q(4, 3), Q(3, 2), Q(2), Q(3)]
    aa = [Q(1, 4), Q(1, 2), Q(1), Q(3, 2), Q(2), Q(3), Q(4)]
    possible = [(m, a) for m in ms for a in aa if m <= 1 + a]
    for n in range(2, 7):
        for trial in range(30):
            par = tuple(r.choice(possible) for _ in range(n))
            best = tuple(sorted(par, key=score, reverse=True))
            worst = tuple(sorted(par, key=score))
            m0, cmin = stats(best)
            m1, cmax = stats(worst)
            check(m0 == m1, 'calendar mean invariance')
            check(cmin <= cmax, 'ranked spread boundary')
            for s in (Q(0), Q(1, 5), Q(1, 2), Q(4, 5)):
                check(total_pgf(best, s) == 1 - m0 * (1-s)/(1+cmin*(1-s)), 'closed form PGF')
            for pc in set(permutations(par)):
                m, c = stats(pc)
                check(m == m0 and cmin <= c <= cmax, 'all permutations lie between score-sorted extremes')
                check(total_pgf(pc, Q(0)) == 1 - survival(pc), 'extinction from PGF')
                check(Q(0) < survival(pc) <= 1, 'valid survival')
                check(c >= m-1, 'valid zero mass')
                for t in (1,2,3):
                    # The exact stop-loss formula for t>=1.
                    check(m*(c/(1+c))**t >= 0, 'stop loss nonnegative')
            for t in (1, 2, 3, 5):
                lo = m0 * (cmin/(1+cmin))**t
                hi = m0 * (cmax/(1+cmax))**t
                check(lo <= hi, 'convex order of terminal counts')
            check(survival(best) >= survival(worst), 'highest survival first')
            check(lifetime_survival(best) >= lifetime_survival(worst), 'periodic survival order')

    for _ in range(200):
        first = r.choice(possible)
        second = r.choice(possible)
        left = (first, second)
        right = (second, first)
        dl = stats(left)[1] - stats(right)[1]
        expected = first[1]*second[1]*(score(second)-score(first))
        check(dl == expected, 'adjacent commutator identity')
        for s in (Q(0), Q(1, 3), Q(3, 4)):
            v1, v2 = total_pgf(left, s), total_pgf(right, s)
            check((v1 < v2) == (score(first) > score(second)), 'strict pairwise PGF comparison')
            check((v1 == v2) == (score(first) == score(second)), 'commutation iff equal scores')

    high = (Q(3), Q(3))
    low = (Q(1,2), Q(1))
    first = (high, low)
    last = (low, high)
    check(stats(first) == (Q(3,2), Q(5,2)), 'high-first calendar parameters')
    check(stats(last) == (Q(3,2), Q(6)), 'low-first calendar parameters')
    check(survival(first) == Q(3,7), 'high-first two-generation survival')
    check(survival(last) == Q(3,14), 'low-first two-generation survival')
    check(lifetime_survival(first) == Q(1,5), 'high-first repeated cycle survival')
    check(lifetime_survival(last) == Q(1,12), 'low-first repeated cycle survival')
    # Mean-only scheduling is not generally optimal; offspring dispersion matters.
    noisy_high = (Q(3), Q(7))
    steady_low = (Q(2), Q(2))
    mean_sorted = (noisy_high, steady_low)
    score_sorted = (steady_low, noisy_high)
    check(score(steady_low) > score(noisy_high), 'score reverses mean ranking')
    check(stats(mean_sorted) == (Q(6), Q(16)), 'mean-first compound PGF')
    check(stats(score_sorted) == (Q(6), Q(13)), 'score-first compound PGF')
    check(survival(mean_sorted) == Q(6,17), 'mean-first survival')
    check(survival(score_sorted) == Q(3,7), 'score-first survival')
    check(lifetime_survival(mean_sorted) == Q(5,16), 'mean-first periodic survival')
    check(lifetime_survival(score_sorted) == Q(5,13), 'score-first periodic survival')
    print('PASS:', CHECKS, 'exact-rational assertions')

if __name__ == '__main__':
    main()
