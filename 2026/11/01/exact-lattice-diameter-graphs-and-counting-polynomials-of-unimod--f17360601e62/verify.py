"""Independent finite checks of an exact lattice-diameter classification.
Run with: python3 verify.py
Standard library only.
"""
from itertools import product
from collections import Counter
from math import gcd, comb
from functools import reduce
from operator import mul


def formula(lengths, t):
    assert lengths and all(isinstance(a, int) and a > 0 for a in lengths) and t >= 1
    d = len(lengths)
    a = max(lengths)
    k = lengths.count(a)
    L = t * a
    B = reduce(mul, (t * z + 1 for z in lengths if z < a), 1)
    sizes = {2 ** s: B * comb(k, s) * (L - 1) ** (k - s) for s in range(k + 1) if (L - 1) ** (k - s) > 0}
    total_segments = B * ((L + 3) ** k - (L + 1) ** k) // 2
    max_diameter = L
    borsuk = 2 ** k
    directions = (3 ** k - 1) // 2
    return max_diameter, total_segments, sizes, borsuk, directions


def brute_points(pts):
    n = len(pts)
    maxg = 0
    edges = []
    # Use all endpoint pairs and gcd, not the claimed coordinate characterization.
    for i in range(n):
        for j in range(i + 1, n):
            g = 0
            for x, y in zip(pts[i], pts[j]):
                g = gcd(g, abs(y - x))
            if g > maxg:
                maxg = g
                edges = [(i, j)]
            elif g == maxg:
                edges.append((i, j))
    adj = [set() for _ in range(n)]
    dirs = set()
    for i, j in edges:
        adj[i].add(j)
        adj[j].add(i)
        v = tuple((pts[j][r] - pts[i][r]) // maxg for r in range(len(pts[0])))
        v = v if next(c for c in v if c) > 0 else tuple(-c for c in v)
        dirs.add(v)
    unseen = set(range(n))
    cc = Counter()
    while unseen:
        seed = unseen.pop()
        component = {seed}
        queue = [seed]
        while queue:
            i = queue.pop()
            for j in adj[i] & unseen:
                unseen.remove(j)
                component.add(j)
                queue.append(j)
        # Every component must be a clique if the classification is correct.
        for i in component:
            assert len(adj[i] & component) == len(component)-1, (lengths, t, component)
        cc[len(component)] += 1
    return maxg, len(edges), cc, max(cc), len(dirs)


def brute(lengths, t):
    return brute_points(list(product(*(range(t * a + 1) for a in lengths))))


def transform_points(lengths, t, matrix, shift):
    d = len(lengths)
    assert len(matrix) == d and all(len(row) == d for row in matrix)
    return [tuple(shift[i] + sum(matrix[i][j]*p[j] for j in range(d))
                  for i in range(d))
            for p in product(*(range(t*a+1) for a in lengths))]


def main():
    checks = 0
    for d in range(1,5):
        for lengths in product(range(1,4), repeat=d):
            tmax = 2 if d <= 3 else 1
            for t in range(1, tmax+1):
                f = formula(lengths, t)
                b = brute(lengths, t)
                assert f[0] == b[0] and f[1] == b[1] and f[2] == b[2] and f[3] == b[3] and f[4] == b[4], (lengths, t, f, b)
                checks += 1
    matrices = [((1, 1), (0, 1)), ((-1, 2), (0, 1)),
                ((1, 1, 0), (0, 1, 1), (0, 0, 1)),
                ((-1, 1, 0), (0, 1, 0), (0, 0, 1))]
    for matrix in matrices:
        d = len(matrix)
        for lengths in product(range(1, 3), repeat=d):
            for t in (1, 2):
                pts = transform_points(lengths, t, matrix, tuple(7*i-2 for i in range(d)))
                f = formula(lengths, t)
                b = brute_points(pts)
                assert f[0] == b[0] and f[1] == b[1] and f[2] == b[2] and f[3] == b[3] and f[4] == b[4], (matrix, lengths, t, f, b)
                checks += 1
    print('PASS', checks, 'independent finite axis-box and unimodular-image instances (all pairs enumerated)')
    for lens in [(3,3), (3,2), (2,2,2), (3,3,1), (3,3,3), (1,2,2,2)]:
        print('example',lens,'t=2',formula(lens,2))

if __name__ == '__main__':
    main()
