#!/usr/bin/env python3
"""Exact binary rank tests for the 8-neighbour parity rule on two-dimensional tori."""

def columns(m, n):
    out=[]
    for i in range(m):
        for j in range(n):
            v=0
            for di in (-1,0,1):
                for dj in (-1,0,1):
                    if di==dj==0: continue
                    v ^= 1 << (((i+di)%m)*n+(j+dj)%n)
            out.append(v)
    return out

def apply(v, col):
    out=0
    while v:
        bit=v&-v
        out ^= col[bit.bit_length()-1]
        v^=bit
    return out

def gf2rank(vectors):
    pivots={}
    for v in vectors:
        while v:
            index=v.bit_length()-1
            if index not in pivots:
                pivots[index]=v
                break
            v^=pivots[index]
    return len(pivots)

def predicted_rank(m,n,t):
    k,l=m//5,n//5
    K,L=max(k,l),min(k,l)
    if K==1:
        return 25 if t==0 else 16
    return 16*k*l+8*L*max(0,K-t)+2*L*max(0,K//2-t)

def gf4mul(a,b):
    v=0
    for i in range(2):
        for j in range(2):
            if (a>>i)&1 and (b>>j)&1:
                v ^= 1 << (i+j)
    if v&8: v^=0b1110
    if v&4: v^=0b0111
    return v

def check_fifth_root_traces():
    # 1 occurs once; each of the two nonzero trace values occurs twice.
    traces=(0,2,2,3,3)
    assert gf4mul(2,2)==3 and gf4mul(2,3)==1 and gf4mul(3,3)==2
    zeros=sum((a^b^gf4mul(a,b))==0 for a in traces for b in traces)
    assert zeros==9
    print('fifth_root_zero_pairs=9 nonzero_pairs=16')

def check_pair(m,n):
    assert m%5==n%5==0
    k,l=m//5,n//5
    assert k>0 and (k&(k-1))==0 and l>0 and (l&(l-1))==0
    K=max(k,l)
    c=columns(m,n)
    orbit=[1<<j for j in range(m*n)]
    ranks=[gf2rank(orbit)]
    for t in range(1,K+2):
        orbit=[apply(x,c) for x in orbit]
        ranks.append(gf2rank(orbit))
    for t,r in enumerate(ranks):
        assert r==predicted_rank(m,n,t),(m,n,t,r,predicted_rank(m,n,t))
    assert ranks[K]==ranks[K+1]==16*k*l
    assert ranks[K-1]>ranks[K]
    print(f'{m}x{n} ranks={ranks} recurrent_dimension={16*k*l}')

if __name__=='__main__':
    check_fifth_root_traces()
    for m,n in ((5,5),(5,10),(10,10),(5,20),(10,20),(20,20),
                (10,40),(20,40),(40,40)):
        check_pair(m,n)
    print('MOORE_VERIFICATION_OK')
