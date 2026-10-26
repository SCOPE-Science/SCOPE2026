#!/usr/bin/env python3
"""Exact four-quantifier-rank classification of nonempty Hamming graphs.

Only standard-library Python is required. Computations are finite and exact;
see RESULT.md for the separate mathematical reduction to all parameters.
"""
from functools import lru_cache
from itertools import product
from hashlib import sha256
from collections import defaultdict
from math import prod

P3 = ('000', '001', '010', '011', '012')
P2 = ('00', '01')
CAPS = {2: {'000':2, '001':4, '010':4, '011':4},
        3: {'000':2, '001':3, '010':3, '011':3, '012':3},
        4: {'000':2, '001':3, '010':3, '011':3, '012':3}}


def option_vectors(q, pattern):
    symbols=set(pattern)
    assert len(symbols)<=q
    out={tuple(int(x!=a) for x in pattern) for a in symbols}
    if len(symbols)<q:
        out.add((1,1,1))
    return tuple(sorted(out))


def step(states, choices):
    return frozenset(tuple(min(2,a[i]+b[i]) for i in range(3))
                     for a in states for b in choices)


def test_transition_caps():
    initial=tuple(product(range(3), repeat=3))
    for q in (2,3,4):
        for p,cap in CAPS[q].items():
            choices=option_vectors(q,p)
            cur={s:frozenset((s,)) for s in initial}
            for _ in range(cap):
                cur={s:step(x,choices) for s,x in cur.items()}
            next_cur={s:step(x,choices) for s,x in cur.items()}
            assert cur==next_cur,(q,p,cap)
    print('TRANSITION_STATIONARITY_OK: all 27 starting states, all patterns and alphabets')


def orbit_signature(q,d):
    @lru_cache(None)
    def triple(c):
        atom=[]
        for i,j in ((0,1),(0,2),(1,2)):
            atom.append(min(2,sum(c[h] for h,p in enumerate(P3) if p[i]!=p[j])))
        states=frozenset(((0,0,0),))
        for i,p in enumerate(P3):
            if c[i] and len(set(p))>q:
                raise AssertionError('impossible tuple-column type')
            if not c[i]:
                continue
            choices=option_vectors(q,p)
            for _ in range(c[i]):
                states=step(states,choices)
        return (tuple(atom), tuple(sorted(states)))
    @lru_cache(None)
    def pair(t):
        same,diff=d-t,t
        signatures=set()
        for eq in range(same+1):
            for first in range(diff+1):
                for second in range(diff-first+1):
                    third=diff-first-second
                    if third and q==2:
                        continue
                    signatures.add(triple((eq,same-eq,first,second,third)))
        return (min(2,t),tuple(sorted(signatures)))
    return tuple(sorted(set(pair(t) for t in range(d+1))))


def verify_classification():
    classes=defaultdict(list)
    rows=[]
    for q in (2,3,4):
        for d in range(1,15):
            signature=orbit_signature(q,d)
            classes[signature].append((q,d))
            digest=sha256(repr(signature).encode('utf-8')).hexdigest()[:16]
            rows.append((q,d,len(signature),digest))
    assert len(classes)==16, len(classes)
    # Exhaustive rank-four back-and-forth profiles show these sharp cutoffs.
    for q,t in ((2,6),(3,5),(4,5)):
        assert all(orbit_signature(q,d)==orbit_signature(q,t) for d in range(t,15))
        assert all(orbit_signature(q,d)!=orbit_signature(q,t) for d in range(1,t))
    # The 16 class representatives are all inequivalent.
    representatives=[(2,d) for d in range(1,7)] + [(q,d) for q in (3,4) for d in range(1,6)]
    assert len(representatives)==16
    assert len({orbit_signature(q,d) for q,d in representatives})==16
    assert max(q**d for q,d in representatives)==1024
    for q,d in representatives:
        profile=orbit_signature(q,d)
        print('CLASS',q,d,'vertices',q**d,'pair_types',len(profile),
              'digest',sha256(repr(profile).encode()).hexdigest()[:16])
    print('FINITE_CLASSIFICATION_OK: 16 classes, all q=2,3,4 and d=1..14')
    return classes


def verify_direct_games():
    # Completely separate graph-level quantifier-type recursion. It never uses
    # coordinate columns, orbit counts or the optimized rank-four algorithm.
    type_ids={}
    def intern(key):
        if key not in type_ids:
            type_ids[key]=len(type_ids)
        return type_ids[key]
    def direct_type(q,d):
        words=list(product(range(q),repeat=d))
        n=len(words)
        adj={(i,j) for i,a in enumerate(words) for j,b in enumerate(words)
             if sum(x!=y for x,y in zip(a,b))==1}
        @lru_cache(None)
        def recurse(vertices,r):
            relation=tuple((int(vertices[i]==vertices[j]),int((vertices[i],vertices[j]) in adj))
                           for i in range(len(vertices)) for j in range(i+1,len(vertices)))
            if r==0:
                return intern(('atom',relation))
            children=tuple(sorted({recurse(vertices+(v,),r-1) for v in range(n)}))
            return intern(('lift',r,relation,children))
        return recurse((),4)
    samples=[(2,1),(2,2),(2,3),(2,4),(3,1),(3,2),(4,1),(4,2),(5,1)]
    direct={x:direct_type(*x) for x in samples}
    for a in samples:
        for b in samples:
            assert ((direct[a]==direct[b]) == (orbit_signature(*a)==orbit_signature(*b))),(a,b)
    print('DIRECT_GAME_COMPARISON_OK:',len(samples),'graphs,',len(samples)**2,'ordered comparisons')


if __name__=='__main__':
    test_transition_caps()
    verify_classification()
    verify_direct_games()
    print('VERIFY_OK')
