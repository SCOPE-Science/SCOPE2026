#!/usr/bin/env python3
"""Exact finite certificate for sharp tree sentinel-switch classification.

Python standard library only. Run with: python3 check.py
"""
from collections import deque, Counter
from fractions import Fraction
from itertools import product
from math import comb


def prufer_tree(code):
    """Decode a length-n-2 Prufer word into its uniquely associated labeled tree."""
    n = len(code) + 2
    deg = [1] * n
    for x in code:
        deg[x] += 1
    edges = []
    for x in code:
        leaf = next(i for i in range(n) if deg[i] == 1)
        edges.append((leaf, x))
        deg[leaf] -= 1
        deg[x] -= 1
    leaves = [i for i in range(n) if deg[i] == 1]
    assert len(leaves) == 2
    edges.append(tuple(leaves))
    return edges


def adjacency(n, edges):
    a = [set() for _ in range(n)]
    for u, v in edges:
        assert u != v
        a[u].add(v)
        a[v].add(u)
    assert sum(map(len, a)) == 2 * (n - 1)
    return a


def canon(a):
    """Isomorphism-complete AHU encoding for an unrooted tree."""
    n = len(a)
    alive = set(range(n))
    while len(alive) > 2:
        leaves = {v for v in alive if len(a[v] & alive) <= 1}
        assert leaves
        alive -= leaves
    def rooted(v, parent):
        return '(' + ''.join(sorted(rooted(w, v) for w in a[v] if w != parent)) + ')'
    return min(rooted(c, -1) for c in alive)


def distances(a, v):
    n = len(a)
    dist = [-1] * n
    dist[v] = 0
    todo = deque([v])
    while todo:
        w = todo.popleft()
        for z in a[w]:
            if dist[z] < 0:
                dist[z] = dist[w] + 1
                todo.append(z)
    assert all(x >= 0 for x in dist)
    return dist


def shells(a):
    n = len(a)
    out = []
    for v in range(n):
        c = [0] * n
        for d in distances(a, v):
            c[d] += 1
        assert sum(c) == n and c[0] == 1
        out.append(c)
    return out


def bernstein_coefficients(monomials):
    """Degree-m Bernstein coefficients of sum a_k p^k, m=len(a)-1."""
    m = len(monomials) - 1
    return [sum((Fraction(monomials[k] * comb(j, k), comb(m, k))
                 for k in range(j + 1)), Fraction(0)) for j in range(m + 1)]


def universal_maximizers(a):
    """Find vertices with exact coefficientwise nonnegative Bernstein gap."""
    cs = shells(a)
    n = len(a)
    winners = []
    for v in range(n):
        if all(all(x >= 0 for x in bernstein_coefficients(
            [cs[v][k] - cs[w][k] for k in range(n)]))
            for w in range(n)):
            winners.append(v)
    return winners


def exact_s_canonical_classes():
    representatives = {}
    word_counts = {}
    for n in range(2, 8):
        found = {}
        codes = 0
        for word in product(range(n), repeat=n-2):
            a = adjacency(n, prufer_tree(word))
            key = canon(a)
            if key not in found:
                found[key] = a
            codes += 1
        representatives[n] = found
        word_counts[n] = codes
        assert codes == n ** (n - 2)
    return representatives, word_counts


def check():
    reps, words = exact_s_canonical_classes()
    assert [len(reps[n]) for n in range(2,8)] == [1,1,2,3,6,11]
    exceptions = []
    positive_count = 0
    for n in range(2, 8):
        for key, a in reps[n].items():
            winners = universal_maximizers(a)
            if winners:
                positive_count += 1
            else:
                assert n == 7
                exceptions.append(key)
    # Explicit exception A: a 4-edge arm and two leaves at the hub.
    broom = adjacency(7, [(0,1),(1,2),(2,3),(3,4),(0,5),(0,6)])
    # Explicit exception B: two degree-3 hubs joined by a 2-edge arm.
    double = adjacency(7, [(0,1),(1,2),(0,3),(0,4),(2,5),(2,6)])
    assert set(exceptions) == {canon(broom), canon(double)}
    assert len(exceptions) == 2
    # Closed-form polynomial equalities of the candidates.
    cb, cd = shells(broom), shells(double)
    assert cb[0] == [1,3,1,1,1,0,0]
    assert cb[1] == [1,2,3,1,0,0,0]
    assert [cb[0][k] - cb[1][k] for k in range(7)] == [0,1,-2,0,1,0,0]
    assert cd[0] == cd[2] == [1,3,1,2,0,0,0]
    assert cd[1] == [1,2,4,0,0,0,0]
    assert [cd[0][k] - cd[1][k] for k in range(7)] == [0,1,-3,2,0,0,0]
    # For all p in (0,1), the candidates strictly dominate every noncandidate.
    for a, candidates in ((broom, {0,1}), (double, {0,1,2})):
        cs = shells(a)
        for v in range(7):
            if v in candidates:
                continue
            assert any(all(z >= 0 for z in bernstein_coefficients(
                [cs[c][k] - cs[v][k] for k in range(7)])) and
                any(z != 0 for z in [cs[c][k] - cs[v][k] for k in range(7)])
                for c in candidates)
    # Tie polynomials: broom p(1-p)(1-p-p^2), double p(1-p)(1-2p).
    # 1-p-p^2 strictly decreases from 1 to -1, with unique root in (0,1).
    # 1-2p strictly decreases from 1 to -1, with unique root p=1/2.
    print('VERIFY_OK', 'unlabeled_tree_classes=',[len(reps[n]) for n in range(2,8)],
          'labeled_Prufer_codes=',sum(words.values()),
          'stable_classes=',positive_count, 'exceptional_seven_vertex_classes=',len(exceptions),
          'candidate_shell_identites=2', 'Bernstein_exact=1')

if __name__ == '__main__':
    check()
