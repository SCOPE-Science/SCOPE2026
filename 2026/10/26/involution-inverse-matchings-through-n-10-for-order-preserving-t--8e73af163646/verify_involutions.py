"""Validate a complete finite involution-matching certificate; Python >=3.8, standard library only.

Usage: python verify_involutions.py INVOLUTION_MATCHINGS.tsv
"""
from collections import defaultdict
from itertools import combinations
from math import comb
from pathlib import Path
import sys


def encoded_maps(n, r):
    partitions = list(combinations(range(1, n), r - 1))
    images = list(combinations(range(1, n + 1), r))
    return partitions, images


def is_idempotent(cuts, image, n):
    ends = (0,) + cuts + (n,)
    return all(ends[i] < image[i] <= ends[i+1] for i in range(len(image)))


def mutual_inverse(P, Q, n, r, u, v):
    q = len(Q)
    au, bu = divmod(u, q)
    av, bv = divmod(v, q)
    # The image of each map meets each kernel block of the other exactly once.
    return is_idempotent(P[au], Q[bv], n) and is_idempotent(P[av], Q[bu], n)


def mapping(P, Q, n, r, u):
    a, b = divmod(u, len(Q))
    ends = (0,) + P[a] + (n,)
    return tuple(Q[b][i] for i in range(r) for _ in range(ends[i+1] - ends[i]))


def composition(f, g):
    return tuple(f[g[i]-1] for i in range(len(g)))


def main(path):
    edges = defaultdict(list)
    with Path(path).open(encoding='utf-8') as fh:
        for line in fh:
            if not line.strip() or line.startswith('#'):
                continue
            n, r, u, v = map(int, line.split())
            assert 2 <= n <= 10 and 1 < r < n
            assert 0 <= u < v
            edges[(n,r)].append((u,v))
    count_pairs = 0
    for n in range(1,11):
        fixed_count = 0
        for r in range(1,n+1):
            P, Q = encoded_maps(n,r)
            N = len(P)*len(Q)
            assert sum(1 for _ in P) * len(Q) == comb(n-1,r-1)*comb(n,r)
            used = set()
            for u,v in edges[n,r]:
                assert v < N and u not in used and v not in used, (n,r,u,v)
                used.update((u,v))
                assert mutual_inverse(P,Q,n,r,u,v), (n,r,u,v)
                if n <= 5:
                    f,g = mapping(P,Q,n,r,u), mapping(P,Q,n,r,v)
                    assert composition(f,composition(g,f)) == f
                    assert composition(g,composition(f,g)) == g
                count_pairs += 1
            for u in range(N):
                if u not in used:
                    a,b = divmod(u,len(Q))
                    assert is_idempotent(P[a],Q[b],n), (n,r,u)
                    if n <= 5:
                        f = mapping(P,Q,n,r,u)
                        assert composition(f,f) == f
                    fixed_count += 1
        print(f'n={n}: |O_n|={comb(2*n-1,n)}; fixed points={fixed_count}; paired points={comb(2*n-1,n)-fixed_count}')
    print(f'VERIFIED: {count_pairs} two-cycles; all transformations in O_1,...,O_10 are covered by inverse pairs or idempotent fixed points.')

if __name__ == '__main__':
    if len(sys.argv)!=2:
        raise SystemExit('Usage: python verify_involutions.py INVOLUTION_MATCHINGS.tsv')
    main(sys.argv[1])
