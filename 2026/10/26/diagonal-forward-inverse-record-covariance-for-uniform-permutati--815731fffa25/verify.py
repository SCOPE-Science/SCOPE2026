"""Exact enumeration checks for a forward/inverse record covariance identity."""
from fractions import Fraction
from itertools import permutations
from math import comb, factorial


def flags(values):
    current = 0
    out = []
    for value in values:
        active = value > current
        out.append(int(active))
        if active:
            current = value
    return out


def check(n):
    joint = [[0] * n for _ in range(n)]
    ma = [0] * n
    mb = [0] * n
    count = 0
    for perm in permutations(range(1, n + 1)):
        inverse = [0] * n
        for i, v in enumerate(perm):
            inverse[v - 1] = i + 1
        a = flags(perm)
        b = flags(inverse)
        count += 1
        for i in range(n):
            ma[i] += a[i]
            mb[i] += b[i]
            if a[i]:
                for j in range(n):
                    joint[i][j] += b[j]
    assert count == factorial(n)
    for i in range(1, n + 1):
        assert Fraction(ma[i - 1], count) == Fraction(1, i)
        assert Fraction(mb[i - 1], count) == Fraction(1, i)
        for j in range(1, n + 1):
            cov = Fraction(joint[i - 1][j - 1], count) - Fraction(1, i*j)
            expected = (Fraction(i - 1, i*i*comb(n, i)) if i == j else Fraction(0))
            assert cov == expected, (n, i, j, cov, expected)
    return n*n, count


def exact_total(n):
    return sum((Fraction(i-1, i*i*comb(n, i)) for i in range(2, n+1)), Fraction(0))


def main():
    comparisons = 0
    permutations_examined = 0
    for n in range(1, 9):
        c, p = check(n)
        comparisons += c
        permutations_examined += p
    # Algebraic formula checked by independent explicit rational summation.
    assert exact_total(2) == Fraction(1, 4)
    assert exact_total(3) == Fraction(11, 36)
    assert exact_total(4) == Fraction(41, 144)
    assert all(exact_total(n) > 0 for n in range(2, 101))
    print(f"PASS: {comparisons} exact covariance entries checked across {permutations_examined} permutations; 99 positive total-covariance checks")


if __name__ == "__main__":
    main()
