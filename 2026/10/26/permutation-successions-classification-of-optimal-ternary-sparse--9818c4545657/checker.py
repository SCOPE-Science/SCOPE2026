#!/usr/bin/env python3
"""Reproduce finite checks of sparse ternary deletion-code classification.
This code is only a finite test; the all-length theorem is proved in RESULT.md.
"""
from collections import defaultdict
from itertools import combinations, permutations, product


def delete_one(word):
    return {word[:j] + word[j + 1:] for j in range(len(word))}


def source_word(k, row, col, orientation):
    """Zero-based singleton-output positions, orientation '+' means 1 before 2."""
    n = k + 1
    if orientation == '+':
        one, two = row, col + 1
        assert row <= col
    else:
        one, two = row + 1, col
        assert row >= col
    out = ['0'] * n
    out[one], out[two] = '1', '2'
    return ''.join(out)


def choices(row, col):
    if row < col:
        return ('+',)
    if row > col:
        return ('-',)
    return ('+', '-')


def allowed_signed_permutation(columns, orientations):
    k = len(columns)
    if sorted(columns) != list(range(k)):
        return False
    for row in range(k):
        if orientations[row] not in choices(row, columns[row]):
            return False
        if row and columns[row] == columns[row - 1] + 1 and orientations[row] == orientations[row - 1]:
            return False
    return True


def permutation_formula(k):
    total = 0
    for p in permutations(range(k)):
        if any(p[i + 1] == p[i] + 1 and p[i] != i for i in range(k - 1)):
            continue
        runs = sum(p[i] == i and (i == 0 or p[i - 1] != i - 1) for i in range(k))
        total += 1 << runs
    return total


def dynamic_count(k):
    dp = defaultdict(int)
    for col in range(k):
        for o in choices(0, col):
            dp[(1 << col, col, o)] += 1
    for i in range(1, k):
        nd = defaultdict(int)
        for (used, prev_col, prev_o), weight in dp.items():
            for col in range(k):
                if (used >> col) & 1:
                    continue
                for o in choices(i, col):
                    if col == prev_col + 1 and o == prev_o:
                        continue
                    nd[(used | (1 << col), col, o)] += weight
        dp = nd
    return sum(dp.values())


def direct_max_codes(n):
    words = []
    for one in range(n):
        for two in range(n):
            if one == two:
                continue
            w = ['0'] * n
            w[one], w[two] = '1', '2'
            words.append(''.join(w))
    d = [delete_one(w) for w in words]
    optimum_count = 0
    for sub in combinations(range(len(words)), n - 1):
        seen = set()
        good = True
        for ix in sub:
            if seen.intersection(d[ix]):
                good = False
                break
            seen.update(d[ix])
        optimum_count += good
    return optimum_count


def direct_signed_codes(k):
    total = 0
    for columns in permutations(range(k)):
        options = [choices(i, c) for i, c in enumerate(columns)]
        for signs in product(*options):
            encoded = [source_word(k, i, c, o) for i, (c, o) in enumerate(zip(columns, signs))]
            descendant_sets = [delete_one(w) for w in encoded]
            direct = all(not descendant_sets[i].intersection(descendant_sets[j])
                         for i in range(k) for j in range(i + 1, k))
            criterion = allowed_signed_permutation(columns, signs)
            assert direct == criterion, (k, columns, signs, encoded)
            total += direct
    return total


def explicit_code(n):
    k = n - 1
    return [source_word(k, i, i, '+' if i % 2 == 0 else '-') for i in range(k)]


def main():
    expected = [2, 3, 8, 32, 158, 918, 6258, 49076, 434408, 4282508, 46532354]
    for k, val in enumerate(expected, start=1):
        found = dynamic_count(k)
        assert found == val, (k, found, val)
    for k in range(1, 9):
        assert permutation_formula(k) == expected[k - 1]
        assert direct_signed_codes(k) == expected[k - 1]
    for n in range(2, 7):
        assert direct_max_codes(n) == expected[n - 2]
    for n in range(2, 101):
        code = explicit_code(n)
        assert len(set(code)) == n - 1
        d = [delete_one(w) for w in code]
        assert all(not d[i].intersection(d[j]) for i in range(n - 1)
                   for j in range(i + 1, n - 1))
    print('PASS: DP through k=11, permutation and signed-code counts through k=8,')
    print('independent brute-force maximum-code census for n=2..6,')
    print('and an explicit optimum construction for n=2..100.')


if __name__ == '__main__':
    main()
