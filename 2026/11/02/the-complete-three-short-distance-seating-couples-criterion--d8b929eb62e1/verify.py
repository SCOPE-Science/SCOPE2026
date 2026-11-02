#!/usr/bin/env python3
"""Independent finite validation of prescribed circular lengths 1, 2, 3.
Standard library only. This code is finite verification, not the infinite proof.
"""
from collections import Counter
from functools import lru_cache

# Each block is given as (block vertex count, edges with relative vertex labels).
BLOCKS = {
    'A': (2, ((0, 1),)),
    'B': (4, ((0, 2), (1, 3))),
    'C': (4, ((0, 3), (1, 2))),
    'D': (6, ((0, 3), (1, 4), (2, 5))),
    'E': (6, ((0, 2), (1, 4), (3, 5))),
    'F': (8, ((0, 2), (1, 4), (3, 6), (5, 7))),
}

def permitted(a, b, c):
    n = a+b+c
    return n >= 3 and a >= 0 and b >= 0 and c >= 0 and b%2 == 0 and not (n%3 == 0 and a == 1 and b == 0)

def construct(a, b, c):
    n = a+b+c
    if not permitted(a,b,c):
        return None
    if b == 0 and a == 0 and c%3:
        return [tuple(sorted((e, (e+3)%(2*n)))) for e in range(0,2*n,2)]
    parts = []
    if b >= 2:
        q,r=divmod(c,3)
        parts = ['B']*((b-2)//2) + [ ('B','E','F')[r] ] + ['D']*q + ['A']*a
    else:
        q,r=divmod(c,3)
        assert a>=r
        parts = ['A']*(a-r) + ['C']*r + ['D']*q
    edges=[]; base=0
    for t in parts:
        k,small_edges=BLOCKS[t]
        edges.extend((base+i,base+j) for i,j in small_edges)
        base+=k
    assert base==2*n
    return edges

def check_matching(n, edges):
    assert len(edges)==n
    flat=[v for pair in edges for v in pair]
    assert sorted(flat)==list(range(2*n))
    return Counter(min(abs(i-j),2*n-abs(i-j)) for i,j in edges)

# A structurally independent exact subset recursion enumerates all attainable
# length profiles without using any of the six constructive blocks.
def brute_profiles(n):
    N=2*n
    adjacency=[]
    for v in range(N):
        js=[]
        for w in range(N):
            if v==w: continue
            d=min(abs(v-w),N-abs(v-w))
            if d in (1,2,3):js.append((w,d))
        adjacency.append(js)
    @lru_cache(None)
    def rec(mask):
        if mask==0: return frozenset({(0,0)})
        low=mask & -mask
        i=low.bit_length()-1
        out=set()
        for j,d in adjacency[i]:
            if mask & (1<<j):
                for b,c in rec(mask ^ low ^ (1<<j)):
                    out.add((b+(d==2),c+(d==3)))
        return frozenset(out)
    return rec((1<<N)-1)

def main():
    # Every nonnegative multiplicity profile through 2n=160 is constructed
    # or rejected, and constructed edges are checked against the original
    # circular-distance and perfect-matching definition.
    constructed=0
    for n in range(3,81):
        for a in range(n+1):
            for b in range(n-a+1):
                c=n-a-b
                edges=construct(a,b,c)
                assert (edges is not None)==permitted(a,b,c),(n,a,b,c)
                if edges is not None:
                    observed=check_matching(n,edges)
                    assert tuple(observed[d] for d in (1,2,3))==(a,b,c),(n,a,b,c,edges)
                    constructed+=1
    print('CONSTRUCTIVE_CHECK_OK',constructed,'profiles through n=80')
    # Exhaustive independent short-order enumeration: unlike construction,
    # this uses only the definition and a first-unmatched-vertex recursion.
    finite_total=0
    for n in range(3,19):
        observed=brute_profiles(n)
        predicted={(b,c) for b in range(n+1) for c in range(n-b+1)
                   if permitted(n-b-c,b,c)}
        assert observed==predicted, (n,sorted(observed ^ predicted))
        finite_total+=len(observed)
    print('EXHAUSTIVE_PROFILE_CHECK_OK',finite_total,'profiles n=3..18')
    # Hand-check each block separately, including the two rare ones.
    for label,(size,edges) in BLOCKS.items():
        n=size//2
        flat=[v for i,j in edges for v in (i,j)]
        assert sorted(flat)==list(range(size))
        d=Counter(abs(i-j) for i,j in edges)
        assert sum(d.values())==n
        print('BLOCK',label,(d[1],d[2],d[3]))
    print('VERIFY_OK')
if __name__=='__main__':main()
