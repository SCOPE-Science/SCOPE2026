#!/usr/bin/env python3
"""Independent finite graph-distance checker for metric-threshold obstructions."""
from itertools import combinations
from collections import deque
from math import comb


def verify(n, kneser=False):
    verts = tuple(combinations(range(n), 2))
    m = len(verts)
    adj = [[] for _ in range(m)]
    for i in range(m):
        for j in range(i):
            inter = len(set(verts[i]) & set(verts[j]))
            if (inter == 0 if kneser else inter == 1):
                adj[i].append(j); adj[j].append(i)
    dists = []
    for start in range(m):
        dist=[-1]*m; dist[start]=0; dq=deque([start])
        while dq:
            u=dq.popleft()
            for v in adj[u]:
                if dist[v]<0: dist[v]=dist[u]+1;dq.append(v)
        assert all(x>=0 for x in dist), (n,kneser)
        dists.append(dist)

    bisectors=set()
    for u in range(m):
        for v in range(u):
            mask=sum(1<<w for w in range(m) if dists[u][w]==dists[v][w])
            bisectors.add(mask)

    # Compute maximal bisectors by inclusion from the raw graph metric.
    maximal={x for x in bisectors if not any(x!=y and x&y==x for y in bisectors)}
    maximum=max(x.bit_count() for x in maximal)
    critical={x for x in maximal if x.bit_count()==maximum}

    A=set()
    for b,c in combinations(range(n),2):
        components={b,c}
        A.add(sum(1<<i for i,v in enumerate(verts)
                  if (len(set(v)&components) in (0,2))))
    B=set()
    for quadruple in combinations(range(n),4):
        for part1 in combinations(quadruple,2):
            if min(part1) != quadruple[0]: continue
            part2=set(quadruple)-set(part1)
            X,Y=set(part1),part2
            B.add(sum(1<<i for i,v in enumerate(verts)
                      if (v[0] in X and v[1] in Y) or
                         (v[1] in X and v[0] in Y) or
                         (v[0] not in X|Y and v[1] not in X|Y)))

    expected = B if n==4 else A|B if n==5 or n>=7 else A
    assert maximal==expected, (n,kneser,'maximal',len(maximal),len(expected),len(maximal^expected))
    expected_maximum = 4 if n==4 else comb(n-2,2)+1
    assert maximum==expected_maximum
    expected_critical_count=3 if n==4 else 25 if n==5 else comb(n,2)
    assert len(critical)==expected_critical_count
    if n>=7: assert len(maximal)==comb(n,2)+3*comb(n,4)

    # For the two smallest graphs, independently test all subsets
    # against the original resolving-set predicate (not just bisectors).
    if n<=5:
        for s in range(1<<m):
            resolving=True
            for i in range(m):
                for j in range(i):
                    if not any((s>>w)&1 and dists[i][w]!=dists[j][w]
                               for w in range(m)):
                        resolving=False; break
                if not resolving:break
            predicted=any((s&x)==s for x in expected)
            assert resolving == (not predicted), (n,kneser,s)
    return n, 'KG' if kneser else 'J', m,len(bisectors),maximum+1,len(critical),len(maximal)

if __name__=='__main__':
    for n in range(4,11):
        print(*verify(n),sep='\t')
        if n>=5:print(*verify(n,True),sep='\t')
    print('VERIFY_OK')
