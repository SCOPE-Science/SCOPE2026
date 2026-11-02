#!/usr/bin/env python3
"""Exact verification for consecutive Stern-polynomial resultant identities."""
from functools import lru_cache


def add(a, b):
    return tuple((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(max(len(a), len(b))))


@lru_cache(None)
def stern(n):
    assert n >= 0
    if n == 0:
        return (0,)
    if n == 1:
        return (1,)
    if n % 2 == 0:
        return (0,) + stern(n // 2)
    return add(stern(n // 2), stern(n // 2 + 1))


@lru_cache(None)
def top(n):
    assert n >= 1
    if n == 1:
        return (0, 1)
    if n % 2 == 0:
        degree, leading = top(n // 2)
        return (degree + 1, leading)
    a, la = top(n // 2)
    b, lb = top(n // 2 + 1)
    if a > b:
        return a, la
    if b > a:
        return b, lb
    return a, la + lb


@lru_cache(None)
def predicted_abs_resultant(n):
    assert n >= 1
    if n == 1:
        return 1
    parent = n // 2
    ea, la = top(parent)
    eb, lb = top(parent + 1)
    if n % 2 == 0:
        return predicted_abs_resultant(parent) * la ** max(0, ea - eb)
    return predicted_abs_resultant(parent) * lb ** max(0, eb - ea)


def exact_det_bareiss(mat):
    n = len(mat)
    if n == 0:
        return 1
    a = [row[:] for row in mat]
    previous_pivot = 1
    sign = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            row = next((j for j in range(k + 1, n) if a[j][k] != 0), None)
            if row is None:
                return 0
            a[k], a[row] = a[row], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = a[i][j] * pivot - a[i][k] * a[k][j]
                assert numerator % previous_pivot == 0
                a[i][j] = numerator // previous_pivot
            a[i][k] = 0
        previous_pivot = pivot
    return sign * a[-1][-1]


def sylvester_resultant(f, g):
    a = len(f) - 1
    b = len(g) - 1
    if a == 0 and b == 0:
        return 1
    f_desc = f[::-1]
    g_desc = g[::-1]
    size = a + b
    rows = []
    for k in range(b):
        rows.append([0] * k + list(f_desc) + [0] * (b - k - 1))
    for k in range(a):
        rows.append([0] * k + list(g_desc) + [0] * (a - k - 1))
    assert all(len(row) == size for row in rows)
    return exact_det_bareiss(rows)


def main():
    exact_pairs = 0
    for n in range(1, 260):
        f, g = stern(n), stern(n + 1)
        assert f[-1] > 0 and g[-1] > 0
        assert (len(f) - 1, f[-1]) == top(n)
        assert (len(g) - 1, g[-1]) == top(n + 1)
        assert abs(len(f) - len(g)) <= 1
        assert f[0] + g[0] == 1
        assert abs(sylvester_resultant(f, g)) == predicted_abs_resultant(n), n
        exact_pairs += 1
    family_cases = 0
    for m in range(1, 17):
        n = (7 * 4 ** m + 5) // 3
        assert 3 * n == 7 * 4 ** m + 5
        assert predicted_abs_resultant(n) == m
        assert abs(sylvester_resultant(stern(n), stern(n + 1))) == m
        assert top(n + 1)[0] == top(n)[0] + 1
        initial = 2 * n
        assert top(initial)[0] == top(initial + 1)[0]
        assert predicted_abs_resultant(initial) == m
        for _ in range(3):
            initial = 4 * initial + 1
            assert top(initial)[0] == top(initial + 1)[0]
            assert predicted_abs_resultant(initial) == m
        family_cases += 1
    assert stern(39) == (1, 3, 4, 2)
    assert stern(40) == (0, 0, 0, 1, 2)
    print(f'VERIFY_OK: {exact_pairs} independent Sylvester determinant comparisons; '
          f'{family_cases} exact surjectivity witnesses, each with 4 recurring-value checks; '
          'binary degree/leading-coefficient invariants confirmed')


if __name__ == '__main__':
    main()
