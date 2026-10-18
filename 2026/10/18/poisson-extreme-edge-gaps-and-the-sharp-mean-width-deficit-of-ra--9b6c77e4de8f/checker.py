"""Exact finite support-loss checks and reproducible limit-model simulations.

Only scientific computations are performed. Python 3.10+; standard library only.
The exact tests do not establish asymptotic theorems.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb, log
import random


def all_edges(n):
    return list(combinations(range(n), 2))


def loss(scores, selected_edges):
    r = max(scores) - min(scores)
    return r - max([F(0)] + [abs(scores[i] - scores[j]) for i, j in selected_edges])


def predicted_loss_mean(scores, p):
    """Integrate the exact conditional tail (1-p)^N(t), with rational input."""
    r = max(scores) - min(scores)
    deficits = sorted(r - abs(scores[i] - scores[j]) for i, j in all_edges(len(scores)))
    q = 1 - p
    knots = sorted(set([F(0), r] + deficits))
    total = F(0)
    for lo, hi in zip(knots[:-1], knots[1:]):
        count = sum(d <= lo for d in deficits)
        total += (hi - lo) * q ** count
    return total


def check_exact():
    p = F(2, 5)
    cases = 0
    graphs = 0
    scoresets = [
        [F(-3), F(-1, 2), F(1)],
        [F(-3), F(-1, 2), F(1), F(4)],
        [F(-7, 3), F(-1), F(0), F(3, 2), F(5)],
    ]
    for z in scoresets:
        n = len(z)
        edges = all_edges(n)
        E = len(edges)
        weighted_mean = F(0)
        probability_zero = F(0)
        for mask in range(1 << E):
            chosen = [edge for i, edge in enumerate(edges) if mask & (1 << i)]
            number = mask.bit_count()
            weight = p ** number * (1 - p) ** (E - number)
            this_loss = loss(z, chosen)
            weighted_mean += weight * this_loss
            if this_loss == 0:
                probability_zero += weight
            graphs += 1
        assert probability_zero == p, (n, probability_zero)
        assert weighted_mean == predicted_loss_mean(z, p), n
        cases += 1
    print(f'EXACT_PASS: {cases} score sets, {graphs} edge-labeled graphs; '
          'conditional tail, zero atom, and rational conditional means')


def simulate_limit(p, trials=6000, k=45, seed=1729):
    """Finite truncation of the PPP Bernoulli bipartite model, for diagnostics."""
    rng = random.Random(seed)
    samples = []
    no_contact = 0
    for _ in range(trials):
        y, v = [], []
        sy = sv = 0.0
        for i in range(k):
            sy += rng.expovariate(1)
            sv += rng.expovariate(1)
            y.append(log(sy))
            v.append(log(sv))
        a = [u - y[0] for u in y]
        b = [w - v[0] for w in v]
        best = float('inf')
        contact = False
        for i in range(k):
            if a[i] >= best:
                break
            for j in range(k):
                candidate = a[i] + b[j]
                if candidate >= best:
                    break
                if rng.random() < p:
                    best = candidate
                    if i == j == 0:
                        contact = True
                    break
        if best == float('inf'):
            raise AssertionError('PPP truncation did not find an edge')
        samples.append(best)
        no_contact += contact
    mean = sum(samples) / trials
    mass0 = no_contact / trials
    assert abs(mass0 - p) < 0.035, (p, mass0)
    assert 0 < mean < -log(p) * 1.30, (p, mean)
    print(f'PPP_DIAGNOSTIC: p={p}, trials={trials}, truncation={k}, '
          f'mean_gap={mean:.5f}, mass_at_zero={mass0:.5f} (target={p})')


if __name__ == '__main__':
    check_exact()
    for probability in (0.2, 0.5, 0.8, 0.95):
        simulate_limit(probability)
