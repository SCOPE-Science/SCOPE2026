#!/usr/bin/env python3
"""Exact finite-order verification for rank-two spectra of finite posets."""
import json
from functools import lru_cache
from itertools import combinations
from pathlib import Path

HERE=Path(__file__).resolve().parent
W=json.loads((HERE/'witnesses.json').read_text())['witnesses']


def close_rel(up):
    up=list(up)
    for i in range(len(up)-1,-1,-1):
        todo=up[i]
        while todo:
            t=todo & -todo
            j=t.bit_length()-1
            todo^=t
            up[i]|=up[j]
    return up


def spectrum(up):
    n=len(up)
    assert n>=1
    assert all(not (up[i]>>i&1) for i in range(n))
    assert close_rel(up)==list(up)
    out=0
    for i in range(n):
        lower=any(up[j]>>i&1 for j in range(n))
        upper=up[i]!=0
        inc=any(j!=i and not(up[i]>>j&1) and not(up[j]>>i&1) for j in range(n))
        out|=1<<(int(lower)+2*int(upper)+4*int(inc))
    return out


def locally_iso(U,V,a,b):
    assert len(a)==len(b)
    for i in range(len(a)):
        for j in range(len(a)):
            if (a[i]==a[j])!=(b[i]==b[j]): return False
            if bool(U[a[i]]>>a[j]&1)!=bool(V[b[i]]>>b[j]&1):return False
    return True


def ef_wins(U,V):
    # Direct two-round EF game, independent of spectrum calculations.
    @lru_cache(None)
    def win(aa,bb,r):
        if not locally_iso(U,V,aa,bb): return False
        if r==0:return True
        for x in range(len(U)):
            if not any(win(aa+(x,),bb+(y,),r-1) for y in range(len(V))):
                return False
        for y in range(len(V)):
            if not any(win(aa+(x,),bb+(y,),r-1) for x in range(len(U))):
                return False
        return True
    return win((),(),2)


assert len(W)==20
seen={}
for r in W:
    u=r['strict_upper_sets'];n=r['size'];s=r['spectrum']
    assert n==len(u) and all((a >> n)==0 for a in u)
    assert spectrum(u)==s and s not in seen
    seen[s]=r
assert set(seen)=={1,6,14,16,36,44,66,74,96,104,112,134,142,164,172,194,202,224,232,240}
# Exhaustive finite search over all 2^(n choose 2) naturally labelled DAG
# seeds: a linear extension makes every finite poset isomorphic to one seed.
min_seen={}
for n in range(1,7):
    pairs=list(combinations(range(n),2))
    for seed in range(1<<len(pairs)):
        up=[0]*n
        for bit,(i,j) in enumerate(pairs):
            if seed>>bit&1:up[i]|=1<<j
        up=close_rel(up)
        s=spectrum(up)
        min_seen.setdefault(s,n)
        assert s in seen
        assert n>=seen[s]['size']
    print('n=%d: new-theories=%d, total-theories=%d' % (n,sum(k==n for k in min_seen.values()),len(min_seen)))
assert len(min_seen)==20
assert {s:r['size'] for s,r in seen.items()}==min_seen
# E-F round-two game independently checks that different witnessed spectra
# are not rank-two equivalent.
checks=0
for i,r in enumerate(W):
    for t in W[i:]:
        eq=ef_wins(r['strict_upper_sets'],t['strict_upper_sets'])
        assert eq==(r['spectrum']==t['spectrum'])
        checks+=1
print('pairwise-two-round-EF-comparisons:',checks)

# Nonisomorphic / differently sized sample comparisons also check the equivalence
# direction for shared profiles, not just separation of canonical witnesses.
extra=0
for n in range(1,5):
    pairs=list(combinations(range(n),2))
    orders=set()
    for seed in range(1<<len(pairs)):
        up=[0]*n
        for bit,(i,j) in enumerate(pairs):
            if seed>>bit&1:up[i]|=1<<j
        orders.add(tuple(close_rel(up)))
    for up in orders:
        t=spectrum(up)
        for w in W:
            assert ef_wins(up,tuple(w['strict_upper_sets']))==(t==w['spectrum'])
            extra+=1
print('additional-EF-crosschecks:',extra)
print('minimum-representative-size-distribution:',{n:sum(z==n for z in min_seen.values()) for n in range(1,7)})
print('CLASSIFICATION_OK')
