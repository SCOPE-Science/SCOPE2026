#!/usr/bin/env python3
"""Exact finite sanity tests for stable-extension diversity on directed paths/cycles."""
from itertools import product, combinations

def stable_sets(n, arcs):
    arcs=set(arcs)
    result=[]
    for mask in range(1<<n):
        s={i for i in range(n) if mask&(1<<i)}
        if any(u in s and v in s for u,v in arcs):
            continue
        if all(v in s or any(u in s and (u,v) in arcs for u in range(n)) for v in range(n)):
            result.append(mask)
    return result

def arcs_of_components(parts):
    arcs=[]; offset=0
    for typ,length in parts:
        if typ=='path':
            arcs.extend((offset+i,offset+i+1) for i in range(length-1))
        elif typ=='cycle':
            arcs.extend((offset+i,offset+(i+1)%length) for i in range(length))
        else: raise ValueError(typ)
        offset+=length
    return offset,arcs

def partition_value(weights):
    W=sum(weights)
    states={(0,0)}; sofar=0
    for w in weights:
        states={(a+w,b) for a,b in states}|{(a,b+w) for a,b in states}|set(states)
        sofar+=w
    return W-min(max(a,b,W-a-b) for a,b in states) if len(weights)>=2 else None

def brute_value(extensions):
    if len(extensions)<3: return None
    return max(min((a^b).bit_count(),(a^c).bit_count(),(b^c).bit_count())
               for a,b,c in combinations(extensions,3))

checks=0
for parts in ([('cycle',2),('cycle',2)], [('cycle',2),('cycle',4)],
              [('cycle',2),('cycle',6)], [('path',3),('cycle',2),('cycle',4)],
              [('cycle',3)], [('path',2),('cycle',3),('cycle',2)],
              [('cycle',2),('cycle',2),('cycle',2)],
              [('cycle',4),('cycle',4)], [('path',3),('path',2)]):
    n,arcs=arcs_of_components(parts)
    if n>14: continue
    stable=stable_sets(n,arcs)
    odds=any(typ=='cycle' and length%2 for typ,length in parts)
    weights=[length for typ,length in parts if typ=='cycle' and length%2==0]
    predicted=0 if odds else (1<<len(weights))
    assert len(stable)==predicted,(parts,len(stable),predicted)
    expected=None if odds else partition_value(weights)
    actual=brute_value(stable)
    assert actual==expected,(parts,actual,expected)
    checks+=1
for weights in product([2,4,6],repeat=3):
    W=sum(weights)
    if W>16:continue
    n,arcs=arcs_of_components([('cycle',w) for w in weights])
    vals=stable_sets(n,arcs)
    assert len(vals)==8
    assert partition_value(weights)==brute_value(vals)
    checks+=1
print(f'PASS {checks} exact stable-extension/three-diversity tests')
