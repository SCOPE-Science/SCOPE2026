#!/usr/bin/env python3
"""Exact finite proof certificate for three-case outbreak-risk vaccination on trees.

Run with Python 3.10+. No third-party dependencies or inputs.
This code complements, rather than replaces, the mathematical proof.
"""
from itertools import product
from collections import Counter
from math import comb
from fractions import Fraction


def tree_from_prufer(n, seq):
    if n == 2:
        return [(0, 1)]
    degrees = [1] * n
    for x in seq:
        degrees[x] += 1
    edges = []
    for x in seq:
        leaf = next(i for i, d in enumerate(degrees) if d == 1)
        edges.append((leaf, x))
        degrees[leaf] -= 1
        degrees[x] -= 1
    a, b = [i for i, d in enumerate(degrees) if d == 1]
    edges.append((a, b))
    return edges


def adjacency(n, edges):
    adj = [set() for _ in range(n)]
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    return adj


def rooted_code(adj, v, parent):
    return '(' + ''.join(sorted(rooted_code(adj, w, v) for w in adj[v] if w != parent)) + ')'


def canonical(n, edges):
    adj = adjacency(n, edges)
    degrees = [len(x) for x in adj]
    remaining = set(range(n))
    while len(remaining) > 2:
        leaves = [x for x in remaining if degrees[x] == 1]
        for x in leaves:
            remaining.remove(x)
        for x in leaves:
            for y in adj[x]:
                degrees[y] -= 1
    centers = sorted(remaining)
    if len(centers) == 1:
        return rooted_code(adj, centers[0], -1)
    a, b = centers
    return '[' + '|'.join(sorted([rooted_code(adj, a, b), rooted_code(adj, b, a)])) + ']'


def om(k):
    return [(-1)**j * comb(k, j) for j in range(k + 1)]


def risk_numer(n, edges, vaccinee):
    # Integer coefficients of (n-1)*P(|outbreak| >= 3).
    remaining = [i for i in range(n) if i != vaccinee]
    adj = adjacency(n, [e for e in edges if vaccinee not in e])
    co = [0] * (n + 1)
    for v in remaining:
        d = len(adj[v])
        co[0] += 1
        for j, x in enumerate(om(d)):
            co[j] -= x
        for u in adj[v]:
            for j, x in enumerate(om(d + len(adj[u]) - 2)):
                co[j + 1] -= x
    return tuple(co)


def coeff_ge_on_unit(f):
    """Exact nonnegative power coefficients after p=t/(1+t); strips p=0 factor.

    Returned True certifies f(p)>=0 for all p in [0,1]. For these
    particular comparisons this sufficient certificate always succeeds.
    """
    f = list(f)
    while f and f[0] == 0:
        f.pop(0)
    while f and f[-1] == 0:
        f.pop()
    if not f:
        return True
    d = len(f) - 1
    bern = [sum(f[j] * comb(d-j, k-j) for j in range(k+1)) for k in range(d+1)]
    return all(x >= 0 for x in bern)


def subtract(f, g):
    return tuple(a-b for a,b in zip(f,g))


def brute_risk(n, edges, v, p):
    rem = [u for u in range(n) if u != v]
    E = [e for e in edges if v not in e]
    ans = Fraction(0)
    for mask in range(1 << len(E)):
        chosen = [E[j] for j in range(len(E)) if mask & (1 << j)]
        adj = adjacency(n, chosen)
        seen = set()
        good = 0
        for root in rem:
            if root in seen:
                continue
            comp = {root}
            frontier = [root]
            seen.add(root)
            while frontier:
                w = frontier.pop()
                for x in adj[w]:
                    if x not in seen:
                        seen.add(x)
                        comp.add(x)
                        frontier.append(x)
            if len(comp) >= 3:
                good += len(comp)
        k = mask.bit_count()
        ans += Fraction(good, n-1) * p**k * (1-p)**(len(E)-k)
    return ans


def eval_poly(f,p):
    return sum(Fraction(a)*p**j for j,a in enumerate(f))


def verify():
    witness = [(0,1),(0,2),(0,3),(3,4),(4,5),(4,6)]
    special = canonical(7, witness)
    counts = {}
    fixed = 0
    exceptional = []
    for n in range(2,8):
        reps = {}
        for seq in product(range(n), repeat=n-2):
            edges = tree_from_prufer(n,seq)
            reps.setdefault(canonical(n,edges),edges)
        counts[n] = len(reps)
        for key, edges in reps.items():
            values = [risk_numer(n,edges,v) for v in range(n)]
            assert all(z[0] == z[1] == 0 for z in values)
            has_fixed = any(all(coeff_ge_on_unit(subtract(values[u],values[v])) for u in range(n)) for v in range(n))
            if has_fixed:
                fixed += 1
            else:
                exceptional.append((n,key))
    assert counts == {2:1,3:1,4:2,5:3,6:6,7:11}, counts
    assert exceptional == [(7,special)], exceptional
    # Express the exceptional witness with connectors/hubs/leaves in fixed order.
    polys = [risk_numer(7,witness,v) for v in range(7)]
    # Here indices 0,3,4 are hub, bridge, hub respectively, not all leaves.
    # Expected bridge: 6*p^2, hubs: 9*p^2-5*p^3,
    # leaves: 15*p^2-11*p^3+2*p^4.
    assert polys[3] == (0,0,6,0,0,0,0,0)
    for i in (0,4):
        assert polys[i] == (0,0,9,-5,0,0,0,0)
    for i in (1,2,5,6):
        assert polys[i] == (0,0,15,-11,2,0,0,0)
    for p in [Fraction(1,4),Fraction(1,2),Fraction(3,5),Fraction(3,4),Fraction(1)]:
        for v in range(7):
            assert brute_risk(7,witness,v,p) == eval_poly(polys[v],p) / 6
    # Hub minus bridge is p^2*(3-5p)/6; leaf minus bridge is
    # p^2*(1-p)*(9-2p)/6; leaf minus hub is p^2*(6-6p+2p^2)/6.
    print('VERIFY_OK shape_counts=' + str(counts) +
          ' exact_stable_shapes=' + str(fixed) +
          ' exceptional_seven_shape=1 witness_reconstructions=35 crossover=3/5')

if __name__ == '__main__':
    verify()
