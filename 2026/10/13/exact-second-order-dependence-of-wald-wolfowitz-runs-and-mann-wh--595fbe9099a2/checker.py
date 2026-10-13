from fractions import Fraction
from itertools import combinations

def expected_formulas(m, n):
    N = m + n
    p = m * n
    ER = Fraction(1, 1) + Fraction(2 * p, N)
    VR = Fraction(2 * p * (2 * p - N), N * N * (N - 1))
    EU = Fraction(p, 2)
    VU = Fraction(p * (N + 1), 12)
    cov_R_Q2 = -Fraction(p * (p - 1), 3 * N)
    var_Q2 = Fraction(
        p * (N + 1) * (5 * p * N + 8 * p - 3 * N * (N + 1)),
        360,
    )
    cov_R_Z2 = -Fraction(4 * (p - 1), N * (N + 1))
    corr2 = None
    if p > 1:
        corr2 = Fraction(
            20 * (p - 1) ** 2 * (N - 1),
            (N + 1)
            * (2 * p - N)
            * (5 * p * N + 8 * p - 3 * N * (N + 1)),
        )
    return ER, VR, EU, VU, cov_R_Q2, var_Q2, cov_R_Z2, corr2

def enumerate_word_moments(m, n):
    N = m + n
    values = []
    for selected in combinations(range(N), m):
        bits = [0] * N
        for i in selected:
            bits[i] = 1

        R = 1 + sum(bits[i] != bits[i + 1] for i in range(N - 1))

        zeros_after = n
        U = 0
        for bit in bits:
            if bit:
                U += zeros_after
            else:
                zeros_after -= 1

        values.append((R, U))

    den = len(values)
    ER = Fraction(sum(r for r, _ in values), den)
    EU = Fraction(sum(u for _, u in values), den)
    VR = Fraction(sum((r - ER) ** 2 for r, _ in values), den)
    VU = Fraction(sum((u - EU) ** 2 for _, u in values), den)
    cov_R_U = Fraction(sum((r - ER) * (u - EU) for r, u in values), den)

    q2 = [(u - EU) ** 2 for _, u in values]
    EQ2 = VU
    cov_R_Q2 = Fraction(
        sum((r - ER) * (q - EQ2) for (r, _), q in zip(values, q2)),
        den,
    )
    var_Q2 = Fraction(sum((q - EQ2) ** 2 for q in q2), den)
    return ER, VR, EU, VU, cov_R_U, cov_R_Q2, var_Q2

def main():
    checks = 0
    words = 0
    for N in range(2, 15):
        for m in range(1, N):
            n = N - m
            words += 1
            got = enumerate_word_moments(m, n)
            ER, VR, EU, VU, cov_R_Q2, var_Q2, cov_R_Z2, corr2 = expected_formulas(m, n)
            expected = (ER, VR, EU, VU, Fraction(0), cov_R_Q2, var_Q2)

            for lhs, rhs in zip(got, expected):
                assert lhs == rhs, (m, n, lhs, rhs)
                checks += 1

            assert cov_R_Q2 / VU == cov_R_Z2
            checks += 1

            if m * n > 1:
                assert cov_R_Q2 * cov_R_Q2 / (VR * var_Q2) == corr2
                checks += 1

    print("VERIFY_OK")
    print("max_pooled_size=14")
    print(f"sample_size_pairs={words}")
    print(f"exact_formula_checks={checks}")

if __name__ == "__main__":
    main()
