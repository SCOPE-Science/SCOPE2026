"""Standalone exhaustive checker for modal operators on finite Kleene chains.

Runs without third-party packages: python checker.py
Enumerates all weakly increasing maps for chain lengths 2 through 9;
checks the displayed equations directly, and compares the proved normal forms
and closed counting formulas. This finite enumeration does not prove the theorem.
"""
from itertools import combinations_with_replacement
from math import comb


def satisfies_axioms(f):
    """Meet preservation, (Pos), and (Con) on the De Morgan chain."""
    n = len(f)
    neg = lambda x: n - 1 - x
    for x in range(n):
        for y in range(n):
            if f[min(x, y)] != min(f[x], f[y]):
                return False
        for z in range(n):
            high = max(z, neg(z))
            low = min(z, neg(z))
            if neg(f[high]) > f[high]:
                return False
            v = f[max(x, low)]
            if v > max(f[x], neg(v)):
                return False
    return True


def normal_form(f):
    """Independent structural recognition of the two allowed types."""
    n = len(f)
    m = n // 2
    if n % 2 == 0:
        first = f[m - 1] <= m - 1 and f[m] >= m
        second = f[0] >= m and all(f[i] == f[0] for i in range(m))
    else:
        first = f[m] == m
        second = f[m] > m and all(f[i] == f[m] for i in range(m + 1))
    return first or second


def formulas(n):
    m = n // 2
    if n % 2 == 0:
        b = comb(2 * m - 1, m)
        return b * b + comb(2 * m, m + 1), b * (
            comb(2 * m - 2, m - 1) + 1
        )
    b = comb(2 * m, m)
    return b * b + comb(2 * m, m + 1), (
        b * (b + 1) // 2
    )


def main():
    for n in range(2, 10):
        observed = [0, 0]
        for f in combinations_with_replacement(range(n), n):
            ok = satisfies_axioms(f)
            assert ok == normal_form(f), (n, f, ok)
            if ok:
                observed[0] += 1
                observed[1] += f[-1] == n - 1
        expected = formulas(n)
        assert tuple(observed) == expected, (n, observed, expected)
        print(f"n={n}: all={expected[0]}, top-preserving={expected[1]}")
    print("Passed: exhaustive agreement of equations, structural forms and counts.")


if __name__ == "__main__":
    main()
