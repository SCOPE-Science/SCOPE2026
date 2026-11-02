"""Independent exhaustive check of embedded monogenic submonoid census.

Usage: python verify.py
No third-party modules required.
"""
from fractions import Fraction as F
from math import factorial, gcd
from itertools import product
from collections import defaultdict


def divisors(a):
    return [d for d in range(1, a + 1) if a % d == 0]


def mu(n):
    primes = 0
    p = 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            primes += 1
            if n % p == 0:
                return 0
        p += 1
    if n > 1:
        primes += 1
    return -1 if primes & 1 else 1


def phi(n):
    return sum(gcd(k, n) == 1 for k in range(1, n + 1))


def mul(a, b, N):
    c = [F(0)] * (N+1)
    for i in range(min(N, len(a)-1)+1):
        for j in range(min(N-i, len(b)-1)+1):
            c[i+j] += a[i]*b[j]
    return c


def exp_series(a, N):
    assert a[0] == 0
    b = [F(0)] * (N+1)
    b[0] = F(1)
    for n in range(1, N+1):
        b[n] = sum(F(k)*a[k]*b[n-k] for k in range(1,n+1))/n
    return b


def cycle_egfs(N, H, m):
    z = [F(0)]*(N+1)
    z[1] = F(1)
    trees = [z]
    for h in range(1,H+1):
        trees.append(mul(z,exp_series(trees[-1],N),N))
    out = []
    for t in trees:
        powers = {0: [F(1)]+[F(0)]*N}
        for j in range(1,N+1):
            powers[j]=mul(powers[j-1],t,N)
        s = [F(0)]*(N+1)
        for j in divisors(m):
            if j<=N:
                s=[x+y/F(j) for x,y in zip(s,powers[j])]
        out.append(exp_series(s,N))
    return out


def formula(n, h, period):
    series = {}
    for d in divisors(period):
        series[d]=cycle_egfs(n,h,d)
    coef=F(0)
    for d in divisors(period):
        es=series[d]
        v=es[h][n]-(es[h-1][n] if h else F(0))
        coef+=mu(period//d)*v
    ans=coef*factorial(n)
    assert ans.denominator==1 and ans>=0
    divisor = phi(period) if h <= 1 else 1
    assert ans.numerator % divisor == 0
    return int(ans)//divisor


def map_data(f):
    n=len(f)
    cycle=set()
    visited_global=set()
    sizes=[]
    for i in range(n):
        if i in visited_global: continue
        path=[]
        pos={}
        j=i
        while j not in visited_global and j not in pos:
            pos[j]=len(path)
            path.append(j)
            j=f[j]
        if j in pos:
            c=path[pos[j]:]
            cycle.update(c)
            sizes.append(len(c))
        visited_global.update(path)
    assert cycle
    h=0
    for i in range(n):
        j=i
        depth=0
        while j not in cycle:
            j=f[j]
            depth+=1
        h=max(h,depth)
    p=1
    for s in sizes:
        p=p*s//gcd(p,s)
    return (h,p)


def powers_key(f):
    n=len(f)
    ident=tuple(range(n))
    powers={ident}
    g=ident
    while True:
        g=tuple(f[x] for x in g)
        if g in powers:
            break
        powers.add(g)
    return tuple(sorted(powers))


def check(n):
    groups=defaultdict(set)
    map_counts=defaultdict(int)
    seen={}
    for f in product(range(n),repeat=n):
        hp=map_data(f)
        key=powers_key(f)
        if key in seen:
            assert seen[key]==hp, ('incompatible generator types',n,hp,seen[key])
        seen[key]=hp
        groups[hp].add(key)
        map_counts[hp]+=1
    for (h,p),keys in groups.items():
        expected=formula(n,h,p)
        assert expected==len(keys),(n,h,p,expected,len(keys))
        divisor=phi(p) if h<=1 else 1
        assert len(keys)*divisor==map_counts[h,p]
    for h in range(n):
        for p in range(1, 2*n+1):
            if (h,p) not in groups:
                assert formula(n,h,p)==0,(n,h,p)
    assert sum(len(x) for x in groups.values())==len(seen)
    print('n=',n,'transformations=',n**n,'distinct_submonoids=',len(seen),'classes=',len(groups))


if __name__=='__main__':
    for n in range(1,7):
        check(n)
    print('VERIFY_OK')
