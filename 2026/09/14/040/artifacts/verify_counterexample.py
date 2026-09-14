"""Independent verification of Bl2 reverse-mutation counterexample (j=2).

Two methods:
 (A) hand-derived closed forms for single/double mutation along v=(-1,0);
 (B) generic wall-crossing pullback code (mut2.py) cross-check.
Then proves no SL(2,Z) carries (W0,V0) to (W2,V2) via intersection-count invariant.
"""
from collections import Counter

W0 = {(1,0):1,(0,1):1,(-1,0):1,(0,-1):1,(-1,-1):1}
V0 = [(1,-1),(-1,1),(-1,0),(0,-1),(1,1)]

# Hand-computed double mutant along index 2 (v=(-1,0) then (1,0)):
# W1 = x + xy + y + 1/(xy) + 1/y ; V1 as below
# W2 = xy + y + 1/(xy) + 1/(xy^2) + 1/y ; V2 as below
W2_hand = {(1,1):1,(0,1):1,(-1,-1):1,(-1,-2):1,(0,-1):1}
V2_hand = [(2,-1),(-2,1),(-1,0),(1,-1),(0,1)]

import sys
sys.path.insert(0, '/srv/scope-research/rounds/2026-09-14-hands-on-first-light-01/workspaces/research/lane-20030/output/artifacts')
from mut2 import seed_mutate

W1, V1 = seed_mutate(W0, V0, 2)
W2, V2 = seed_mutate(W1, V1, 2)
assert W1 is not None and W2 is not None, 'mutations must stay Laurent'
assert dict(W2_hand) == dict(W2), f'hand W2 {sorted(W2_hand.items())} vs code {sorted(W2.items())}'
assert Counter(V2_hand) == Counter(V2), f'hand V2 {V2_hand} vs code {V2}'
print('cross-check OK')
print('W2 =', sorted(W2.items()))
print('V2 =', V2)

sW0 = set(W0.keys()); sW2 = set(W2.keys())
n0 = sum(1 for v in V0 if tuple(v) in sW0)
n2 = sum(1 for v in V2 if tuple(v) in sW2)
print(f'|V0 cap W0| = {n0}, |V2 cap W2| = {n2}')
assert n0 == 2 and n2 == 1, 'invariant counts'
print('inequivalence invariant holds: 2 != 1, no common SL(2,Z) can carry both W and V')

# Exhaustive backup: columns of any W0->W2 SL map lie in W2; enumerate.
cands = []
for c1 in sW2:
    for c2 in sW2:
        if c1[0]*c2[1]-c1[1]*c2[0] == 1:
            M = ((c1[0],c2[0]),(c1[1],c2[1]))  # columns c1,c2
            mapped = {(M[0][0]*a+M[0][1]*b, M[1][0]*a+M[1][1]*b): c for (a,b),c in W0.items()}
            if mapped == dict(W2):
                cands.append(M)
print(f'W-only SL maps W0->W2: {cands}')
ok = False
for M in cands:
    if Counter((M[0][0]*a+M[0][1]*b, M[1][0]*a+M[1][1]*b) for (a,b) in V0) == Counter(V2):
        ok = True
        print('simultaneous map found (unexpected):', M)
assert not ok, 'no simultaneous map'
print('exhaustive check confirms no simultaneous SL(2,Z) map')
