#!/usr/bin/env python3
"""Independent geometric-model check of the cuboctahedron dissociation complex."""
from itertools import product, permutations
from collections import Counter
V=tuple(sorted(v for v in product((-1,0,1), repeat=3)
               if sum(t==0 for t in v)==1 and sum(t*t for t in v)==2))
assert len(V)==12
N=len(V)
adj=tuple(sum(1<<j for j,w in enumerate(V)
              if j!=i and sum((v[k]-w[k])**2 for k in range(3))==2)
          for i,v in enumerate(V))
assert all(mask.bit_count()==4 for mask in adj)
def connected_component_ok(mask):
    left=mask
    while left:
        start=left & -left;left-=start
        component=start
        frontier=start
        while frontier:
            next_frontier=0
            vmask=frontier
            while vmask:
                a=vmask & -vmask;vmask-=a
                i=a.bit_length()-1
                next_frontier |= adj[i] & mask & ~component
            frontier=next_frontier
            component |= frontier
        if component.bit_count()>2:return False
        left &= ~component
    return True
F=[mask for mask in range(1,1<<12) if connected_component_ok(mask)]
f=Counter(mask.bit_count()-1 for mask in F)
assert f=={0:12,1:66,2:164,3:177,4:36},f
assert sum((-1)**d*count for d,count in f.items())==-31
print('coordinate_model=',V)
print('independent_face_vector=',dict(sorted(f.items())))
print('euler_characteristic=',sum((-1)**d*count for d,count in f.items()))
# Independent orientation sign: fixed simplex oriented by sorted vertex coordinates.
def sign_fixed(s, mapping):
    old=[j for j in range(N) if s>>j&1]
    new=[mapping[j] for j in old]
    if set(new)!=set(old):return 0
    return (-1)**sum(new[i]>new[j] for i in range(len(new)) for j in range(i+1,len(new)))
def character(mapping):
    return 1-sum((-1)**(s.bit_count()-1)*sign_fixed(s,mapping) for s in F)
coord_index={v:i for i,v in enumerate(V)}
chars=[]
for perm in permutations(range(3)):
    for signs in product((-1,1),repeat=3):
        fperm=tuple(coord_index[tuple(signs[i]*v[perm[i]] for i in range(3))] for v in V)
        chars.append((perm, signs, character(fperm)))
assert len(chars)==48
id_trace=next(t for perm,sgn,t in chars if perm==(0,1,2) and sgn==(1,1,1))
anti_trace=next(t for perm,sgn,t in chars if perm==(0,1,2) and sgn==(-1,-1,-1))
assert id_trace==32 and anti_trace==10
assert sum(t for _,_,t in chars)==96
print('identity_H3_trace=',id_trace)
print('antipodal_H3_trace=',anti_trace)
print('full_group_invariant_dimension=',sum(t for _,_,t in chars)//48)
