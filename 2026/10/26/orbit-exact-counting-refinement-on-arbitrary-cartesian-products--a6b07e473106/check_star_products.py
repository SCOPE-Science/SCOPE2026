"""Direct finite checks for orbit-exact colour refinement on Cartesian star products.
All factors K_{1,p}; centre = 0, leaves = 1,...,p. Standard library only.
"""
from itertools import combinations_with_replacement, product
from collections import Counter, defaultdict
from math import comb, factorial


def graph(ps):
    vertices = list(product(*(range(p + 1) for p in ps)))
    adj = {}
    for v in vertices:
        neigh = []
        for i, p in enumerate(ps):
            for val in (range(1, p + 1) if v[i] == 0 else (0,)):
                neigh.append(v[:i] + (val,) + v[i + 1:])
        adj[v] = neigh
    return vertices, adj


def refine(vertices, adj):
    colors = {v: 0 for v in vertices}
    snapshots = [colors]
    while True:
        signatures = {
            v: (colors[v], tuple(sorted(Counter(colors[w] for w in adj[v]).items())))
            for v in vertices
        }
        palette = {s: i for i, s in enumerate(sorted(set(signatures.values())))}
        new = {v: palette[signatures[v]] for v in vertices}
        snapshots.append(new)
        if len(set(new.values())) == len(set(colors.values())):
            return snapshots
        colors = new


def orbit(ps, v):
    # Factors of unequal leaf counts cannot be permuted; equal factors can.
    return tuple((p, sum(x != 0 and q == p for q, x in zip(ps, v))) for p in sorted(set(ps)))


def orbit_size(ps, o):
    d = Counter(ps)
    z = 1
    for p, j in o:
        z *= comb(d[p], j) * p**j
    return z


def check_one(ps):
    vertices, adj = graph(ps)
    snapshots = refine(vertices, adj)
    colors = snapshots[-1]
    by_color = defaultdict(set)
    by_orbit = defaultdict(set)
    for v in vertices:
        by_color[colors[v]].add(orbit(ps, v))
        by_orbit[orbit(ps, v)].add(colors[v])
    assert all(len(x) == 1 for x in by_color.values())
    assert all(len(x) == 1 for x in by_orbit.values())
    count_formula = 1
    for m in Counter(ps).values():
        count_formula *= m + 1
    assert len(by_color) == count_formula
    for o in by_orbit:
        actual = sum(orbit(ps, v) == o for v in vertices)
        assert actual == orbit_size(ps, o)
    assert len(snapshots) - 2 <= 3 * len(ps) + 1
    return len(vertices), len(by_color), len(snapshots) - 2


def check_walk_factor(ps):
    # Exact integer root-to-vertex walk coefficients for length <= 9.
    vertices, adj = graph(ps)
    root = tuple(0 for _ in ps)
    W = {v: int(v == root) for v in vertices}
    coeffs = {v: [W[v]] for v in vertices}
    for t in range(1, 10):
        W = {v: sum(W[u] for u in adj[v]) for v in vertices}
        for v in vertices:
            coeffs[v].append(W[v])
    # Factorial denominators: e^{t A_i}_{0,0}=sum_j p^j t^{2j}/(2j)!
    # e^{t A_i}_{0,leaf}=sum_j p^j t^{2j+1}/(2j+1)!
    polys = []
    for p in ps:
        cc = [0] * 10
        ll = [0] * 10
        for j in range(5):
            if 2*j <= 9: cc[2*j] = p**j
            if 2*j+1 <= 9: ll[2*j+1] = p**j
        polys.append((cc,ll))
    from fractions import Fraction
    for v in vertices:
        prod = [Fraction(1)] + [Fraction(0)] * 9
        for (cc,ll),x in zip(polys,v):
            a = cc if x == 0 else ll
            new = [Fraction(0)] * 10
            for i in range(10):
                for j in range(10-i):
                    new[i+j] += prod[i] * Fraction(a[j], factorial(j))
            prod = new
        assert [int(factorial(j)*prod[j]) for j in range(10)] == coeffs[v]
    return len(vertices)


def main():
    n = 0
    for k in range(1,5):
        for ps in combinations_with_replacement(range(2, 6), k):
            check_one(ps)
            n += 1
    extra = [(2,2,2,2,2), (2,2,3,3,4), (2,3,4,5), (2,2,2,3,4), (3,3,3,3), (2,5,5)]
    for ps in extra:
        check_one(ps); n += 1
    wc = 0
    for ps in [(2,), (3,3), (2,3), (2,3,4), (3,3,3), (2,2,4), (2,2,3,3)]:
        wc += check_walk_factor(ps)
    print('ORBIT_PARTITION_CHECKS', n)
    print('EXACT_WALK_SERIES_VERTICES', wc)
    print('MAX_FACTOR_COUNT', 5)
    print('ALL_TESTS_PASS')


if __name__ == '__main__':
    main()
