#!/usr/bin/env python3
"""Independent group-theoretic check of shortest 6-switch distances.

Represent Steiner triple systems as cosets S9/AGL(2,3). A 6-cycle switch
is a transposition, so distance is the minimum transposition length of a
coset representative. Use: python3 verify_affine_cosets.py.
"""
from itertools import permutations,combinations,product
from collections import Counter

pts=list(product(range(3),repeat=2))
pointidx={x:i for i,x in enumerate(pts)}
lines=frozenset(tuple(sorted((pointidx[(a,b)],pointidx[((a+dx)%3,(b+dy)%3)],pointidx[((a+2*dx)%3,(b+2*dy)%3)])))
     for a,b in pts for dx,dy in [(1,0),(0,1),(1,1),(1,2)])
assert len(lines)==12

def apply(p):
    return tuple(sorted(tuple(sorted(p[x] for x in line)) for line in lines))
identity=tuple(range(9))
S0=apply(identity)
A=[]
for a,b,c,d in product(range(3),repeat=4):
    if (a*d-b*c)%3==0:continue
    for x,y in pts:
        A.append(tuple(pointidx[((a*i+b*j+x)%3,(c*i+d*j+y)%3)] for i,j in pts))
assert len(A)==432 and len(set(A))==432
assert all(apply(g)==S0 for g in A)
# The stabilizer is all of A, since its size is 432 and the known orbit has 840 designs.

# Transposition length = 9 minus number of cycles, including fixed points.
def transposition_length(p):
    visited=set()
    cycles=0
    for x in range(9):
        if x not in visited:
            cycles+=1
            while x not in visited:
                visited.add(x)
                x=p[x]
    return 9-cycles

systems={}
for p in permutations(range(9)):
    blocks=apply(p)
    if blocks not in systems:
        systems[blocks]=p
assert len(systems)==840
assert set(systems)==set(apply(g) for g in permutations(range(9)))
# Each coset corresponding to S'=p(S0) consists of p o h with h in A.
# Thus length min_{h in A} l(p h) is EXACT graph distance, not heuristic BFS.
count_by_c=Counter()
count_by_d=Counter()
class_spectrum={}
for blocks,p in systems.items():
    c=len(set(blocks)&set(S0))
    dist=min(transposition_length(tuple(p[h[i]] for i in range(9))) for h in A)
    count_by_c[c]+=1
    count_by_d[dist]+=1
    class_spectrum.setdefault(c,set()).add(dist)
assert sorted(class_spectrum)==[0,1,2,3,4,6,12]
assert {k:tuple(v) for k,v in class_spectrum.items()}=={0:(3,),1:(3,),2:(2,),3:(2,),4:(2,),6:(1,),12:(0,)}
assert count_by_d=={0:1,1:36,2:395,3:408}
assert count_by_c=={0:192,1:216,2:216,3:152,4:27,6:36,12:1}
# 36 point transpositions give 36 distinct cosets at distance one.
flips={}
for a,b in combinations(range(9),2):
    t=list(range(9));t[a],t[b]=t[b],t[a]
    flips[apply(t)]=(a,b)
assert len(flips)==36
assert all(len(set(s)&set(S0))==6 for s in flips)
print('AFFINE_COSETS_OK')
print('line_count=12')
print('affine_automorphisms=',len(A),sep='')
print('labeled_systems=',len(systems),sep='')
print('single_transposition_neighbors=',len(flips),sep='')
print('reference_intersection_counts=',sorted(count_by_c.items()),sep='')
print('reference_distance_counts=',sorted(count_by_d.items()),sep='')
print('intersection_to_distance=',{k:next(iter(v)) for k,v in sorted(class_spectrum.items())},sep='')
print('maximum_coset_transposition_length=3')
