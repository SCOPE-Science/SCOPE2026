"""Finite exact tests of leaf-controlled temporal periods on rooted tree posets.
Run: python3 tree_temporal_verifier.py (Python standard library only).
The proof in RESULT.md is independent of these finite tests.
"""
from itertools import product
from math import gcd


def lcm(a,b):
    return a//gcd(a,b)*b


def lambda_budget(n):
    if n==1:
        return 0
    s=0
    p=2
    while p*p<=n:
        if n%p==0:
            power=1
            while n%p==0:
                n//=p
                power*=p
            s+=power
        p+=1
    if n>1:
        s+=n
    return s


def tree_order(parent):
    n=len(parent)
    mask=[]
    for i in range(n):
        b=1<<i
        j=i
        while j:
            j=parent[j]
            b |=1<<j
        mask.append(b)
    return mask


def temporal_period(f, initial):
    n=len(f)
    seen={}
    x=initial
    t=0
    while x not in seen:
        seen[x]=t
        x=sum((1<<j) for j in range(n) if (x>>f[j])&1)
        t+=1
    return t-seen[x]


def perm_order(f):
    n=len(f)
    seen=set()
    ans=1
    for i in range(n):
        if i in seen:
            continue
        j=i
        r=0
        while j not in seen:
            seen.add(j)
            j=f[j]
            r+=1
        assert j==i
        ans=lcm(ans,r)
    return ans


def run():
    maps=valuations=trees=0
    max_period_by_k={}
    for n in range(1,6):
        for prefix in product(*(range(i) for i in range(1,n))):
            parent=(0,)+prefix
            ancestors=tree_order(parent)
            leaves=set(range(n))-{parent[j] for j in range(1,n)}
            k=len(leaves)
            trees+=1
            for f in product(range(n),repeat=n):
                if any((ancestors[i]>>j)&1 and not ((ancestors[f[i]]>>f[j])&1)
                       for i in range(n) for j in range(n)):
                    # Current convention ancestors[i] contains j when j<=i, so f(j)<=f(i).
                    continue
                maps+=1
                for mask in range(1<<n):
                    period=temporal_period(f,mask)
                    valuations+=1
                    assert lambda_budget(period)<=k, (n,parent,f,mask,period,k)
                    max_period_by_k[k]=max(max_period_by_k.get(k,1),period)
    # Sharp construction on any parent-vector rooted tree: nonleaves map to root,
    # selected distinct leaves rotate in disjoint cycles.
    for n in range(1,10):
        parent=(0,)+tuple((j-1)//2 for j in range(1,n))
        leaves=sorted(set(range(n))-{parent[j] for j in range(1,n)})
        k=len(leaves)
        best=max(x for x in range(1,80) if lambda_budget(x)<=k)
        for target in range(1,best+1):
            if lambda_budget(target)>k:
                continue
            q=target
            prime_powers=[]
            p=2
            while p*p<=q:
                if q%p==0:
                    pp=1
                    while q%p==0:
                        q//=p; pp*=p
                    prime_powers.append(pp)
                p+=1
            if q>1:
                prime_powers.append(q)
            f=[0]*n
            chosen=0
            cursor=0
            for cycle_size in prime_powers:
                cyc=leaves[cursor:cursor+cycle_size]
                cursor+=cycle_size
                chosen|=1<<cyc[0]
                for a,b in zip(cyc,cyc[1:]+cyc[:1]):
                    f[a]=b
            for leaf in leaves[cursor:]:
                f[leaf]=leaf
            A=tree_order(parent)
            assert all(not ((A[i]>>j)&1) or ((A[f[i]]>>f[j])&1)
                       for i in range(n) for j in range(n))
            assert temporal_period(f,chosen)==target,(n,k,target,f)
    # Sharp failure of leaf control outside tree orders: diamond 0<a,b<1.
    # Its unique maximal point is 3, yet swapping 1 and 2 is order-preserving.
    diamond_downsets=(1,3,5,15)
    flip=(0,2,1,3)
    assert all(not ((diamond_downsets[i]>>j)&1)
                   or ((diamond_downsets[flip[i]]>>flip[j])&1)
                   for i in range(4) for j in range(4))
    assert temporal_period(flip,1<<1)==2
    # A five-leaf rooted star exhibits temporal period six via a 2-cycle and 3-cycle.
    star=(0,)+ (0,)*5
    star_map=(0,2,1,4,5,3)
    star_downsets=tree_order(star)
    assert all(not ((star_downsets[i]>>j)&1)
                   or ((star_downsets[star_map[i]]>>star_map[j])&1)
                   for i in range(6) for j in range(6))
    assert temporal_period(star_map,(1<<1)|(1<<3))==6
    print('VERIFY_OK trees=',trees,'monotone_maps=',maps,
          'valuation_tests=',valuations,'max_periods_seen=',sorted(max_period_by_k.items()),
          'constructed_spectra_through_n=9')

if __name__=='__main__':
    run()
