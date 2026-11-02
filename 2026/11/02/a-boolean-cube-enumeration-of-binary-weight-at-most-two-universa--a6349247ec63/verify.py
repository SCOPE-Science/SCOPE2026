#!/usr/bin/env python3
"""Independent finite checks for the bounded-weight-two universal-cycle count."""
from itertools import product
from math import comb


def target(k):
    return 1 << ((k - 1)//2)


def weight2_words(k):
    return [x for x in range(1<<k) if x.bit_count()<=2]


def bareiss_det(M):
    M = [row[:] for row in M]
    n = len(M)
    if n == 0:
        return 1
    sign = 1
    old = 1
    for k in range(n-1):
        if M[k][k] == 0:
            for j in range(k+1,n):
                if M[j][k]:
                    M[j],M[k]=M[k],M[j]
                    sign=-sign
                    break
            else:
                return 0
        pivot=M[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                t=M[i][j]*pivot-M[i][k]*M[k][j]
                assert t%old ==0
                M[i][j]=t//old
        for i in range(k+1,n):M[i][k]=0
        old=pivot
    return sign*M[n-1][n-1]


def graph_tree_count(k):
    m=k-1
    states=sorted({w & ((1<<m)-1) for w in weight2_words(k)})
    assert 0 in states
    nonroot=[v for v in states if v !=0]
    ids={v:i for i,v in enumerate(nonroot)}
    L=[[0]*len(nonroot) for _ in nonroot]
    for v in nonroot:
        i=ids[v]
        for bit in (0,1):
            w=(v<<1)|bit
            if w.bit_count()>2:continue
            to=w&((1<<m)-1)
            L[i][i]+=1
            if to in ids:L[i][ids[to]]-=1
    return bareiss_det(L)


def reduced_tree_count(k):
    m=k-1
    total=0
    for bits in product((0,1), repeat=m):
        good=True
        for start in range(m):
            cur=start
            seen=set()
            while cur>=0:
                if cur in seen:
                    good=False
                    break
                seen.add(cur)
                if bits[cur]==0:cur-=1
                else:cur=m-1-cur
            if not good:break
        if good:total+=1
    return total


def brute_circular_count(k):
    n=1+k+comb(k,2)
    allowed=set(weight2_words(k))
    assert len(allowed)==n
    mask=(1<<k)-1
    found=set()
    for x in range(1<<n):
        # First compute cyclic k-window. Every allowed factor must appear once.
        ext=(x<<k)|(x>>(n-k))
        windows=set()
        valid=True
        for p in range(n):
            w=(ext>>p)&mask
            if w not in allowed or w in windows:
                valid=False
                break
            windows.add(w)
        if valid:
            rotations=[]
            for shift in range(n):
                rotations.append(((x<<shift)|(x>>(n-shift))) & ((1<<n)-1) if shift else x)
            found.add(min(rotations))
    return len(found)


def main():
    for k in range(2,12):
        d=graph_tree_count(k)
        assert d==target(k),('FULL_GRAPH',k,d,target(k))
        print('FULL_GRAPH',k,d)
    for k in range(2,16):
        r=reduced_tree_count(k)
        assert r==target(k),('REDUCED',k,r,target(k))
        print('REDUCED',k,r)
    for k in range(2,6):
        b=brute_circular_count(k)
        assert b==target(k),('CIRCULAR',k,b,target(k))
        print('CIRCULAR',k,b)
    print('VERIFY_OK')

if __name__=='__main__':main()
