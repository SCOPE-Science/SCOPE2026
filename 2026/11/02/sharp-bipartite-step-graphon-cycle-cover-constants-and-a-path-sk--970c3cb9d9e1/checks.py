"""Exact finite multinomial checks for balanced path-supported step-graphons.

Run with Python 3. Standard library only. The analytic asymptotics require
separate proof; this program checks the finite cone identities and examples.
"""
from fractions import Fraction
from math import comb, factorial, sqrt, pi


def compositions(total, parts):
    if parts == 1:
        yield (total,)
    else:
        for first in range(total + 1):
            for tail in compositions(total - first, parts - 1):
                yield (first,) + tail


def multinomial(counts):
    s = sum(counts)
    v = factorial(s)
    d = 1
    for x in counts:
        d *= factorial(x)
    return v // d


def path_edge_flows(left, right):
    """Twice the successive unnormalized edge-flow coordinates."""
    n = []
    for a, b in zip(left, right):
        n.extend((a, b))
    edge = []
    previous = 0
    for j in range(len(n) - 1):
        previous = 2 * n[j] - previous
        edge.append(previous)
    return edge, previous == 2 * n[-1]


def in_edge_cone(left, right):
    if sum(left) != sum(right):
        return False
    edge, balanced = path_edge_flows(left, right)
    return balanced and all(t >= 0 for t in edge)


def prefix_nonnegative(left, right):
    x = 0
    for a, b in list(zip(left, right))[:-1]:
        x += b - a
        if x < 0:
            return False
    return True


def block_matching_possible(left, right):
    """Exact small integral max-flow test for the blown-up bipartite path."""
    r = len(left)
    source = 0
    a0 = 1
    b0 = 1 + r
    sink = 1 + 2 * r
    count = sink + 1
    cap = [[0] * count for _ in range(count)]
    for i in range(r):
        cap[source][a0 + i] = left[i]
        cap[b0 + i][sink] = right[i]
        cap[a0 + i][b0 + i] = sum(left) + 1
        if i > 0:
            cap[a0 + i][b0 + i - 1] = sum(left) + 1
    flow = 0
    while True:
        parent = [-1] * count
        parent[source] = source
        queue = [source]
        for u in queue:
            for v in range(count):
                if parent[v] < 0 and cap[u][v] > 0:
                    parent[v] = u
                    queue.append(v)
        if parent[sink] < 0:
            break
        delta = sum(left)
        v = sink
        while v != source:
            u = parent[v]
            delta = min(delta, cap[u][v])
            v = u
        v = sink
        while v != source:
            u = parent[v]
            cap[u][v] -= delta
            cap[v][u] += delta
            v = u
        flow += delta
    return flow == sum(left)


def exact_cone_probability(half_n, r):
    weighted = [(a, multinomial(a)) for a in compositions(half_n, r)]
    s_cone = s_prefix = 0
    for a, wa in weighted:
        for b, wb in weighted:
            w = wa * wb
            if prefix_nonnegative(a, b):
                s_prefix += w
            if in_edge_cone(a, b):
                s_cone += w
    total = r ** (2 * half_n)
    return Fraction(s_cone, total), Fraction(s_prefix, total)


def check():
    assertions = 0
    for r in (2, 3, 4):
        for half_n in range(0, 5):
            C = list(compositions(half_n, r))
            for a in C:
                for b in C:
                    assert in_edge_cone(a, b) == block_matching_possible(a, b)
                    assertions += 1
                    assert not in_edge_cone(a, b) or prefix_nonnegative(a, b)
                    assertions += 1
    print('Exact cone ↔ integral block matching and prefix checks:', assertions)

    print('r, half_n, P(cone | balanced), target=1/r, prefix_cone_gap, sqrt(n) P(graph-cone)')
    for r, N_values in ((2, (2, 4, 8, 15, 25)), (3, (2, 4, 8, 12, 20, 30)), (4, (2, 4, 6, 8))):
        target = 1 / r
        for h in N_values:
            p, pr = exact_cone_probability(h, r)
            assert 0 < p <= pr <= 1
            assert p.denominator > 0
            assertions += 3
            bprob = Fraction(comb(2*h, h), 2**(2*h))
            print(r, h, round(float(p), 10), round(target, 10), round(float(pr-p), 10), round(sqrt(2*h)*float(bprob*p), 10))
    assert abs(float(exact_cone_probability(30,3)[0]) - 1/3) < .07
    assertions += 1
    print('PASS:', assertions, 'exact and numerical assertions')


if __name__ == '__main__':
    check()
