#!/usr/bin/env python3
"""Independent finite-field checks of star-quiver subrepresentation strata."""
from itertools import combinations, product
from collections import Counter
from random import Random


def rank(vectors, q, d):
    rows = [list(map(lambda t: t % q, v)) for v in vectors]
    k = 0
    for c in range(d):
        piv = next((i for i in range(k, len(rows)) if rows[i][c] % q), None)
        if piv is None:
            continue
        rows[k], rows[piv] = rows[piv], rows[k]
        inv = pow(rows[k][c], -1, q)
        rows[k] = [(v * inv) % q for v in rows[k]]
        for i in range(len(rows)):
            if i != k:
                fac = rows[i][c]
                rows[i] = [(a - fac*b) % q for a, b in zip(rows[i], rows[k])]
        k += 1
    return k


def subspaces(q, d):
    """Produce each subspace exactly once using its unique RREF row basis."""
    for k in range(d+1):
        for piv in combinations(range(d), k):
            free = [(i,j) for i, p in enumerate(piv)
                         for j in range(p+1, d) if j not in piv]
            for vals in product(range(q), repeat=len(free)):
                mat = [[0]*d for _ in range(k)]
                for i,p in enumerate(piv):
                    mat[i][p] = 1
                for (i,j),v in zip(free,vals):
                    mat[i][j] = v
                yield k, mat


def gb(q,n,k):
    if k < 0 or k > n: return 0
    prod = 1
    for i in range(k):
        prod *= (q**(n-i)-1)
    den = 1
    for i in range(1,k+1):
        den *= (q**i-1)
    assert prod%den==0
    return prod//den


def profiles(q, vectors):
    d = len(vectors[0]); m = len(vectors)
    vs = list(subspaces(q,d))
    full = Counter(); coarse = Counter(); ranks = {}
    for mask in range(1<<m):
        chosen = [vectors[i] for i in range(m) if (mask>>i)&1]
        rS = rank(chosen,q,d)
        ranks[mask] = rS
        for k in range(d+1):
            actual = sum(k==j and rank(W+chosen,q,d)==k
                         for j,W in vs)
            theory = gb(q,d-rS,k-rS)
            assert actual == theory, (q,vectors,mask,k,actual,theory)
            full[(mask,k)]=actual
            coarse[(mask.bit_count(),k)]+=actual
        assert min(k for (ms,k),v in full.items() if ms==mask and v) == rS
    # Recover ranks from presence of dimension-vector quiver Grassmannians.
    reconstructed = {mask:min(k for k in range(d+1) if full[(mask,k)])
                     for mask in range(1<<m)}
    assert reconstructed == ranks
    # Independently invert the Gaussian-binomial transform for the coarse counts.
    A = Counter((mask.bit_count(),r) for mask,r in ranks.items())
    for s in range(m+1):
        residual = [coarse[(s,k)] for k in range(d+1)]
        inverse = []
        for h in range(d+1):
            v=residual[h]
            inverse.append(v)
            for k in range(h,d+1):
                residual[k] -= v*gb(q,d-h,k-h)
        assert all(v==0 for v in residual)
        assert inverse == [A[(s,h)] for h in range(d+1)]
    return full,coarse,A


def same_labeled_quiver_representation(q, X, Y):
    """Search for central GL(2,q) together with arbitrary leaf rescalings."""
    for a,b,c,d in product(range(q), repeat=4):
        if (a*d-b*c)%q == 0: continue
        if all(((a*x+b*y)*w - (c*x+d*y)*z) % q == 0 for (x,y),(z,w) in zip(X,Y)):
            return True
    return False


def run():
    rng = Random(17389)
    configs = 0; comparisons = 0
    for q in (2,3,5):
        for d in (2,3):
            for m in (2,3,4,5):
                for rep in range(4):
                    V=[]
                    for i in range(m):
                        v=tuple(rng.randrange(q) for _ in range(d))
                        if not any(v): v=(1,)+(0,)*(d-1)
                        V.append(v)
                    profiles(q,V)
                    configs += 1; comparisons += 1<<m
    X=[(1,0),(0,1),(1,1),(1,2)]
    Y=[(1,0),(0,1),(1,1),(1,3)]
    px=profiles(5,X); py=profiles(5,Y)
    assert px==py
    assert not same_labeled_quiver_representation(5,X,Y)
    assert all(px[0][(mask,k)] == py[0][(mask,k)]
               for mask in range(16) for k in range(3))
    assert all(rank([X[i] for i in range(4) if mask>>i&1],5,2)==min(2,mask.bit_count())
               for mask in range(16))
    print('ALL_STAR_QUIVER_CHECKS_PASSED',configs,'configurations',comparisons,'support sets',
          'cross_ratio_example_q5')
    print('UNIFORM_U2_4_COARSE_COUNTS',sorted(px[1].items()))

if __name__ == '__main__':
    run()
