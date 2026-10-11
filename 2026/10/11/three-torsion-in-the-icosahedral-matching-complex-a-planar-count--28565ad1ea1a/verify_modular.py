#!/usr/bin/env python3
"""Independent standard-library simplicial boundary-rank check.
Constructs the icosahedron by explicit edges and uses tuple faces rather than
bit-mask Morse cells. The output is not a substitute for integral verification.
"""
from itertools import combinations
# Standard icosahedron on two staggered pentagons and two apices.
E=[(0,1),(0,2),(0,3),(0,4),(0,5),
   (1,2),(1,5),(1,6),(1,10),
   (2,3),(2,6),(2,7),
   (3,4),(3,7),(3,8),
   (4,5),(4,8),(4,9),
   (5,9),(5,10),
   (6,7),(6,10),(6,11),
   (7,8),(7,11),(8,9),(8,11),(9,10),(9,11),(10,11)]
assert E==sorted(E)
assert len(set(E))==30
can_follow=[[not (set(E[i])&set(E[j])) for j in range(30)] for i in range(30)]
levels=[[(i,) for i in range(30)]]
for k in range(2,7):
    levels.append([c+(j,) for c in levels[-1] for j in range(c[-1]+1,30)
                   if all(can_follow[j][i] for i in c)])
assert list(map(len,levels))==[30,315,1400,2535,1482,125]

def modular_rank(k,p):
    lower={t:i for i,t in enumerate(levels[k-1])}
    basis={}
    for f in levels[k]:
        col={lower[f[:i]+f[i+1:]]:(-1 if i%2 else 1)%p for i in range(len(f))}
        while col:
            pivot=max(col)
            if pivot not in basis:
                inv=pow(col[pivot],-1,p)
                basis[pivot]={i:v*inv%p for i,v in col.items()}
                break
            factor=col[pivot]
            for i,v in basis[pivot].items():
                remainder=(col.get(i,0)-factor*v)%p
                if remainder:col[i]=remainder
                else:col.pop(i,None)
    return len(basis)

expected={2:([29,286,1114,1357,125],[0,0,0,64,0,0]),
          3:([29,286,1114,1356,125],[0,0,0,65,1,0]),
          5:([29,286,1114,1357,125],[0,0,0,64,0,0])}
for p,(ranks_expected,betti_expected) in expected.items():
    ranks=[modular_rank(k,p) for k in range(1,6)]
    betti=[len(levels[0])-ranks[0]-1]+[
        len(levels[i])-ranks[i-1]-ranks[i] for i in range(1,5)]+[
        len(levels[5])-ranks[4]]
    assert ranks==ranks_expected,(p,ranks)
    assert betti==betti_expected,(p,betti)
    print('p=%d boundary_ranks=%s reduced_Betti=%s'%(p,ranks,betti))
assert sum((-1)**i*len(levels[i]) for i in range(6))==-63
print('ICOSAHEDRON_MODULAR_PASS')
