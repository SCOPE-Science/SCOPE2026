#!/usr/bin/env python3
"""Independent period/index enumeration for cyclic submonoids of finite full transformation monoids."""
from fractions import Fraction
from math import factorial, gcd
from itertools import product
from collections import Counter, defaultdict


def convolution(a,b,N):
    return [sum(a[i]*b[k-i] for i in range(k+1)) for k in range(N+1)]

def exp_series(a,N):
    assert a[0]==0
    f=[Fraction(1)]+[Fraction(0)]*N
    for n in range(1,N+1):
        f[n]=sum(k*a[k]*f[n-k] for k in range(1,n+1))/n
    return f

def rooted_tree_series(height,N):
    T=[Fraction(0)]*(N+1)
    if N:T[1]=1
    for i in range(height):
        e=exp_series(T,N)
        T=[Fraction(0)]+e[:N]
    return T

def divisible_series(n,h,p):
    T=rooted_tree_series(h,n)
    U=[Fraction(0)]*(n+1)
    powers=[[Fraction(int(k==0)) for k in range(n+1)]]
    for j in range(1,n+1): powers.append(convolution(powers[-1],T,n))
    for j in range(1,min(p,n)+1):
        if p%j==0:
            for k in range(n+1): U[k]+=powers[j][k]/j
    return factorial(n)*exp_series(U,n)[n]

def mobius(n):
    if n==1:return 1
    p=2; sign=1
    while p*p<=n:
        if n%p==0:
            n//=p;sign=-sign
            if n%p==0:return 0
        p+=1
    if n>1: sign=-sign
    return sign

def totient(n):return sum(gcd(k,n)==1 for k in range(1,n+1))

def formula(n):
    cnt={}
    # actual possible periods are lcms of cycle lengths of permutations on <=n points
    from math import lcm
    periods={1}
    for c in range(1,n+1):
        periods|={lcm(p,c) for p in list(periods)}
    for p in sorted(periods):
        for h in range(n):
            F=lambda x: sum(mobius(p//d)*divisible_series(n,x,d) for d in range(1,p+1) if p%d==0) if x>=0 else 0
            num=F(h)-F(h-1)
            assert num.denominator==1 and num>=0,(n,p,h,num)
            if num:
                den=totient(p) if h<=1 else 1
                assert num%den==0,(n,p,h,num,den)
                cnt[h,p]=int(num/den)
    return cnt

def brute(n):
    id=tuple(range(n))
    submonoids=defaultdict(set)
    generators=Counter()
    for f in product(range(n),repeat=n):
        powers=[id]
        where={id:0}
        g=id
        while True:
            g=tuple(f[g[i]] for i in range(n))
            if g in where:
                h=where[g]
                p=len(powers)-h
                break
            where[g]=len(powers)
            powers.append(g)
        generators[h,p]+=1
        submonoids[h,p].add(frozenset(powers))
    ans={k:len(v) for k,v in submonoids.items()}
    for (h,p),a in generators.items():
        assert a==ans[h,p]*(totient(p) if h<=1 else 1), (n,h,p,a,ans[h,p])
    return ans,generators

if __name__=='__main__':
    for n in range(1,7):
        x=formula(n)
        y,g=brute(n)
        assert x==y,(n,x,y)
        print(n,'submonoids',sum(x.values()),'generator_count',sum(g.values()),'t<=1',sum(v for (h,p),v in g.items() if h<=1),'period-index',sorted(x.items()))
    print('CHECKER_OK')
