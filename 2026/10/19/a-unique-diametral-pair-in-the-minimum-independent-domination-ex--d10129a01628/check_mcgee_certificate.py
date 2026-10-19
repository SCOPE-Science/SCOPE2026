#!/usr/bin/env python3
"""Independent certificate checker: no third-party packages needed.
Run: python3 check_mcgee_certificate.py > checker_output.txt
"""
import collections
import itertools
import json
from collections import deque
from pathlib import Path

N=24
M=(1<<N)-1
c=json.loads(Path(__file__).with_name('mcgee_certificate.json').read_text(encoding='utf-8'))
assert c['graph']['vertex_count']==24
E={tuple(sorted(x)) for x in c['graph']['edges']}
assert len(E)==36 and all(0<=u<v<24 for u,v in E)
nb=[0]*N
for u,v in E:nb[u]|=1<<v;nb[v]|=1<<u
assert all(x.bit_count()==3 for x in nb)
# Construct an LCF graph afresh, using a separate edge-building rule.
L={tuple(sorted((u,(u+1)%N))) for u in range(N)}
for u in range(N):
    L.add(tuple(sorted((u,(u+(-12,7,-7)[u%3])%N))))
assert L==E

def candidate(s):
    return all(not((nb[v]&s) and (s>>v&1)) for v in range(N)) and all((s>>v&1) or nb[v]&s for v in range(N))

claimed=c['minimum_masks']
assert claimed==sorted(set(claimed)) and len(claimed)==146
for s in claimed:assert s.bit_count()==8 and candidate(s)
# Exhaustively check the entire search region below and at the reported optimum.
check=[]
for k in range(9):
    for bits in itertools.combinations(range(N),k):
        mask=sum(1<<x for x in bits)
        if candidate(mask):
            assert k==8
            check.append(mask)
assert sorted(check)==claimed
P={s:i for i,s in enumerate(claimed)}
expected=set()
for i,s in enumerate(claimed):
    for j in range(i+1,len(claimed)):
        t=claimed[j]
        if (s^t).bit_count()==2:
            a=(s&~t).bit_length()-1
            b=(t&~s).bit_length()-1
            assert nb[a]>>b&1, 'An optimal independent-dominating token jump must be a slide'
            expected.add((i,j))
assert [list(p) for p in sorted(expected)]==c['exchange_edges']
h=[[] for s in claimed]
for i,j in expected:h[i].append(j);h[j].append(i)
assert [len(row) for row in h]==c['exchange_degrees']
D=[]
for src in range(len(h)):
    d=[-1]*len(h);d[src]=0;q=deque([src])
    while q:
        u=q.popleft()
        for v in h[u]:
            if d[v]==-1:d[v]=d[u]+1;q.append(v)
    assert -1 not in d
    D.append(d)
assert [max(row) for row in D]==c['exchange_eccentricities']
assert (min(map(max,D)),max(map(max,D)))==(11,12)
assert [[i,j] for i in range(len(h)) for j in range(i+1,len(h)) if D[i][j]==12]==c['diametral_pairs']
assert c['diametral_pairs']==[[claimed.index(4793490),claimed.index(9586980)]]
triangles=sum(len(set(h[i])&set(h[j])) for i,j in expected)//3
assert triangles==0==c['triangles']
# Independently validate each supplied automorphism and orbit classification.
A=c['automorphisms']
assert len(A)==32 and len({tuple(a) for a in A})==32
for a in A:
    assert sorted(a)==list(range(N))
    assert {tuple(sorted((a[u],a[v]))) for u,v in E}==E
covered=set()
orbits=[]
for s in claimed:
    if s in covered:continue
    orb={sum(1<<a[u] for u in range(N) if s>>u&1) for a in A}
    assert orb<=P.keys() and not orb&covered
    covered|=orb
    orbits.append({'representative_mask':min(orb),'size':len(orb),
                   'degree':len(h[P[min(orb)]]),'eccentricity':max(D[P[min(orb)]])})
assert covered==set(claimed)
assert sorted(orbits,key=lambda x:x['representative_mask'])==c['orbits']
print('Certificate verified against LCF adjacency, complete size-at-most-eight search, all transitions, and all graph distances.')
print('minimum_sets:',len(claimed),'exchange_edges:',len(expected))
print('eccentricities:',dict(sorted(collections.Counter(map(max,D)).items())))
print('diametral_pairs:',[(claimed[i],claimed[j]) for i,j in c['diametral_pairs']])
print('automorphisms_verified:',len(A),'orbit_sizes:',sorted(x['size'] for x in orbits))
print('triangles:',triangles)
