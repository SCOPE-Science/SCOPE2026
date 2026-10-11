#!/usr/bin/env python3
from itertools import product, combinations

def is_matching(mask, word):
    chosen=[i for i in range(len(word)) if (mask>>i)&1]
    if len(chosen)%2:
        return False
    if not chosen:
        return True
    expect='U'
    for i in chosen:
        if word[i] != expect:
            return False
        expect = 'D' if expect=='U' else 'U'
    return expect=='U'

def vertices(word):
    out=[]
    for mask in range(1<<len(word)):
        if is_matching(mask,word):
            out.append(mask)
    return out

def runs(word):
    ps=[]; qs=[]
    i=0
    while i<len(word):
        assert word[i]=='U'
        j=i
        while j<len(word) and word[j]=='U':
            j+=1
        ps.append(j-i)
        i=j
        assert i<len(word) and word[i]=='D'
        j=i
        while j<len(word) and word[j]=='D':
            j+=1
        qs.append(j-i)
        i=j
    return ps,qs

def spare_g(ps,qs):
    g=0
    pending=False
    for p,q in zip(ps,qs):
        if p>=2 and not pending:
            pending=True
        if q>=2 and pending:
            g+=1
            pending=False
    return g

def popcount(x):
    return x.bit_count()

words=0
pairs=0
for L in range(2,11):
    for middle in product('UD', repeat=L-2):
        word='U'+''.join(middle)+'D'
        vs=vertices(word)
        ps,qs=runs(word)
        f=len(ps)
        g=spare_g(ps,qs)
        predicted=2*(f+g)

        direct=0
        for i,a in enumerate(vs):
            for b in vs[i:]:
                direct=max(direct,popcount(a^b))
                pairs+=1
        assert direct==predicted, (word,direct,predicted,ps,qs,g)

        maxzero=max(popcount(v) for v in vs)
        assert maxzero==2*f
        far=sum(1 for v in vs if popcount(v)==2*f)
        prod=1
        for p,q in zip(ps,qs):
            prod*=p*q
        assert far==prod, (word,far,prod)

        assert 2*f <= predicted <= 4*f
        if predicted==4*f:
            assert all(p>=2 and q>=2 for p,q in zip(ps,qs))
        words+=1

print(f"VERIFY_OK shard-diameter words={words} vertex_pairs={pairs} lengths=2..10")
