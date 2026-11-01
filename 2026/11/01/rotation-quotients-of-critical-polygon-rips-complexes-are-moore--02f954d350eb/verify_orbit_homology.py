#!/usr/bin/env python3
"""Independent finite checks for cyclic quotients of critical polygon clique complexes."""
from itertools import combinations

def faces(n,k):
    # All cliques of the circular-distance-at-most-k graph, as bit masks.
    V=list(range(n)); E={(i,j) for i in V for j in range(i+1,n) if min(j-i,n-(j-i))<=k}
    out=set()
    for size in range(1,k+2):
        for S in combinations(V,size):
            if all((u,v) in E for u,v in combinations(S,2)):
                out.add(sum(1<<i for i in S))
    return out

def rotate(mask,n,r):
    return ((mask << r) | (mask>>(n-r)))&((1<<n)-1) if r else mask

def canon(flag,n):
    return min(tuple(rotate(s,n,r) for s in flag) for r in range(n))

def build(n,k):
    F=faces(n,k)
    subs={m:[a for a in F if a!=m and a & m==a] for m in F}
    # chains are tuples ordered increasing cardinality, so append larger faces
    bylen=[{canon((m,),n) for m in F}]
    cur={(m,) for m in F}
    while True:
        nxt=set()
        # expensive if comparing many faces; list supersets
        for f in cur:
            last=f[-1]
            for m in F:
                if m !=last and (m & last)==last:
                    nxt.add(f+(m,))
        if not nxt:break
        bylen.append({canon(f,n) for f in nxt})
        cur=nxt
    # issue building all original flags small fine
    return bylen

def rank_modp(rows,p):
    pivots={}; r=0
    for row in rows:
        a=dict((j,v%p) for j,v in row.items() if v%p)
        while a:
            j=min(a)
            if j not in pivots:
                q=pow(a[j],-1,p)
                pivots[j]={t:(v*q)%p for t,v in a.items()}
                r+=1;break
            v=a[j];b=pivots[j]
            for t,c in b.items():
                x=(a.get(t,0)-v*c)%p
                if x:a[t]=x
                elif t in a:del a[t]
    return r

def run(n,k,p):
    bylen=build(n,k)
    idx=[{f:i for i,f in enumerate(sorted(level))} for level in bylen]
    ns=[len(l) for l in idx]
    ranks=[]
    for d in range(1,len(idx)):
        rows=[]
        for flag in idx[d]:
            row={}
            for j in range(d+1):
                small=canon(flag[:j]+flag[j+1:],n)
                t=idx[d-1][small]
                row[t]=(row.get(t,0)+(-1)**j)%p
            rows.append(row)
        ranks.append(rank_modp(rows,p))
    bettis=[ns[0]-ranks[0]]+[ns[d]-ranks[d-1]-ranks[d] for d in range(1,len(ns)-1)]+[ns[-1]-ranks[-1]]
    print('n',n,'k',k,'p',p,'cells',ns,'ranks',ranks,'betti',bettis,flush=True)
    if p==2 and k%2==0 or p==3 and k%3==0 or p==5 and k%5==0:
        assert bettis==[1,1,1]+[0]*(len(ns)-3)
    else:
        assert bettis==[1]+[0]*(len(ns)-1)
if __name__=='__main__':
    for n,k,primes in [(6,2,[2,3]),(9,3,[2,3]),(12,4,[2,3])]:
        for p in primes:run(n,k,p)
    print('VERIFY_OK')
