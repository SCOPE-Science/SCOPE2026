#!/usr/bin/env python3
from collections import deque

INF=10**9

def transitions(n):
    b = tuple((i + 1) % n for i in range(n))
    c = list(b); c[0]=2; c[1]=2
    return b, tuple(c)

def image(mask, trans):
    out=0
    for i,j in enumerate(trans):
        if mask>>i & 1: out |= 1<<j
    return out

def distance_arrays(n):
    b,c=transitions(n); N=1<<n; full=N-1
    dist=[INF]*N; dist[full]=0; q=deque([full])
    while q:
        s=q.popleft(); nd=dist[s]+1
        for t in (b,c):
            u=image(s,t)
            if dist[u]==INF:
                dist[u]=nd; q.append(u)
    # best[C] = minimum dist[S] over S subset C.
    best=dist[:]
    for bit in range(n):
        step=1<<bit
        for mask in range(N):
            if mask & step:
                v=best[mask ^ step]
                if v<best[mask]: best[mask]=v
    return dist,best

def target_mask(n,k):
    m=1
    for i in range(n-k+1,n): m|=1<<i
    return m

def witness(n,k):
    return ("c"+"b"*(n-2))*(k-1)+"c"+"b"*(n-1)

def apply_word(n,word):
    b,c=transitions(n); mp={'b':b,'c':c}; s=(1<<n)-1
    for ch in word: s=image(s,mp[ch])
    return s

def exhaustive_check(n):
    dist,best=distance_arrays(n); full=(1<<n)-1
    seen=sum(d<INF for d in dist)
    vals=[]
    for k in range(1,n):
        maxd=-1; maxm=[]
        for target in range(1,1<<n):
            if target.bit_count()!=k: continue
            d=best[full ^ target]
            if d>maxd: maxd=d; maxm=[target]
            elif d==maxd: maxm.append(target)
        exp=k*(n-1)+1; tm=target_mask(n,k)
        assert maxd==exp,(n,k,maxd,exp)
        assert maxm==[tm],(n,k,maxm,tm)
        w=witness(n,k)
        assert len(w)==exp
        assert apply_word(n,w)&tm==0,(n,k,w)
        vals.append((k,maxd))
    return seen,vals

def witness_sweep(limit):
    for n in range(3,limit+1):
        for k in range(1,n):
            w=witness(n,k); tm=target_mask(n,k)
            assert len(w)==k*(n-1)+1
            assert apply_word(n,w)&tm==0

if __name__=='__main__':
    for n in range(3,12):
        seen,vals=exhaustive_check(n)
        print(f"n={n} reachable_image_subsets={seen} thresholds="+','.join(f'k{k}:{d}' for k,d in vals))
    witness_sweep(40)
    print('explicit_witness_replay_n=3..40:OK')
    print('VERIFY_OK')
