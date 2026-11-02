#!/usr/bin/env python3
"""Reproducibility checks for finite-path partial-automorphism monoid algebras."""
from collections import Counter, defaultdict
from itertools import combinations, permutations
from math import comb, factorial


def partition_number(n):
    values=[0]*(n+1);values[0]=1
    for k in range(1,n+1):
        for v in range(k,n+1):values[v]+=values[v-k]
    return values[n]


def bipartition_number(n):
    return sum(partition_number(k)*partition_number(n-k) for k in range(n+1))


def signature(subset):
    if not subset:return ()
    arr=sorted(subset);lens=[];length=1
    for a,b in zip(arr,arr[1:]):
        if b==a+1:length+=1
        else:lens.append(length);length=1
    lens.append(length)
    return tuple(sorted(lens))


def formula(n,lam):
    if not lam:return 1
    m=sum(lam);k=len(lam)
    if n<m+k-1:return 0
    repeats=Counter(lam)
    arrangements=factorial(k)
    for a in repeats.values():arrangements//=factorial(a)
    return arrangements*comb(n-m+1,k)


def local_group_size(lam):
    cc=Counter(lam)
    ans=1
    for length,a in cc.items():ans*=factorial(a)*(2**a if length>=2 else 1)
    return ans


def number_irreps(lam):
    if not lam:return 1
    cc=Counter(lam)
    ans=1
    for length,a in cc.items():ans*=partition_number(a) if length==1 else bipartition_number(a)
    return ans


def by_types(n):
    counts=Counter()
    for mask in range(1<<n):
        subset=[i for i in range(n) if mask>>i&1]
        counts[signature(subset)]+=1
    return counts


def direct_mon_cardinality(n):
    # Unlike the formula, this loops over every domain/range pair and every bijection.
    vertices=set(range(n));ans=0
    for m in range(n+1):
        for dom in combinations(range(n),m):
            de={(i,j) for i in dom for j in dom if abs(i-j)==1}
            for ran in combinations(range(n),m):
                re={(i,j) for i in ran for j in ran if abs(i-j)==1}
                for perm in permutations(ran):
                    mp=dict(zip(dom,perm))
                    if {(mp[i],mp[j]) for i,j in de}==re:ans+=1
    return ans


def coeff_series(n_max):
    # Builds the Euler products P(z^2) and prod_{k>=3}P(z^k)^2 directly.
    lim=n_max+1
    v=[0]*(lim+1);v[0]=1
    for k in range(2,lim+1):
        mult=1 if k==2 else 2
        # p(h) factors at degree k*h, each raised to power mult.
        for h in range(1,lim//k+1):
            for _ in range(mult):
                for d in range(k*h,lim+1):v[d]+=v[d-k*h]
    result=[]
    for n in range(n_max+1):result.append(1+sum(v[j] for j in range(1,n+2)))
    return result


def check():
    d=coeff_series(10)
    print('n  #types  #simple  #monoid')
    for n in range(0,11):
        counts=by_types(n)
        for lam,val in counts.items():assert val==formula(n,lam),(n,lam,val)
        class_count=sum(number_irreps(lam) for lam in counts)
        mon_count=sum(cnt**2*local_group_size(lam) for lam,cnt in counts.items())
        assert class_count==d[n],(n,class_count,d[n])
        if n<=6:
            direct=direct_mon_cardinality(n)
            assert direct==mon_count,(n,mon_count,direct)
        print(n,len(counts),class_count,mon_count)
    assert d[:7]==[1,2,4,8,12,24,36],d[:7]
    print('VERIFY_OK path graph partial-automorphism matrix blocks and simple modules')

if __name__=='__main__':check()


def monoid_elements(n):
    """Enumerate partial graph isomorphisms as sorted source-target pairs."""
    maps=set()
    for m in range(n+1):
        for dom in combinations(range(n),m):
            de={(i,j) for i in dom for j in dom if abs(i-j)==1}
            for ran in combinations(range(n),m):
                re={(i,j) for i in ran for j in ran if abs(i-j)==1}
                for perm in permutations(ran):
                    mp=dict(zip(dom,perm))
                    if {(mp[i],mp[j]) for i,j in de}==re:
                        maps.add(tuple(zip(dom,perm)))
    return sorted(maps,key=lambda s:(len(s),s))


def compose(s,t):
    # Function composition s after t, with unspecified arguments omitted.
    ss=dict(s)
    return tuple((i,ss[j]) for i,j in t if j in ss)


def mobius_coefficients(s):
    # Inclusion-exclusion on restrictions to domain subsets.
    out={}
    for m in range(len(s)+1):
        for pairs in combinations(s,m):
            out[pairs]=(-1)**(len(s)-m)
    return out


def check_groupoid_basis(n):
    elems=monoid_elements(n)
    transformed={s:mobius_coefficients(s) for s in elems}
    for s in elems:
        for t in elems:
            actual=defaultdict(int)
            for u,a in transformed[s].items():
                for v,b in transformed[t].items():
                    actual[compose(u,v)]+=a*b
            actual={x:c for x,c in actual.items() if c}
            if set(i for i,_ in s)==set(j for _,j in t):
                expected=transformed[compose(s,t)]
            else:
                expected={}
            assert actual==expected,(n,s,t,actual,expected)
    return len(elems)


if __name__=='__main__':
    for _n in range(1,5):
        print('MOBIUS_OK',_n,check_groupoid_basis(_n))
