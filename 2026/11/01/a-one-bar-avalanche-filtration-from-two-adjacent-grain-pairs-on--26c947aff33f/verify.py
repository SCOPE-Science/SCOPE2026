#!/usr/bin/env python3
"""Independent finite checks for two-block path avalanche complexes."""
from itertools import combinations

def faces(simplex):
    a=tuple(sorted(simplex))
    return {frozenset(x) for r in range(len(a)+1) for x in combinations(a,r)}

def step(state):
    return (0,)+tuple(state[:-1])

def firing_history(k,n):
    assert k>=1 and n>=k+4
    c=[0]*n
    for i in (0,1,k+2,k+3): c[i]=1
    out=[]
    for t in range(n):
        out.append(frozenset(i for i,x in enumerate(c) if x>0))
        c=list(step(c))
    return out

def check_pair(k,n):
    fs=firing_history(k,n)
    for t,f in enumerate(fs):
        assert f==frozenset(i for i in (t,t+1,t+k+2,t+k+3) if i<n),(k,n,t,f)
    accum=faces(fs[0]); assert len(fs[0])==4
    for t in range(1,n):
        cur=faces(fs[t]); inter=accum & cur
        if t<=k:
            expected=faces({t,t+k+2} & set(range(n)))
        elif t==k+1:
            expected=faces({t,t+k+2}&set(range(n)))|faces({t+1})
        elif t<=n-2:
            expected=faces({t,t+1}) | faces({t,t+k+2}&set(range(n)))
        else:
            expected=faces({n-1})
        assert inter==expected,(k,n,t,inter,expected)
        accum |= cur
    return len(accum)

def rank_mod2(cols):
    piv={}
    for v in cols:
        while v:
            p=v.bit_length()-1
            if p in piv: v^=piv[p]
            else: piv[p]=v; break
    return len(piv)

def betti(fs):
    alls=set()
    for f in fs: alls.update(faces(f))
    bydim={d: sorted((f for f in alls if len(f)==d+1),key=lambda s:tuple(sorted(s))) for d in range(0,max(map(len,alls)))}
    ranks={0:0}
    for d in range(1,max(bydim)+1):
        lower={f:i for i,f in enumerate(bydim[d-1])}
        cols=[sum(1<<lower[frozenset(set(s)-{v})] for v in s) for s in bydim[d]]
        ranks[d]=rank_mod2(cols)
    return tuple(len(bydim.get(d,()))-ranks.get(d,0)-ranks.get(d+1,0) for d in range(max(bydim)+1))

if __name__=='__main__':
    tests=0
    for k in range(1,13):
        for n in range(k+4,k+20):
            check_pair(k,n);tests+=1
    for k in range(1,7):
        for n in range(k+4,min(k+12,18)):
            fs=firing_history(k,n)
            for t in range(n):
                b=betti(fs[:t+1]); expected=(1,0,0,0) if t<=k else (1,1,0,0)
                assert b==expected,(k,n,t,b,expected)
    print('PASS',tests,'integer-parameter pairs for exact firing shifts and every attaching intersection; all finite mod-2 Betti checks passed')
