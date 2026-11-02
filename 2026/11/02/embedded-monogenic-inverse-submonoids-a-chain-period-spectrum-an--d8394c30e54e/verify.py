#!/usr/bin/env python3
"""Standalone finite verification of an embedded monogenic inverse-submonoid census.
Only finite tests are checked here; the all-n claims require the written proof.
"""
import itertools, collections, math
from fractions import Fraction

def partial_injections(n):
    for k in range(n+1):
        for domain in itertools.combinations(range(n), k):
            for image in itertools.permutations(range(n), k):
                f=[-1]*n
                for i,j in zip(domain,image): f[i]=j
                yield tuple(f)

def multiply(f,g):
    return tuple(g[f[i]] if f[i]>=0 and g[f[i]]>=0 else -1 for i in range(len(f)))

def inverse(f):
    b=[-1]*len(f)
    for i,j in enumerate(f):
        if j>=0:b[j]=i
    return tuple(b)

def inverse_submonoid(f):
    n=len(f); id_n=tuple(range(n)); have={id_n}; pending=[f,inverse(f)]
    while pending:
        v=pending.pop()
        if v in have:continue
        have.add(v)
        for u in tuple(have):
            for w in (multiply(u,v),multiply(v,u)):
                if w not in have:pending.append(w)
    return frozenset(have)

def profile(f):
    n=len(f); incoming={j for j in f if j>=0}; visited=set();h=0;cycle_lcm=1
    for i in range(n):
        if i in incoming:continue
        j=i;length=0
        while j>=0:
            assert j not in visited
            visited.add(j);length+=1;j=f[j]
        h=max(h,length-1)
    for i in range(n):
        if i in visited:continue
        j=i;length=0
        while j not in visited:
            visited.add(j);length+=1;j=f[j]
        assert j==i
        cycle_lcm=math.lcm(cycle_lcm,length)
    return h,cycle_lcm

def divisors(m):return [d for d in range(1,m+1) if m%d==0]

def mu(m):
    n=m;ans=1;p=2
    while p*p<=n:
        if n%p==0:
            n//=p;ans=-ans
            if n%p==0:return 0
        while n%p==0:n//=p
        p+=1
    if n>1:ans=-ans
    return ans

def exponential_of_log(log_coeff,n):
    a=[Fraction(1)]+[Fraction(0)]*n
    for k in range(1,n+1):
        a[k]=sum((j*log_coeff[j]*a[k-j] for j in range(1,k+1)), Fraction(0))/k
    return a

def coef_refined(n,h,m):
    assert h>=1
    up=exponential_of_log([Fraction(0)]+[Fraction(int(j<=h+1)) for j in range(1,n+1)],n)
    low=exponential_of_log([Fraction(0)]+[Fraction(int(j<=h)) for j in range(1,n+1)],n)
    cyc=[Fraction(0)]*(n+1)
    for d in divisors(m):
        if not mu(m//d):continue
        poly=exponential_of_log([Fraction(0)]+[Fraction(int(j>0 and d%j==0),j) for j in range(1,n+1)],n)
        for i in range(n+1):cyc[i]+=mu(m//d)*poly[i]
    coefficient=sum((up[j]-low[j])*cyc[n-j] for j in range(n+1))
    ans=coefficient*math.factorial(n)/2
    assert ans.denominator==1,(n,h,m,ans)
    return int(ans)

def phi(k):
    v=k;n=k;p=2
    while p*p<=n:
        if n%p==0:
            v=v//p*(p-1)
            while n%p==0:n//=p
        p+=1
    if n>1:v=v//n*(n-1)
    return v

def cyclic_subgroups(k):
    ans=Fraction(0)
    for p in itertools.permutations(range(k)):
        seen=set();order=1
        for i in range(k):
            if i in seen:continue
            v=i;length=0
            while v not in seen:
                seen.add(v);length+=1;v=p[v]
            order=math.lcm(order,length)
        ans+=Fraction(1,phi(order))
    assert ans.denominator==1
    return int(ans)

def check():
    for n in range(0,6):
        all_f=list(partial_injections(n))
        indexed=collections.defaultdict(list)
        profile_counts=collections.Counter()
        for f in all_f:
            indexed[inverse_submonoid(f)].append(f)
            profile_counts[profile(f)]+=1
        for sub,gens in indexed.items():
            h,m=profile(gens[0]);assert all(profile(f)==(h,m) for f in gens)
            if h>=1:
                assert len(gens)==2 and set(gens)=={gens[0],inverse(gens[0])}
            else:
                assert len(gens)==phi(m),(n,m,len(gens),gens)
        for (h,m),number in profile_counts.items():
            if h>=1:
                assert number%2==0
                assert coef_refined(n,h,m)==number//2,(n,h,m,number)
        total=sum(math.comb(n,k)**2*math.factorial(k) for k in range(n+1))
        partial_permutations=sum(math.comb(n,k)*math.factorial(k) for k in range(n+1))
        subgroup_sum=sum(math.comb(n,k)*cyclic_subgroups(k) for k in range(n+1))
        answer=(total-partial_permutations)//2+subgroup_sum
        assert answer==len(indexed)
        print(n, 'partial_injections',total, 'embedded_monogenic_inverse_submonoids', answer,
              'distinct_refined_noncyclic', sum(h>=1 for h,m in profile_counts))
    print('VERIFY_OK: generator rigidity, embedded census, refined EGF n<=5')
if __name__=='__main__':check()
