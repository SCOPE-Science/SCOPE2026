"""Standalone finite verification of cardinality-distortion modal extremizers.
Run: python3 checker.py
No external dependencies.
"""
from itertools import combinations, product
from math import comb, factorial


def diamond(rows, a):
    value = 0
    for j, r in enumerate(rows):
        if a & (1 << j):
            value |= r
    return value


def defect(rows):
    n = len(rows)
    return max(abs(diamond(rows, a).bit_count() - a.bit_count())
               for a in range(1 << n))


def common_hub(rows, n):
    return [c for c in range(n) if all(row & (1 << c) for row in rows)]


def star_normal_form(rows, n):
    hubs = common_hub(rows, n)
    if len(hubs) != 1:
        return False
    c = hubs[0]
    leaves = []
    for row in rows:
        if row.bit_count() != 2 or not row & (1 << c):
            return False
        leaves.append((row ^ (1 << c)).bit_length() - 1)
    return len(set(leaves)) >= n - 2


def labelled_formula(n):
    return factorial(n) * (comb(n, 2) + comb(n, 3) + 3 * comb(n, 4))


def verify():
    for n in range(1, 5):
        max_e = -1
        count_at_max = 0
        zero_count = 0
        for rows in product(range(1 << n), repeat=n):
            d = defect(rows)
            if d == 0:
                zero_count += 1
            if d <= 1:
                e = sum(row.bit_count() for row in rows)
                if e > max_e:
                    max_e = e
                    count_at_max = 1
                elif e == max_e:
                    count_at_max += 1
        assert zero_count == factorial(n), (n, zero_count)
        assert max_e == (1 if n == 1 else 2*n), (n, max_e)
        if n == 4:
            assert count_at_max == 456
        print('all-relations', n, 'maximum_edges', max_e,
              'maximizers', count_at_max, 'zero_defect', zero_count)

    for n, wanted in ((4, 456), (5, 4200)):
        two_sets = [sum(1 << j for j in pair)
                    for pair in combinations(range(n), 2)]
        good = 0
        star_good = 0
        nonstar_good = 0
        for rows in product(two_sets, repeat=n):
            if defect(rows) > 1:
                continue
            good += 1
            if common_hub(rows, n):
                star_good += 1
                if n == 5:
                    assert star_normal_form(rows, n)
            else:
                nonstar_good += 1
        assert good == wanted, (n, good, wanted)
        if n == 4:
            assert (star_good, nonstar_good) == (312, 144)
            assert star_good == labelled_formula(4)
        else:
            assert nonstar_good == 0
            assert star_good == labelled_formula(5)
        print('all-degree-two', n, 'maximizers', good,
              'stars', star_good, 'exceptions', nonstar_good)

    for n in range(5, 13):
        # Exact Stirling-number counting, independently via recurrence.
        S = [[0] * (n+1) for _ in range(n+1)]
        S[0][0] = 1
        for i in range(1, n+1):
            for j in range(1, i+1):
                S[i][j] = j*S[i-1][j] + S[i-1][j-1]
        count = n*(factorial(n-1)*S[n][n-1]
                   + (n-1)*factorial(n-2)*S[n][n-2])
        assert count == labelled_formula(n)
    print('stirling-identity-through-12 OK')
    print('ALL_CHECKS_OK')


if __name__ == '__main__':
    verify()
