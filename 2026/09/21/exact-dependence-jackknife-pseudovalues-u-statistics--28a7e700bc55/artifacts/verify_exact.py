from fractions import Fraction
from itertools import product
from math import comb


def pseudo_coefficients(n, r, i, subset):
    if i in subset:
        return Fraction(r, comb(n - 1, r - 1))
    return Fraction(1 - r, comb(n - 1, r))


def exact_coefficients(n, r):
    subsets = [tuple(s) for s in __import__('itertools').combinations(range(n), r)]
    d = sum((pseudo_coefficients(n, r, 0, s) ** 2 for s in subsets), Fraction(0))
    c = sum((pseudo_coefficients(n, r, 0, s) * pseudo_coefficients(n, r, 1, s) for s in subsets), Fraction(0))
    d_formula = Fraction(r * (n - 2) + 1, comb(n - 1, r))
    c_formula = -Fraction(r - 1, comb(n - 1, r))
    return d, c, d_formula, c_formula


def u_pair_product(xs):
    n = len(xs)
    return Fraction(sum(xs[i] * xs[j] for i in range(n) for j in range(i + 1, n)), comb(n, 2))


def pseudovalues_pair_product(xs):
    n = len(xs)
    full = u_pair_product(xs)
    vals = []
    for i in range(n):
        reduced = xs[:i] + xs[i + 1:]
        vals.append(n * full - (n - 1) * u_pair_product(reduced))
    return vals


def brute_rademacher(n):
    states = list(product((-1, 1), repeat=n))
    vals = [pseudovalues_pair_product(x) for x in states]
    denom = len(states)
    means = [sum((v[i] for v in vals), Fraction(0)) / denom for i in range(n)]
    var = sum(((v[0] - means[0]) ** 2 for v in vals), Fraction(0)) / denom
    cov = sum(((v[0] - means[0]) * (v[1] - means[1]) for v in vals), Fraction(0)) / denom
    var_formula = Fraction(2 * (2 * n - 3), (n - 1) * (n - 2))
    cov_formula = -Fraction(2, (n - 1) * (n - 2))
    assert var == var_formula
    assert cov == cov_formula
    assert cov / var == -Fraction(1, 2 * n - 3)
    return var, cov


def verify_bias_ratios():
    checks = 0
    for n in range(3, 31):
        for m in range(1, min(8, n - 1) + 1):
            ratios = []
            for r in range(1, m + 1):
                true_coeff = Fraction(comb(m, r) ** 2, comb(n, r))
                bias_coeff = Fraction(comb(m, r) ** 2 * (r - 1), comb(n - 1, r))
                ratio = Fraction(0) if true_coeff == 0 else bias_coeff / true_coeff
                assert ratio == Fraction(n * (r - 1), n - r)
                ratios.append(ratio)
                checks += 1
            assert ratios == sorted(ratios)
            if m >= 1:
                assert Fraction(1) + ratios[-1] == Fraction(m * (n - 1), n - m)
    return checks


def main():
    coefficient_checks = 0
    for n in range(3, 13):
        for r in range(1, min(5, n - 1) + 1):
            d, c, df, cf = exact_coefficients(n, r)
            assert d == df
            assert c == cf
            coefficient_checks += 2

    rademacher_checks = 0
    examples = []
    for n in range(3, 10):
        var, cov = brute_rademacher(n)
        examples.append((n, var, cov, cov / var))
        rademacher_checks += 3

    bias_checks = verify_bias_ratios()

    print(f"coefficient identities: {coefficient_checks} exact checks passed")
    print(f"Rademacher pair-product moments: {rademacher_checks} exact checks passed")
    print(f"jackknife-bias coefficient ratios: {bias_checks} exact checks passed")
    print("representative Rademacher results:")
    for n, var, cov, corr in examples[:4]:
        print(f"n={n}: Var={var}, Cov={cov}, Corr={corr}")


if __name__ == "__main__":
    main()
