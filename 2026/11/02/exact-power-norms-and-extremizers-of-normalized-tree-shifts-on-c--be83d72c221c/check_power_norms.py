"""Finite-support checks of exact Cesaro shift norms and tree-averaging identities.
No numerical experiment is used as a proof for infinite dimensions.
"""
import math
import random

ZETA2 = math.pi ** 2 / 6


def ces2_sq(sequence):
    """Exact infinite tail to floating precision for finite-support complex data."""
    a = [abs(v) for v in sequence]
    if not a:
        return 0.0
    acc = 0.0
    partial = 0.0
    for i, x in enumerate(a[:-1]):
        partial += x
        acc += (partial / (i + 1)) ** 2
    total = sum(a)
    tail = ZETA2 - sum(1.0 / j ** 2 for j in range(1, len(a)))
    return acc + total * total * tail


def constant_sq(k):
    return ZETA2 / (ZETA2 - sum(1.0 / j ** 2 for j in range(1, k + 1)))


def tree_levels(branches):
    levels = [[0]]
    for b in branches:
        levels.append(list(range(len(levels[-1]) * b)))
    return [len(x) for x in levels]


def average_step(values, branches):
    return [
        [sum(values[d + 1][i * branches[d]:(i + 1) * branches[d]]) / branches[d]
         for i in range(len(values[d]))]
        for d in range(len(values) - 1)
    ]


def tree_ces2_sq(values):
    return ces2_sq([sum(abs(z) for z in row) / len(row) for row in values])


def check():
    rng = random.Random(260921752)
    checks = 0
    for k in range(1, 7):
        target = constant_sq(k)
        spike = [0j] * k + [1 + 0j]
        assert math.isclose(ces2_sq(spike[k:]) / ces2_sq(spike), target, rel_tol=4e-13)
        checks += 1
        for _ in range(200):
            values = [complex(rng.gauss(0, 1), rng.gauss(0, 1)) for _ in range(k + 5)]
            ratio = ces2_sq(values[k:]) / ces2_sq(values)
            assert ratio <= target * (1 + 4e-12), (k, ratio, target)
            checks += 1
    for branches in ([2, 3, 1, 2, 2], [1, 1, 1, 1, 1], [3, 2, 2, 1, 2]):
        sizes = tree_levels(branches)
        for k in range(1, 5):
            target = constant_sq(k)
            # Attainment with all same-phase values at level k, nonuniform magnitudes.
            aligned = [[0j] * size for size in sizes]
            aligned[k] = [complex(0, 1 + i / (sizes[k] + 1)) for i in range(sizes[k])]
            image = aligned
            for _ in range(k):
                image = average_step(image, branches)
            assert math.isclose(tree_ces2_sq(image) / tree_ces2_sq(aligned), target, rel_tol=2e-12)
            checks += 1
            for _ in range(75):
                values = [[complex(rng.gauss(0, 1), rng.gauss(0, 1)) for __ in range(size)] for size in sizes]
                image = values
                for __ in range(k):
                    image = average_step(image, branches)
                quotient = tree_ces2_sq(image) / tree_ces2_sq(values)
                assert quotient <= target * (1 + 5e-12), (branches, k, quotient, target)
                checks += 1
    print(f"PASS: {checks} finite identities and inequalities; exact infinite tails for finite-support p=2 inputs.")


if __name__ == '__main__':
    check()
