#!/usr/bin/env python3
"""Reproduce the finite transition lemma and numerical consequences.

Proof beyond finite ranks is mathematical induction given in RESULT.md.
No external dependencies.
"""
from collections import defaultdict
from itertools import product

BASE = '1101100111001001'

def block(x,y):
    z=list(BASE)
    z[7]=str(x); z[15]=str(y)
    return ''.join(z)

def endpoint_distribution(word,start,steps):
    d={start:1}
    for _ in range(steps):
        h=defaultdict(int)
        for pos,count in d.items():
            for sym in '01':
                ix=word.find(sym,pos)
                if ix>=0: h[ix+1]+=count
        d=dict(h)
    return d

def lemma():
    # Initial 16-bit block, plus the first letter of the next block.
    for x,y in product('01', repeat=2):
        w=block(x,y)+block('1','1')
        d=endpoint_distribution(w,0,6)
        peak=16+(y=='0')
        assert max(d)==peak and d[peak]==2
        assert max(p for p in d if p!=peak)==14
    # Starting after the previous block, with its last bit possibly 0.
    # 16<=start<=17, and a previous non-maximal endpoint is at most 14.
    for prev,x,y in product('01',repeat=3):
        w=block('1',prev)+block(x,y)+block('1','1')
        start=16+(prev=='0')
        goal=32+(y=='0')
        d=endpoint_distribution(w,start,6)
        assert max(d)==goal and d[goal]==2
        assert max(p for p in d if p!=goal)==30
        low=endpoint_distribution(w,14,6)
        assert max(low)==29
    print('finite lemma: 4 initial + 8 transition instances passed')

def paperfolding_prefix(k):
    return ''.join('1' if (n//(n&-n))%4==1 else '0'
                   for n in range(1,2**k+1))

def shortest_absent_stats(w):
    n=len(w)
    following={0:set()}
    # More efficient dynamic distribution, with dead state n+1.
    next_pos=[[n+1,n+1] for _ in range(n+1)]
    p0=p1=n+1
    for i in range(n,-1,-1):
        next_pos[i]=[p0,p1]
        if i:
            if w[i-1]=='0': p0=i
            else: p1=i
    d={0:1};ell=0
    while d and ell<=n:
        reached=defaultdict(int)
        for p,c in d.items():
            for a in (0,1):
                t=next_pos[p][a]
                if t<=n: reached[t]+=c
        absent=2**(ell+1)-sum(reached.values())
        if absent: return ell,absent,d.get(n,0)
        d=dict(reached)
        ell+=1
    raise AssertionError('impossible')

def sample():
    for k in range(4,11):
        w=paperfolding_prefix(k)
        q=2**(k-4)
        u,a,end=shortest_absent_stats(w)
        assert (u,a,end)==(6*q,2**(q+1),2**q),(k,u,a,end)
        print(f'paperfolding rank={k}, length={len(w)}, universality={u}, shortest_absent={a}')

def family():
    # Exhaustive finite cross-check, independent of the six-step lemma.
    for q in range(1,6):
        for flags in product('01', repeat=2*q-1):
            x=flags[:q]
            y=flags[q:]+('1',)
            w=''.join(block(a,b) for a,b in zip(x,y))
            u,c,_=shortest_absent_stats(w)
            assert (u,c)==(6*q,2**(q+1)),(q,flags,u,c)
        print(f'skeleton q={q}, all {2**(2*q-1)} choices passed')

if __name__=='__main__':
    lemma()
    sample()
    family()
    print('ALL CHECKS PASSED')
