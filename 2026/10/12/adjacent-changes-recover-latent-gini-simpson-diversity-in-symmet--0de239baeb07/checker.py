from fractions import Fraction
from itertools import product


def theory(m, alpha, n):
    A = m * alpha
    mean_d = alpha * (m - 1) / (A + 1)
    var_d = Fraction(2) * alpha * (alpha + 1) * (m - 1) / ((A + 1)**2 * (A + 2) * (A + 3))
    var_t = alpha * (alpha + 1) * (m - 1) * (
        A*A*(n - 1) + A*(7*n - 9) + 2*n*n + 2*n - 6
    ) / ((A + 1)**2 * (A + 2) * (A + 3))
    return mean_d, var_d, var_t


def enumerate_polya(m, alpha, n):
    total = Fraction(0)
    e_t = Fraction(0)
    e_t2 = Fraction(0)
    e_td = Fraction(0)
    for seq in product(range(m), repeat=n):
        counts = [0] * m
        prob = Fraction(1)
        for i, x in enumerate(seq):
            prob *= (alpha + counts[x]) / (m * alpha + i)
            counts[x] += 1
        t = sum(seq[i] != seq[i + 1] for i in range(n - 1))
        beta = [alpha + c for c in counts]
        B = m * alpha + n
        posterior_s2 = sum(b * (b + 1) for b in beta) / (B * (B + 1))
        posterior_d = 1 - posterior_s2
        total += prob
        e_t += prob * t
        e_t2 += prob * t * t
        e_td += prob * t * posterior_d
    mean_d, var_d, var_t = theory(m, alpha, n)
    assert total == 1
    assert e_t == (n - 1) * mean_d
    assert e_t2 - e_t * e_t == var_t
    assert e_td - e_t * mean_d == (n - 1) * var_d


def main():
    cases = 0
    states = 0
    for m in (2, 3, 4):
        for alpha in (Fraction(1, 2), Fraction(1), Fraction(3, 2)):
            for n in range(2, 7):
                enumerate_polya(m, alpha, n)
                cases += 1
                states += m ** n
    print("CHECK_OK")
    print(f"exact_parameter_cases={cases}")
    print(f"exact_sequence_states={states}")
    print("verified=normalization,mean_transition_count,transition_count_variance,mixed_transition_diversity_covariance")

if __name__ == "__main__":
    main()
