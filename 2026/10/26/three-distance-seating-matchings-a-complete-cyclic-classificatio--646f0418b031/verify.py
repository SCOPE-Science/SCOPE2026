#!/usr/bin/env python3
"""Independent finite checks for cyclic prescribed-distance matching theorem.

Uses explicit local templates and a separate exhaustive bitmask recurrence.
The all-order conclusion rests on the mathematical proof, not these checks.
"""
from collections import Counter
from functools import lru_cache

TILES = {
    'A': (((0,1),), (1,0,0)),
    'B': (((0,3),(1,2)), (1,0,1)),
    'C': (((0,2),(1,3)), (0,2,0)),
    'D': (((0,3),(1,4),(2,5)), (0,0,3)),
    'E': (((0,2),(1,4),(3,5)), (0,2,1)),
    'F': (((0,2),(1,4),(3,6),(5,7)), (0,2,2)),
}

def construct(n,a,b,c):
    assert n >= 3 and a>=0 and b>=0 and c>=0 and a+b+c==n
    if b % 2 or (n%3==0 and a==1 and b==0 and c==n-1):
        return None
    if a==b==0 and c%3:
        # Since 3 does not divide n, +3 is one Hamiltonian cycle modulo 2n.
        N=2*n
        return [((6*i)%N, (6*i+3)%N) for i in range(n)]
    seq=[]
    if b:
        t=b//2
        q,r=divmod(c,3)
        if r==1:seq.append('E')
        if r==2:seq.append('F')
        seq.extend(['C']*(t-(r>0)))
        seq.extend(['D']*q)
        seq.extend(['A']*a)
    else:
        q,r=divmod(c,3)
        assert a>=r
        seq.extend(['B']*r)
        seq.extend(['D']*q)
        seq.extend(['A']*(a-r))
    out=[]; offset=0
    for name in seq:
        pairs,counts = TILES[name]
        out.extend((v+offset,w+offset) for v,w in pairs)
        offset+=2*sum(counts)
    assert offset == 2*n
    return out

def verify_matching(n,a,b,c,edges):
    if edges is None:return False
    N=2*n
    vertices=[]
    counts=Counter()
    for x,y in edges:
        assert 0<=x<N and 0<=y<N and x!=y
        vertices.extend([x,y]);counts[min((y-x)%N,(x-y)%N)]+=1
    assert len(edges)==n and sorted(vertices)==list(range(N))
    assert (counts[1],counts[2],counts[3]) == (a,b,c)
    assert sum(counts.values())==n
    return True


def brute_vectors(n):
    N=2*n
    neighbors=[[v for v in range(N) if v!=u and min((v-u)%N,(u-v)%N)<=3] for u in range(N)]
    @lru_cache(None)
    def rec(mask):
        if mask==0:return frozenset(((0,0,0),))
        u=(mask & -mask).bit_length()-1
        ans=set()
        for v in neighbors[u]:
            if (mask>>v)&1:
                d=min((v-u)%N,(u-v)%N)
                submask=mask & ~(1<<u) & ~(1<<v)
                for counts in rec(submask):
                    x=list(counts);x[d-1]+=1;ans.add(tuple(x))
        return frozenset(ans)
    return rec((1<<N)-1)

if __name__=='__main__':
    for name,(edges,count) in TILES.items():
        n=sum(count); assert n>=1
        assert sorted([v for e in edges for v in e])==list(range(2*n))
        lengths=Counter(abs(v-u) for u,v in edges)
        assert (lengths[1],lengths[2],lengths[3])==count
    constructed=0
    for n in range(3,61):
        for b in range(0,n+1,2):
            for a in range(n-b+1):
                c=n-a-b
                edges=construct(n,a,b,c)
                if (n%3==0 and a==1 and b==0 and c==n-1):
                    assert edges is None
                else:
                    assert verify_matching(n,a,b,c,edges)
                    constructed+=1
    for n in range(3,11):
        actual=brute_vectors(n)
        predicted={(a,b,n-a-b) for b in range(0,n+1,2)
                   for a in range(n-b+1)
                   if not (n%3==0 and a==1 and b==0)}
        assert actual==predicted,(n,actual-predicted,predicted-actual)
        print('n',n,'admissible_multisets',len(actual),'exhaustive_ok')
    print('CONSTRUCT_OK',constructed,'instances checked for 3<=n<=60')
    print('VERIFICATION_OK')
