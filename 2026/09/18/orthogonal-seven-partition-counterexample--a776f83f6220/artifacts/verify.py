#!/usr/bin/env python3
"""Exact certificate for a 70-point orthogonal 7-partition counterexample."""

from collections import Counter
from functools import cmp_to_key
from itertools import combinations
from math import gcd

K = 7
REPS = [
    (9819, -2040),
    (11243, 4733),
    (14190, 7834),
    (11346, 2091),
    (12771, 7469),
    (11823, 5289),
    (12740, 7482),
    (14801, 23200),
    (6088, 7088),
    (21833, 30621),
    (5789, 7430),
    (-555, 12635),
    (7842, 15683),
    (1395, 11274),
    (5735, 7425),
    (5790, 5801),
    (-1581, 7384),
    (-86, 11967),
    (5479, 6853),
    (-19959, 27734),
    (-9521, 2933),
    (-20592, 27518),
    (-12753, 10971),
    (-9879, 1919),
    (-22191, 22391),
    (-26821, 30017),
    (-6656, 5663),
    (-8957, 3615),
    (-28523, 33939),
    (-4555, 6755),
    (-9719, 2427),
    (-9202, 3386),
    (-3277, 7149),
    (-9554, 2691),
    (-8713, 3961),
]
P = REPS + [(-x, -y) for x, y in REPS]
N = len(P)
M = N // 2


def dot(p, v):
    return p[0] * v[0] + p[1] * v[1]


def canonical_ray(v):
    x, y = v
    g = gcd(abs(x), abs(y))
    if g == 0:
        raise ValueError("zero vector has no ray")
    x //= g
    y //= g
    if y < 0 or (y == 0 and x < 0):
        x, y = -x, -y
    return x, y


def ray_cmp(a, b):
    cross = a[0] * b[1] - a[1] * b[0]
    if cross > 0:
        return -1
    if cross < 0:
        return 1
    return 0


def top_sets(values, r):
    threshold = sorted(values, reverse=True)[r - 1]
    mandatory = {i for i, value in enumerate(values) if value > threshold}
    tied = [i for i, value in enumerate(values) if value == threshold]
    need = r - len(mandatory)
    return [mandatory | set(choice) for choice in combinations(tied, need)]


def unique_top(values, r):
    order = sorted(range(N), key=lambda i: values[i], reverse=True)
    # Open-chamber samples have no projection ties.
    assert values[order[r - 1]] > values[order[r]]
    return set(order[:r])


def q_open(n):
    u = (-n[1], n[0])
    a = unique_top([dot(p, u) for p in P], M)
    b = unique_top([dot(p, n) for p in P], 2 * K)
    return len(a & b)


def no_three_collinear():
    for i, j, k in combinations(range(N), 3):
        xi, yi = P[i]
        xj, yj = P[j]
        xk, yk = P[k]
        if (xj - xi) * (yk - yi) == (yj - yi) * (xk - xi):
            return False
    return True


assert N == 70
assert len(set(P)) == N
assert no_three_collinear()

# Projection orders can change only when n is parallel or perpendicular to a
# point difference.  Central symmetry makes n and -n equivalent, so projective
# directions (one half-turn) suffice.
rays = set()
for i in range(N):
    xi, yi = P[i]
    for j in range(i):
        xj, yj = P[j]
        d = (xi - xj, yi - yj)
        rays.add(canonical_ray(d))
        rays.add(canonical_ray((-d[1], d[0])))
rays = sorted(rays, key=cmp_to_key(ray_cmp))

open_counts = Counter()
for i, a in enumerate(rays):
    if i + 1 < len(rays):
        b = rays[i + 1]
        sample = (a[0] + b[0], a[1] + b[1])
    else:
        # The last projective chamber ends at the antipode of the first ray.
        first = rays[0]
        sample = (a[0] - first[0], a[1] - first[1])
    open_counts[q_open(sample)] += 1

critical_q_sets = Counter()
max_cutoff_tie = 0
for n in rays:
    u = (-n[1], n[0])
    values_a = [dot(p, u) for p in P]
    values_b = [dot(p, n) for p in P]

    threshold_a = sorted(values_a, reverse=True)[M - 1]
    threshold_b = sorted(values_b, reverse=True)[2 * K - 1]
    max_cutoff_tie = max(
        max_cutoff_tie,
        sum(v == threshold_a for v in values_a),
        sum(v == threshold_b for v in values_b),
    )

    a_choices = top_sets(values_a, M)
    b_choices = top_sets(values_b, 2 * K)
    q_values = tuple(sorted({len(a & b) for a in a_choices for b in b_choices}))
    critical_q_sets[q_values] += 1

assert K not in open_counts
assert all(K not in q_values for q_values in critical_q_sets)

print(f"points={N}")
print(f"representatives={len(REPS)}")
print(f"critical_projective_rays={len(rays)}")
print(f"open_projective_chambers={sum(open_counts.values())}")
print(f"open_q_counts={dict(sorted(open_counts.items()))}")
print(
    "critical_q_sets={"
    + ", ".join(f"{key}: {critical_q_sets[key]}" for key in sorted(critical_q_sets))
    + "}"
)
print(f"max_cutoff_tie={max_cutoff_tie}")
print("distinct_points=True")
print("no_three_collinear=True")
print("no_weak_orthogonal_7_partition=True")
