#!/usr/bin/env python3
"""Independent exhaustive Ehrenfeucht--Fraisse type recursion.
Uses only the named-zero relational multiplication atomic diagrams; no reduced 8-bit criteria.
"""
from itertools import product

def theory(q):
    types={}
    children={}
    def atomic(t,p):
        a=p+(t,)
        return (tuple(a[i]==a[j] for i in range(len(a)) for j in range(i+1,len(a))),
                tuple(min(t,u+v)==w for u in a for v in a for w in a))
    for depth in range(q,-1,-1):
        for t in (16,20):
            for p in product(range(1,t+1),repeat=depth):
                base=atomic(t,p)
                if depth<q:
                    pattern=(base,tuple(sorted(set(children[(t,p+(y,))] for y in range(1,t+1)))))
                else: pattern=(base,)
                key=(depth,pattern)
                if key not in types:types[key]=len(types)
                children[(t,p)]=types[key]
    return children[(16,())]==children[(20,())], len(types)
assert theory(1)[0]
assert theory(2)[0]
assert not theory(3)[0]
for q in (1,2,3):print('quantifier rank',q,'equivalent?',theory(q)[0],'type signatures',theory(q)[1])
print('Independent full-atomic-game check PASS')
