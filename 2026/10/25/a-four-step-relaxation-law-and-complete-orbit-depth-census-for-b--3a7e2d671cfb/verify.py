#!/usr/bin/env python3
"""Exact checks for three-state deterministic Greenberg--Hastings dynamics on complete bipartite graphs."""
from itertools import product
from collections import Counter
import random

STATES=(0,1,2)
MASKS=(1,2,4,3,5,6,7)
PERIOD_DEPTH=(
 ((1,0),(1,3),(1,1),(1,4),(1,1),(1,4),(1,4)),
 ((1,3),(1,2),(1,2),(1,3),(1,3),(1,2),(1,3)),
 ((1,1),(1,2),(1,1),(1,2),(1,1),(1,2),(1,2)),
 ((1,4),(1,3),(1,2),(1,3),(4,0),(4,2),(4,3)),
 ((1,1),(1,3),(1,1),(4,0),(1,1),(4,1),(4,1)),
 ((1,4),(1,2),(1,2),(4,2),(4,1),(1,2),(4,2)),
 ((1,4),(1,3),(1,2),(4,3),(4,1),(4,2),(3,0))
)

def step(x,a):
    left=x[:a]
    right=x[a:]
    excite_left=(1 in left)
    excite_right=(1 in right)
    return tuple((z+1 if z==0 and excite_right else z) if z==0 else (z+1)%3 for z in left)+tuple((z+1 if z==0 and excite_left else z) if z==0 else (z+1)%3 for z in right)

def support(x):
    return sum(1<<z for z in set(x))

def macro_step(pair):
    a,b=pair
    aa=bb=0
    for c in STATES:
        if (a>>c)&1:
            new= 1 if c==0 and (b&2) else (0 if c==0 else (c+1)%3)
            aa |= 1<<new
        if (b>>c)&1:
            new= 1 if c==0 and (a&2) else (0 if c==0 else (c+1)%3)
            bb |= 1<<new
    return aa,bb

def temporal_type(x,a):
    seen={}
    z=x
    for i in range(50):
        if z in seen: return i-seen[z],seen[z]
        seen[z]=i
        z=step(z,a)
    raise AssertionError('Unexpectedly long orbit')

def type_from_macro(pair):
    seen={};q=pair
    while q not in seen:
        seen[q]=len(seen)
        q=macro_step(q)
    cyc=frozenset(k for k,d in seen.items() if d>=seen[q])
    if cyc==frozenset(((1,1),)):p=1
    elif cyc==frozenset(((7,7),)):p=3
    elif cyc==frozenset(((3,5),(5,3))):p=4
    else:raise AssertionError(('Unexpected macro cycle',cyc))
    return p,seen[q]

def pred_count(a,b):
    from math import comb
    def w(m,z):
        q=z.bit_count()
        return sum((-1)**j*comb(q,j)*(q-j)**m for j in range(q+1))
    out=Counter()
    for i,u in enumerate(MASKS):
        for j,v in enumerate(MASKS):
            out[PERIOD_DEPTH[i][j]]+=w(a,u)*w(b,v)
    return out

def symbolic_count(a,b):
    A,B=2**a,2**b
    P,Q=3**a,3**b
    U,V=A-2,P-3*A+3
    W,Z=B-2,Q-3*B+3
    return Counter({
        (1,0):1,
        (1,1):A*B-1,
        (1,2):A*B-2*A-2*B+P+Q+1,
        (1,3):A*B-3*A-3*B+P+Q+4,
        (1,4):P+Q-A-B-2,
        (3,0):V*Z,
        (4,0):2*U*W,
        (4,1):2*U*W+U*Z+V*W,
        (4,2):2*U*W+U*Z+V*W,
        (4,3):U*Z+V*W,
    })

def main():
    for i,u in enumerate(MASKS):
        for j,v in enumerate(MASKS):
            assert type_from_macro((u,v))==PERIOD_DEPTH[i][j],(u,v)
    brute=0
    for a in range(1,6):
        for b in range(1,6):
            if a+b>9:continue
            expected=pred_count(a,b)
            assert expected==symbolic_count(a,b),(a,b,expected,symbolic_count(a,b))
            assert sum(expected.values())==3**(a+b)
            got=Counter()
            for x in product(STATES,repeat=a+b):
                got[temporal_type(x,a)]+=1
                brute+=1
            assert got==+expected,(a,b,got,expected)
    rng=random.Random(20261021)
    random_cases=3000
    for z in range(random_cases):
        a=rng.randint(1,16);b=rng.randint(1,16)
        x=tuple(rng.choice(STATES) for _ in range(a+b))
        key=PERIOD_DEPTH[MASKS.index(support(x[:a]))][MASKS.index(support(x[a:]))]
        assert temporal_type(x,a)==key,(a,b,x,key)
    print(f'VERIFY_OK macro_pairs=49 exhaustive_states={brute} random_states={random_cases} support_table_and_all_formulas=verified')
if __name__=='__main__': main()
