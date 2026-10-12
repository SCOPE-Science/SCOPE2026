from fractions import Fraction
from itertools import permutations, combinations


def mean(vals):
    return sum(vals, Fraction(0)) / len(vals)


def uniform_contrast_checks():
    checks = 0
    perms = 0
    for N in range(2, 9):
        contrasts = [[1, -1] + [0] * (N - 2)]
        if N >= 3:
            contrasts.append([1, 1, -2] + [0] * (N - 3))
        contrasts.append([2 * i - N + 1 for i in range(N)])
        P = list(permutations(range(1, N + 1)))
        perms += len(P)
        for c in contrasts:
            assert sum(c) == 0 and any(c)
            s2 = sum(x * x for x in c)
            T = [sum(c[i] * p[i] for i in range(N)) for p in P]
            ET = mean([Fraction(x) for x in T])
            varT = mean([Fraction(x * x) for x in T]) - ET * ET
            target_varT = Fraction(N * (N + 1) * s2, 12)
            assert varT == target_varT
            checks += 1

            # For iid U[0,1], E[X_i | rank r] = r/(N+1).
            EVgiven = [Fraction(t, N + 1) for t in T]
            cov = mean([Fraction(T[j]) * EVgiven[j] for j in range(len(P))]) - ET * mean(EVgiven)
            target_cov = Fraction(N * s2, 12)  # G=1/3, so N G s2 / 4.
            assert cov == target_cov
            checks += 1
    return perms, checks


def two_sample_checks():
    checks = 0
    allocations = 0
    for N in range(2, 13):
        for m in range(1, N):
            n = N - m
            rows = []
            allr = set(range(1, N + 1))
            for Y in combinations(range(1, N + 1), n):
                Y = set(Y)
                X = allr - Y
                WY = sum(Y)
                U = WY - n * (n + 1) // 2
                # Uniform conditional mean difference from rank expectations.
                delta_cond = Fraction(sum(Y), n * (N + 1)) - Fraction(sum(X), m * (N + 1))
                rows.append((U, delta_cond))
            allocations += len(rows)
            EU = mean([Fraction(u) for u, d in rows])
            ED = mean([d for u, d in rows])
            cov = mean([Fraction(u) * d for u, d in rows]) - EU * ED
            assert cov == Fraction(N, 12)  # G=1/3 -> N G / 4.
            checks += 1

            varU = mean([Fraction(u * u) for u, d in rows]) - EU * EU
            assert varU == Fraction(m * n * (N + 1), 12)
            checks += 1

            # Full unconditional Var(Delta) for iid U[0,1].
            varDelta = Fraction(N, 12 * m * n)
            corr2 = cov * cov / (varU * varDelta)
            assert corr2 == Fraction(N, N + 1)
            checks += 1
    return allocations, checks


def beta_power_checks(max_k=500):
    checks = 0
    equalities = 0
    for k in range(1, max_k + 1):
        mu = Fraction(k, k + 1)
        ex2 = Fraction(k, k + 2)
        var = ex2 - mu * mu
        # For F(x)=x^k, E max(X1,X2)=2k/(2k+1), and G=2(E max-E X).
        G = 2 * (Fraction(2 * k, 2 * k + 1) - mu)
        assert G * G <= Fraction(4, 3) * var
        checks += 1
        if G * G == Fraction(4, 3) * var:
            assert k == 1
            equalities += 1
        else:
            assert k != 1
        checks += 1
    assert equalities == 1
    return checks


def run():
    perms, contrast_checks = uniform_contrast_checks()
    allocations, two_checks = two_sample_checks()
    beta_checks = beta_power_checks()
    print('VERIFY_OK')
    print(f'rank_permutations_checked={perms}')
    print(f'contrast_formula_checks={contrast_checks}')
    print(f'two_sample_allocations_checked={allocations}')
    print(f'two_sample_formula_checks={two_checks}')
    print(f'beta_power_checks={beta_checks}')


if __name__ == '__main__':
    run()
