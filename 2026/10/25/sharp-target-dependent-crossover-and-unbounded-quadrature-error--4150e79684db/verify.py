#!/usr/bin/env python3
"""Exact finite checks for a two-level diagonal-kernel quadrature comparison.

This verifier is supporting evidence only: the all-parameter inequality and
asymptotic statements are proved in the accompanying mathematical text.
"""
from fractions import Fraction as F
from itertools import combinations
from math import factorial


def rp_subset_probabilities(m, k, L):
    # Summation over all possible distinct *ordered* pivot paths.
    # On a diagonal matrix the residual entries equal initial entries
    # until a coordinate is selected, at which point they vanish.
    weights = [L] + [F(1)] * m
    result = {}

    def branch(selected, mass):
        if len(selected) == k:
            subset = tuple(sorted(selected))
            result[subset] = result.get(subset, F(0)) + mass
            return
        denominator = sum(weights[i] for i in range(m + 1) if i not in selected)
        for i in range(m + 1):
            if i not in selected:
                branch(selected + (i,), mass * weights[i] / denominator)

    branch((), F(1))
    return result


def dpp_subset_probabilities(m, k, L):
    subsets = list(combinations(range(m + 1), k))
    determinants = [L if 0 in s else F(1) for s in subsets]
    z = sum(determinants)
    return dict(zip(subsets, (v / z for v in determinants)))


def predicted_p(m, k, L):
    rp = F(1)
    for j in range(k):
        rp *= F(m - j, 1) / (L + m - j)
    dpp = F(m - k + 1, 1) / (k * L + m - k + 1)
    return rp, dpp


def exact_quadrature_error(S, g, L):
    return sum((L if i == 0 else F(1)) * (value * value)
               for i, value in enumerate(g) if i not in S)


def model_risk(m, k, L, g, p):
    tail_sq = sum(a * a for a in g[1:])
    return L * g[0] ** 2 * p + F(m - k + 1, 1) * tail_sq / m - p * tail_sq / m


def main():
    checks = 0
    for m in range(2, 6):
        for k in range(2, m + 1):
            for L in (F(1), F(3, 2), F(2), F(5), F(20)):
                rp = rp_subset_probabilities(m, k, L)
                dpp = dpp_subset_probabilities(m, k, L)
                assert sum(rp.values()) == sum(dpp.values()) == 1
                assert set(rp) == set(dpp)
                p_r, p_d = predicted_p(m, k, L)
                assert sum(prob for s, prob in rp.items() if 0 not in s) == p_r
                assert sum(prob for s, prob in dpp.items() if 0 not in s) == p_d
                if L > 1:
                    assert 0 < p_r < p_d
                else:
                    assert p_r == p_d
                vectors = [tuple([F(1)] + [F(0)] * m),
                           tuple([F(0), F(1)] + [F(0)] * (m - 1)),
                           tuple(F((-1) ** j * (j + 1), j + 2)
                                 for j in range(m + 1))]
                for g in vectors:
                    e_r = sum(prob * exact_quadrature_error(s, g, L)
                              for s, prob in rp.items())
                    e_d = sum(prob * exact_quadrature_error(s, g, L)
                              for s, prob in dpp.items())
                    assert e_r == model_risk(m, k, L, g, p_r)
                    assert e_d == model_risk(m, k, L, g, p_d)
                    q = sum(a*a for a in g[1:])
                    assert e_d - e_r == (p_d - p_r) * (L*g[0]*g[0] - q/m)
                    checks += 1

    # Explicit two-pivot witness: m=3, k=2.
    for L in (F(3), F(100), F(10**6)):
        p_r, p_d = predicted_p(3, 2, L)
        assert p_r == F(6) / ((L+3)*(L+2))
        assert p_d == F(1) / (L+1)
        assert L*p_d > L*p_r
    # The coefficient in P_D/P_R ~ L^(k-1)/[k (m)_(k-1)]
    for m in range(2, 6):
        for k in range(2, m+1):
            L = F(10**7)
            p_r, p_d = predicted_p(m, k, L)
            falling = factorial(m) // factorial(m-k+1)
            normalized = (p_d / p_r) / L**(k-1)
            limit = F(1, k * falling)
            assert abs(normalized - limit) < F(1, 10**5)
    print('VERIFY_OK: exact subset enumeration, optimal quadrature risks, crossover and high-contrast limit;', checks, 'integrand checks')


if __name__ == '__main__':
    main()
