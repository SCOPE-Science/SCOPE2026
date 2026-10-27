"""Independent arithmetic checks for the minimum-total-domination census of J(n,2).

Uses labelled-forest component counting; does not search vertex subsets.
"""
from fractions import Fraction
from math import factorial


def multiplicity(n, isolated, sizes):
    assert isolated + sum(sizes) == n
    assert all(s >= 3 for s in sizes)
    numerator = factorial(n)
    denominator = factorial(isolated)
    for s in set(sizes):
        count = sizes.count(s)
        numerator *= s ** ((s - 2) * count)
        denominator *= factorial(s) ** count * factorial(count)
    assert numerator % denominator == 0
    return numerator // denominator


def shape_counts(n):
    k, r = divmod(n, 3)
    if r == 0:
        data = {'full_P3': multiplicity(n, 0, [3] * k)}
        if k >= 2:
            data['isolated_T5'] = multiplicity(n, 1, [5] + [3] * (k - 2))
        if k >= 3:
            data['isolated_T4_T4'] = multiplicity(n, 1, [4, 4] + [3] * (k - 3))
    elif r == 1:
        data = {'isolated_P3': multiplicity(n, 1, [3] * k)}
    else:
        data = {'isolated_T4': multiplicity(n, 1, [4] + [3] * (k - 1))}
    return data


def explicit_formula(n):
    k, r = divmod(n, 3)
    base = Fraction(factorial(n), 2 ** k * factorial(k))
    if r == 0:
        factor = 1 + Fraction(25 * k * (k - 1), 6) + Fraction(16 * k * (k - 1) * (k - 2), 9)
    elif r == 1:
        factor = 1
    else:
        factor = Fraction(4 * k, 3)
    ans = base * factor
    assert ans.denominator == 1
    return ans.numerator


if __name__ == '__main__':
    expected = {4: 12, 5: 80, 6: 840, 7: 630, 8: 13440, 9: 277200, 10: 75600}
    for n in range(4, 101):
        data = shape_counts(n)
        total = sum(data.values())
        assert total == explicit_formula(n), (n, data, total)
        if n in expected:
            assert total == expected[n], (n, total)
    print('VERIFY_FORMULA_OK n=4..100; minimum counts n=4..10:', expected)
