"""Full exact-rational census for the first binary-opinion FJ edge-insertion reversal.

Python 3 standard library only.  No random sampling; all connected labeled graphs,
all nonedges and all binary innate opinions are enumerated through order five.
"""
from fractions import Fraction as F
from itertools import combinations, permutations, product
from collections import Counter


def inverse(a):
    n = len(a)
    aug = [[F(v) for v in row] + [F(i == j) for j in range(n)] for i, row in enumerate(a)]
    for col in range(n):
        pivot = next(i for i in range(col, n) if aug[i][col])
        aug[col], aug[pivot] = aug[pivot], aug[col]
        d = aug[col][col]
        aug[col] = [q / d for q in aug[col]]
        for i in range(n):
            if i != col:
                d = aug[i][col]
                aug[i] = [x - d * y for x, y in zip(aug[i], aug[col])]
    inv = [row[n:] for row in aug]
    assert all(sum(a[i][k] * inv[k][j] for k in range(n)) == F(i == j)
               for i in range(n) for j in range(n))
    return inv


def mat(n, edges, added=None):
    a = [[F(i == j) for j in range(n)] for i in range(n)]
    for i, j in (edges + ([added] if added is not None else [])):
        a[i][i] += 1; a[j][j] += 1
        a[i][j] -= 1; a[j][i] -= 1
    return a


def energy(inv, bits):
    z = [sum(x * b for x, b in zip(row, bits)) for row in inv]
    return sum(x*x for x in z)


def connected(n, edges):
    known = {0}
    while True:
        nxt = known | {j for i, j in edges if i in known} | {i for i, j in edges if j in known}
        if nxt == known:
            return len(known) == n
        known = nxt


def orbit_canonical(n, pairs, record):
    mask, edge_id, bits_mask = record
    edges = [p for i,p in enumerate(pairs) if mask >> i & 1]
    edge = pairs[edge_id]
    bits = [1 if (bits_mask >> i) & 1 else -1 for i in range(n)]
    lookup = {p:i for i,p in enumerate(pairs)}
    best = None
    for p in permutations(range(n)):
        renamed_edges = [tuple(sorted((p[a], p[b]))) for a,b in edges]
        gm = sum(1 << lookup[e] for e in renamed_edges)
        re = lookup[tuple(sorted((p[edge[0]], p[edge[1]])))]
        vals = [None]*n
        for i in range(n): vals[p[i]] = bits[i]
        sm = sum(1 << i for i,v in enumerate(vals) if v == 1)
        item = (gm,re,min(sm, ((1<<n)-1)^sm))
        if best is None or item < best: best = item
    return best


def run():
    counts = {}
    winners = []
    for n in range(2,6):
        pairs = list(combinations(range(n),2))
        graphs = tests = increases = 0
        for mask in range(1 << len(pairs)):
            edges = [e for i,e in enumerate(pairs) if mask >> i & 1]
            if not connected(n, edges): continue
            graphs += 1
            orig = inverse(mat(n, edges))
            for eidx, edge in enumerate(pairs):
                if mask >> eidx & 1: continue
                upd = inverse(mat(n, edges, edge))
                for bmask in range(1<<n):
                    bits = [1 if bmask >> i & 1 else -1 for i in range(n)]
                    tests += 1
                    if energy(upd, bits) > energy(orig, bits):
                        increases += 1
                        if n==5: winners.append((mask,eidx,bmask))
        counts[n] = (graphs, tests, increases)
    assert counts == {2:(1,0,0), 3:(4,24,0), 4:(38,1344,0), 5:(728,100480,480)}, counts
    pairs = list(combinations(range(5),2))
    orbit_counts = Counter(orbit_canonical(5,pairs,w) for w in winners)
    assert orbit_counts == {(58,0,9):240, (185,1,11):240}, orbit_counts
    # Independent two explicit rational checks for their displayed representatives.
    for gm, ei, sm, expected in [(58,0,9,F(8,405)),(185,1,11,F(18123,1250600))]:
        edges = [p for j,p in enumerate(pairs) if gm >> j & 1]
        bits = [1 if sm >> i & 1 else -1 for i in range(5)]
        diff = energy(inverse(mat(5,edges,pairs[ei])), bits) - energy(inverse(mat(5,edges)),bits)
        assert diff == expected, (gm,diff)
    print('EXHAUSTIVE_RATIONAL_CENSUS_OK')
    for n,triplet in counts.items():print('order',n,'graphs/tests/reversals',*triplet)
    print('orbits',sorted(orbit_counts.items()))

if __name__ == '__main__':run()
