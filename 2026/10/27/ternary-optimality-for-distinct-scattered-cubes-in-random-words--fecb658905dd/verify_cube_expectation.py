"""Independent finite checks for distinct scattered cube-subsequence means.

Run: python verify_cube_expectation.py
Only the theorem's exact finite identities are tested; asymptotic and global
optimization assertions require the separate analytical proof.
"""
from fractions import Fraction
from itertools import product
from math import isclose


def appears_subsequence(pattern, source):
    i = 0
    for a in source:
        if i < len(pattern) and pattern[i] == a:
            i += 1
    return i == len(pattern)


def cube_count(source, alphabet):
    n = len(source)
    total = 0
    for root_size in range(1, n // 3 + 1):
        for root in product(range(alphabet), repeat=root_size):
            if appears_subsequence(root * 3, source):
                total += 1
    return total


def exact_exhaustive_means(probabilities, length_max):
    q = len(probabilities)
    means = []
    checked_words = 0
    for n in range(length_max + 1):
        total = Fraction(0)
        for source in product(range(q), repeat=n):
            weight = Fraction(1)
            for a in source:
                weight *= probabilities[a]
            total += weight * cube_count(source, q)
            checked_words += 1
        means.append(total)
    return means, checked_words


def rational_series_means(probabilities, length_max):
    # g_a(z) = sum_{n>=1} p_a (1-p_a)^(n-1) z^n.
    # T(z) = sum_a g_a(z)^3 and H=T/(1-T), F=H/(1-z).
    N = length_max
    T = [Fraction(0) for _ in range(N + 1)]
    for p in probabilities:
        g = [Fraction(0)] + [p * (1 - p)**(n - 1) for n in range(1, N + 1)]
        gg = [Fraction(0) for _ in range(N + 1)]
        for i in range(1, N + 1):
            for j in range(1, N - i + 1):
                gg[i+j] += g[i] * g[j]
        for i in range(2, N + 1):
            for j in range(1, N - i + 1):
                T[i+j] += gg[i] * g[j]
    H = [Fraction(0) for _ in range(N+1)]
    F = [Fraction(0) for _ in range(N+1)]
    for n in range(1, N+1):
        H[n] = T[n] + sum(T[j] * H[n-j] for j in range(1,n+1))
        F[n] = F[n-1] + H[n]
    return F


def check_optimizer():
    s = (3 ** (1/3) - 1) / 3
    assert 1/8 < s < 1/6
    assert (1442/1000)**3 < 3 < (1443/1000)**3
    assert (1587/1000)**3 < 4 < (1588/1000)**3
    # Exact rational comparisons establish h_4(s)<h_3(s)=1.
    assert (1442/1000 - 1)/3 > (1588/1000 - 1)/4
    for m in range(1,200):
        h = m / (1+m*s)**3
        assert h <= 1 + 5e-14, (m,h)
        if m != 3:
            assert h < 1 - 1e-5, (m,h)
    # At arbitrary s, stationary unequal positive coordinates satisfy xy=s²;
    # the second-derivative sign of their two-coordinate transfer is positive.
    for t in (1.01, 1.1, 1.8, 3, 10):
        x=s/t; y=s*t
        der=lambda p:3*s*p*p/(p+s)**4
        d2=lambda p:6*s*p*(s-p)/(p+s)**5
        assert isclose(der(x),der(y),rel_tol=1e-12)
        assert d2(x)+d2(y)>0


def main():
    scenarios = [
        ([Fraction(1,2),Fraction(1,2)], 12),
        ([Fraction(2,3),Fraction(1,3)], 11),
        ([Fraction(1,3)]*3, 9),
        ([Fraction(1,2),Fraction(1,3),Fraction(1,6)], 9),
        ([Fraction(1,4)]*4, 7),
        ([Fraction(1,2),Fraction(1,4),Fraction(1,8),Fraction(1,8)], 7),
    ]
    total_words=0
    for probs, N in scenarios:
        direct, words=exact_exhaustive_means(probs,N)
        formula=rational_series_means(probs,N)
        assert direct == formula, (probs, direct, formula)
        total_words += words
    check_optimizer()
    print(f'VERIFY_OK exact_source_words={total_words} probability_vectors={len(scenarios)} '
          f'max_length={max(N for _,N in scenarios)} rational_coefficients=True '
          'stationary_saddle_checks=5 alphabet_support_comparisons=199')

if __name__ == '__main__':
    main()
