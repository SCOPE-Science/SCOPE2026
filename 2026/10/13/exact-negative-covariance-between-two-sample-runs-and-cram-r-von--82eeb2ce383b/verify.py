from fractions import Fraction
from itertools import combinations


def enumerate_pair(m, n):
    N = m + n
    rows = []
    for ones in combinations(range(N), m):
        one = set(ones)
        word = [1 if k in one else 0 for k in range(N)]
        R = 1 + sum(word[k] != word[k + 1] for k in range(N - 1))
        A = 0
        S = 0
        for j in range(1, N):
            A += word[j - 1]
            B = N * A - m * j
            S += B * B
        T = Fraction(S, m * n * N * N)
        rows.append((R, S, T))
    count = len(rows)
    ER = sum(Fraction(r, count) for r, _, _ in rows)
    ES = sum(Fraction(s, count) for _, s, _ in rows)
    ET = sum(t for _, _, t in rows) / count
    cov_RS = sum(Fraction(r * s, count) for r, s, _ in rows) - ER * ES
    cov_RT = sum(Fraction(r, 1) * t for r, _, t in rows) / count - ER * ET
    return count, ER, ES, ET, cov_RS, cov_RT


def conditional_sum(m, n):
    N = m + n
    if N < 4:
        return None
    total = Fraction(0)
    for i in range(1, N):
        e_si = Fraction(0)
        for j in range(1, N):
            if j < i:
                mean = Fraction(j * (m - n), N - 2)
                var = Fraction(N * N * j * (N - 2 - j) * (m - 1) * (n - 1), (N - 2) ** 2 * (N - 3))
            elif j == i:
                mean = Fraction((2 * i - N) * (m - n), 2 * (N - 2))
                var = Fraction(N * N * (i - 1) * (N - i - 1) * (m - 1) * (n - 1), (N - 2) ** 2 * (N - 3)) + Fraction(N * N, 4)
            else:
                mean = Fraction(-(N - j) * (m - n), N - 2)
                var = Fraction(N * N * (j - 2) * (N - j) * (m - 1) * (n - 1), (N - 2) ** 2 * (N - 3))
            e_si += var + mean * mean
        total += e_si
    return total

word_checks = 0
pair_checks = 0
for N in range(2, 13):
    for m in range(1, N):
        n = N - m
        count, ER, ES, ET, cov_RS, cov_RT = enumerate_pair(m, n)
        word_checks += count
        pair_checks += 1
        assert ER == Fraction(2 * m * n, N) + 1
        assert ES == Fraction(m * n * N * (N + 1), 6)
        assert ET == Fraction(N + 1, 6 * N)
        assert cov_RS == Fraction(-m * n * (2 * m * n - N), 3)
        assert cov_RT == Fraction(-(2 * m * n - N), 3 * N * N)

conditional_checks = 0
for N in range(4, 41):
    for m in range(1, N):
        n = N - m
        got = conditional_sum(m, n)
        expected = Fraction(N * (N - 1) * ((N - 1) * m * n + N), 6)
        assert got == expected
        conditional_checks += 1

print(f"exact binary words enumerated: {word_checks}")
print(f"sample-size pairs checked by enumeration: {pair_checks}")
print(f"conditional aggregate identities checked: {conditional_checks}")
print("all exact checks passed")
