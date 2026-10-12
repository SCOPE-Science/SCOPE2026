from fractions import Fraction
from math import factorial, comb

def stirling2(n, k):
    if n < 0:
        return 0
    if n == 0:
        return 1 if k == 0 else 0
    if k < 0 or k > n:
        return 0
    dp = [0] * (k + 1)
    dp[0] = 1
    for r in range(1, n + 1):
        nd = [0] * (k + 1)
        for j in range(1, min(r, k) + 1):
            nd[j] = j * dp[j] + dp[j - 1]
        dp = nd
    return dp[k]

def compositions(total, parts, prefix=()):
    if parts == 1:
        yield prefix + (total,)
        return
    for x in range(total + 1):
        yield from compositions(total - x, parts - 1, prefix + (x,))

def multinomial_probability(counts, m):
    N = sum(counts)
    den = 1
    for x in counts:
        den *= factorial(x)
    return Fraction(factorial(N), den * (m ** N))

def verify():
    strata = 0
    assertions = 0
    vectors = 0
    for m in range(2, 7):
        for N in range(2, 8):
            by_k = {}
            for counts in compositions(N, m):
                vectors += 1
                p = multinomial_probability(counts, m)
                k = sum(x > 0 for x in counts)
                U = sum(comb(x, 2) for x in counts)
                X2 = Fraction(m, N) * sum(x*x for x in counts) - N
                assert X2 == Fraction(m - N) + Fraction(2*m, N) * U
                assertions += 1
                rec = by_k.setdefault(k, [Fraction(0), Fraction(0), Fraction(0)])
                rec[0] += p
                rec[1] += p * X2
                rec[2] += p * X2 * X2

            for k, (pk, sx, sx2) in by_k.items():
                strata += 1
                mean = sx / pk
                var = sx2 / pk - mean * mean

                S = stirling2(N, k)
                a = Fraction(stirling2(N - 1, k), S)
                b = Fraction(stirling2(N - 2, k), S)
                M = comb(N, 2)

                mean_formula = Fraction(m - N) + m * (N - 1) * a
                var_u = M * a * (1 - a) + M * (M - 1) * (b - a*a)
                var_formula = Fraction(4*m*m, N*N) * var_u

                assert mean == mean_formula
                assertions += 1
                assert var == var_formula
                assertions += 1

    print("VERIFY_OK")
    print(f"count_vectors={vectors}")
    print(f"conditional_strata={strata}")
    print(f"exact_assertions={assertions}")

if __name__ == "__main__":
    verify()
