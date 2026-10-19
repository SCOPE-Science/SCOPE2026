#!/usr/bin/env python3
"""Bit-mask/arc-partition reconstruction of the weak-coloring exchange graph of AG(2,3)."""
import hashlib
import itertools
import json
from collections import Counter, deque

# The twelve blocks of the Steiner triple system of order nine in row-major labels.
BLOCKS = (
    (0,1,2), (3,4,5), (6,7,8),
    (0,3,6), (1,4,7), (2,5,8),
    (0,4,8), (1,5,6), (2,3,7),
    (0,5,7), (1,3,8), (2,4,6)
)
assert len(set(tuple(sorted(x)) for x in BLOCKS)) == 12
linebits = [sum(1 << i for i in line) for line in BLOCKS]
allbits = (1 << 9) - 1

def arc(mask):
    return all(mask & line != line for line in linebits)

arcs = {m for m in range(1 << 9) if arc(m)}
partitions = []
# Any weak coloring is a partition into three labeled independent point sets.
for a in sorted(arcs):
    for b in sorted(arcs):
        if a & b: continue
        c = allbits ^ (a | b)
        if c in arcs:
            partitions.append((a,b,c))

def asword(part):
    return tuple(next(k for k in range(3) if (part[k] >> i) & 1) for i in range(9))

V = sorted(asword(t) for t in partitions)
assert len(V) == len(set(V))
id_by_mask = {p:i for i,p in enumerate(sorted(partitions,key=asword))}
mask_states = sorted(partitions,key=asword)
state_index = {p:i for i,p in enumerate(mask_states)}
E=set();adj=[set() for _ in mask_states]
for i, (a,b,c) in enumerate(mask_states):
    labels = [a,b,c]
    for source_color in range(3):
        active=labels[source_color]
        while active:
            move = active & -active
            active ^= move
            for target_color in range(3):
                if target_color==source_color:continue
                new = list(labels)
                new[source_color] ^= move
                new[target_color] |= move
                if new[target_color] in arcs:
                    j = state_index[tuple(new)]
                    adj[i].add(j)
                    E.add((min(i,j), max(i,j)))
for i in range(len(V)):
    assert all(i in adj[j] for j in adj[i])
E=sorted(E)
kinds=Counter()
for s in mask_states:
    kinds[tuple(sorted(x.bit_count() for x in s if x))]+=1
bicolor=[i for i,s in enumerate(mask_states) if tuple(sorted(x.bit_count() for x in s if x))==(1,4,4)]
bicolor_set=set(bicolor)
ecc=Counter();kind_ecc=Counter();dis=Counter();diam_pair=None
for s in range(len(V)):
    d=[-1]*len(V)
    d[s]=0
    Q=deque([s])
    while Q:
        x=Q.popleft()
        for y in adj[x]:
            if d[y] == -1:
                d[y]=d[x]+1
                Q.append(y)
    assert -1 not in d
    ex=max(d)
    ecc[ex]+=1
    k=tuple(sorted(x.bit_count() for x in mask_states[s] if x))
    kind_ecc[k,ex]+=1
    if diam_pair is None and ex==10:
        diam_pair=(V[s],V[d.index(10)])
    if s in bicolor_set:
        for t in bicolor:
            if t>s: dis[d[t]]+=1
vertices_blob='\n'.join(''.join(map(str,c)) for c in V)+'\n'
edges_blob='\n'.join(f'{a},{b}' for a,b in E)+'\n'
summary={
    'lines': len(BLOCKS),
    'valid_two_colorings':sum(1 for a in arcs if (allbits ^ a) in arcs),
    'valid_three_colorings':len(V), 'edges':len(E),
    'degrees':{str(k):v for k,v in sorted(Counter(map(len,adj)).items())},
    'color_class_sizes':{'-'.join(map(str,k)):v for k,v in sorted(kinds.items())},
    'eccentricities':{str(k):v for k,v in sorted(ecc.items())},
    'eccentricity_by_type':{'-'.join(map(str,k))+'|'+str(e):v for (k,e),v in sorted(kind_ecc.items())},
    'bicoloring_distances':{str(k):v for k,v in sorted(dis.items())},
    'radius':min(ecc), 'diameter':max(ecc), 'connected_components':1,
    'diameter_witness':[''.join(map(str,c)) for c in diam_pair],
    'vertices_sha256':hashlib.sha256(vertices_blob.encode()).hexdigest(),
    'edges_sha256':hashlib.sha256(edges_blob.encode()).hexdigest()
}
assert summary['valid_three_colorings']==3762 and summary['edges']==16848
assert summary['valid_two_colorings']==0
assert summary['degrees']=={'8':162,'9':3600}
assert summary['eccentricities']=={'9':3456,'10':306}
print(json.dumps(summary,sort_keys=True,separators=(',',':')))
print('VERIFY_OK')
