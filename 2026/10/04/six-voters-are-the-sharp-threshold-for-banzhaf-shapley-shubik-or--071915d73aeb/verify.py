#!/usr/bin/env python3
from fractions import Fraction
from math import factorial

EXPECTED_MONOTONE = {1: 3, 2: 6, 3: 20, 4: 168, 5: 7581}
EXPECTED_SIMPLE = {1: 1, 2: 4, 3: 18, 4: 166, 5: 7579}

def monotone_functions(n):
    funcs = [0, 1]
    width = 1
    for _ in range(1, n + 1):
        old = funcs
        funcs = []
        for low in old:
            for high in old:
                if low & ~high == 0:
                    funcs.append(low | (high << width))
        width *= 2
    return funcs

def power_indices(n, truth):
    banzhaf = []
    shapley = []
    for i in range(n):
        bit = 1 << i
        swings = 0
        ss = Fraction(0, 1)
        for coalition in range(1 << n):
            if coalition & bit:
                continue
            before = (truth >> coalition) & 1
            after = (truth >> (coalition | bit)) & 1
            if before == 0 and after == 1:
                swings += 1
                k = coalition.bit_count()
                ss += Fraction(factorial(k) * factorial(n - k - 1), factorial(n))
        banzhaf.append(swings)
        shapley.append(ss)
    total_swings = sum(banzhaf)
    return [Fraction(x, total_swings) for x in banzhaf], shapley

def sign(x):
    return (x > 0) - (x < 0)

def same_weak_order(a, b):
    n = len(a)
    return all(sign(a[i] - a[j]) == sign(b[i] - b[j])
               for i in range(n) for j in range(i + 1, n))

def truth_from_minimal_winners(n, winners):
    truth = 0
    for coalition in range(1 << n):
        if any((coalition & w) == w for w in winners):
            truth |= 1 << coalition
    return truth

def mask(*players):
    out = 0
    for p in players:
        out |= 1 << (p - 1)
    return out

def main():
    checked = {}
    for n in range(1, 6):
        funcs = monotone_functions(n)
        assert len(funcs) == EXPECTED_MONOTONE[n]
        simple = []
        grand = (1 << n) - 1
        for truth in funcs:
            if truth & 1:
                continue
            if ((truth >> grand) & 1) != 1:
                continue
            simple.append(truth)
            bz, ss = power_indices(n, truth)
            assert same_weak_order(bz, ss), (n, truth, bz, ss)
        assert len(simple) == EXPECTED_SIMPLE[n]
        checked[n] = len(simple)

    minimal_winners = [mask(2, 3, 4, 5), mask(1, 5, 6), mask(3, 6), mask(2, 6)]
    truth = truth_from_minimal_winners(6, minimal_winners)
    bz, ss = power_indices(6, truth)
    expected_bz = [Fraction(1, 24), Fraction(1, 6), Fraction(1, 6), Fraction(1, 24), Fraction(1, 12), Fraction(1, 2)]
    expected_ss = [Fraction(1, 30), Fraction(1, 6), Fraction(1, 6), Fraction(1, 20), Fraction(1, 12), Fraction(1, 2)]
    assert bz == expected_bz
    assert ss == expected_ss
    assert bz[0] == bz[3]
    assert ss[0] < ss[3]
    assert not same_weak_order(bz, ss)
    print('VERIFY_OK')
    print('simple_games_checked=' + repr(checked))
    print('witness_banzhaf=' + repr([str(x) for x in bz]))
    print('witness_shapley_shubik=' + repr([str(x) for x in ss]))

if __name__ == '__main__':
    main()
