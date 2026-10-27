#!/usr/bin/env python3
"""Independent finite checks for a zero-ended word exclusion in gap shifts.

Uses Python's standard library and no unproved black-box numerical identities.
Finite tests are supplements, not a proof of the infinite-alphabet theorem.
"""
from fractions import Fraction

TEST_SETS = ((0, 1, 3), (0, 2, 5), (0, 1, 2, 4))
THRESHOLDS = ((1, 1), (1, 2), (2, 1), (2, 2), (3, 2), (2, 3))


def short_transfer(S, r, s, z):
    weights = {g: Fraction(1, z ** (g + 1)) for g in S}
    total = sum(weights.values(), Fraction(0))
    a = sum((weights[g] for g in S if g >= r), Fraction(0))
    b = sum((weights[g] for g in S if g >= s), Fraction(0))
    c = sum((weights[g] for g in S if g >= max(r, s)), Fraction(0))
    low = total - a
    other_low = sum((weights[g] for g in S if g < min(r, s)), Fraction(0))
    other_high = sum((weights[g] for g in S if r <= g < s), Fraction(0))
    determinant = (1 - low) * (1 - other_high) - a * other_low
    formula = (1 - total) * (1 + c) + a * b
    return determinant, formula


def expanded_matrix(S, r, s):
    maximal = max(S)
    states = tuple((flag, age) for flag in (0, 1) for age in range(maximal + 1))
    indices = {state: i for i, state in enumerate(states)}
    n = len(states)
    matrix = [[0] * n for _ in range(n)]
    for state, index in indices.items():
        old_large, age = state
        if age < maximal:
            matrix[index][indices[(old_large, age + 1)]] += 1
        if age in S and not (old_large and age >= s):
            matrix[index][indices[(int(age >= r), 0)]] += 1
    return matrix


def multiply(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            a = A[i][k]
            if a:
                for j in range(n):
                    C[i][j] += a * B[k][j]
    return C


def cyclic_count(length, S, r, s):
    result = 0
    for word in range(1, 1 << length):
        ones = [i for i in range(length) if (word >> i) & 1]
        gaps = [(ones[(j + 1) % len(ones)] - ones[j] - 1) % length
                for j in range(len(ones))]
        if any(g not in S for g in gaps):
            continue
        if any(gaps[j - 1] >= r and gaps[j] >= s
               for j in range(len(gaps))):
            continue
        result += 1
    return result


def dominant_eigenvalue(M):
    n = len(M)
    vector = [1.0] * n
    value = None
    for _ in range(3200):
        nxt = [sum(M[i][j] * vector[j] for j in range(n)) for i in range(n)]
        scale = max(nxt)
        assert scale > 0
        vector = [v / scale for v in nxt]
        value = scale
    return value


def root_equation(z, S, r, s):
    total = sum(z ** (-g - 1) for g in S)
    a = sum(z ** (-g - 1) for g in S if g >= r)
    b = sum(z ** (-g - 1) for g in S if g >= s)
    c = sum(z ** (-g - 1) for g in S if g >= max(r, s))
    return (1 - total) * (1 + c) + a * b


def bisection(S, r, s):
    lo, hi = 1.000001, 3.0
    assert root_equation(lo, S, r, s) < 0
    assert root_equation(hi, S, r, s) > 0
    for _ in range(150):
        mid = (lo + hi) / 2
        if root_equation(mid, S, r, s) < 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def main():
    checks = 0
    for S in TEST_SETS:
        for r, s in THRESHOLDS:
            for z in (2, 3, 5):
                left, right = short_transfer(S, r, s, z)
                assert left == right, (S, r, s, z, left, right)
                checks += 1
            M = expanded_matrix(S, r, s)
            predicted = bisection(S, r, s)
            independent = dominant_eigenvalue(M)
            assert abs(predicted - independent) < 1e-9, (S, r, s, predicted, independent)
            checks += 1
            n = len(M)
            power = [[int(i == j) for j in range(n)] for i in range(n)]
            for length in range(1, 13):
                power = multiply(power, M)
                from_matrix = sum(power[i][i] for i in range(n))
                from_words = cyclic_count(length, S, r, s)
                assert from_matrix == from_words, (S, r, s, length, from_matrix, from_words)
                checks += 1
    print('PASS:', checks, 'independent exact/numerical finite checks')
    print('18 finite constrained-gap models; each cyclic enumeration covers lengths 1..12')


if __name__ == '__main__':
    main()
