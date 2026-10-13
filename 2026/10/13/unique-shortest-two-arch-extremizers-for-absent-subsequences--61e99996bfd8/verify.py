#!/usr/bin/env python3
from itertools import permutations, combinations
from math import comb, factorial
from pathlib import Path
import json

def subsequences3(w):
    return {tuple(w[i] for i in I) for I in combinations(range(len(w)),3)}

def predicted(sigma,q):
    pos={x:i for i,x in enumerate(q)}
    A=sum(pos[a]<pos[b] for a in range(sigma) for b in range(a+1,sigma))
    E=0
    good={(0,1,2),(0,2,1),(1,0,2)}
    for a,b,c in combinations(range(sigma),3):
        triple=(a,b,c)
        order=tuple(sorted(range(3), key=lambda i: pos[triple[i]]))
        if order in good:
            E+=1
    return 3*comb(sigma,2)+A+4*comb(sigma,3)+E, A, E

# Local tables used in the proof.
pair_counts={}
for q in permutations((0,1)):
    pair_counts[q]=len({u for u in subsequences3((0,1)+q) if len(set(u))==2})
assert pair_counts=={(0,1):4,(1,0):3}

triple_counts={}
for q in permutations((0,1,2)):
    triple_counts[q]=len({u for u in subsequences3((0,1,2)+q) if len(set(u))==3})
assert triple_counts=={
    (0,1,2):5,(0,2,1):5,(1,0,2):5,
    (1,2,0):4,(2,0,1):4,(2,1,0):4
}

# Exhaustive fixed-first-arch verification through sigma=8.
summary={}
for sigma in range(2,9):
    P=tuple(range(sigma))
    minimum=None
    extremizers=[]
    checked=0
    for Q in permutations(range(sigma)):
        direct=len(subsequences3(P+Q))
        formula,A,E=predicted(sigma,Q)
        assert direct==formula,(sigma,Q,direct,formula,A,E)
        if minimum is None or direct<minimum:
            minimum=direct
            extremizers=[Q]
        elif direct==minimum:
            extremizers.append(Q)
        checked+=1
    target=3*comb(sigma,2)+4*comb(sigma,3)
    assert minimum==target
    assert extremizers==[P[::-1]]
    summary[sigma]={"permutations_checked":checked,"minimum":minimum}

# Full labeled census for sigma=4 and sigma=5.
for sigma in (4,5):
    alph=tuple(range(sigma))
    target=3*comb(sigma,2)+4*comb(sigma,3)
    ex=0
    total=0
    for P in permutations(alph):
        # relabel by the order in P and check every second arch directly
        rank={x:i for i,x in enumerate(P)}
        for Q in permutations(alph):
            normalized=tuple(rank[x] for x in Q)
            direct=len(subsequences3(tuple(range(sigma))+normalized))
            if direct==target:
                ex+=1
                assert Q==P[::-1]
            total+=1
    assert ex==factorial(sigma)
    assert total==factorial(sigma)**2

cert=json.loads((Path(__file__).resolve().parent/"certificate.json").read_text())
assert cert["source_primary_msc"]=="68R15"
assert cert["classification"]=="exactly P P^R for permutations P of the alphabet"

print("VERIFY_OK local_pair_table=3/4 local_triple_table=4/5 "
      "fixed_first_exhaustive_sigma=2..8 unique_reverse=1 "
      "full_labeled_sigma=4,5 extremizers=sigma_factorial "
      "formula=3C2+A+4C3+E")
