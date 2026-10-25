#!/usr/bin/env python3
"""Independent explicit isomorphism witness between two Coxeter graph presentations."""
from itertools import combinations
import json
lines={frozenset((t,(t+1)%7,(t+3)%7)) for t in range(7)}
triples=[c for c in combinations(range(7),3) if frozenset(c) not in lines]
E1={frozenset((i,j)) for i in range(28) for j in range(i+1,28) if set(triples[i]).isdisjoint(triples[j])}
E2=set()
for t in range(7):
 for ring,step in enumerate((1,2,4)):
  a=7+7*ring+t
  E2.add(frozenset((t,a)))
  E2.add(frozenset((a,7+7*ring+(t+step)%7)))
mapping=[0, 19, 21, 22, 7, 16, 11, 27, 4, 18, 9, 13, 10, 12, 26, 6, 1, 17, 24, 5, 15, 25, 8, 2, 3, 14, 23, 20]
assert len(set(mapping))==28
assert {frozenset((mapping[x],mapping[y])) for x,y in (tuple(e) for e in E2)} == E1
print(json.dumps({'same_graph':True,'vertices':28,'edges':42,'isomorphism':mapping},sort_keys=True,separators=(',',':')))
