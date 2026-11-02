#!/usr/bin/env python3
"""Finite checks for scattered-subsequence results on Rudin-Shapiro blocks."""
from itertools import product

BLOCKS = {
    'A':'0001001000011101',
    'B':'0001001011100010',
    'C':'1110110100011101',
    'D':'1110110111100010',
}
MORPHISM={'A':'AB','B':'AC','C':'DB','D':'DC'}

def word(k):
    return ''.join(str((i & (i >> 1)).bit_count() % 2) for i in range(1 << k))

def greedy_arch_index(w):
    found=0;arches=0
    for b in w:
        found |= 1 << int(b)
        if found==3:
            arches+=1;found=0
    return arches

def shortest_absent(w):
    # Independent implementation of the shortest-absent-subsequence recurrence
    # using next-occurrence positions and reverse dynamic programming.
    n=len(w)
    nxt=[[n,n] for _ in range(n+1)]
    for i in range(n-1,-1,-1):
        nxt[i] = nxt[i+1].copy()
        nxt[i][int(w[i])]=i
    dist=[0]*(n+2)
    count=[1]*(n+2)
    for i in range(n,-1,-1):
        a=[(0,1) if nxt[i][x] == n else (dist[nxt[i][x]+1],count[nxt[i][x]+1]) for x in (0,1)]
        d=min(x[0] for x in a)
        dist[i] = d+1
        count[i] = sum(c for v,c in a if v==d)
    return dist[0],count[0]

def transducer(w,q=0):
    d=[1,0] if q==1 else ([0,1] if q==-1 else [0,0]);c=[1,1]
    for b in reversed(w):
        v=min(d)
        total=sum(c[t] for t in (0,1) if d[t]==v)
        c[int(b)]=total
        d[int(b)]=v+1
    return d,c

if __name__=='__main__':
    for code, block in BLOCKS.items():
        for q in (-1,0,1):
            d,c=transducer(block,q)
            m=min(d);out=d[0]-d[1]
            assert out == (1 if code in 'AB' else -1)
            assert c[0] == c[1] == 2**(m-4)
            print('block',code,'input',q,'delta',m,'output',out,'multiplier',c[0])
    for blocks in range(1,5):
        for chars in product('ABCD',repeat=blocks):
            w=''.join(BLOCKS[c] for c in chars)
            length,count=shortest_absent(w)
            assert count==2**(length-1-4*blocks)
            assert length-1==greedy_arch_index(w)
        print('all block strings',blocks,'checked',4**blocks)
    labels='A'
    for k in range(4,14):
        w=''.join(BLOCKS[c] for c in labels)
        assert w==word(k),(k,'different words')
        length,cnt=shortest_absent(w)
        q=1<<(k-4);eps=int(k%2==0)
        assert length-1 == 5*q-eps
        assert cnt == 2**(q-eps)
        assert length-1 == greedy_arch_index(w)
        print('Rudin-Shapiro',k,'length',len(w),'index',length-1,'SAS exponent',cnt.bit_length()-1)
        labels=''.join(MORPHISM[x] for x in labels)
    print('ALL CHECKS PASS')
