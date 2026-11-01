#!/usr/bin/env python3
"""Finite checks of a uniform simplicial collapse for cyclic co-bipartite complexes.

Run: python3 verify.py
Pure Python 3; no external dependencies.
"""
from collections import defaultdict


def faces(n,t):
    full=(1<<n)-1
    result=set()
    for a in range(1<<n):
        common=full
        for i in range(n):
            if a>>i&1:
                common &= sum(1<<((i+j)%n) for j in range(t))
        b=common
        while True:
            result.add(a|(b<<n))
            if b==0:break
            b=(b-1)&common
    return result


def clique_link(n,s,i,added):
    # Return full link, with the empty simplex, using actual graph adjacency.
    def edge(x,y):
        if x==y:return False
        if (x<n)==(y<n):return True
        a=x if x<n else y
        b=(y-n) if x<n else (x-n)
        return ((b-a)%n)<s-1 or (a,b) in added
    a=i;b=n+(i+s-1)%n
    common=[v for v in range(2*n) if v!=a and v!=b and edge(a,v) and edge(b,v)]
    L={0}
    for mask in range(1,1<<len(common)):
        V=[common[k] for k in range(len(common)) if mask>>k&1]
        if all(edge(v,w) for j,v in enumerate(V) for w in V[j+1:]):
            L.add(sum(1<<v for v in V))
    return L


def relative_pairs(n,s,i):
    a=1<<i;b=1<<(n+(i+s-1)%n);e=a|b
    # The abstract Ferrers link contains A_1..A_(s-1), B_0..B_(s-2).
    A=[1<<((i+r)%n) for r in range(1,s)]
    B=[1<<(n+(i+q)%n) for q in range(s-1)]
    cur=set()
    for am in range(1<<(s-1)):
        for bm in range(1<<(s-1)):
            indsA=[r+1 for r in range(s-1) if (am>>r)&1]
            indsB=[q for q in range(s-1) if (bm>>q)&1]
            if indsA and indsB and max(indsA)>min(indsB):continue
            v=e
            for r in range(s-1):
                if am>>r&1:v |=A[r]
                if bm>>r&1:v |=B[r]
            cur.add(v)
    pairs=[]
    # Strong collapse link: delete all but A_1, then all but B_(s-2).
    for v,w in [(A[r],A[0]) for r in range(1,s-1)]+[(B[q],B[-1]) for q in range(s-2)]:
        small=[z for z in cur if z&v and not z&w]
        for low in sorted(small,key=lambda x:(-x.bit_count(),x)):
            high=low|w
            assert low in cur and high in cur
            pairs.append((low,high))
            cur.remove(low);cur.remove(high)
    # Remaining edge between A_1 and B_(s-2).
    assert cur=={e,e|A[0],e|B[-1],e|A[0]|B[-1]}
    for low,high in [(e|A[0],e|A[0]|B[-1]),(e,e|B[-1])]:
        assert low in cur and high in cur
        pairs.append((low,high));cur.remove(low);cur.remove(high)
    assert not cur
    return pairs


def verify_case(n,t):
    current=faces(n,2)
    assert len(current)==2**(n+1)-1+4*n
    total_pairs=0
    for s in range(3,t+1):
        target=faces(n,s)
        assert len(target)==2**(n+1)-1+n*s*2**(s-1)
        remaining=target.copy()
        added=set()
        for i in range(n):
            new=(i,(i+s-1)%n)
            added.add(new)
            L=clique_link(n,s,i,added)
            pairs=relative_pairs(n,s,i)
            edge_mask=(1<<i)|(1<<(n+(i+s-1)%n))
            expected={0}
            for low,high in pairs:
                expected.add(low & ~edge_mask)
                expected.add(high & ~edge_mask)
            assert L==expected,('link mismatch',n,s,i,len(L),len(expected))
            for low,high in pairs:
                assert low in remaining and high in remaining
                # A free codimension-one face has only one remaining
                # immediate coface, and its coface is maximal.
                assert high.bit_count()==low.bit_count()+1
                cofaces=[low|(1<<v) for v in range(2*n) if not low>>v&1 and (low|(1<<v)) in remaining]
                assert cofaces==[high],('not free',n,s,i,low,cofaces,high)
                assert not any(high|(1<<v) in remaining for v in range(2*n) if not high>>v&1)
                remaining.remove(low);remaining.remove(high)
                total_pairs+=1
        assert remaining==current,('collapse remainder',n,s,len(remaining^current))
        current=target
    assert total_pairs == n*(t*2**(t-2)-2)
    return len(current),total_pairs


def main():
    for n in range(3,12):
        for t in range(2,(n+1)//2+1):
            count,pairs=verify_case(n,t)
            print('n=',n,'t=',t,'faces=',count,'collapse_pairs=',pairs)
    print('CYCLIC_BAND_COLLAPSE_OK')

if __name__=='__main__':main()
