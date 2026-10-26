#!/usr/bin/env python3
"""Self-contained exact checker for the displayed full-systematic PID codebooks."""
from itertools import permutations
from math import factorial

BOOKS={
 1: [(1,)],
 2: [(1,2,3),(3,2,1)],
 3: [(1,5,2,3,4),(1,4,5,3,2),(2,1,4,3,5),
     (4,2,3,1,5),(3,4,5,1,2),(5,4,3,2,1)],
 4: [(1,2,3,4,5,6),(1,2,5,4,6,3),(5,6,1,3,2,4),
     (1,3,4,2,6,5),(1,4,6,5,2,3),(1,4,6,3,2,5),
     (2,1,6,3,4,5),(2,6,1,4,5,3),(2,6,3,5,1,4),
     (6,2,3,4,1,5),(2,4,5,6,1,3),(2,4,3,1,5,6),
     (5,3,1,2,4,6),(3,1,6,5,4,2),(6,3,2,1,5,4),
     (6,5,3,2,4,1),(5,6,3,4,1,2),(3,4,6,5,2,1),
     (6,5,4,1,2,3),(6,4,1,5,3,2),(4,2,5,1,6,3),
     (4,2,5,3,6,1),(4,3,6,1,5,2),(4,5,3,2,1,6)]
}

def standardize(seq):
    ranks={x:i+1 for i,x in enumerate(sorted(seq))}
    return tuple(ranks[x] for x in seq)

def shadow(c):
    return {standardize(c[:i]+c[i+1:]) for i in range(len(c))}

for n in range(1,5):
    words=BOOKS[n]
    r=len(words[0])-n
    assert len(words)==factorial(n)
    assert len(set(words))==len(words)
    labels=tuple(range(1,n+r+1))
    seen={}
    hist={}
    for c in words:
        assert tuple(sorted(c))==labels
        m=tuple(x for x in c if x<=n)
        hist[m]=hist.get(m,0)+1
        for y in shadow(c):
            assert y not in seen, ('collision', n, c,seen.get(y),y)
            seen[y]=c
    assert len(hist)==factorial(n) and all(v==1 for v in hist.values())
    print('n=%d r=%d messages=%d outputs=%d total_universe=%d' %
          (n,r,len(words),len(seen),factorial(n+r-1)))

# Exhaustively cross-check that a rank-standardized single-deletion
# ball is singleton iff the permutation is monotone, for N <= 7.
for N in range(2,8):
    single=[]
    for p in permutations(range(1,N+1)):
        if len(shadow(p))==1:
            single.append(p)
    assert set(single)=={tuple(range(1,N+1)),tuple(range(N,0,-1))}
    print('N=%d singleton_PID_words=%d' % (N,len(single)))
print('VERIFY_OK')
