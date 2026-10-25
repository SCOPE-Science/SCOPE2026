"""Exact finite-instance corroboration for the paired-representative metric theorem.

This is supplementary testing; the proof covers all finite metric spaces.
Usage: python3 verify.py
"""
from itertools import combinations, product
from fractions import Fraction

checks = 0

def audit(points, metric):
    global checks
    n = len(points)
    assert n % 2 == 0 and n >= 4
    k = n // 2
    distance = [[metric(points[i], points[j]) for j in range(n)] for i in range(n)]
    for i in range(n):
        assert distance[i][i] == 0
        for j in range(n):
            assert distance[i][j] == distance[j][i] >= 0
            for t in range(n):
                assert distance[i][j] <= distance[i][t] + distance[t][j]
    centrality = [sum(distance[i]) for i in range(n)]
    costs = []
    for subset in combinations(range(n), k):
        costs.append((sum(centrality[i] for i in subset), subset))
    best = min(costs)[0]
    for cost, subset in costs:
        assert k * cost <= (3 * k - 2) * best
        alt = tuple(i for i in range(n) if i not in subset)
        intra_a = sum(distance[i][j] for i, j in combinations(subset, 2))
        intra_b = sum(distance[i][j] for i, j in combinations(alt, 2))
        cross = sum(distance[i][j] for i in subset for j in alt)
        assert k * intra_a <= (k - 1) * cross
        assert cost == 2 * intra_a + cross
        assert sum(centrality[i] for i in alt) == 2 * intra_b + cross
        checks += 1
    # In the paired model, each of k fixed pairs provides one of its two indices.
    for assignment in product((0, 1), repeat=k):
        selected = tuple(2 * i + assignment[i] for i in range(k))
        assert k * sum(centrality[i] for i in selected) <= (3 * k - 2) * best
        checks += 1

for k in (2, 3, 4):
    # All small nonnegative integral line profiles, allowing repeated locations.
    for coords in product(range(3), repeat=2 * k):
        audit(coords, lambda a, b: abs(a - b))

for k in (2, 3):
    # Complete 4-point square metrics, including repeated agent locations.
    square = ((0, 0), (0, 1), (1, 0), (1, 1))
    for labels in product(range(4), repeat=2 * k):
        pts = [square[z] for z in labels]
        audit(pts, lambda a, b: abs(a[0]-b[0])+abs(a[1]-b[1]))

# Sharp two-location construction for each k, with a fixed local rule selecting 1.
for k in range(2, 101):
    x = [1, 0] + [0] * (2 * k - 2)
    d = lambda a, b: abs(a-b)
    c = [sum(d(a, b) for b in x) for a in x]
    selected = [0] + list(range(2, 2*k, 2))
    opt = sum(sorted(c)[:k]); got = sum(c[i] for i in selected)
    assert got == 3 * k - 2 and opt == k
    assert Fraction(got, opt) == Fraction(3*k-2,k)
    checks += 1
print('PASS:', checks, 'exact combinatorial and metric assertions')
