"""Numerical reproduction of the fixed-sign adaptive edge-sampling theorem.

The proof is probabilistic and does not depend on this finite simulation.
Python 3.10+ standard library only.
"""
from math import exp, log, isclose
from random import Random


def simulate(initial_weights, friendly, gamma, delta, steps, seed):
    """Sample proportionally to weights; for unfriendly edges store log-weights."""
    rng = Random(seed)
    m = len(initial_weights)
    assert 0 < len(friendly) < m or len(friendly) == 0
    assert all(0 < v < 1 for v in initial_weights)
    counts = [0] * m
    logw = [log(v) for v in initial_weights]
    checkpoints = {1000, 10000, 100000, steps}
    out = []
    for t in range(1, steps + 1):
        greatest = max(logw)
        raw = [exp(z - greatest) for z in logw]
        total = sum(raw)
        u = rng.random() * total
        accum = 0.0
        selected = m - 1
        for i, w in enumerate(raw):
            accum += w
            if u <= accum:
                selected = i
                break
        counts[selected] += 1
        if selected in friendly:
            w = exp(logw[selected])
            w = w + gamma[selected] * (1 - w)
            # At large times, stored double precision may round to one.
            logw[selected] = log(w)
        else:
            logw[selected] += log(delta[selected])
        if t in checkpoints:
            out.append((t, tuple(counts), tuple(logw)))
    return out


def main():
    delta = [0.5, 0.35, 0.7]
    gamma = [0.3, 0.25, 0.45]
    rows = simulate([0.31, 0.43, 0.25], {0}, gamma, delta, 200000, 20261016)
    for t, n, l in rows:
        print('mixed t=', t, 'counts=', n,
              'negative_count_to_log=', tuple(round(n[i] / log(t), 4) for i in (1, 2)),
              'negative_weight_log_to_log=', tuple(round(l[i] / log(t), 4) for i in (1, 2)))
    t, n, l = rows[-1]
    # These are finite-time corroboration, intentionally very loose.
    assert n[0] > 0.99 * t
    assert 3 < n[1] < 2 * log(t) / abs(log(delta[1]))
    assert 3 < n[2] < 2 * log(t) / abs(log(delta[2]))
    # Pure discount comparator, previously treated by self-balancing samplers.
    rows2 = simulate([0.31, 0.43, 0.25], set(), gamma, delta, 100000, 20261017)
    t2, n2, l2 = rows2[-1]
    target = [1 / abs(log(d)) for d in delta]
    target = [x / sum(target) for x in target]
    print('all-discount t=', t2, 'counts=', n2, 'fractions=', tuple(round(x/t2, 6) for x in n2),
          'comparator_target=', tuple(round(x, 6) for x in target))
    assert max(abs(n2[i]/t2 - target[i]) for i in range(3)) < 0.005

    # A rigorous no-status-switch configuration for the original DW model:
    # opinions 0.2,0.3,0.9; confidence 0.25. The first edge always
    # remains receptive, the second always unreceptive under averaging.
    opinions = [0.2, 0.3, 0.9]
    c = 0.25
    for u in [0, 0.15, 0.30, 0.4, 0.5]:
        av1 = (1-u)*opinions[0] + u*opinions[1]
        av2 = u*opinions[0] + (1-u)*opinions[1]
        assert abs(av1-av2) < c
        assert abs(av2-opinions[2]) > c
    # Algebraic unit checks for selection-hazard bounds.
    wplus = 0.31
    wneg = 0.43*(0.35**5)
    probability = wneg / (wplus + wneg)
    assert wneg/(2.0) <= probability <= wneg/wplus
    print('ALL CHECKS PASSED; simulations corroborate but cannot prove almost-sure limits')

if __name__ == '__main__':
    main()
