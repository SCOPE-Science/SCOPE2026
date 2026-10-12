#!/usr/bin/env python3
from collections import Counter, deque


def graph(n):
    N = 2*n
    adj = [set() for _ in range(N)]
    for i in range(n):
        for j in range(n):
            if i != j:
                u, v = i, n+j
                adj[u].add(v)
                adj[v].add(u)
    return adj


def distances(adj):
    out=[]
    for s in range(len(adj)):
        d=[None]*len(adj); d[s]=0; q=deque([s])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if d[v] is None:
                    d[v]=d[u]+1; q.append(v)
        assert all(x is not None for x in d)
        out.append(d)
    return out


def direct_resolving(n, D, mask):
    N=2*n
    S=[s for s in range(N) if (mask>>s)&1]
    reps=[]
    for v in range(N):
        if (mask>>v)&1: continue
        reps.append(tuple(sorted(D[v][s] for s in S)))
    return len(reps)==len(set(reps))


def theorem_resolving(n, mask):
    X={i for i in range(n) if not ((mask>>i)&1)}
    Y={i for i in range(n) if not ((mask>>(n+i))&1)}
    x,y=len(X),len(Y)
    if (x,y) in {(0,0),(1,0),(0,1)}:
        return True
    if (x,y)==(2,1):
        return len(X & Y)==1
    if (x,y)==(1,2):
        return len(X & Y)==1
    return False


def main():
    total_subsets=0
    total_bases=0
    for n in range(3,9):
        adj=graph(n); D=distances(adj)
        counts=Counter()
        for mask in range(1<<(2*n)):
            total_subsets += 1
            direct=direct_resolving(n,D,mask)
            theorem=theorem_resolving(n,mask)
            assert direct==theorem, (n,mask,direct,theorem)
            if direct:
                counts[mask.bit_count()] += 1
        expected=Counter({2*n:1, 2*n-1:2*n, 2*n-3:2*n*(n-1)})
        assert counts==expected, (n,counts,expected)
        assert min(counts)==2*n-3
        assert counts[2*n-3]==2*n*(n-1)
        total_bases += counts[2*n-3]
    assert total_subsets==87360, total_subsets
    assert total_bases==332, total_bases
    print('ALL CHECKS PASSED; orders=3..8; subsets=87360; bases=332')

if __name__=='__main__':
    main()
