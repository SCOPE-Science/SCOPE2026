#!/usr/bin/env python3
"""Independent exact face, GF(2) boundary-rank, and fixed-simplex trace calculator."""
import json
from collections import Counter

N=12
edges={(min(i,(i+d)%N),max(i,(i+d)%N)) for i in range(N) for d in (1,2)}
# Enumerate by forbidding a three-vertex path within the induced subgraph, without consulting the matching.
triples=set()
for v in range(N):
    neighbors=[u for u in range(N) if (min(u,v),max(u,v)) in edges]
    for ix,u in enumerate(neighbors):
        for w in neighbors[ix+1:]:
            triples.add((1<<v)|(1<<u)|(1<<w))
face_set={m for m in range(1,1<<N) if not any(m&t==t for t in triples)}
assert len(face_set)==521
levels={q:sorted(m for m in face_set if m.bit_count()==q) for q in range(1,7)}

# Boundary matrices over F_2: columns represented as unbounded integers.
def rank(cols):
    base={}
    for val in cols:
        while val:
            k=val.bit_length()-1
            if k in base:val^=base[k]
            else:base[k]=val;break
    return len(base)
boundary_rank={}
for q in range(2,7):
    idx={v:i for i,v in enumerate(levels[q-1])}
    cols=[sum(1<<idx[v^(1<<i)] for i in range(N) if v&(1<<i))
          for v in levels[q]]
    boundary_rank[q-1]=rank(cols)
boundary_rank[0]=0
betti={q-1:len(levels[q])-boundary_rank.get(q-1,0)-boundary_rank.get(q,0) - (q==1)
       for q in range(1,7)}
assert betti=={0:0,1:0,2:0,3:34,4:0,5:0},betti

def action_trace(p):
    sum_fixed=0
    for f in face_set:
        bits=[i for i in range(N) if f&(1<<i)]
        new=[p[i] for i in bits]
        if set(new)!=set(bits):continue
        inv=sum(new[a]>new[b] for a in range(len(new)) for b in range(a+1,len(new)))
        sum_fixed += -1 if (len(bits)-1+inv)%2 else 1
    # Since only reduced H_3 is nonzero, its trace is 1 - the ordinary Lefschetz number.
    return 1-sum_fixed
rot=[action_trace([(i+k)%N for i in range(N)]) for k in range(N)]
ref=[action_trace([(k-i)%N for i in range(N)]) for k in range(N)]
assert rot==[34,1,1,-2,1,1,10,1,1,-2,1,1],rot
assert ref==[4]*12,ref
assert (sum(rot)+sum(ref))%24==0
assert (sum(rot)+sum(ref))//24==4
assert (rot[0]+rot[6])//2==22 and (rot[0]-rot[6])//2==12
print(json.dumps({'face_count':len(face_set),'forbidden_triples':len(triples),
 'mod2_boundary_ranks':{str(i):boundary_rank[i] for i in range(6)},
 'reduced_mod2_betti':{str(i):betti[i] for i in range(6)},
 'rotation_character':rot,'reflection_character':ref,
 'dihedral_invariant_dimension':4,'half_turn_eigenspace_dimensions':[22,12]},sort_keys=True))
