"""Independent, literal convex-hull iterate test of shortest graph returns.

The reference return iterates convex hulls of the images of *all* integer
members of the current hull, not a graph adjacency matrix.
"""
import itertools
import random


def direct_return(perm, i):
    n = len(perm)
    lo, hi = i, i+1
    for k in range(1, n+1):
        image = perm[lo:hi+1]
        lo, hi = min(image), max(image)
        if lo <= i < hi:
            return k
    raise AssertionError('No return within n steps')


def graph_return(perm, i):
    n = len(perm)
    adj = [set(range(min(perm[j],perm[j+1]),
                     max(perm[j],perm[j+1]))) for j in range(n-1)]
    layer = set(adj[i])
    for k in range(1,n+1):
        if i in layer:
            return k
        layer = set().union(*(adj[j] for j in layer)) if layer else set()
    raise AssertionError('No return within n steps')


def check(p):
    d = [direct_return(p,i) for i in range(len(p)-1)]
    g = [graph_return(p,i) for i in range(len(p)-1)]
    assert d == g,(p,d,g)
    return sorted(d)


def main():
    total = 0
    for n in range(3,9):
        for rest in itertools.permutations(range(1,n)):
            seq=(0,)+rest
            p = [0]*n
            for u,v in zip(seq,seq[1:]+seq[:1]):
                p[u]=v
            profile=check(p)
            assert all(m<=i+1 for i,m in enumerate(profile))
            total+=1
    rng=random.Random(91731)
    for _ in range(10000):
        n=13
        seq=list(range(n))
        rng.shuffle(seq)
        p=[0]*n
        for j in range(n):p[seq[j]]=seq[(j+1)%n]
        profile=check(p)
        assert all(m<=i+1 for i,m in enumerate(profile))
        total+=1
    near = [
        (2,3,4,5,6,7,8,9,10,12,11,1,0),
        (12,11,1,0,2,3,4,5,6,7,8,9,10),
    ]
    expected_near = [1,2,3,4,5,6,6,8,9,10,11,12]
    for p in near:
        profile=check(p)
        assert profile == expected_near, (p, profile)
        assert sum(profile)==77
    for q in range(1,13):
        p=tuple((j+q)%13 for j in range(13))
        assert check(p)==list(range(1,13))
    print('Independent convex-hull/graph comparison passed for',total,'cycles')
    print('Both near-maximal representatives and all 12 modular shifts passed direct replay')

if __name__=='__main__': main()
