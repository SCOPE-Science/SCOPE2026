#!/usr/bin/env python3
"""Independent finite checks of circular prefix-maximality and the three-one gap classification.

Standard library only. The mathematical theorem is proved symbolically in RESULT.md;
finite tests here are safeguards against indexing and counting mistakes.
"""
from itertools import combinations


def canonical(w):
    return min(w[i:] + w[:i] for i in range(len(w)))


def brute_roots(w):
    n = len(w)
    # Compute maximum circular length-l one-count without using a gap formula.
    doubled = w + w
    pref = [0]
    for z in doubled:
        pref.append(pref[-1] + z)
    maxima = [0] + [max(pref[i+l]-pref[i] for i in range(n)) for l in range(1,n+1)]
    return tuple(i for i in range(n)
                 if all(pref[i+l]-pref[i] == maxima[l] for l in range(1,n+1)))


def gap_roots(w):
    n = len(w)
    ones = [i for i,z in enumerate(w) if z]
    if len(ones) != 3:
        raise ValueError('Three ones required')
    gaps = [(ones[(j+1)%3]-ones[j]-1) % n for j in range(3)]
    low, high = min(gaps), max(gaps)
    return tuple(ones[i] for i in range(3)
                 if gaps[i] == low and gaps[(i-1)%3] == high)


def coeff(n):
    target = n-6
    if target < 0:
        return 0
    return sum(1 for z in range(target//3+1)
               for y in range((target-3*z)//2+1))


def run():
    # Unrestricted first-obstruction check, all words through length 11.
    for n in range(1,12):
        missing = set()
        for x in range(1<<n):
            w = tuple((x>>i)&1 for i in range(n))
            if not brute_roots(w):
                missing.add(canonical(w))
        if n < 6:
            assert not missing, (n, missing)
        if n == 6:
            assert missing == {tuple(map(int,'001011'))}, missing
    print('ALL_BINARY_N_LE_11_OK')

    # Independent exhaustive triple-word scan vs gap criterion and rational GF.
    for n in range(3,42):
        absent = set()
        for positions in combinations(range(n),3):
            w = [0]*n
            for i in positions:
                w[i] = 1
            w = tuple(w)
            direct = brute_roots(w)
            predicted = gap_roots(w)
            assert direct == predicted, (n, w, direct, predicted)
            if not direct:
                absent.add(canonical(w))
        expected = coeff(n)
        assert len(absent) == expected, (n,len(absent),expected)
        if n <= 15:
            print(f'n={n} absent_necklaces={len(absent)} labeled={n*len(absent)}')
    print('ALL_THREE_ONE_N_LE_41_OK')
    print('VERIFY_OK')


if __name__ == '__main__':
    run()
