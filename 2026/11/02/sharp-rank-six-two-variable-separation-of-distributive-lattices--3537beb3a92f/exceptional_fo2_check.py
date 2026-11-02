#!/usr/bin/env python3
"""Independent direct Hintikka-type check of the two depth-five collisions."""
PAIRS=[((112,80,96,0,0,0,0),(112,112,96,0,0,0,0)),
       ((124,120,64,96,96,0,0),(124,120,64,112,96,0,0))]

def lower_sets(out):
    n=len(out);lower=[sum(1<<j for j in range(n) if out[j]>>i&1) for i in range(n)]
    return [s for s in range(1<<n) if not any(s>>i&1 and (s&lower[i])!=lower[i] for i in range(n))]

def pair_relation(a,b):
    if a==b:return '='
    if a&b==a:return '<'
    if a&b==b:return '>'
    return '#'

def signatures(posets):
    Ds=[lower_sets(p) for p in posets];codes=[[0]*len(d)for d in Ds]
    out=[]
    for q in range(1,7):
        if q>1:
            forms=[[frozenset((pair_relation(a,b),codes[i][j])for j,b in enumerate(D)) for a in D]for i,D in enumerate(Ds)]
            universe=sorted(set(f for row in forms for f in row),key=lambda f:tuple(sorted(f)))
            names={s:j for j,s in enumerate(universe)}
            codes=[[names[s] for s in row]for row in forms]
        roots=[frozenset(c) for c in codes]
        out.append((roots[0]==roots[1],roots[2]==roots[3]))
    return out, [len(d)for d in Ds]

states,sizes=signatures([p for pair in PAIRS for p in pair]);assert states[-2]==(True,True);assert states[-1]==(False,False),states
print('witness_lattice_sizes',sizes)
print('pair_equivalences_by_sentence_rank_1_to_6',states)
print('PASS depth-five equivalence and depth-six distinction for both exceptional pairs')
