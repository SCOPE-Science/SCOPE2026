"""Brute-force check of bounded morphisms and closed-form counts for finite weak orders."""
from itertools import product
from math import factorial, comb

def ordered_levels(sizes):
    levels = []
    t=0
    for n in sizes:
        levels.append(tuple(range(t,t+n)));t+=n
    heights = [0]*t
    for i,lev in enumerate(levels):
        for x in lev: heights[x]=i
    ups=[]
    for x in range(t):
        ups.append(frozenset(y for y in range(t) if heights[y]<heights[x] or y==x))
    return levels,ups

def is_pmorphism(source,target,f):
    _,up=ordered_levels(source)
    _,uq=ordered_levels(target)
    return all({f[y] for y in up[x]}==uq[f[x]] for x in range(sum(source)))

def surj(m,n):
    return sum((-1)**j*comb(n,j)*(n-j)**m for j in range(n+1))

def formula(source,target):
    h,k=len(source),len(target)
    if h==1:return target[0]**source[0]
    z=target[0]
    prod=1
    for i in range(min(h,k)):
        if i>0:
            z+=prod* (target[i] if i<h-1 else target[i]**source[i])
        if i<h-1:prod*=surj(source[i],target[i])
    return z

def rank_polynomial(sizes):
    h=len(sizes)
    out={}
    pref=1
    for j in range(h-1):
        rank=1+sum(sizes[:j])
        out[rank]=out.get(rank,0)+pref*sizes[j]
        pref*=factorial(sizes[j])
    for t in range(1,sizes[-1]+1):
        rank=sum(sizes[:-1])+t
        out[rank]=out.get(rank,0)+pref*comb(sizes[-1],t)*surj(sizes[-1],t)
    return out

def idempotents_formula(sizes):
    n=sizes[-1]
    return sum(sizes[:-1])+sum(comb(n,j)*j**(n-j) for j in range(1,n+1))

if __name__=='__main__':
    tests=[([2],[2]),([2,2],[2,2]),([2,2],[2,3]),([2,3],[2,2]),
           ([2,2,2],[2,2]),([2,2],[2,2,2]),([2,2,2],[2,2,2]),
           ([2,3],[2,2,2]),([3,2],[2,2]),([2,2,2],[3,2]),
           ([2,2,2],[2,3,2]),([2,2],[2]),([2,2,2],[2]),
           ([3,2],[3,2]),([2,2,2],[2,2,3]),([2,2,3],[2,2,2])]
    for src,tgt in tests:
        if sum(tgt)**sum(src)>1_000_000:continue
        actual=sum(is_pmorphism(src,tgt,f) for f in product(range(sum(tgt)),repeat=sum(src)))
        pred=formula(src,tgt)
        assert actual==pred,(src,tgt,actual,pred)
        print('COUNT',src,tgt,actual)
    for sizes in [[2],[2,2],[3,2],[2,3],[2,2,2],[2,3,2]]:
        n=sum(sizes)
        if n**n>1_000_000:continue
        actual=sum(is_pmorphism(sizes,sizes,f) and all(f[f[i]]==f[i] for i in range(n)) for f in product(range(n),repeat=n))
        expected=idempotents_formula(sizes)
        assert actual==expected,(sizes,actual,expected)
        print('IDEMPOTENTS',sizes,actual)
    for sizes in [[2,2],[3,2],[2,2,2],[2,3,2]]:
        n=sum(sizes)
        actual={}
        for f in product(range(n),repeat=n):
            if is_pmorphism(sizes,sizes,f):
                r=len(set(f));actual[r]=actual.get(r,0)+1
        pred=rank_polynomial(sizes)
        assert actual==pred,(sizes,actual,pred)
        print('RANKS',sizes,sorted(actual.items()))
    print('VERIFY_OK')
