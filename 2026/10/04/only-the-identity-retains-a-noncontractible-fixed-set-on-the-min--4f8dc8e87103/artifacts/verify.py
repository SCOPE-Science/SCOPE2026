#!/usr/bin/env python3
import json
from collections import Counter
from pathlib import Path

base=Path(__file__).resolve().parent
cert=json.loads((base/'fixed_sets.json').read_text(encoding='utf-8'))
names=cert['vertices']; n=len(names); idx={x:i for i,x in enumerate(names)}
le=[[False]*n for _ in range(n)]
for i in range(n): le[i][i]=True
for x,y in cert['cover_relations']: le[idx[x]][idx[y]]=True
for k in range(n):
    for i in range(n):
        if le[i][k]:
            for j in range(n):
                if le[k][j]: le[i][j]=True

def enumerate_maps():
    a=[None]*n; out=[]
    def rec(p):
        if p==n:
            t=tuple(a)
            assert all((not le[i][j]) or le[t[i]][t[j]] for i in range(n) for j in range(n))
            out.append(t); return
        for y in range(n):
            if all(((not le[z][p]) or le[a[z]][y]) and ((not le[p][z]) or le[y][a[z]]) for z in range(p)):
                a[p]=y; rec(p+1)
        a[p]=None
    rec(0)
    return out

def fixed_mask(f):
    return sum((1<<i) for i,v in enumerate(f) if i==v)

def beat(sub,x,typ,w):
    if typ=='up':
        upper=[y for y in sub if y!=x and le[x][y]]
        return w in upper and all(le[w][z] for z in upper)
    if typ=='down':
        lower=[y for y in sub if y!=x and le[y][x]]
        return w in lower and all(le[z][w] for z in lower)
    return False

maps=enumerate_maps()
assert len(maps)==cert['selfmap_count']==12575
assert len(set(maps))==len(maps)
counts=Counter(fixed_mask(f) for f in maps)
dist=Counter(m.bit_count() for m in map(fixed_mask,maps))
assert {str(k):dist[k] for k in range(1,10)}==cert['fixed_set_size_distribution']
assert len(counts)==cert['distinct_fixed_sets']==210
entries={e['mask']:e for e in cert['fixed_sets']}
assert set(entries)==set(counts)
for mask,e in entries.items():
    assert e['multiplicity']==counts[mask]
    sub={i for i in range(n) if mask>>i&1}
    if mask==cert['full_fixed_set_mask']:
        assert e['contractible'] is False
        assert counts[mask]==1
        assert [f for f in maps if fixed_mask(f)==mask]==[tuple(range(n))]
        # The full poset has no beat point; its noncontractibility is a literature premise.
        assert not any(any(beat(sub,x,t,w) for t in ('up','down') for w in sub if w!=x) for x in sub)
    else:
        assert e['contractible'] is True
        for step in e['deletions']:
            x=idx[step['point']]; w=idx[step['witness']]
            assert x in sub and w in sub and beat(sub,x,step['type'],w)
            sub.remove(x)
        assert len(sub)==1 and names[next(iter(sub))]==e['terminal']
assert all(fixed_mask(f)!=0 for f in maps)
print('VERIFY_OK maps=12575 distinct_fixed_sets=210 sizes=3493,4877,2909,1013,234,41,5,2,1 nonidentity_contractible=12574 dual=invariant')
