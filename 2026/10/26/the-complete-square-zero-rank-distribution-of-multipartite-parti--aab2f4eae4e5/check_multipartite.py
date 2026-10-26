#!/usr/bin/env python3
"""Directly enumerate distance-preserving partial injections with square zero.
Compare against a separately implemented part-injection coefficient formula.
"""
from itertools import product, combinations, permutations
from math import comb, factorial


def formula(sizes):
    r=len(sizes)
    n=sum(sizes)
    co=[0]*(n//2+1)
    co[0]=1
    for ss in product(*(range(x+1) for x in sizes)):
        k=sum(ss)
        if k==0 or k>n//2: continue
        active=[i for i,s in enumerate(ss) if s]
        outside=1
        for i in active: outside *= comb(sizes[i],ss[i])*factorial(ss[i])
        choices=0
        for theta in permutations(range(r),len(active)):
            p=1
            for i,j in zip(active,theta):
                room=sizes[j]-ss[j]
                if room<ss[i]: p=0;break
                p*=comb(room,ss[i])
            choices+=p
        co[k]+=outside*choices
    return co


def direct(sizes):
    parts=sum(([i]*n for i,n in enumerate(sizes)),[])
    N=len(parts)
    out=[0]*(N//2+1)
    vertices=range(N)
    for k in range(N//2+1):
        for dom in combinations(vertices,k):
            complement=tuple(x for x in vertices if x not in dom)
            for image in permutations(complement,k):
                if all((parts[dom[i]]==parts[dom[j]])==(parts[image[i]]==parts[image[j]]) for i in range(k) for j in range(i+1,k)):
                    out[k]+=1
    return out


def bipartite_closed(a,b):
    vals=[0]*( (a+b)//2+1)
    for i in range(a+1):
        for j in range(b+1):
            k=i+j
            if k>len(vals)-1:continue
            p=comb(a,i)*comb(b,j)*factorial(i)*factorial(j)
            def cb(n,h):return comb(n,h) if 0<=h<=n else 0
            vals[k]+=p*(cb(a-i,i)*cb(b-j,j)+cb(b-j,i)*cb(a-i,j))
    vals[0]-=1
    return vals

configs=[(1,1),(1,2),(1,3),(2,2),(2,3),(2,4),(3,3),(3,4),(3,5),(4,4),
         (1,1,1),(2,1,1),(2,2,1),(2,2,2),(3,2,1),(3,2,2),(2,2,3),(1,1,1,1),(2,1,1,1)]
total=0
for sizes in configs:
    f=formula(sizes)
    d=direct(sizes)
    assert f==d,(sizes,f,d)
    if len(sizes)==2:
        a,b=sizes
        assert bipartite_closed(a,b)==f
        assert max(i for i,x in enumerate(f) if x)!=0
        assert max(i for i,x in enumerate(f) if x)==max(a//2+b//2,min(a,b))
    total+=sum(d)
    print('PASS',','.join(map(str,sizes)), 'coefficients',f)
print('ALL_MULTIPARTITE_SQUARE_ZERO_CHECKS_PASSED',len(configs),total)
