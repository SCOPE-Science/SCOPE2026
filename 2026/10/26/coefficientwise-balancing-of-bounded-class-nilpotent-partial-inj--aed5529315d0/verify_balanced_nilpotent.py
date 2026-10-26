"""Independent finite checks for layered nilpotent partial injections."""
from functools import lru_cache
from itertools import combinations, permutations
from math import comb, factorial


def add_shift(target, source, factor, shift):
    for j, v in enumerate(source):
        while len(target) <= j+shift: target.append(0)
        target[j+shift] += factor*v

@lru_cache(None)
def rank_polynomial(sizes):
    if not any(sizes): return (1,)
    i=next(j for j,x in enumerate(sizes) if x)
    js=[j for j in range(i+1,len(sizes)) if sizes[j]]
    ans=[]
    for mask in range(1<<len(js)):
        nxt=list(sizes); nxt[i]-=1; ways=1; shift=0
        for p,j in enumerate(js):
            if mask>>p&1:
                ways*=sizes[j]; nxt[j]-=1; shift+=1
        add_shift(ans,rank_polynomial(tuple(nxt)),ways,shift)
    return tuple(ans)

def partial_injections(n):
    yield ()
    X=range(n)
    for r in range(1,n+1):
        for D in combinations(X,r):
            for Y in combinations(X,r):
                for targets in permutations(Y):
                    yield tuple(zip(D,targets))

def direct_rank_polynomial(sizes):
    L=[j for j,m in enumerate(sizes) for _ in range(m)]
    counts=[0]*(sum(sizes)+1)
    for f in partial_injections(len(L)):
        if all(L[x]<L[y] for x,y in f): counts[len(f)]+=1
    while len(counts)>1 and counts[-1]==0:counts.pop()
    return tuple(counts)

@lru_cache(None)
def compositions(n,k):
    if k==1:return ((n,),)
    return tuple((i,)+s for i in range(1,n-k+2) for s in compositions(n-i,k-1))

for n in range(2,7):
    for k in range(2,min(n,4)+1):
        for sizes in compositions(n,k):
            a=rank_polynomial(sizes); b=direct_rank_polynomial(sizes)
            assert a==b,(n,k,sizes,a,b)
for n in range(3,13):
    for k in range(3,min(n,5)+1):
        val={s:rank_polynomial(s) for s in compositions(n,k)}
        q,r=divmod(n,k)
        balanced=(q,)*(k-r)+(q+1,)*r
        best=val[balanced]
        for s,p in val.items():
            assert all((p[j] if j<len(p) else 0)<=best[j] for j in range(len(best))), (n,k,s)
        assert {s for s,p in val.items() if p==best}=={s for s in val if max(s)-min(s)<=1}
print('VERIFY_OK_BALANCED_NILPOTENT_LAYERS')
