"""Direct finite verification of the nilpotent spectrum of star partial isometries.

Run: python verify_star_nilpotent.py
Pure Python standard library. No external data files.
"""
import itertools
from collections import Counter
from fractions import Fraction
from math import factorial


def partial_injections(n):
    for r in range(n+1):
        for domain in itertools.combinations(range(n), r):
            for images in itertools.permutations(range(n), r):
                yield dict(zip(domain, images))


def dist(i, j):
    if i == j: return 0
    return 1 if (i == 0 or j == 0) else 2


def isometry(f):
    return all(dist(i,j)==dist(f[i],f[j]) for i in f for j in f)


def nilpotency_index(f):
    # Sequentially compose, treating the empty map as zero.
    p = f
    i = 1
    while p:
        p = {a:f[b] for a,b in p.items() if b in f}
        i += 1
        if i > len(f)+2: return None
    return i


def predicted(m):
    # Enumerate set partitions into ordered lists with bounded longest list.
    # Recover the coefficient of exp(sum_{j<=t} x^j u^(j-1)).
    from math import comb
    D = [[0]*(m+1) for _ in range(m+2)]
    D[0][0] = 1
    bylen=[]
    for ell in range(1,m+1):
        nxt=[v[:] for v in D]
        # Build as product e^(x^ell u^(ell-1)) times old exponential.
        # Coefficient arrays normalized by m! and via integer labeled choices.
        bylen.append(None)
    # integer-valued DP via all cycle-free partial injections on leaf labels,
    # direct *independent* count by labeled chain set partitions.
    all_chains = Counter()
    points=tuple(range(m))
    def rec(left,chain_sizes,edges):
        if not left:
            all_chains[(edges,max(chain_sizes,default=1))]+=1
            return
        v=min(left)
        for size in range(1,len(left)+1):
            for other in itertools.combinations(left-{v},size-1):
                chunk=(v,)+other
                for order in itertools.permutations(chunk):
                    rec(left-set(chunk),chain_sizes+[size],edges+size-1)
    rec(set(points),[],0)
    all_chains[(1,2)] += 2*m
    all_chains[(2,3)] += m*(m-1)
    return all_chains


def main():
    for m in range(1,7):
        got = Counter()
        tested=0
        for f in partial_injections(m+1):
            if not isometry(f): continue
            tested+=1
            idx=nilpotency_index(f)
            if idx is not None:
                got[(len(f),idx)]+=1
        expected=predicted(m)
        assert got == expected, (m,got,expected)
        print(f'm={m}: tested {tested} star isometries, {sum(got.values())} nilpotents; rank-index spectrum verified')
    print('VERIFY_OK full star-isometry enumeration, nilpotent rank and index m=1..6')

if __name__=='__main__':main()
