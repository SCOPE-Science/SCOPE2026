#!/usr/bin/env python3
"""Exact finite-network-flow checks for logistic patch corridor attainability.

Pure Python 3 standard library; deterministic, no external datasets.
"""
from fractions import Fraction as Q
from random import Random


def maxflow_exact(n, xs, g, arcs):
    """Use Edmonds-Karp with Fraction capacities; return whether all sources saturate."""
    total = sum((z for z in g if z > 0), Q(0))
    V = n + 2
    source, sink = n, n + 1
    cap = [[Q(0) for _ in range(V)] for _ in range(V)]
    for i, z in enumerate(g):
        if z > 0: cap[source][i] = z
        if z < 0: cap[i][sink] = -z
    for a, b in arcs:
        assert xs[a] > xs[b]
        cap[a][b] = total
    flowed = Q(0)
    while True:
        prev = [-1] * V
        prev[source] = source
        queue = [source]
        for u in queue:
            for v in range(V):
                if prev[v] == -1 and cap[u][v] > 0:
                    prev[v] = u
                    queue.append(v)
        if prev[sink] < 0: break
        v, aug = sink, total
        while v != source:
            u = prev[v]
            aug = min(aug, cap[u][v])
            v = u
        v = sink
        while v != source:
            u = prev[v]
            cap[u][v] -= aug
            cap[v][u] += aug
            v = u
        flowed += aug
    return flowed == total


def cuts_pass(n, g, arcs):
    return all(sum((g[i] for i in range(n) if (m >> i) & 1), Q(0)) <= 0
       for m in range(1 << n)
       if all(not ((m >> i) & 1 and not ((m >> j) & 1)) for i, j in arcs))


def exact_witnesses():
    r = (Q(1), Q(2), Q(3))
    k = (Q(1), Q(2), Q(90, 11))
    R = sum((a*b for a, b in zip(r, k)), Q(0))
    S = sum((b/a for a, b in zip(r, k)), Q(0))
    c = Q(5, 2)
    assert R == Q(325, 11) and S == Q(52, 11) and c*c == R/S
    x = [b/2*(1+c/a) for a, b in zip(r, k)]
    g = [a*t*(1-t/b) for a, b, t in zip(r, k, x)]
    assert x == [Q(7, 4), Q(9, 4), Q(15, 2)]
    assert g == [Q(-21, 16), Q(-9, 16), Q(15, 8)]
    assert sum(x) == Q(23, 2)
    conductance = {(0, 1): Q(21, 8), (1, 2): Q(5, 14)}
    for i in range(3):
        assert g[i] + sum((d*(x[j]-x[i]) for (u,v),d in conductance.items()
                            for j in ([v] if u == i else [u] if v == i else [])), Q(0)) == 0
    assert cuts_pass(3, g, [(1,0), (2,1)])
    assert maxflow_exact(3, x, g, [(1,0), (2,1)])
    assert R/S == c*c
    deficit_at_k = sum((a/b*(b-t)**2 for a,b,t in zip(r,k,x)), Q(0))
    assert deficit_at_k == c*(sum(x)-sum(k))
    # Impossibility example: unique minimum target is vertex index 1.
    r2 = (Q(1), Q(2), Q(3)); k2 = (Q(3),Q(1),Q(2))
    R2 = sum((a*b for a,b in zip(r2,k2)),Q(0))
    S2 = sum((b/a for a,b in zip(r2,k2)),Q(0))
    assert R2 == 11 and S2 == Q(25,6) and R2/S2 == Q(66,25)
    # c2=sqrt(66)/5 satisfies 8/5<c2<5/3.
    assert Q(64,25)<R2/S2<Q(25,9)
    assert Q(1,4)*(2-R2/S2/2) == Q(17,100)  # g_2^* > 0
    # This is the unique minimum target, so {2} has no outward edge.
    return True


def random_cut_consistency(trials=600):
    rnd = Random(4411)
    for rep in range(trials):
        n = rnd.randint(2,7)
        x = [Q(rnd.randint(1,6)) for _ in range(n)]
        g = [Q(rnd.randint(-4,4)) for _ in range(n-1)]
        g.append(-sum(g, Q(0)))
        arcs = [(i,j) for i in range(n) for j in range(n)
                if x[i] > x[j] and rnd.randint(0,1)]
        assert cuts_pass(n,g,arcs)==maxflow_exact(n,x,g,arcs), (rep,n,x,g,arcs)
    return trials


if __name__ == '__main__':
    exact_witnesses()
    count=random_cut_consistency()
    print(f"PASS: exact three-patch witnesses and {count} deterministic flow/cut checks")
