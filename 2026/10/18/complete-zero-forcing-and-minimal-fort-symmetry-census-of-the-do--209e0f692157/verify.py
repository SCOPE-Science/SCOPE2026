#!/usr/bin/env python3
"""Reconstruct the dodecahedral zero-forcing and fort orbit certificate.

Usage (in the folder containing the files):
    g++ -O3 -std=c++17 direct.cpp -o direct && ./direct
    g++ -O3 -std=c++17 fort.cpp -o fort && ./fort
    python3 verify.py
No non-standard Python modules are needed.
"""
import collections
import json
import struct

N=20
FULL=(1<<N)-1
adj=[set() for _ in range(N)]
for j in range(10):
    for a,b in ((j,(j+1)%10),(j,10+j),(10+j,10+(j+2)%10)):
        adj[a].add(b); adj[b].add(a)
assert len({tuple(sorted((a,b))) for a in range(N) for b in adj[a]}) == 30
assert all(len(x)==3 for x in adj)

with open('direct_status.bin','rb') as f: ddata=f.read()
with open('fort_status.bin','rb') as f: fdata=f.read()
assert len(ddata)==4*(1<<N) and len(fdata)==(1<<N)
status=list(struct.unpack('<'+str(1<<N)+'i',ddata))
assert status==list(fdata)
assert set(status)=={0,1}
assert sum(status)==804264
coeff=collections.Counter(m.bit_count() for m in range(1<<N) if status[m])
expected={6:2040,7:16900,8:62890,9:127480,10:168244,11:163560,12:125230,13:77460,14:38760,15:15504,16:4845,17:1140,18:190,19:20,20:1}
assert dict(coeff)==expected
print('CROSSCHECK_OK all_1048576_masks_agree=true total_forcing=804264')

minimal=set(int(m) for m in open('minimal_masks.txt'))
forts=set(int(m) for m in open('minfort_masks.txt'))
assert len(minimal)==3000 and len(forts)==830
assert all(status[m] and all(not status[m^(1<<v)] for v in range(N) if (m>>v)&1) for m in minimal)
# Forcing is upward-closed: deleting each vertex detects inclusion minimality.
assert all(not status[m] or any(status[m^(1<<v)] for v in range(N) if (m>>v)&1) or m in minimal for m in range(1<<N))
assert collections.Counter(m.bit_count() for m in minimal)=={6:2040,7:180,8:780}
assert collections.Counter(m.bit_count() for m in forts)=={7:60,8:20,9:200,10:410,11:120,12:20}
for m in forts:
    assert m
    for v in range(N):
        if (m>>v)&1:continue
        assert len(adj[v]&{i for i in range(N) if (m>>i)&1})!=1
print('MINIMALITY_OK minimal_forcing=3000 sizes=6:2040,7:180,8:780 minimal_forts=830')

perms=[]
def dfs(mapping,unused):
    if len(mapping)==N:
        perms.append(tuple(mapping[i] for i in range(N)))
        return
    best=None; vertex=None
    for v in range(N):
        if v in mapping:continue
        candidates=[w for w in unused if all((u in adj[v])==(mapping[u] in adj[w]) for u in mapping)]
        if not candidates:return
        if best is None or len(candidates)<len(best):best,vertex=candidates,v
        if len(candidates)==1:break
    for w in best:
        mapping[vertex]=w;unused.remove(w)
        dfs(mapping,unused)
        unused.add(w);del mapping[vertex]
dfs({},set(range(N)))
perms.sort()
assert len(perms)==120 and len(set(perms))==120
for p in perms:
    assert sorted(p)==list(range(N))
    for v in range(N):
        assert {p[u] for u in adj[v]}==adj[p[v]]

cert=json.load(open('orbit_certificate.json'))
assert cert['graph']=='GP(10,2)' and cert['automorphism_order']==120
assert cert['automorphisms']==[list(p) for p in perms]

def map_mask(mask,p):
    value=0
    for i in range(N):
        if mask>>i&1:value|=1<<p[i]
    return value

def check_orbits(label,allowed,spect):
    found=set()
    spectrum=collections.Counter()
    for o in cert[label]:
        mask=int(o['representative_mask'],16)
        assert mask.bit_count()==o['size']
        orbit={map_mask(mask,p) for p in perms}
        assert len(orbit)==o['orbit_size']
        assert orbit <= allowed and not orbit.intersection(found)
        found.update(orbit)
        spectrum[(o['size'],o['orbit_size'])]+=1
    assert found==allowed and dict(spectrum)==spect
    print('ORBITS_OK',label,'orbits=',len(cert[label]),'sets=',len(allowed),'spectrum=',dict(sorted(spectrum.items())))
check_orbits('minimal_zero_forcing_orbits',minimal,{(6,120):14,(6,60):6,(7,120):1,(7,60):1,(8,120):5,(8,60):3})
check_orbits('minimal_fort_orbits',forts,{(7,60):1,(8,15):1,(8,5):1,(9,120):1,(9,60):1,(9,20):1,(10,120):1,(10,60):3,(10,40):2,(10,30):1,(11,120):1,(12,20):1})
print('VERIFY_ALL_OK graph_vertices=20 edges=30 automorphism_order=120')
