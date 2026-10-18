#!/usr/bin/env python3
"""Standalone finite checks for the q-ary 3-abelian singleton construction."""
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import product
from math import comb

def classes(q):
    assert q >= 2
    out=[(0,0)]
    out.extend((0,j) for j in range(1,q))
    for pivot in range(q-1,0,-1):
        out.append((pivot,pivot))
        out.extend((j,pivot) for j in range(1,pivot))
    assert len(out)==q*(q+1)//2 and len(set(out))==len(out)
    return out

def make(q, multipliers):
    es=classes(q)
    assert len(es)==len(multipliers)
    shared=[]
    for a,b in zip(es,es[1:]):
        both=set(a)&set(b)
        assert both
        shared.append(min(both))
    cs=[]
    for i,e in enumerate(es):
        cycle=[(e[0],e[1])] if e[0]==e[1] else [(e[0],e[1]),(e[1],e[0])]
        entry=next(x for x in cycle if x[0]==shared[i-1]) if i else (0,0)
        exit=next(x for x in cycle if x[1]==shared[i]) if i<len(es)-1 else entry
        start=cycle.index(entry); end=cycle.index(exit)
        delta=(end-start)%len(cycle)
        cs.append((cycle,entry,exit,delta))
    states=[cs[0][1]]
    for i,(cycle,entry,exit,delta) in enumerate(cs):
        assert states[-1]==entry
        for _ in range(delta+len(cycle)*multipliers[i]):
            u=states[-1]
            pos=cycle.index(u)
            states.append(cycle[(pos+1)%len(cycle)])
        assert states[-1]==exit
        if i+1<len(cs):
            nextent=cs[i+1][1]
            assert states[-1][1]==nextent[0]
            states.append(nextent)
    word=tuple(states[0])+tuple(v[1] for v in states[1:])
    assert len(word)==2*q*q-q+2 + sum(len(x[0])*(m-1) for x,m in zip(cs,multipliers))
    return word,es,cs

def count_euler(w):
    # Dynamic counting of all words with same first two symbols and triple multiset; saturates at two.
    cnt=Counter(tuple(w[i:i+3]) for i in range(len(w)-2)); types=tuple(sorted(cnt))
    amounts=tuple(cnt[t] for t in types)
    edges=defaultdict(list)
    for i,t in enumerate(types):edges[t[:2]].append((i,t[1:]))
    @lru_cache(maxsize=None)
    def go(u, nums):
        if sum(nums)==0:return 1
        ans=0
        for i,v in edges[u]:
            if nums[i]:
                nxt=list(nums);nxt[i]-=1
                ans+=go(v,tuple(nxt))
                if ans>1:return 2
        return ans
    return go(w[:2], amounts)

def signature(w):
    return w[:2],tuple(Counter(tuple(w[i:i+3]) for i in range(len(w)-2)).get(t,0) for t in product(range(2),repeat=3))

for q in range(2,8):
    es=classes(q)
    assert len(es)==q*(q+1)//2
    qpaths=sum(a!=b for a,b in es)
    assert qpaths==comb(q,2)
    w,_,cs=make(q,[1]*len(es))
    assert sum(x[3] for x in cs)==comb(q-1,2)
    assert len(w)==2*q*q-q+2
    # For larger q, connector states and formula are checked, with no costly full recursion.
    if q<=4:
        for idx in [0,len(es)//2,len(es)-1]:
            v=[1]*len(es);v[idx]=2
            w2,*_=make(q,v)
            assert count_euler(w2)==1,(q,idx)
        assert count_euler(w)==1
    print('q',q,'necklaces',len(es),'base_length',len(w),'singleton_check',q<=4)

for n in range(8,16):
    represent={}
    for w in product(range(2),repeat=n):
        k=signature(w)
        represent[k]=represent.get(k,0)+1
    for a in range(n-7):
        for b in range(n-7):
            for c in range(n-7):
                if a+b*2+c !=n-8:continue # q=2 baseline 8, t increases
                w,*_=make(2,[a+1,b+1,c+1])
                assert represent[signature(w)]==1
    print('binary exhaustive n',n,'complete')
print('ALL_CHECKS_PASS')
