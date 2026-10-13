from itertools import product
from collections import Counter
from math import comb, factorial


def windmill(n,m):
    N=1+n*m
    adj=[set() for _ in range(N)]
    for i in range(n):
        blade=range(1+i*m,1+(i+1)*m)
        for u in blade:
            adj[0].add(u);adj[u].add(0)
            for v in blade:
                if u!=v:adj[u].add(v)
    return adj


def direct(n,m,colors):
    adj=ADJ_CACHE[(n,m)]
    for v,neighbors in enumerate(adj):
        freq=Counter(colors[w] for w in neighbors)
        if any(2*count>len(neighbors) for count in freq.values()):
            return False
    return True


def structural(n,m,colors):
    h=m//2
    if m==2:
        if colors[0] in colors[1:]:return False
        freq=Counter(colors[1:])
        return all(z<=n for z in freq.values())
    for j in range(n):
        block=colors[1+j*m:1+(j+1)*m]
        cnt=Counter(block)
        if cnt.get(colors[0],0)>h-1:return False
        if any(z>h for c,z in cnt.items() if c!=colors[0]):return False
    return True


def local_count(m,q):
    # Fix the universal vertex to color zero. Count one blade.
    h=m//2
    dp=[0]*(m+1);dp[0]=1
    for c in range(q):
        lim=(h-1 if c==0 else h)
        ndp=[0]*(m+1)
        for used in range(m+1):
            if dp[used]==0:continue
            for k in range(min(lim,m-used)+1):
                ndp[used+k]+=dp[used]*comb(used+k,k)
        dp=ndp
    return dp[m]


def formula(n,m,q):
    if q==0:return 0
    if m>=3:
        return q*local_count(m,q)**n
    # m=2, all leaves avoid center and other color classes <=n.
    dp={(0,0):1} # (number of leaves assigned, number of palette leaf colors processed)
    for j in range(1,q):
        nxt={}
        for (used,_),val in dp.items():
            for k in range(min(n,2*n-used)+1):
                key=(used+k,j)
                nxt[key]=nxt.get(key,0)+val*comb(used+k,k)
        dp=nxt
    return q*dp.get((2*n,q-1),0)


def construction(n,m):
    if m==3:
        block=[1,2,3];q=4
    elif m==2:
        block=[1,2];q=3
    else:
        h=m//2
        block=[0]+[1]*h+[2]*(m-1-h)
        q=3
    labels=[0]+block*n
    assert len(set(labels))==q
    return labels,q

ADJ_CACHE={(n,m):windmill(n,m) for n in range(1,41) for m in range(2,41)}
cases=0; brute_maps=0; local_counts={}
for n in range(1,5):
    for m in range(2,6):
        if 1+n*m>9:continue
        N=1+n*m
        q_min=3 if m!=3 else 4
        for q in range(1,min(4,N)+1):
            cases+=1
            cnt=0
            for cols in product(range(q),repeat=N):
                brute_maps+=1
                d=direct(n,m,cols)
                s=structural(n,m,cols)
                if d!=s:
                    raise AssertionError(('criterion',n,m,q,cols,d,s))
                cnt+=d
            theoretical=formula(n,m,q)
            if cnt!=theoretical:
                raise AssertionError(('count',n,m,q,cnt,theoretical))
            if (cnt>0)!=(q>=q_min):
                raise AssertionError(('minimum',n,m,q,cnt,q_min))
        local_counts[(n,m)]=formula(n,m,q_min)

constructions=0
for n in range(1,41):
    for m in range(2,41):
        labels,q=construction(n,m)
        if not direct(n,m,labels):
            raise AssertionError(('construction',n,m,labels))
        constructions+=1

for n in range(1,8):
    assert formula(n,2,3)==3*comb(2*n,n)
    assert formula(n,3,4)==4*6**n
for m in range(4,18):
    for n in range(1,8):
        h=m//2
        f=local_count(m,3)
        assert f>0
        assert formula(n,m,3)==3*f**n
print('ALL CHECKS PASSED;',f'exhaustive_parameter_cases={cases};',f'labeled_maps_checked={brute_maps};',f'constructions={constructions};',f'exact_special_counts={local_counts}')
