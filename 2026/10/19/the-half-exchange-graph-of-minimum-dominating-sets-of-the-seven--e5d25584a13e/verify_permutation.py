#!/usr/bin/env python3
"""Independent parity-check and permutation enumeration, validating the saved certificate."""
import hashlib,itertools,json,sys
from collections import deque,Counter
if len(sys.argv)!=2:raise SystemExit('usage verify_permutation.py certificate.json')
certificate=open(sys.argv[1],'rb').read()
data=json.loads(certificate)
H=[]
for w in range(128):
    syndrome=0
    for i in range(7):
        if w>>i&1:syndrome^=i+1
    if syndrome==0:H.append(w)
assert len(H)==16
allcodes=set()
for p in itertools.permutations(range(7)):
    T=[sum(1<<p[i] for i in range(7) if word>>i&1) for word in H]
    for a in range(128):
        allcodes.add(tuple(sorted(w^a for w in T)))
codes=sorted(allcodes)
assert len(codes)==240
assert codes==[tuple(c) for c in data['codes']]
edge_list=[]; counts=Counter()
for i in range(240):
    for j in range(i+1,240):
        common=len(set(codes[i])&set(codes[j]));counts[common]+=1
        if common==8:edge_list.append([i,j])
assert edge_list==data['edges']
assert dict(counts)=={0:12600,2:7680,4:6720,8:1680}
# Independent distance via matrix-style synchronous neighborhood expansion.
adj=[set() for _ in codes]
for i,j in edge_list:adj[i].add(j);adj[j].add(i)
assert all(len(x)==14 for x in adj)
for x in range(240):
    frontier={x};reached={x};profile=[1]
    while frontier:
        nxt=set.union(set(),*(adj[y] for y in frontier))-reached
        if not nxt:break
        profile.append(len(nxt));reached|=nxt;frontier=nxt
    assert profile==[1,14,63,106,56] and len(reached)==240
print('PERMUTATION_OK 240_CODES 1680_EDGES 14_REGULAR DIAMETER_4')
print('INTERSECTIONS '+ ' '.join(f'{k}:{counts[k]}' for k in sorted(counts)))
print('DISTANCE_SPHERES 1 14 63 106 56')
print('CERTIFICATE_SHA256',hashlib.sha256(certificate).hexdigest())
