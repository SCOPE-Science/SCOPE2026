from fractions import Fraction
from itertools import product


def stirling2(n, k):
    if n < 0 or k < 0 or k > n:
        return 0
    dp = [0] * (k + 1)
    dp[0] = 1
    for r in range(1, n + 1):
        nd = [0] * (k + 1)
        for j in range(1, min(r, k) + 1):
            nd[j] = j * dp[j] + dp[j - 1]
        dp = nd
    return dp[k]


def conditional_coefficient(N, b, k):
    a = Fraction(stirling2(b - 1, k), stirling2(b, k))
    return Fraction(N - b + N * (b - 1) * a, N * b)


def run(max_N=6, max_b=7):
    sequences = 0
    strata = 0
    exact_assertions = 0
    parameter_pairs = 0

    for N in range(2, max_N + 1):
        xs = [i * i + 2 * i for i in range(N)]
        xsum = sum(xs)
        mu = Fraction(xsum, N)
        s2 = sum((Fraction(x) - mu) ** 2 for x in xs) / (N - 1)

        for b in range(1, max_b + 1):
            parameter_pairs += 1
            groups = {}
            sum_K = 0
            sum_err2 = Fraction(0)
            sum_Kerr2 = Fraction(0)

            for seq in product(range(N), repeat=b):
                sequences += 1
                k = len(set(seq))
                total = sum(xs[i] for i in seq)
                mean = Fraction(total, b)
                err2 = (mean - mu) ** 2
                rec = groups.setdefault(k, [0, Fraction(0), Fraction(0)])
                rec[0] += 1
                rec[1] += mean
                rec[2] += err2
                sum_K += k
                sum_err2 += err2
                sum_Kerr2 += k * err2

            total_sequences = N ** b
            for k, (count, sum_mean, sum_e2) in groups.items():
                strata += 1
                assert sum_mean / count == mu
                exact_assertions += 1
                target_var = conditional_coefficient(N, b, k) * s2
                assert sum_e2 / count == target_var
                exact_assertions += 1

            EK = Fraction(sum_K, total_sequences)
            Ee2 = sum_err2 / total_sequences
            EKe2 = sum_Kerr2 / total_sequences
            covariance = EKe2 - EK * Ee2
            target = -Fraction(b - 1, b * (N - 1)) * Fraction(N - 1, N) ** b * s2
            assert covariance == target
            exact_assertions += 1

    print("VERIFY_OK")
    print(f"parameter_pairs={parameter_pairs}")
    print(f"sequences_enumerated={sequences}")
    print(f"support_strata={strata}")
    print(f"exact_assertions={exact_assertions}")


if __name__ == "__main__":
    run()
