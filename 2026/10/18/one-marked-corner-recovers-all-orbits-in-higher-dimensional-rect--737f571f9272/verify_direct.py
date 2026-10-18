"""Exact rooted one-dimensional colour refinement on finite products of paths.

Uses explicit vertices and adjacency. Predicted classes are the multisets of
coordinate values grouped by factor length; no graph-isomorphism assumption is
used by the refinement implementation.
"""
from collections import defaultdict
from itertools import combinations_with_replacement, product
from math import comb, prod, factorial


def check(dims):
    vs = list(product(*[range(n) for n in dims]))
    locate = {v: i for i, v in enumerate(vs)}
    adj = []
    for v in vs:
        nei = []
        for j, n in enumerate(dims):
            for step in (-1, 1):
                if 0 <= v[j] + step < n:
                    w = v[:j] + (v[j] + step,) + v[j + 1:]
                    nei.append(locate[w])
        adj.append(nei)
    colors = [0 if v == tuple(0 for _ in dims) else 1 for v in vs]
    rounds = 0
    while True:
        signatures = [(colors[i], tuple(sorted(colors[j] for j in adj[i]))) for i in range(len(vs))]
        names = {sig: k for k, sig in enumerate(sorted(set(signatures)))}
        nxt = [names[sig] for sig in signatures]
        if len(set(nxt)) == len(set(colors)):
            colors = nxt
            break
        colors = nxt
        rounds += 1
    groups = defaultdict(list)
    for i, col in enumerate(colors):
        groups[col].append(vs[i])
    def profile(v):
        return tuple((n, tuple(sorted(v[i] for i, length in enumerate(dims) if length == n)))
                     for n in sorted(set(dims)))
    assert all(len({profile(v) for v in group}) == 1 for group in groups.values()), dims
    count = prod(comb(dims.count(n) + n - 1, n - 1) for n in set(dims))
    assert len(groups) == count, (dims, len(groups), count)
    for group in groups.values():
        pr = profile(group[0])
        expected = prod(factorial(len(vals)) // prod(factorial(vals.count(k)) for k in set(vals))
                        for _, vals in pr)
        assert len(group) == expected, (dims, pr, len(group), expected)
    return len(vs), rounds

if __name__ == '__main__':
    cases = vertices = max_round = 0
    for d in range(1, 6):
        for dims in combinations_with_replacement(range(2, 7), d):
            if prod(dims) > 3000: continue
            v, r = check(dims)
            cases += 1; vertices += v; max_round = max(max_round, r)
    print('PASS direct adjacency: parameter tuples', cases,
          'total tested vertices', vertices, 'max strict splitting rounds', max_round)
