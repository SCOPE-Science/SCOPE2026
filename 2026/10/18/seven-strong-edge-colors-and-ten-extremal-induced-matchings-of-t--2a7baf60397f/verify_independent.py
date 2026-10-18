#!/usr/bin/env python3
"""Alternative Tutte--Coxeter strong-colouring verifier using maximal cliques.

Python standard library only. Execute: python3 verify_independent.py
"""
from itertools import combinations
from collections import Counter
import json
from pathlib import Path

DUADS=list(combinations(range(6),2))
SYN=sorted(tuple(DUADS[i] for i in indices) for indices in combinations(range(15),3)
           if len(set(v for i in indices for v in DUADS[i]))==6)
assert len(SYN)==15
EDGES=[(i,15+j) for i in range(15) for j,s in enumerate(SYN) if DUADS[i] in s]
assert len(EDGES)==45
CERT=json.loads(Path(__file__).with_name('CERTIFICATE.json').read_text(encoding='utf8'))
assert CERT['ordered_edges']==[list(e) for e in EDGES]
G=[set() for _ in range(30)]
for a,b in EDGES:G[a].add(b);G[b].add(a)
C=[set()for _ in range(45)]
for i,e in enumerate(EDGES):
    for j,f in enumerate(EDGES):
        if i!=j and all(u!=v and v not in G[u] for u in e for v in f):C[i].add(j)


COLOR=(0,6,1,3,6,4,0,1,4,6,2,0,5,2,0,2,3,4,0,5,4,2,5,3,1,6,5,2,4,6,5,3,1,4,6,3,2,0,6,4,0,1,5,1,6)
assert len(COLOR)==45 and set(COLOR)==set(range(7))
assert CERT['strong_seven_colors']==list(COLOR)
assert all(COLOR[i]!=COLOR[j] for i in range(45) for j in range(i) if j not in C[i])

def bron_kerbosch(R,P,X):
    if not P and not X:
        yield frozenset(R)
        return
    pivot=max(P|X,key=lambda v: len(P&C[v]),default=None)
    candidates=set(P) if pivot is None else P-C[pivot]
    for v in sorted(candidates):
        yield from bron_kerbosch(R|{v},P&C[v],X&C[v])
        P.remove(v);X.add(v)

maximal=list(bron_kerbosch(set(),set(range(45)),set()))
maximal_dist=Counter(map(len,maximal))
assert maximal_dist==Counter({5:3060,6:5520,7:360,9:10}),maximal_dist
maxima=sorted([c for c in maximal if len(c)==9],key=lambda x:sum(1<<i for i in x))
assert CERT['maximum_induced_matchings_as_edge_indices']==[sorted(x) for x in maxima]
assert len(maxima)==10 and all(len(x&y)==1 for i,x in enumerate(maxima)for y in maxima[:i])
assert Counter(sum(e in m for m in maxima) for e in range(45))==Counter({2:45})
all_subsets=set()
for clique in maximal:
    ordered=sorted(clique)
    for k in range(1,len(ordered)+1):
        all_subsets.update(map(frozenset,combinations(ordered,k)))
counts=Counter(map(len,all_subsets))
assert counts==Counter({1:45,2:720,3:5160,4:16920,5:22680,6:8520,7:720,8:90,9:10}),counts
seven=[c for c in all_subsets if len(c)==7]
assert len(seven)==720
checks=0
for a in maxima:
    for b in maxima:
        if a==b:continue
        removed=a| (b-a)
        R=set(range(45))-removed
        assert len(R)==28
        cand=[s for s in seven if s<=R]
        assert len(cand)==32
        # Four seven-element independent sets would have to partition R.
        # Check every unordered four-set among the 32 permitted candidates.
        for A,B,Cc,D in combinations(cand,4):
            assert len(A|B|Cc|D)<28
        checks+=1
assert checks==90
print('ALTERNATIVE maximal_induced_matchings_by_size',','.join('%d:%d'%(k,maximal_dist[k])for k in sorted(maximal_dist)))
print('ALTERNATIVE all_induced_matchings_by_size',','.join('%d:%d'%(k,counts[k])for k in sorted(counts)))
print('ALTERNATIVE maximum_size=9 count=10 pairwise_overlap=1 edge_multiplicity=2')
print('ALTERNATIVE six_color_obstructions=90 no_four_seven_set_covers')
print('ALTERNATIVE seven_color_certificate=VALID')
