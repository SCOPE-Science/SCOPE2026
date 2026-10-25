#!/usr/bin/env python3
"""Exact small-graph checks for lag-repetition variance of synchronous noisy voting."""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import floor


def transitions(adjacency, eps):
    """Full one-step probability kernel; vertices update independently."""
    n = len(adjacency)
    kernel = {}
    for before in product((0, 1), repeat=n):
        prob_ones = []
        for v, neighbors in enumerate(adjacency):
            # Cast to Fraction before multiplication, avoiding float arithmetic.
            copy_one = Fraction(sum(before[w] for w in neighbors), len(neighbors))
            prob_ones.append(eps / 2 + (1 - eps) * copy_one)
        row = {}
        for after in product((0, 1), repeat=n):
            q = Fraction(1)
            for v in range(n):
                q *= prob_ones[v] if after[v] else 1 - prob_ones[v]
            if q: row[after] = q
        assert sum(row.values()) == 1
        kernel[before] = row
    return kernel


def moments(adjacency, eps, lag, T, marked=0):
    """Exact E[count] and E[count squared] from full finite-state Markov DP."""
    kernel = transitions(adjacency, eps)
    n = len(adjacency)
    # Each entry carries (probability, unnormalized first moment, second moment).
    dp = {}
    for state in kernel:
        dp[(state, (state[marked],))] = (Fraction(1, 2**n), Fraction(0), Fraction(0))
    for time in range(1, T + lag + 1):
        out = defaultdict(lambda: (Fraction(0), Fraction(0), Fraction(0)))
        for (before, history), (prob, first, second) in dp.items():
            for after, trans in kernel[before].items():
                increment = int(time >= lag+1 and history[0] == after[marked])
                next_history = (history + (after[marked],))[-lag:]
                key = (after, next_history)
                p_old, m_old, s_old = out[key]
                out[key] = (
                    p_old + trans * prob,
                    m_old + trans * (first + increment * prob),
                    s_old + trans * (second + 2 * increment * first + increment * prob),
                )
        dp = out
        assert sum(v[0] for v in dp.values()) == 1
    mean = sum(v[1] for v in dp.values())
    second = sum(v[2] for v in dp.values())
    return mean, second - mean * mean


def bound(eps, degree, lag, T):
    """Exact local-innovation bound in the theorem."""
    times = range(lag + 1, T + 1, 2 * (lag + 1))
    return len(times) * eps**(degree + 4) / 2


def run():
    graphs = [
        ('edge', ((1,), (0,)), 0),
        ('path3_middle', ((1,), (0, 2), (1,)), 1),
        ('triangle', ((1, 2), (0, 2), (0, 1)), 0),
    ]
    count = 0
    for name, graph, marked in graphs:
        degree = len(graph[marked])
        for eps in (Fraction(1, 2), Fraction(2, 3)):
            for lag in (1, 2, 3):
                for T in (lag + 1, 2 * lag + 3, 3 * lag + 5):
                    if len(graph) == 3 and lag == 3 and T > 11:
                        continue
                    mean, variance = moments(graph, eps, lag, T, marked)
                    b = bound(eps, degree, lag, T)
                    assert variance >= b, (name, eps, lag, T, variance, b)
                    assert 0 <= mean <= T
                    assert variance > 0
                    count += 3
    print(f'PASS: {count} exact moment/variance/lower-bound assertions')


if __name__ == '__main__':
    run()
