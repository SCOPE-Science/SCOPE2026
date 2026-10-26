#!/usr/bin/env python3
"""Independent finite checks for the diamond p-morphism enumeration theorem."""
from itertools import combinations_with_replacement, product
from collections import defaultdict
from math import comb


def closed(a, b):
    return sum((2 ** k - 2) * comb(a, k) * comb(b, k)
               for k in range(2, min(a, b) + 1))


def delannoy(a, b):
    d = [[0] * (b + 1) for _ in range(a + 1)]
    for i in range(a + 1):
        for j in range(b + 1):
            d[i][j] = 1 if i == 0 or j == 0 else (
                d[i - 1][j] + d[i][j - 1] + d[i - 1][j - 1])
    return d[a][b]


def independent_brute(a, b):
    pts = list(product(range(a), range(b)))
    allbits = (1 << (a * b)) - 1
    choices = []
    for bounds_reverse in combinations_with_replacement(range(b + 1), a):
        bounds = bounds_reverse[::-1]
        down = sum(1 << (i * b + j)
                   for i, width in enumerate(bounds) for j in range(width))
        choices.append(allbits ^ down)  # each upset independently
    upcones = []
    for x, y in pts:
        upcones.append([idx for idx, (u, v) in enumerate(pts)
                        if x <= u and y <= v])
    count = 0
    for p in choices:
        for q in choices:
            f = [int(bool(p & (1 << i))) + 2 * int(bool(q & (1 << i)))
                 for i in range(len(pts))]
            if set(f) != {0, 1, 2, 3}:
                continue
            valid = True
            for i, indices in enumerate(upcones):
                expected = {z for z in range(4) if z & f[i] == f[i]}
                actual = {f[j] for j in indices}
                if expected != actual:
                    valid = False
                    break
            count += valid
    return count


def threshold_transfer(a, b):
    # Orientation is implicit and restored by factor two.
    if a < 2 or b < 2:
        return 0
    state = {(m, M): 1 for m in range(1, a) for M in range(m + 1, a + 1)}
    for _ in range(b - 1):
        next_state = defaultdict(int)
        for (m, M), count in state.items():
            if m == 0:
                for new_M in range(M + 1):
                    next_state[(0, new_M)] += count
            else:
                for new_M in range(m + 1, M + 1):
                    next_state[(m, new_M)] += count
                for new_m in range(m):
                    next_state[(new_m, m)] += count
        state = next_state
    return 2 * sum(count for (m, M), count in state.items() if m == 0)


def main():
    direct_cases = 0
    for a in range(1, 6):
        for b in range(1, 6):
            actual = independent_brute(a, b)
            predicted = closed(a, b)
            assert actual == predicted, (a, b, actual, predicted)
            direct_cases += 1
    transfer_cases = 0
    for a in range(1, 14):
        for b in range(1, 20):
            n = closed(a, b)
            assert threshold_transfer(a, b) == n, (a, b, n)
            assert delannoy(a, b) - 2 * comb(a + b, a) + 1 == n
            assert n == closed(b, a)
            transfer_cases += 1
    assert [closed(n, n) for n in range(2, 7)] == [2, 24, 182, 1180, 7142]
    print(f'DIRECT_BOUNDED_MORPHISM_CASES_PASS {direct_cases}')
    print(f'THRESHOLD_RECURRENCE_AND_DELANNOY_CASES_PASS {transfer_cases}')
    print('DIAGONAL_SEQUENCE_PASS 2 24 182 1180 7142')
    print('ALL_TESTS_PASS')


if __name__ == '__main__':
    main()
