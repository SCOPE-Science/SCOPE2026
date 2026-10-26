#!/usr/bin/env python3
"""Independent finite verification of bounded-morphism extrema for rooted trees.
No external libraries. Shape is a canonically ordered tuple of child shapes.
"""
from functools import lru_cache
from itertools import product
from collections import defaultdict

@lru_cache(None)
def size(t): return 1+sum(size(c) for c in t)

@lru_cache(None)
def shapes(n):
    if n==1: return ((),)
    options=[]
    for j in range(1,n):
        for t in shapes(j): options.append((j,repr(t),t))
    options.sort(key=lambda x:(x[0],x[1]))
    result=[]
    def go(rem,at,children):
        if not rem:
            result.append(tuple(children)); return
        for idx in range(at,len(options)):
            j,_,t=options[idx]
            if j>rem:break
            go(rem-j,idx,children+[t])
    go(n-1,0,[])
    return tuple(result)

def graph(t):
    parents=[-1]; desc=[]
    def build(sub,u):
        for ch in sub:
            v=len(parents);parents.append(u);build(ch,v)
    build(t,0)
    for u in range(len(parents)):
        vset=[]
        for v in range(len(parents)):
            w=v
            while w>=0 and w!=u:w=parents[w]
            if w==u:vset.append(v)
        desc.append(vset)
    return parents,desc

# diamond 0 -> a,b -> 1 with bit-coded upward cones.
up=(0b1111,0b1010,0b1100,0b1000)
def brute(t):
    parents,desc=graph(t)
    N=len(parents);ans=0
    colors=[0]*N
    def go(i):
        nonlocal ans
        if i==N:
            for u in range(N):
                image=0
                for v in desc[u]:image|=1<<colors[v]
                if image!=up[colors[u]]:return
            ans+=1;return
        for c in range(4):
            if i and not (up[colors[parents[i]]]>>c)&1:continue
            colors[i]=c;go(i+1)
    go(0)
    return ans

def dp(t):
    if not t:return 1
    v=2
    p=1
    for ch in t:p*=dp(ch)
    return v+p

def max_formula(n):
    if n==1:return 1
    if n==2:return 3
    if n%2:return 3**((n-1)//2)+2
    return 5*3**((n-4)//2)+2

if __name__=='__main__':
    for n in range(1,11):
        ss=shapes(n)
        values=[dp(t) for t in ss]
        mx=max(values);mn=min(values)
        assert mx==max_formula(n),(n,mx,max_formula(n))
        assert mn==(1 if n==1 else 3)
        assert values.count(mx)==1,(n,values.count(mx))
        if n<=7:
            for t,expected in zip(ss,values):
                actual=brute(t)
                assert actual==expected,(n,t,actual,expected)
        print(f'order={n} shapes={len(ss)} min={mn} max={mx} maximizer_unique=True direct_check={n<=7}')
    # Check extremal sharp witness constructions to larger order.
    for n in range(2,41):
        if n==2:t=((),)
        elif n%2:t=tuple(((),) for _ in range((n-1)//2))
        else:t=((((),),),) + tuple(((),) for _ in range((n-4)//2))
        assert size(t)==n and dp(t)==max_formula(n),(n,size(t),dp(t),max_formula(n))
    print('ALL_CHECKS_PASS')
