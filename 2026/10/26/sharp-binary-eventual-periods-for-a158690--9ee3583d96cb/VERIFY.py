"""Exact modular checks for the binary periods of sequence A158690.

Pure integer arithmetic; finite checks complement the infinite argument.
"""
from math import comb, factorial


def direct_coefficient(n):
    if n == 0:
        return 1
    total = 0
    for m in range(1, n + 1):
        for mask in range(1 << m):
            subset_sum = sum(2 * j + 1 for j in range(m) if mask & (1 << j))
            total += (-1) ** mask.bit_count() * (-subset_sum) ** n
    return total


def power_sum_weights(modulus):
    M = 1
    while factorial(M) % modulus:
        M += 1
    precision = M - 1
    product = [1] + [0] * precision
    series = [1] + [0] * precision
    for m in range(1, M):
        d = 2 * m - 1
        factor = [0] + [(-1) ** (j + 1) * comb(d + j - 1, j) % modulus
                        for j in range(1, precision + 1)]
        next_product = [0] * (precision + 1)
        for i, value in enumerate(product):
            for j in range(1, precision + 1 - i):
                next_product[i + j] += value * factor[j]
        product = [value % modulus for value in next_product]
        series = [(series[j] + product[j]) % modulus for j in range(precision + 1)]
    weights = [sum((-1) ** (m - j) * comb(m, j) * series[m]
                   for m in range(j, M)) % modulus for j in range(M)]
    return M, weights


def value(n, modulus, weights):
    if n == 0:
        return 1
    return sum(w * pow(j, n, modulus) for j, w in enumerate(weights)) % modulus


def check():
    known = [1, 1, 5, 55, 1073, 32671, 1431665, 85363615, 6646603073]
    assert [direct_coefficient(i) for i in range(9)] == known
    assert (known[8] - known[6]) % 32 == 16
    tests = 9
    for r in range(2, 17):
        modulus = 1 << r
        M, weights = power_sum_weights(modulus)
        for n in range(1, 9):
            assert value(n, modulus, weights) == known[n] % modulus
            tests += 1
        p = 2 if r <= 3 else 1 << (r - 3)
        for n in range(max(r, 4), max(r, 4) + 12):
            assert value(n + p, modulus, weights) == value(n, modulus, weights)
            tests += 1
        if r >= 5:
            half = p // 2
            for n in range(r + (r & 1), r + (r & 1) + 12, 2):
                difference = (value(n + half, modulus, weights)
                              - value(n, modulus, weights)) % modulus
                assert difference == modulus // 2
                tests += 1
            B = sum(weights[j] * ((j * j - 1) // 8)
                    for j in range(1, M, 2))
            assert B % 4 == 2
            tests += 1
    print('VERIFY_OK', tests)


if __name__ == '__main__':
    check()
