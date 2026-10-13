#!/usr/bin/env python3
from itertools import combinations
from collections import defaultdict, Counter, deque
from pathlib import Path
import json

def E(s):
    return ''.join('1' if c=='0' else '0' for c in reversed(s))
def R(s):
    return s[::-1]

def closure(s,theta):
    f=R if theta=='R' else E
    for cut in range(len(s)+1):
        suffix=s[cut:]
        if f(suffix)==suffix:
            out=s+f(s[:cut])
            assert out.startswith(s)
            assert f(out)==out
            # Minimality: every shorter extension would correspond to a longer fixed suffix.
            for c2 in range(cut):
                assert f(s[c2:])!=s[c2:]
            return out
    raise AssertionError('closure not found')

def factor_masks(w):
    n=len(w)
    factors=set(w[i:j] for i in range(n) for j in range(i+1,n+1))
    masks=[]
    for f in factors:
        m=len(f); mask=0
        for i in range(n-m+1):
            if w[i:i+m]==f:
                mask |= ((1<<m)-1)<<i
        masks.append(mask)
    return tuple(masks)

def minimum_attractor_mask_engine(w):
    masks=factor_masks(w); n=len(w)
    for k in range(1,n+1):
        for C in combinations(range(n),k):
            cm=sum(1<<i for i in C)
            if all(cm&m for m in masks):
                return k,C
    raise AssertionError

def direct_is_attractor(w,C):
    C=set(C); n=len(w)
    factors=set(w[i:j] for i in range(n) for j in range(i+1,n+1))
    for f in factors:
        m=len(f); covered=False
        for i in range(n-m+1):
            if w[i:i+m]==f and any(i<=p<i+m for p in C):
                covered=True; break
        if not covered:
            return False
    return True

def minimum_attractor_direct_engine(w):
    n=len(w)
    for k in range(1,n+1):
        for C in combinations(range(n),k):
            if direct_is_attractor(w,C):
                return k,C
    raise AssertionError

MAX=15
seen={''}; parent={'':None}; edge={}; q=deque([''])
while q:
    w=q.popleft()
    for d in '01':
        for theta in 'ER':
            v=closure(w+d,theta)
            assert len(v)>len(w)
            if len(v)<=MAX and v not in seen:
                seen.add(v); parent[v]=w; edge[v]=(d,theta); q.append(v)

levels=defaultdict(list)
for w in seen:
    if w: levels[len(w)].append(w)
for n in levels: levels[n].sort()
expected_counts=[2,4,4,8,6,12,10,18,12,24,16,34,18,40,28]
assert [len(levels[n]) for n in range(1,16)]==expected_counts

expected_hists={
1:{1:2},2:{1:2,2:2},3:{1:2,2:2},4:{1:2,2:6},5:{1:2,2:4},
6:{1:2,2:10},7:{1:2,2:8},8:{1:2,2:12,3:4},9:{1:2,2:10},
10:{1:2,2:18,3:4},11:{1:2,2:14},12:{1:2,2:24,3:8},
13:{1:2,2:14,3:2},14:{1:2,2:24,3:14},15:{1:2,2:22,3:2,4:2}}
mins={}
for n in range(1,16):
    hist=Counter()
    for w in levels[n]:
        a=minimum_attractor_mask_engine(w)
        b=minimum_attractor_direct_engine(w)
        assert a[0]==b[0]
        assert direct_is_attractor(w,a[1])
        mins[w]=a; hist[a[0]]+=1
    assert dict(sorted(hist.items()))==expected_hists[n],(n,hist)

assert max(mins[w][0] for n in range(1,15) for w in levels[n])<=3
critical=sorted(w for w in levels[15] if mins[w][0]==4)
assert critical==['010011010110010','101100101001101']
assert ''.join('1' if c=='0' else '0' for c in critical[0])==critical[1]
for w in critical:
    assert mins[w][1]==(0,4,7,11)
    assert direct_is_attractor(w,(0,4,7,11))
    assert not any(direct_is_attractor(w,C) for C in combinations(range(15),3))

paths=[]
for w in critical:
    p=[]; x=w
    while parent[x] is not None:
        p.append(edge[x]); x=parent[x]
    paths.append(list(reversed(p)))
assert paths==[[('0','E'),('0','R'),('0','E'),('0','R')],
               [('1','E'),('1','R'),('1','E'),('1','R')]]

# Reconstruct the two witnesses directly from their directive pairs.
def build(pairs):
    w=''
    for d,t in pairs: w=closure(w+d,t)
    return w
assert build(paths[0])==critical[0]
assert build(paths[1])==critical[1]

cert=json.loads((Path(__file__).resolve().parent/'certificate.json').read_text(encoding='utf-8'))
assert cert['reachable_word_counts_by_length']=={str(i+1):expected_counts[i] for i in range(15)}
assert cert['length_15_size_four_words']==critical
assert cert['zero_based_minimum_attractor']==[0,4,7,11]
print('VERIFY_OK reachable_counts=2,4,4,8,6,12,10,18,12,24,16,34,18,40,28 '
      'gamma4_before15=0 gamma4_at15=2 witnesses=complement_pair '
      'directives=0000/ERER,1111/ERER attractor=0,4,7,11 engines=mask+direct')
