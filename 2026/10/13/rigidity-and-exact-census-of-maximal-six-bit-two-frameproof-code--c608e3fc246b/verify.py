#!/usr/bin/env python3
"""Exact independent enumeration for binary length-six two-frameproof codes."""
from itertools import combinations, permutations

L=6
Q=1<<L

def acceptable(code, word):
    # For every pre-existing pair and each possible framed word,
    # all three directed non-descendancy conditions must hold.
    for u,v in combinations(code,2):
        if not ((u^v)&(word^v)): return False # v is not a descendant of u and word
        if not ((u^v)&(word^u)): return False # u is not a descendant of v and word
        if not ((u^word)&(v^word)): return False # word is not a descendant of u and v
    return True

def enumerate_codes(target):
    answer=[]
    def grow(code,start):
        if len(code)==target:
            answer.append(tuple(code))
            return
        if Q-start<target-len(code): return
        for word in range(start,Q):
            if acceptable(code,word):
                grow(code+[word],word+1)
    grow([0],1)
    return answer

codes8=enumerate_codes(8)
codes9=enumerate_codes(9)
assert len(codes8)==30,(len(codes8),codes8[:2])
assert not codes9
for code in codes8:
    C=set(code)
    assert C=={x^y for x in C for y in C}
    assert [sum(x.bit_count()==i for x in code) for i in range(7)]==[1,0,0,4,3,0,0]

allcodes={tuple(sorted(x^translation for x in code)) for code in codes8 for translation in range(Q)}
assert len(allcodes)==240

def relabel(x,p):
    return sum(((x>>i)&1)<<p[i] for i in range(L))
seed=codes8[0]
orbit={tuple(sorted(relabel(x,p)^t for x in seed)) for p in permutations(range(L)) for t in range(Q)}
assert orbit==allcodes
print('VERIFY_OK max_size=8 zero_containing=30 total=240 affine_orbits=1 no_size9')
