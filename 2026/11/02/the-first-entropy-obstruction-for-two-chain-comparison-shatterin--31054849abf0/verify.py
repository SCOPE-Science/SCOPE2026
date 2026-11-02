#!/usr/bin/env python3
"""Reproduce two-chain comparison-shattering certificates and exact small-parameter dimensions.
Run: python verify.py
The only input is witnesses.json alongside this file.
"""
import json
from functools import lru_cache
from itertools import combinations, combinations_with_replacement
from math import comb
from pathlib import Path

P=Path(__file__).resolve().parent
witnesses=json.loads((P/'witnesses.json').read_text(encoding='utf-8'))

def vectors(a,b):
    # g_i is the number of B letters before A_i in a shuffled word.
    return list(combinations_with_replacement(range(b+1),a))

def masks(a,b,v):
    return {(i,j):sum(1<<k for k,g in enumerate(v) if g[i-1]<j)
        for i in range(1,a+1) for j in range(1,b+1)}

def littlestone(a,b):
    v=vectors(a,b)
    assert len(v)==comb(a+b,a)
    m=masks(a,b,v)
    @lru_cache(maxsize=None)
    def rec(s):
        if s.bit_count()<2: return 0
        best=0
        for t in m.values():
            pos=s&t; neg=s&~t
            if pos and neg:
                best=max(best,1+min(rec(pos),rec(neg)))
        return best
    return rec((1<<len(v))-1),v,m

def direct_word_to_gaps(word,a,b):
    assert len(word)==a+b and word.count('A')==a and word.count('B')==b
    gaps=[]; k=0
    for c in word:
        if c=='B':k+=1
        else:gaps.append(k)
    return tuple(gaps)

def check_tree(node,a,b,remaining,depth):
    if depth==0:
        assert set(node)=={'word'},node
        g=direct_word_to_gaps(node['word'],a,b)
        assert g in remaining,(g,remaining)
        return (1,{g})
    assert set(node)=={'query','0','1'},node
    i,j=map(int,node['query'].split(','))
    assert 1<=i<=a and 1<=j<=b
    r0={g for g in remaining if g[i-1]>=j}
    r1={g for g in remaining if g[i-1]<j}
    assert r0 and r1
    c0,w0=check_tree(node['0'],a,b,r0,depth-1)
    c1,w1=check_tree(node['1'],a,b,r1,depth-1)
    assert w0.isdisjoint(w1)
    return 1+c0+c1,w0|w1

def vc_dimension(a,b,v):
    q=list(masks(a,b,v))
    rows=[sum((g[i-1]<j)<<k for k,(i,j) in enumerate(q)) for g in v]
    best=0
    for size in range(1,len(q)+1):
        if comb(len(q),size)>5000:break
        shattered=False
        for S in combinations(range(len(q)),size):
            patterns={sum(((r>>k)&1)<<z for z,k in enumerate(S)) for r in rows}
            if len(patterns)==2**size: shattered=True;break
        if shattered: best=size
    return best

certificate_count=0
for c in witnesses['certificates']:
    a,b,depth=c['a'],c['b'],c['depth']
    found,v,_=littlestone(a,b)
    assert found==depth,(a,b,found,depth)
    nodes,leaves=check_tree(c['tree'],a,b,set(v),depth)
    assert nodes==2**(depth+1)-1 and len(leaves)==2**depth
    assert c['n_words']==comb(a+b,a)
    certificate_count+=1

pairs=[]
for n in range(2,8):
    for a in range(1,n//2+1):
        b=n-a
        d,v,m=littlestone(a,b)
        cap=comb(n,a).bit_length()-1
        vc=vc_dimension(a,b,v)
        assert vc==min(a,b),(a,b,vc)
        pairs.append((a,b,len(v),vc,d,cap))
        if n<=6: assert d==cap,(a,b,d,cap)
        elif (a,b)==(3,4): assert (d,cap)==(4,5)
        else:assert d==cap,(a,b,d,cap)

for b in range(1,8):
    d,v,m=littlestone(2,b)
    cap=comb(b+2,2).bit_length()-1
    if b<=6: assert d==cap,(2,b,d,cap)
    else: assert (d,cap)==(4,5)

for a,b,expected in [(3,4,15),(2,7,15)]:
    d,v,m=littlestone(a,b)
    full=(1<<len(v))-1
    splits={(i,j):(t.bit_count(),len(v)-t.bit_count()) for (i,j),mask in m.items() if (t:=full&mask) or True}
    assert max(min(*xy) for xy in splits.values())==expected
    assert d==4

# The classical exact positive split count, verified independently of bitset masks.
for a,b in [(3,4),(2,7)]:
    v=vectors(a,b)
    m=masks(a,b,v)
    for i in range(1,a+1):
        for j in range(1,b+1):
            by_position=sum(comb(p-1,i-1)*comb(a+b-p,a-i) for p in range(i,i+j))
            assert by_position==m[i,j].bit_count(),(a,b,i,j)

print('ALL_TWO_CHAIN_COMPARISON_CHECKS_PASS')
print('CERTIFICATES',certificate_count,'SMALL_PAIRS',len(pairs),'MIN_ROOT_BRANCH_MAX_3_4_AND_2_7',15)
for p in pairs: print('PAIR',*p)
