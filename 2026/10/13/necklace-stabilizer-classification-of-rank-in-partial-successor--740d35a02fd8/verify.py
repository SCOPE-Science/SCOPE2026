#!/usr/bin/env python3
"""Independent finite tests for the cyclic partial-successor rank theorem."""
from collections import deque, Counter
from math import gcd, comb
from random import Random

def active(mask, i):
    return bool(mask & (1 << i))

def successor(n, mask, i):
    return (i + 1) % n if active(mask, i) else i

def stabilizer(n, mask):
    return [d for d in range(n) if all(active(mask,i)==active(mask,(i+d)%n) for i in range(n))]

def exhaustive_min_rank(n,mask):
    maps=([((i+1)%n) for i in range(n)], [successor(n,mask,i) for i in range(n)])
    full=(1<<n)-1
    seen={full}
    q=deque([full])
    low=n
    while q:
        s=q.popleft()
        low=min(low,s.bit_count())
        for mp in maps:
            v=0
            for i in range(n):
                if (s>>i)&1:v|=1<<mp[i]
            if v not in seen:
                seen.add(v);q.append(v)
    return low

def constructive_word(n,mask):
    h=len(stabilizer(n,mask)); m=n//h
    if m==1:
        return '',h
    small=sum((1<<i) for i in range(m) if active(mask,i))
    s=set(range(m))
    word=[]
    while len(s)>1:
        x,y=sorted(s)[:2]
        d=(y-x)%m
        while d:
            for t in range(m):
                u=(x+t)%m;v=(y+t)%m
                if active(small,u) and not active(small,v):break
            else:raise AssertionError(('no rotation',n,mask,m,x,y))
            word.extend('a'*t+'b')
            x,y=(x+t+1)%m,(y+t)%m
            s={((z+t+1)%m if active(small,(z+t)%m) else (z+t)%m) for z in s}
            d=(y-x)%m
    # Replay original n-state automaton, independent of quotient calculation.
    img=set(range(n))
    for letter in word:
        if letter=='a':img={(z+1)%n for z in img}
        else:img={successor(n,mask,z) for z in img}
    assert len(img)==h,(n,mask,h,len(img))
    assert len(word)<=m*(m-1)**2,(n,mask,m,len(word))
    return ''.join(word),h

def mobius(m):
    f=0
    for e in range(1,m+1):
        if m%e:continue
        w=e;pr=0;mu=1
        for p in range(2,w+1):
            if p*p>w:break
            if w%p==0:
                w//=p;pr+=1
                if w%p==0:mu=0;break
                while w%p==0:w//=p
        if mu and w>1:pr+=1
        if mu:mu=(-1)**pr
        f+=mu*2**(m//e)
    return f

def mobius_weighted_term(m,z,e):
    w=e;mu=1
    p=2
    while p*p<=w:
        if w%p==0:
            w//=p;mu=-mu
            if w%p==0:return 0
            while w%p==0:w//=p
        p+=1
    if w>1:mu=-mu
    return mu*comb(m//e,z//e)

def run():
    exact=0
    for n in range(2,10):
        for mask in range(1<<n):
            pred=len(stabilizer(n,mask))
            got=exhaustive_min_rank(n,mask)
            assert got==pred,(n,mask,pred,got)
            if n<=8 or (mask%17==0):constructive_word(n,mask)
            exact+=1
    cnt=0
    for n in range(2,16):
        dist=Counter(len(stabilizer(n,mask)) for mask in range(1<<n))
        for d in range(1,n+1):
            if n%d==0:
                assert dist[d]==mobius(n//d),(n,d,dist[d],mobius(n//d))
        cnt+=1<<n
    weighted=0
    for n in range(2,16):
        dist=Counter((len(stabilizer(n,mask)),mask.bit_count()) for mask in range(1<<n))
        for d in range(1,n+1):
            if n%d:continue
            m=n//d
            for k in range(n+1):
                if k%d:expected=0
                else:
                    z=k//d
                    expected=sum(mobius_weighted_term(m,z,e) for e in range(1,gcd(m,z)+1) if m%e==0 and z%e==0) if z else sum(mobius_weighted_term(m,z,e) for e in range(1,m+1) if m%e==0)
                assert dist[d,k]==expected,(n,d,k,dist[d,k],expected)
                weighted+=1
    rng=Random(23451)
    constructions=0
    for n in range(10,43):
        for _ in range(40):
            mask=rng.getrandbits(n)
            constructive_word(n,mask)
            constructions+=1
    qexamples=0
    for n in range(3,46):
        for q in range(2, min(n+1,12)):
            mask=sum(1<<i for i in range(n) if i%q==0)
            expected=n//q if n%q==0 else 1
            assert len(stabilizer(n,mask))==expected,(n,q)
            if n<=20:constructive_word(n,mask)
            qexamples+=1
    print('VERIFY_OK exhaustive_pairs=%d counted_masks=%d weighted_cases=%d constructive_samples=%d stride_cases=%d max_n=%d'%(exact,cnt,weighted,constructions,qexamples,42))
if __name__=='__main__':run()
