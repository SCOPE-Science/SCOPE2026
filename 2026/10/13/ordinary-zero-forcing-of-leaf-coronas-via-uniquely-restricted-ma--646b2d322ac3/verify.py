"""Executable direct-enumeration checks of zero-forcing / cut-peeling theorem.
Run: python3 verify.py (Python 3 stdlib only).
"""
from itertools import combinations
from collections import Counter
import random

def adjacency(n, edges):
    ans=[0]*n
    for i,j in edges:
        ans[i]|=1<<j;ans[j]|=1<<i
    return ans

def zf_sim(adj,S):
    n=len(adj); a=0
    for v in range(n):
        if (S>>v)&1:a|=1<<v
    while True:
        b=a
        for v in range(n):
            if not(a>>v)&1:continue
            w=adj[v]&~a
            if w and not(w&(w-1)):b|=w
        if b==a:return a==(1<<n)-1
        a=b

def direct_corona_zf(base,S):
    n=len(base)
    adj=base[:]+[1<<i for i in range(n)]
    for i in range(n):adj[i]|=1<<(n+i)
    return zf_sim(adj,S)

def peeling(base,D,W):
    n=len(base)
    while W:
        force=0
        for i in range(n):
            if (D>>i)&1:
                x=base[i]&W
                if x and not (x&(x-1)):
                    force|=x
        if not force:return False
        W &= ~force
    return True

def predicted(base,S):
    n=len(base)
    D=(S>>n)&((1<<n)-1)
    R=S&((1<<n)-1)
    W=((1<<n)-1)&~(D|R)
    return peeling(base,D,W)

def polynomial(base):
    n=len(base); pol=Counter()
    for D in range(1<<n):
        for W in range(1<<n):
            if D&W or not peeling(base,D,W):continue
            m=D.bit_count()
            from math import comb
            for j in range(m+1):pol[n-W.bit_count()+j]+=comb(m,j)
    return pol

def min_characterization(n,S):
    base=adjacency(n,combinations(range(n),2))
    if not predicted(base,S):return False
    return all(not predicted(base,S^(1<<k)) for k in range(2*n) if S>>k&1)

def predicted_min_clique(n,S):
    R=S&((1<<n)-1);D=(S>>n)&((1<<n)-1)
    W=((1<<n)-1)&~(R|D)
    if W==0:
        return R==(1<<n)-1 and D==0
    if W.bit_count()!=1 or D==0:return False
    return (R&D)==0 and (R|D|W)==(1<<n)-1

checks=0; graphs=0
for n in range(1,5):
    pp=list(combinations(range(n),2))
    for mask in range(1<<len(pp)):
        base=adjacency(n,[e for k,e in enumerate(pp) if mask>>k&1]);graphs+=1
        direct=Counter()
        for S in range(1<<(2*n)):
            a=direct_corona_zf(base,S);b=predicted(base,S)
            assert a==b,(n,mask,S,'predicate')
            checks+=1
            if a:direct[S.bit_count()]+=1
        assert polynomial(base)==direct,(n,mask,'poly')
print('ALL_GRAPHS_N_LE4',graphs,'PREDICATE_COMPARISONS',checks)

random.seed(20261009)
for n, trials in [(5,100),(6,45),(7,12)]:
    pp=list(combinations(range(n),2))
    for _ in range(trials):
        base=adjacency(n,[e for e in pp if random.getrandbits(1)])
        direct=Counter()
        for S in range(1<<(2*n)):
            a=direct_corona_zf(base,S);b=predicted(base,S)
            assert a==b,(n,S,'random')
            checks+=1
            if a:direct[S.bit_count()]+=1
        assert polynomial(base)==direct
        graphs+=1
print('WITH_RANDOM_N_LE7',graphs,'PREDICATE_COMPARISONS',checks)

from math import comb
for n in range(2,10):
    base=adjacency(n,combinations(range(n),2))
    actual=Counter()
    for S in range(1<<(2*n)):
        is_zf=direct_corona_zf(base,S)
        assert is_zf==predicted(base,S)
        if is_zf:actual[S.bit_count()]+=1
        if n<=8:
            mini=is_zf and all(not direct_corona_zf(base,S^(1<<k)) for k in range(2*n) if S>>k&1)
            assert mini==predicted_min_clique(n,S),(n,S,'minimal')
    expect=Counter()
    for k in range(n+1):
        for j in range(k+1):
            # (2x+x^2)^n -> choose k pairs using x^2
            pass
    # expansion by formal convolution
    p=Counter({0:1})
    for _ in range(n):
        q=Counter()
        for k,c in p.items():q[k+1]+=2*c;q[k+2]+=c
        p=q
    q=Counter({0:1})
    for _ in range(n-1):
        qq=Counter()
        for k,c in q.items():qq[k+1]+=2*c;qq[k+2]+=c
        q=qq
    for k,c in q.items():p[k]+=n*c
    p[n-1]-=n
    p=Counter({k:v for k,v in p.items() if v})
    assert actual==p,(n,actual,p)
    print('CLIQUE_N',n,'Z',min(actual),'MINIMUM_SETS',n*(2**(n-1)-1),'ALL_INCLUSION_MINIMAL',1+n*(2**(n-1)-1),'TOTAL',sum(actual.values()))
# Independently compare the peeling criterion to the graph-theoretic definition
# of a uniquely restricted matching (unique matching on its covered endpoints).
def has_ur_matching_covering_u(base,D,U):
    n=len(base)
    us=[u for u in range(n) if U>>u&1]
    ds=[d for d in range(n) if D>>d&1]
    def cover(k,assigned):
        if k==len(us):
            donor_set=sum(1<<d for d in assigned)
            # Count all perfect matchings on exactly the currently covered donors.
            def count_matchings(j,used):
                if j==len(us):return 1
                total=0
                for d in assigned:
                    if used>>d&1 or not(base[d]>>us[j]&1):continue
                    total+=count_matchings(j+1, used|(1<<d))
                return total
            return count_matchings(0,0)==1
        for d in ds:
            if d in assigned or not(base[d]>>us[k]&1):continue
            if cover(k+1,assigned+[d]):return True
        return False
    return cover(0,[])

matching_checks=0
for n in range(1,5):
    pp=list(combinations(range(n),2))
    for mask in range(1<<len(pp)):
        base=adjacency(n,[e for k,e in enumerate(pp) if mask>>k&1])
        for D in range(1<<n):
            for U in range(1<<n):
                if D&U:continue
                assert peeling(base,D,U)==has_ur_matching_covering_u(base,D,U),(n,mask,D,U)
                matching_checks+=1
print('MATCHING_VS_PEELING_COMPARISONS',matching_checks)
print('VERIFY_OK')
