"""Exact verification of minimum power-dominating subsets of a sunlet graph.
This script requires Python 3 standard library only.
"""
from itertools import combinations
from collections import Counter
from math import comb

def predicted(n):
    if n == 4:
        return (6, 12, 4)
    q, r = divmod(n, 3)
    if r == 0:
        return (3, 0, 0)
    if r == 2:
        return (n, 2*n, 0)
    return (n*(q+2)//2, n*(2*q+1), 2*n*q)

def admissible(n, selected, adj):
    seen = set(selected)
    for s in selected:
        seen.update(adj[s])
    while True:
        extra = set()
        for v in tuple(seen):
            unseen = adj[v] - seen
            if len(unseen) == 1:
                extra.update(unseen)
        if not extra:
            return len(seen) == 2*n
        seen.update(extra)

def verify():
    combinations_checked=0
    for n in range(3, 14):
        adj=[set() for _ in range(2*n)]
        for i in range(n):
            j=(i+1)%n
            adj[i].add(j);adj[j].add(i)
            adj[i].add(i+n);adj[i+n].add(i)
        k=(n+2)//3
        if n <= 8:
            for r in range(k):
                for combo in combinations(range(2*n),r):
                    combinations_checked+=1
                    assert not admissible(n,combo,adj), (n,combo)
        types=Counter()
        for combo in combinations(range(2*n), k):
            combinations_checked+=1
            if admissible(n,combo,adj):
                types[sum(v>=n for v in combo)]+=1
        assert tuple(types[i] for i in (0,1,2))==predicted(n), (n,types,predicted(n))
    print('VERIFICATION_OK n=3..13 checked_subsets=%d minimum_types_match=True lower_orders=3..8' % combinations_checked)
if __name__=='__main__':verify()
