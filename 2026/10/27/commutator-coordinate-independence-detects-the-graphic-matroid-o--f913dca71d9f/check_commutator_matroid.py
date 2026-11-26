"""Compare full marginal factorization with acyclicity in an example."""
from collections import Counter
from itertools import combinations, product
from math import prod

N = 5
EDGES = ((0,2),(0,2),(0,3),(1,2),(1,3))
M = len(EDGES)


def mul(x,y):
    return tuple(x[v]*y[v] for v in range(N)) + tuple(
        x[u]*y[N+j] ^ x[N+j]*y[v] for j,(u,v) in enumerate(EDGES))


def forest(jj):
    edges = [EDGES[j] for j in jj]
    while edges:
        degree = Counter(v for e in edges for v in e)
        leaf_edge = next((e for e in edges if any(degree[v] == 1 for v in e)),None)
        if leaf_edge is None:
            return False
        edges.remove(leaf_edge)
    return True


if __name__ == '__main__':
    fibers = Counter()
    for x,y in product(product(range(2),repeat=N+M),repeat=2):
        a,b = mul(x,y),mul(y,x)
        assert a[:N] == b[:N]
        fibers[tuple(u^v for u,v in zip(a[N:],b[N:]))] += 1
    total = sum(fibers.values())
    singles = [Counter() for _ in EDGES]
    for c,w in fibers.items():
        for j in range(M):
            singles[j][c[j]] += w
    independent = 1  # empty set
    for k in range(1,M+1):
        for jj in combinations(range(M),k):
            law = Counter()
            for c,w in fibers.items():
                law[tuple(c[j] for j in jj)] += w
            factors = all(law[s]*total**(k-1) == prod(singles[j][v] for j,v in zip(jj,s))
                          for s in product(range(2),repeat=k))
            assert factors == forest(jj)
            independent += factors
    print('MATROID_FACTORISATION_OK',total,2**M,independent)
