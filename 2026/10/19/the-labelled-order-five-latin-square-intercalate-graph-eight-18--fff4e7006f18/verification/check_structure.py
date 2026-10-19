#!/usr/bin/env python3
"""Check isotopy transitivity and vertex-transitive component distances.

Input records are 25 symbols and one component tag, in lexical order.
"""
import collections
import itertools
import json
import sys

b=open(sys.argv[1] if len(sys.argv)>1 else 'latin5_components.bin','rb').read()
assert len(b)==4193280
records=[b[i:i+26] for i in range(0,len(b),26)]
assert all(records[i][:25]<records[i+1][:25] for i in range(len(records)-1))
S={row[:25]:row[25] for row in records}
assert len(S)==161280

def normalize(x):
    lab=[None]*5
    for c in range(5):lab[x[c]]=c
    y=bytes(lab[t] for t in x)
    return b''.join(sorted([y[r*5:r*5+5] for r in range(5)], key=lambda row:row[0]))

reduced_mobile={normalize(k) for k,v in S.items() if v!=0}
reduced_frozen={normalize(k) for k,v in S.items() if v==0}
assert len(reduced_mobile)==50 and len(reduced_frozen)==6

p=list(itertools.permutations(range(5)))
def isotopy_reduced_orbit(seed):
    ans=set()
    for rp in p:
        for cp in p:
            y=bytes(seed[5*rp[r]+cp[c]] for r in range(5) for c in range(5))
            ans.add(normalize(y))
    return ans

mob=next(k for k,v in S.items() if v!=0)
fro=next(k for k,v in S.items() if v==0)
assert isotopy_reduced_orbit(mob)==reduced_mobile
assert isotopy_reduced_orbit(fro)==reduced_frozen

def neighbours(x):
    for r in range(5):
        for rr in range(r+1,5):
            for c in range(5):
                for cc in range(c+1,5):
                    a=5*r+c;bb=5*r+cc;d=5*rr+c;dd=5*rr+cc
                    if x[a]==x[dd] and x[bb]==x[d]:
                        q=bytearray(x)
                        q[a],q[bb]=q[bb],q[a];q[d],q[dd]=q[dd],q[d]
                        yield bytes(q)

hist=[]
for tag in range(1,9):
    root=next(x for x,v in S.items() if v==tag)
    dist={root:0};todo=collections.deque((root,))
    while todo:
        a=todo.popleft()
        for c in neighbours(a):
            assert S[c]==tag
            if c not in dist:
                dist[c]=dist[a]+1;todo.append(c)
    assert len(dist)==18000
    d=collections.Counter(dist.values())
    hist.append([d[i] for i in range(1+max(d))])
assert all(a==hist[0] for a in hist)
print(json.dumps({'reduced_mobile_isotopy_class_size':50,
  'reduced_frozen_isotopy_class_size':6,
  'mobile_components_transitive_via_isotopy':True,
  'mobile_component_order':18000,
  'mobile_component_radius':len(hist[0])-1,
  'mobile_component_diameter':len(hist[0])-1,
  'distance_distribution':hist[0]},sort_keys=True,indent=2))
