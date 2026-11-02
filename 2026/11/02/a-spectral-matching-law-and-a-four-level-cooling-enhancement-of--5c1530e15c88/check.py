"""Standalone finite tests for a threshold-work theorem; Python 3 stdlib only.

This is a finite test, not a proof of the dimension-uniform statements.
"""
from fractions import Fraction
from itertools import permutations
from random import Random
from math import exp


def greedy(E, w):
    # E strictly increasing, w positive; destinations indexed from zero.
    chosen = []
    for i, x in enumerate(E):
        k = sum(y <= x - w for y in E)
        if k > len(chosen):
            chosen.append(i)
    return chosen


def brute(E, w, beta_weight=Fraction(1, 2)):
    # For integral spectra, assign p_i proportional to beta_weight ** E_i.
    d = len(E)
    weights = [beta_weight ** int(x) for x in E]
    Z = sum(weights)
    candidates = []
    for pi in permutations(range(d)):
        val = sum(weights[i] for i in range(d) if E[i] - E[pi[i]] >= w)
        candidates.append((val / Z, pi))
    return max(x[0] for x in candidates), candidates


def exact_exhaustive():
    rng = Random(20261030)
    count = 0
    for d in range(2, 7):
        for trial in range(65):
            E = [0]
            for _ in range(d-1):
                E.append(E[-1] + rng.randrange(1, 8))
            # Include strict and equality-at-gap thresholds.
            gaps = sorted(set(E[i] - E[j] for i in range(d) for j in range(i)))
            w = Fraction(rng.choice(gaps)) if trial % 2 == 0 else Fraction(rng.randrange(1, 3 * E[-1] + 2), 2)
            G = greedy(E, w)
            pred = sum(Fraction(1, 2)**x for i, x in enumerate(E) if i in G) / sum(Fraction(1, 2)**x for x in E)
            opt, candidates = brute(E, w)
            assert pred == opt, (d, E, w, G, pred, opt)
            # At positive beta, a permutation optimizer must have precisely the greedy winners.
            for score, pi in candidates:
                if score == opt:
                    winners = [i for i in range(d) if E[i] - E[pi[i]] >= w]
                    assert winners == G, (E, w, G, winners)
            count += 1
    return count


def four_level_test():
    E = (Fraction(0), Fraction(2), Fraction(19, 5), Fraction(39, 10))
    w = Fraction(39, 20)
    assert greedy(E, w) == [1]
    mean = sum(E)/4
    assert mean == Fraction(97, 40)
    assert (mean-E[1])/4 == Fraction(17, 160)
    # Passive mean is never positive, even at the maximizer of success.
    for beta in (0.01, 0.1, 0.1597406884685845, 0.25, 1.0):
        p = [exp(-beta*float(x)) for x in E]
        P = [v/sum(p) for v in p]
        success = P[1]
        # Construct U as the transposition 0<->1, leaving others fixed.
        average_work = P[0]*(float(E[0])-float(E[1]))+P[1]*(float(E[1])-float(E[0]))
        assert average_work < 0
        assert abs(success - exp(-beta*2)/sum(p)) < 1e-14
    beta_star = 0.1597406884685845
    shift = sum((float(e)-2)*exp(-beta_star*float(e)) for e in E)
    assert abs(shift) < 1e-12
    f = lambda beta: exp(-2*beta)/sum(exp(-float(e)*beta) for e in E)
    assert f(beta_star) > f(0)
    assert f(beta_star) > f(beta_star + 0.001)
    assert f(beta_star) > f(beta_star - 0.001)
    assert abs(f(beta_star)-0.25874895776352375)<1e-12


if __name__ == '__main__':
    count = exact_exhaustive()
    four_level_test()
    print(f'PASS: {count} exact finite-spectrum global optimizations and winner-set checks; four-level exact derivative and numeric peak tests.')
