#!/usr/bin/env python3
"""Standalone exact verification for the Paley-17 flag-complex theorem.
Only Python standard library is required.
"""
from itertools import combinations

P = 17
SQUARES = {pow(a, 2, P) for a in range(1, P)}
assert SQUARES == {1,2,4,8,9,13,15,16}
EDGES = tuple((u,v) for u,v in combinations(range(P),2)
              if (v-u)%P in SQUARES)
EDGESET = set(EDGES)
TRIANGLES = tuple((a,b,c) for a,b,c in combinations(range(P),3)
                  if (a,b) in EDGESET and (a,c) in EDGESET and (b,c) in EDGESET)
assert (len(EDGES), len(TRIANGLES)) == (68,68)
assert not any(all(tuple(sorted(e)) in EDGESET for e in combinations(t,2))
               for t in combinations(range(P),4))
assert not any(all(tuple(sorted(e)) not in EDGESET for e in combinations(t,2))
               for t in combinations(range(P),4))
assert all(any(tuple(sorted((u,w))) in EDGESET and tuple(sorted((v,w))) in EDGESET
               for w in range(P) if w!=u and w!=v)
           for u,v in combinations(range(P),2) if (u,v) not in EDGESET)

# Fixed rooted spanning-tree certificate, verified to connect all vertices.
TREE = {(0,1),(0,2),(0,4),(0,8),(0,9),(0,13),(0,15),(0,16),
        (1,3),(1,5),(1,10),(1,14),(2,6),(2,11),(3,7),(3,12)}
assert len(TREE)==16 and TREE.issubset(EDGESET)
seen={0}
for _ in range(P):
    for a,b in TREE:
        if a in seen:seen.add(b)
        if b in seen:seen.add(a)
assert len(seen)==17
NON_TREE = tuple(sorted(EDGESET-TREE))
assert len(NON_TREE)==52
LABEL={edge:i+1 for i,edge in enumerate(NON_TREE)}

def edge_letter(a,b):
    if a>b:return [-v for v in reversed(edge_letter(b,a))]
    return [LABEL[(a,b)]] if (a,b) in LABEL else []

def freely_reduce(word):
    stack=[]
    for ltr in word:
        if stack and stack[-1]==-ltr: stack.pop()
        else:stack.append(ltr)
    return stack

def inverse(word):return [-x for x in reversed(word)]

RELATORS=[freely_reduce(edge_letter(a,b)+edge_letter(b,c)+edge_letter(c,a))
          for a,b,c in TRIANGLES]
STEPS=[]
for step in range(52):
    options=[]
    for k,w in enumerate(RELATORS):
        for x in set(map(abs,w)):
            if sum(abs(y)==x for y in w)==1:
                involvement=sum(len(z) for z in RELATORS if x in z or -x in z)
                options.append((len(w),involvement,k,x))
    assert options, 'Stopped before elimination of all 52 generators'
    _,_,k,x=min(options)
    w=RELATORS[k]
    pos=next(i for i,v in enumerate(w) if abs(v)==x)
    first,last=w[:pos],w[pos+1:]
    # Relation first * (x or x^{-1}) * last = 1;
    # solve x as word in remaining generators.
    expression=inverse(last+first) if w[pos]==x else last+first
    assert x not in map(abs,expression)
    new=[]
    for j,other in enumerate(RELATORS):
        if j==k:continue
        expanded=[]
        for letter in other:
            if letter==x:expanded+=expression
            elif letter==-x:expanded+=inverse(expression)
            else:expanded.append(letter)
        new.append(freely_reduce(expanded))
    RELATORS=new
    STEPS.append(x)
assert set(STEPS)==set(range(1,53))
assert len(RELATORS)==16 and all(not w for w in RELATORS)
print('PI1_T0_RELATOR_ELIMINATIONS_VERIFIED',len(STEPS))

# Exact binary rank of the cellular triangle-to-edge boundary map.
def binary_rank(columns):
    pivots={}
    for vector in columns:
        while vector:
            p=vector.bit_length()-1
            if p in pivots:vector^=pivots[p]
            else:pivots[p]=vector;break
    return len(pivots)

edge_index={edge:i for i,edge in enumerate(EDGES)}
columns=[sum(1<<edge_index[e] for e in ((a,b),(a,c),(b,c)))
         for a,b,c in TRIANGLES]
assert binary_rank(columns)==52
assert 17-68+68==17
print('INTEGER_FREE_H2_RANK_BY_PI1_AND_EULER_VERIFIED',16)

# Signed traces on oriented simplicial chains of EVERY affine symmetry.
def sign_of_order(seq):
    inv=sum(a>b for i,a in enumerate(seq) for b in seq[i+1:])
    return -1 if inv%2 else 1

def trace_on_simplices(simplices,perm):
    result=0
    for simplex in simplices:
        mapped=[perm(v) for v in simplex]
        if set(mapped)==set(simplex): result+=sign_of_order(mapped)
    return result

affine_count=0
for a in sorted(SQUARES):
    for b in range(P):
        affine_count+=1
        p=lambda x:(a*x+b)%P
        assert all(tuple(sorted((p(i),p(j)))) in EDGESET for i,j in EDGES)
        t=trace_on_simplices(TRIANGLES,p)-trace_on_simplices(EDGES,p)+sum(p(v)==v for v in range(P))-1
        wanted=16 if a==1 and b==0 else (-1 if a==1 else 0)
        assert t==wanted,(a,b,t,wanted)
assert affine_count==136
print('ALL_AFFINE_LEFSCHETZ_CHARACTERS_VERIFIED',affine_count)
print('PALEY17_WEDGE_AND_AFFINE_CHARACTER_VERIFIED')
