"""Supplementary finite checks for ultrametric dual bounded-Lipschitz norms.

Requires Python 3, NumPy, and SciPy.  Not a replacement for the proof.
Run: python CHECKER.py
"""

import random
import numpy as np
from scipy.optimize import linprog


def random_hierarchy(rng, n):
    nodes = {i: (0.0, [], [i]) for i in range(n)}
    active = list(range(n))
    next_id, height = n, 0
    while len(active) > 1:
        k = rng.randint(2, min(4, len(active)))
        chosen = rng.sample(active, k)
        active = [j for j in active if j not in chosen]
        height += rng.randint(1, 4)
        leaves = [a for j in chosen for a in nodes[j][2]]
        nodes[next_id] = (float(height), chosen, leaves)
        active.append(next_id)
        next_id += 1
    return nodes, active[0]


def hierarchy_value(nodes, root, mass):
    assert sum(mass) == 0
    masses = {i: sum(mass[k] for k in v[2]) for i, v in nodes.items()}
    levels = sorted({h for h, _, _ in nodes.values() if h > 0})
    evaluations = []
    for r in levels:
        b = sum((min(h, r) - min(nodes[child][0], r)) * abs(masses[child])
                for h, children, _ in nodes.values() for child in children)
        evaluations.append(b / (2 + r))
    return max(evaluations) if evaluations else 0.0


def independent_linear_program(nodes, mass):
    n = len(mass)
    distances = np.zeros((n, n))
    for height, children, _ in nodes.values():
        for ia, a in enumerate(children):
            for b in children[ia + 1:]:
                for x in nodes[a][2]:
                    for y in nodes[b][2]:
                        distances[x, y] = distances[y, x] = height
    rows, bounds = [], []
    for i in range(n):
        for sign in (-1, 1):
            row = np.zeros(n + 2)
            row[i], row[n] = sign, -1
            rows.append(row)
            bounds.append(0)
    for i in range(n):
        for j in range(i):
            for sign in (-1, 1):
                row = np.zeros(n + 2)
                row[i], row[j], row[n + 1] = sign, -sign, -distances[i, j]
                rows.append(row)
                bounds.append(0)
    row = np.zeros(n + 2)
    row[n] = row[n + 1] = 1
    rows.append(row)
    bounds.append(1)
    objective = [-float(z) for z in mass] + [0.0, 0.0]
    result = linprog(objective, A_ub=rows, b_ub=bounds,
                     bounds=[(None, None)] * n + [(0, None), (0, None)],
                     method="highs")
    assert result.success, result.message
    return -result.fun


def two_cluster_value(a, b, mass):
    half_variation = sum(abs(v) for v in mass) / 2
    imbalance = abs(sum(mass[:2]))
    return max(2 * a * half_variation / (2 + a),
               2 * (a * half_variation + (b - a) * imbalance) / (2 + b))


def run_checks():
    rng = random.Random(1643)
    random_count = 180
    for k in range(random_count):
        n = rng.randrange(2, 13)
        nodes, root = random_hierarchy(rng, n)
        mass = [rng.randint(-6, 6) for _ in range(n - 1)]
        mass.append(-sum(mass))
        obtained = hierarchy_value(nodes, root, mass)
        independently = independent_linear_program(nodes, mass)
        assert abs(obtained - independently) <= 4e-8 * (1 + independently), (k, obtained, independently)

    threshold_count = 90
    for k in range(threshold_count):
        a = rng.randint(1, 8)
        b = a + rng.randint(1, 8)
        mass = [rng.randint(-10, 10) for _ in range(3)]
        mass.append(-sum(mass))
        nodes = {i: (0., [], [i]) for i in range(4)}
        nodes[4] = (float(a), [0, 1], [0, 1])
        nodes[5] = (float(a), [2, 3], [2, 3])
        nodes[6] = (float(b), [4, 5], [0, 1, 2, 3])
        obtained = hierarchy_value(nodes, 6, mass)
        explicit = two_cluster_value(a, b, mass)
        lp_value = independent_linear_program(nodes, mass)
        assert abs(obtained - explicit) < 1e-9 and abs(obtained - lp_value) < 1e-8

    for n in range(2, 13):
        nodes, root = random_hierarchy(rng, n)
        height = nodes[root][0]
        mass = [0] * n
        mass[0], mass[-1] = 1, -1
        pair_distance = next(h for h, kids, leaves in nodes.values()
                             if 0 in leaves and n - 1 in leaves and
                             not any(0 in nodes[c][2] and n - 1 in nodes[c][2] for c in kids))
        assert abs(hierarchy_value(nodes, root, mass) - 2 * pair_distance / (2 + pair_distance)) < 1e-10

    print(f"PASS: {random_count} random hierarchical LP comparisons; "
          f"{threshold_count} two-cluster algebra/LP comparisons; "
          "11 two-point formula comparisons.  All are finite checks only.")


if __name__ == "__main__":
    run_checks()
