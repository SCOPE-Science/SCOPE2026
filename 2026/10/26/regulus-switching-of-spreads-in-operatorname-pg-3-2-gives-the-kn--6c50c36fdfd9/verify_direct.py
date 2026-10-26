#!/usr/bin/env python3
"""Independent, direct five-line enumeration of the PG(3,2) spread switch graph.

No dependency on the primary verifier; Python standard library only.
"""
from itertools import combinations
from collections import Counter,deque
import hashlib,json

P=list(range(1,16))
lines=sorted({frozenset((a,b,a^b)) for a in P for b in P if a!=b}, key=lambda z:tuple(sorted(z)))
assert len(lines)==35 and all(len(l)==3 for l in lines)
# This brute-force loop considers all 35-choose-5 five-line selections.
spread_list=[]
for ids in combinations(range(35),5):
    if len(set().union(*(lines[i] for i in ids)))==15:
        spread_list.append(ids)
assert len(spread_list)==56
spreads=set(spread_list)
pair_profile=Counter(); neighbours={s:set() for s in spreads}
for a,b in combinations(spread_list,2):
    common=len(set(a)&set(b))
    pair_profile[common]+=1
    if common==2:
        neighbours[a].add(b);neighbours[b].add(a)
assert pair_profile == {0:840,1:420,2:280}
assert {len(neighbours[s]) for s in spreads}=={10}
mutual=Counter(); lengths=Counter()
for a,b in combinations(spread_list,2):
    c=len(set(a)&set(b))
    mn=len(neighbours[a]&neighbours[b]);mutual[(c,mn)]+=1
    lengths[1 if b in neighbours[a] else 2]+=1
assert mutual=={(0,1):840,(1,4):420,(2,0):280}
assert lengths=={1:280,2:1260}
# The explicit line-cover claim: for every possible 3-line deletion from a
# spread, the other cover of the same nine points is unique.
cover_count=Counter()
for s in spread_list:
    for subset in combinations(s,3):
        nine=set().union(*(lines[i] for i in subset))
        opts=[]
        for triple in combinations(range(35),3):
            if set().union(*(lines[i] for i in triple))==nine:
                opts.append(triple)
        assert len(opts)==2
        cover_count[len(opts)]+=1
assert cover_count=={2:560}
print('BRUTE_FIVE_LINE_COMBINATIONS=324632')
print('SPREADS=56; ADJACENT_SPREAD_PAIRS=280')
print('SHARED_LINE_PROFILE='+json.dumps(dict(sorted(pair_profile.items()))))
print('COMMON_NEIGHBOR_PROFILE='+json.dumps({str(x):y for x,y in sorted(mutual.items())}))
print('TRIPLE_REPLACEMENT_COUNTS='+json.dumps(dict(cover_count)))
print('DIAMETER=2; PAIRS_AT_DISTANCE_1=280; PAIRS_AT_DISTANCE_2=1260')
print('PASS')
