#!/usr/bin/env python3
"""Exact finite meta-classification for six weak-modal principles.

Checks complete enumerations of the parameter sets and three-world neighborhoods.
The nine one-world syntactic witness profiles are established in RESULT.md by
all-formula arguments; here they are used as mathematically proved inputs.
"""
from itertools import combinations
P = set('EGMCNK')

def closure(s):
    s = set(s)
    while True:
        old = set(s)
        if 'G' in s: s.add('N')
        if {'E','N'} <= s: s.add('G')
        if {'G','K'} <= s: s |= P
        if {'E','M','C'} <= s: s.add('K')
        if {'E','M','K'} <= s: s.add('C')
        if s == old: return frozenset(s)

def neighborhood_features(f):
    U = range(8)
    M = all(((a & b) not in f or (a in f and b in f)) for a in U for b in U)
    C = all((a not in f or b not in f or (a & b) in f) for a in U for b in U)
    N = 7 in f
    K = all((((7 ^ a) | b) not in f or a not in f or b in f) for a in U for b in U)
    return frozenset('E' + ('G' if N else '') + ('M' if M else '') +
                     ('C' if C else '') + ('N' if N else '') + ('K' if K else ''))

families = [frozenset(i for i in range(8) if bm & (1 << i)) for bm in range(256)]
profile_witness = {}
for f in families:
    profile_witness.setdefault(neighborhood_features(f), f)
assert len(profile_witness) == 9
expected_neighborhood = {
    'E':(3,4),'CE':(0,3,4),'CEK':(0,),'CEGN':(0,7),
    'EK':(1,2),'CEKM':(), 'CEGKMN':(7,),
    'EGMN':(3,5,7),'EGN':(1,2,7),
}
for text, codes in expected_neighborhood.items():
    assert neighborhood_features(set(codes)) == frozenset(text), (text, codes)
assert {frozenset(x) for x in expected_neighborhood} == set(profile_witness)

syntactic_profiles = [frozenset(x) for x in
    ['GMCN','GCN','GMN','CNK','MNK','MCN','MCNK','EMCK','MCK']]
allsets = {frozenset(xs) for r in range(7) for xs in combinations(sorted(P),r)}
assert len(allsets) == 64
closed = {closure(s) for s in allsets}
assert len(closed) == 30
assert all(closure(s) == s for s in closed)
assert all(s <= closure(s) for s in allsets)
witnesses = set(profile_witness) | set(syntactic_profiles)
assert len(witnesses) == 17
for s in closed:
    for p in P-s:
        matching = [w for w in witnesses if s <= w and p not in w]
        assert matching, (s,p)
for a in allsets:
    for b in allsets:
        implication = closure(b) <= closure(a)
        witness_test = all(not (a <= w and not b <= w) for w in witnesses)
        assert implication == witness_test, (a,b)
assert len({closure(s) for s in allsets}) == 30
print('WEAK_MODAL_30_VERIFY_OK')
