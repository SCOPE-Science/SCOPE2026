#!/usr/bin/env python3
import json
from pathlib import Path
from functools import lru_cache

Z=(0,0,0)
E=((1,0,0),(0,1,0),(0,0,1))
LM=(Z,)+E

def add(a,b): return tuple(a[i]+b[i] for i in range(3))

LINEAR=[]
for mask in range(1,16):
    LINEAR.append(frozenset(LM[i] for i in range(4) if (mask>>i)&1))
INDEX={s:i for i,s in enumerate(LINEAR)}
VARS=[INDEX[frozenset([e])] for e in E]

@lru_cache(None)
def requirements(ft):
    F=set(ft)
    out=[]
    for p in F:
        m=0
        for j,g in enumerate(LINEAR):
            for q in g:
                u=tuple(p[i]-q[i] for i in range(3))
                if min(u)<0:
                    continue
                if {add(u,r) for r in g}.issubset(F):
                    m |= 1<<j
                    break
        out.append(m)
    return tuple(out)

def belongs(F, generators):
    if not F:
        return True
    return all(generators & m for m in requirements(tuple(sorted(F))))

def closure(generators):
    c=0
    for i,F in enumerate(LINEAR):
        if belongs(F,generators):
            c |= 1<<i
    return c

def mul(F,G):
    return frozenset(add(a,b) for a in F for b in G)

closures={}
for generators in range(1<<15):
    c=closure(generators)
    closures.setdefault(c,generators)

variable_closures=set()
for mask in range(8):
    g=0
    for j,i in enumerate(VARS):
        if (mask>>j)&1:
            g |= 1<<i
    variable_closures.add(closure(g))

targets=[]
for c in closures:
    contains_one=bool(c & 1)
    contains_all_variables=all(c & (1<<i) for i in VARS)
    if not contains_one and not contains_all_variables and c not in variable_closures:
        targets.append(c)

data=json.loads(Path(__file__).with_name("witnesses.json").read_text(encoding="utf-8"))
W=data["witnesses"]
assert data["target_count"]==1721
assert len(closures)==1748
assert len(variable_closures)==8
assert len(targets)==1721
assert set(map(str,targets))==set(W)

max_factor_degree=0
max_product_degree=0
for c in targets:
    rec=W[str(c)]
    F=frozenset(tuple(x) for x in rec["f"])
    G=frozenset(tuple(x) for x in rec["g"])
    P=mul(F,G)
    assert not belongs(F,c)
    assert not belongs(G,c)
    assert belongs(P,c)
    max_factor_degree=max(max_factor_degree,max(sum(m) for m in F|G))
    max_product_degree=max(max_product_degree,max(sum(m) for m in P))

print("linear_polynomials=15")
print("generating_subsets=32768")
print("distinct_linear_generated_ideals=1748")
print("variable_generated_closures=8")
print("nonprime_target_closures=1721")
print("all_witnesses_checked=1721")
print("max_factor_degree=%d" % max_factor_degree)
print("max_product_degree=%d" % max_product_degree)
print("CHECK_OK")
