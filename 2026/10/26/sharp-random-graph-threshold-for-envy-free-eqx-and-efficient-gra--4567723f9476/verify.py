"""Reproducible finite cross-check of balanced-orientation cut conditions.

The analytic random-graph theorem is proved separately; finite tests do not
certify its limiting probabilities.
"""
from itertools import combinations
from random import Random
from math import log, isclose


def cuts_hold(n, edges):
    q = len(edges) // n
    for mask in range(1 << n):
        size = mask.bit_count()
        internal = sum(1 for u, v in edges if (mask >> u & 1) and (mask >> v & 1))
        incident = sum(1 for u, v in edges if (mask >> u & 1) or (mask >> v & 1))
        if internal > (q + 1) * size or incident < q * size:
            return False
    return True


def direct_orientation(n, edges):
    q = len(edges) // n
    states = {(0,) * n}
    for u, v in edges:
        nxt = set()
        for state in states:
            for w in (u, v):
                if state[w] <= q:
                    changed = list(state)
                    changed[w] += 1
                    nxt.add(tuple(changed))
        states = nxt
        if not states:
            return False
    return any(all(q <= count <= q + 1 for count in state) for state in states)


def main():
    for n in range(2, 6):
        pairs = list(combinations(range(n), 2))
        for mask in range(1 << len(pairs)):
            edges = [e for i, e in enumerate(pairs) if mask >> i & 1]
            assert cuts_hold(n, edges) == direct_orientation(n, edges)
        print(f"n={n}: {1 << len(pairs)} exhaustive labeled simple graphs passed")

    rng = Random(20261022)
    for n in (6, 7):
        pairs = list(combinations(range(n), 2))
        for _ in range(250):
            p = rng.random()
            edges = [e for e in pairs if rng.random() < p]
            assert cuts_hold(n, edges) == direct_orientation(n, edges)
        print(f"n={n}: 250 sampled labeled simple graphs passed")

    rate_half = 0.5 * (1 - log(2))
    threshold = 1 / rate_half
    assert isclose(threshold, 2 / (1 - log(2)), rel_tol=1e-15)
    assert 6.51 < threshold < 6.52
    print(f"Poisson low-degree rate I(1/2)={rate_half:.12f}; threshold={threshold:.12f}")
    print("CHECK_OK")


if __name__ == "__main__":
    main()
