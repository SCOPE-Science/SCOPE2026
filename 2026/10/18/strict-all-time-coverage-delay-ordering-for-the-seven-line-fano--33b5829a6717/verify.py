"""Exact independent checks for seven-coupon triple-draw completion tails."""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations

POINTS = range(7)
ALL = (1 << 7) - 1
FANO = tuple(sum(1 << ((i + j) % 7) for j in (0, 1, 3)) for i in POINTS)
FULL = tuple(sum(1 << j for j in triple) for triple in combinations(POINTS, 3))
assert len(set(FANO)) == 7 and len(set(FULL)) == 35
assert all(x.bit_count() == 3 for x in FANO + FULL)
assert Counter((i, j) for line in FANO for i in POINTS for j in POINTS
               if i < j and (line >> i) & 1 and (line >> j) & 1) == \
       Counter({pair: 1 for pair in combinations(POINTS, 2)})


def signed_avoidance(blocks):
    coeff = Counter()
    for absent in range(128):
        disjoint = sum(not (block & absent) for block in blocks)
        coeff[Fraction(disjoint, len(blocks))] += -1 if absent.bit_count() % 2 else 1
    return {str(k): v for k, v in sorted(coeff.items()) if v}


def exact_survival_by_ie(blocks, t):
    if t == 0:
        return Fraction(1)
    covered = Fraction(0)
    for absent in range(128):
        disjoint = sum(not (block & absent) for block in blocks)
        covered += (-1 if absent.bit_count() % 2 else 1) * Fraction(disjoint, len(blocks)) ** t
    return 1 - covered


def exact_survival_by_dp(blocks, t):
    dist = {0: Fraction(1)}
    for _ in range(t):
        nxt = defaultdict(Fraction)
        for have, weight in dist.items():
            for block in blocks:
                nxt[have | block] += weight / len(blocks)
        dist = nxt
    assert sum(dist.values()) == 1
    return 1 - dist.get(ALL, 0)


def gap(t):
    if t == 0:
        return Fraction(0)
    return Fraction(21 * 5 ** t - 35 * 4 ** t + 35, 35 ** t)


def main():
    assert signed_avoidance(FANO) == {'0': 6, '1': 1, '1/7': -21, '2/7': 21, '4/7': -7}
    assert signed_avoidance(FULL) == {'0': -15, '1': 1, '1/35': 35,
                                      '2/7': 21, '4/35': -35, '4/7': -7}
    for t in range(0, 13):
        sf_ie, su_ie = exact_survival_by_ie(FANO, t), exact_survival_by_ie(FULL, t)
        sf_dp, su_dp = exact_survival_by_dp(FANO, t), exact_survival_by_dp(FULL, t)
        assert (sf_ie, su_ie) == (sf_dp, su_dp)
        assert sf_ie - su_ie == gap(t)
        assert sf_ie >= su_ie
        assert (sf_ie == su_ie) == (t < 3)
    assert gap(3) == Fraction(12, 1225)
    e_fano = 1 + 7 * Fraction(4, 3) - 21 * Fraction(2, 5) + 21 * Fraction(1, 6)
    e_full = 1 + 7 * Fraction(4, 3) - 21 * Fraction(2, 5) + 35 * Fraction(4, 31) - 35 * Fraction(1, 34)
    assert e_fano == Fraction(163, 30)
    assert e_full == Fraction(85691, 15810)
    assert e_fano - e_full == Fraction(7, 527)
    print('PASS: 128 absence subsets and Fano incidence')
    print('PASS: exact subset inclusion-exclusion equals 128-state DP for t=0,...,12')
    print('PASS: all twelve exact gap values, strict from t=3, and mean difference 7/527')
    print('PROOF-DEPENDENT: infinite-horizon gap positivity derives from monotonic ratio, not finite tests')


if __name__ == '__main__':
    main()
