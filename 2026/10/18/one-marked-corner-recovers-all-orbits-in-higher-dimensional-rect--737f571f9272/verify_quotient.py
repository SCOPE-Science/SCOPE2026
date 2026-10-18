"""Independent weighted-orbit-quotient testing of one-root refinement.

A quotient vertex is a tuple of occupancy counts for every coordinate level
within a given length class. Transition weights are the number of coordinate
moves causing that profile change. Refinement uses weighted neighbor multisets.
"""
from collections import defaultdict
from itertools import combinations_with_replacement, product
from math import comb, prod


def weak_compositions(r, k):
    if k == 1:
        yield (r,)
    else:
        for v in range(r + 1):
            for tail in weak_compositions(r - v, k - 1):
                yield (v,) + tail


def test(dims):
    types = sorted(set(dims))
    specs = tuple((n, dims.count(n)) for n in types)
    profiles = list(product(*(list(weak_compositions(r, n)) for n, r in specs)))
    labels = {p: i for i, p in enumerate(profiles)}
    adj = []
    for pr in profiles:
        row = defaultdict(int)
        for partidx, (n, r) in enumerate(specs):
            cc = pr[partidx]
            for level in range(n):
                if not cc[level]: continue
                for step in (-1, 1):
                    dest = level + step
                    if 0 <= dest < n:
                        pp = list(pr)
                        vv = list(cc); vv[level] -= 1; vv[dest] += 1
                        pp[partidx] = tuple(vv)
                        row[labels[tuple(pp)]] += cc[level]
        adj.append(row)
    colors = [0 if all(cc[0] == r for cc, (n, r) in zip(pr, specs)) else 1 for pr in profiles]
    rounds = 0
    while True:
        # Combine weights going to different profiles of the same color.
        sig = []
        for i, row in enumerate(adj):
            totals = defaultdict(int)
            for j, count in row.items(): totals[colors[j]] += count
            sig.append((colors[i], tuple(sorted(totals.items()))))
        dic = {s: k for k, s in enumerate(sorted(set(sig)))}
        nxt = [dic[s] for s in sig]
        if len(set(nxt)) == len(set(colors)):
            colors = nxt
            break
        colors = nxt
        rounds += 1
    expected = prod(comb(n + r - 1, n - 1) for n, r in specs)
    assert len(profiles) == expected
    assert len(set(colors)) == len(profiles), (dims, len(set(colors)), len(profiles))
    return len(profiles), rounds

if __name__ == '__main__':
    cases = states = max_round = 0
    for d in range(1, 7):
        for dims in combinations_with_replacement(range(2, 6), d):
            if prod(comb(n + dims.count(n) - 1, n - 1) for n in set(dims)) > 500: continue
            size, r = test(dims)
            cases += 1; states += size; max_round = max(max_round, r)
    print('PASS weighted quotient: factor tuples', cases,
          'total quotient states', states, 'max strict splitting rounds', max_round)
