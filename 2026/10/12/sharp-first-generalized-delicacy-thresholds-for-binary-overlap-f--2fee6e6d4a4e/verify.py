#!/usr/bin/env python3
from itertools import product
from pathlib import Path
import json

def contains_overlap(s):
    n=len(s)
    for i in range(n):
        # An overlap xYxYx has length 2p+1 and period p >= 1.
        for p in range(1,(n-i-1)//2+1):
            if i+2*p < n and all(s[i+j] == s[i+p+j] for j in range(p+1)):
                return True
    return False

def overlap_free(s):
    return not contains_overlap(s)

def suffix_creates_overlap(s):
    n=len(s)
    for p in range(1,(n-1)//2+1):
        L=2*p+1
        if L <= n:
            t=s[-L:]
            if all(t[j] == t[p+j] for j in range(p+1)):
                return True
    return False

def prefix_generator(n):
    words=['']
    for _ in range(n):
        nxt=[]
        for w in words:
            for b in '01':
                u=w+b
                if not suffix_creates_overlap(u):
                    nxt.append(u)
        words=nxt
    return sorted(words)

def brute_generator(n):
    # Independent route: inspect all 2^n words and all factors from scratch.
    return sorted(''.join(bits) for bits in product('01',repeat=n) if overlap_free(''.join(bits)))

def hd(a,b):
    return sum(x!=y for x,y in zip(a,b))

def isolation_profile(words):
    ds=[]
    for i,w in enumerate(words):
        ds.append(min(hd(w,v) for j,v in enumerate(words) if i!=j))
    hist={}
    for d in ds: hist[d]=hist.get(d,0)+1
    return ds,hist

def comp(s):
    return s.translate(str.maketrans('01','10'))

def orbit(s):
    c=comp(s)
    return {s,s[::-1],c,c[::-1]}

root=Path(__file__).resolve().parent
cert=json.loads((root/'certificate.json').read_text(encoding='utf-8'))
sets={}
for n in range(1,15):
    A=prefix_generator(n)
    B=brute_generator(n)
    assert A==B
    sets[n]=A
    ds,hist=isolation_profile(A)
    exp=cert['profiles'][str(n)]
    assert len(A)==exp['count']
    assert max(ds)==exp['max_isolation']
    assert {str(k):v for k,v in sorted(hist.items())}==exp['distance_histogram']

E13=sorted(w for i,w in enumerate(sets[13]) if min(hd(w,v) for j,v in enumerate(sets[13]) if i!=j)==3)
E14=sorted(w for i,w in enumerate(sets[14]) if min(hd(w,v) for j,v in enumerate(sets[14]) if i!=j)==4)
assert E13==cert['shortest_2_delicate']['words']
assert E14==cert['shortest_3_delicate']['words']
assert max(cert['profiles'][str(n)]['max_isolation'] for n in range(1,13)) <= 2
assert cert['profiles']['13']['max_isolation']==3
assert max(cert['profiles'][str(n)]['max_isolation'] for n in range(1,14)) <= 3
assert cert['profiles']['14']['max_isolation']==4
assert len({min(orbit(w)) for w in E13})==1
assert len({min(orbit(w)) for w in E14})==1
assert all(w==w[::-1] for w in E14)
assert comp(E14[0])==E14[1]
print('VERIFY_OK n=1..14 engines=2 counts13=60 counts14=62 maxiso13=3 extremizers13=4 maxiso14=4 extremizers14=2 orbits13=1 orbits14=1')
