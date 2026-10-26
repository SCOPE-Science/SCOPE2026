#!/usr/bin/env python3
"""Exact finite tests for independently masked predictable-sign random walks.

The limiting theorem uses a strong law and a martingale functional CLT; these
finite tests check algebraic identities and cannot certify infinite limits.
"""
from fractions import Fraction as Q
from itertools import product


def rule(kind, prefix, k):
    if kind == 0: return 1
    if kind == 1: return -1 if k % 2 else 1
    if kind == 2: return prefix[-1] if prefix else 1
    if kind == 3: return (-1 if sum(prefix) < 0 else 1)
    if kind == 4: return (-1 if sum(v < 0 for v in prefix) % 2 else 1)
    if kind == 5: return (-1 if (sum(prefix) + k) % 4 == 0 else 1)
    raise ValueError(kind)


def mask_law(mask, means):
    probability = Q(1)
    for s, m in zip(mask, means):
        probability *= (1 + s * m) / 2
    return probability


def run():
    checks = 0
    mean_patterns = [
        [Q(0), Q(0), Q(0), Q(0), Q(0)],
        [Q(1, 2), Q(-1, 3), Q(1, 4), Q(0), Q(-1, 2)],
        [Q(-1), Q(1), Q(-1), Q(1), Q(0)],
        [Q(1, 3), Q(1, 3), Q(1, 3), Q(1, 3), Q(1, 3)],
    ]
    for n in (1, 2, 3, 4, 5):
        paths = list(product((-1, 1), repeat=n))
        masks = list(product((-1, 1), repeat=n))
        for means5 in mean_patterns:
            means = means5[:n]
            probs = [mask_law(mask, means) for mask in masks]
            assert sum(probs) == 1
            for kind in range(6):
                cross = Q(0)
                for path in paths:
                    predictable = [rule(kind, path[:k], k+1) for k in range(n)]
                    signed_bias = sum(means[k]*predictable[k] for k in range(n))
                    centered_second = Q(0)
                    centered_mean = Q(0)
                    for mask, probability in zip(masks, probs):
                        corr = sum((mask[k]-means[k])*predictable[k] for k in range(n))
                        centered_mean += probability*corr
                        centered_second += probability*corr*corr
                    assert centered_mean == 0
                    assert centered_second == sum(1-m*m for m in means)
                    checks += 2
                    # Verify the same input path drives both increments;
                    # cross-mean is a sum of predictable mask coefficients.
                    for mask, probability in zip(masks, probs):
                        cross += probability*sum(mask[k]*predictable[k] for k in range(n))/len(paths)
                average_predictable = [sum(rule(kind, path[:k], k+1) for path in paths)/Q(len(paths)) for k in range(n)]
                assert cross == sum(means[k]*average_predictable[k] for k in range(n))
                checks += 1
    # Finite-horizon obstruction: taking deterministic signs of biases
    # maximizes the mean cross bracket among all deterministic sign choices.
    for n in range(1, 6):
        for means5 in mean_patterns:
            means = means5[:n]
            desired = sum(abs(m) for m in means)
            assert desired == max(sum(m*sign[k] for k,m in enumerate(means))
                                  for sign in product((-1,1), repeat=n))
            checks += 1
    print(f"PASS: {checks} exact rational identities and finite-horizon extremal checks")


if __name__ == '__main__':
    run()
