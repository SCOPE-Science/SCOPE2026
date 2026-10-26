#!/usr/bin/env python3
"""Exhaustive small-rank check for idempotents in block-preserving Catalan-character monoids."""
from collections import Counter
from itertools import product
from math import comb

def symbolic(k,d):
    E=[Counter({0:1})]
    for i in range(1,k+1):
        p=Counter()
        for m in range(1,i+1):
            for r in range(1,d+1):
                weight=comb(d,r)*r**(d*m-r)
                for s,count in E[i-m].items():
                    p[s+r]+=count*weight
        E.append(p)
    return E[k]

def direct(k,d):
    if not k: return Counter({0:1})
    out=Counter()
    chars=(v for v in product(range(k),repeat=k) if all(v[j]<=j for j in range(k)) and all(v[j]<=v[j+1] for j in range(k-1)))
    for ch in chars:
        # each source point of block i maps to one of d points in block ch[i]
        offsets=tuple(d*ch[i//d] for i in range(k*d))
        for local in product(range(d), repeat=k*d):
            f=tuple(offsets[i]+local[i] for i in range(k*d))
            if all(f[f[i]]==f[i] for i in range(k*d)):
                out[len(set(f))]+=1
    return out

def run():
    cases=[(k,d) for d in (1,2,3) for k in range(0,4)] + [(2,4)]
    for k,d in cases:
        predicted=symbolic(k,d)
        actual=direct(k,d)
        assert predicted==actual,(k,d,predicted,actual)
        print(f'OK d={d}, k={k}, polynomial={dict(sorted(actual.items()))}, total={sum(actual.values())}')
    assert symbolic(2,2)==Counter({1:2,2:8,3:4,4:1})
    print('VERIFY_OK')
if __name__=='__main__': run()
