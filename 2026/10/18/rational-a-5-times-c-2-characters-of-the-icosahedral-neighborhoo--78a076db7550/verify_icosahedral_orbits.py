#!/usr/bin/env python3
"""Independent fixed-cycle and group-generator check, standard library only.
Generates the full symmetry group from three explicit permutations and recovers the
character using invariant vertex-cycle unions, not oriented-face permutation scans.
"""
from itertools import combinations
from collections import Counter
N=12
NEIGHBOR_BLOCKS=[
[0,1,2,7,9],[0,1,4,6,11],[0,2,5,6,8],[0,4,5,7,10],
[0,8,9,10,11],[1,2,3,4,5],[1,3,6,8,9],[1,5,7,8,11],
[2,3,7,8,10],[2,4,6,9,10],[3,4,7,9,11],[3,5,6,10,11]]
A=(1,0,11,10,9,8,7,6,5,4,3,2)
B=(0,8,9,3,6,1,2,11,7,10,4,5)
Z=(3,10,11,0,8,9,7,6,4,5,1,2)
identity=tuple(range(N))
F={0}
for block in NEIGHBOR_BLOCKS:
 for k in range(1,6):
  for c in combinations(block,k):F.add(sum(1<<i for i in c))
assert len(F)==265

def prod(p,q):return tuple(p[q[i]] for i in range(N))
def closure(gs):
    R={identity}; stack=[identity]
    while stack:
        p=stack.pop()
        for g in gs:
            t=prod(p,g)
            if t not in R:R.add(t);stack.append(t)
    return R
R=closure([A,B])
assert len(R)==60
G=closure([A,B,Z])
assert len(G)==120
assert prod(Z,Z)==identity
assert all(prod(Z,g)==prod(g,Z) for g in R)
blockset={frozenset(b) for b in NEIGHBOR_BLOCKS}
assert all({frozenset(g[i] for i in b) for b in NEIGHBOR_BLOCKS}==blockset for g in G)

def ord_g(g):
    p=identity
    for i in range(1,30):
        p=prod(p,g)
        if p==identity:return i
    raise RuntimeError('order')

assert ord_g(A)==2 and ord_g(B)==5 and ord_g(prod(A,B))==3
assert ord_g(Z)==2

def cycles(g):
    unseen=set(range(N)); cs=[]
    while unseen:
        s=next(iter(unseen));cy=[];v=s
        while v in unseen:
            unseen.remove(v);cy.append(v);v=g[v]
        cs.append(sum(1<<x for x in cy))
    return cs

def char_by_cycles(g):
    cs=cycles(g)
    # A fixed nonempty simplex must be a union of entire vertex cycles.
    # Orientation sign of each selected cycle is (-1)^(cycle_size-1).
    total=-1
    for k in range(1,1<<len(cs)):
        face=0;number=0
        for j,c in enumerate(cs):
            if (k>>j)&1:face|=c;number+=1
        if face not in F:continue
        dimension=face.bit_count()-1
        intrinsic_sign=(-1)**(face.bit_count()-number)
        total+=((-1)**dimension)*intrinsic_sign
    return total

rot=Counter((ord_g(g),char_by_cycles(g)) for g in R)
rev=Counter((ord_g(prod(Z,g)),char_by_cycles(prod(Z,g))) for g in R)
assert rot==Counter({(1,23):1,(2,3):15,(3,-1):20,(5,3):24}),rot
assert rev==Counter({(2,-1):1,(2,-5):15,(6,-1):20,(10,-1):24}),rev
assert sum(char_by_cycles(g) for g in G)==0
assert sum(char_by_cycles(g) for g in R)==120
# A5 irreducible character comparison, using the sum phi + phi' = 1.
# The 5-cycle classes have size 12 each and all observed values agree on them.
plus=(11,-1,-1,1)
minus=(12,4,0,2)
weights=(1,15,20,24)
triv=(1,1,1,1);four=(4,0,1,-1);five=(5,1,-1,0)
def ip(x,y):return sum(w*a*b for w,a,b in zip(weights,x,y))//60
assert [ip(plus,t) for t in (triv,four,five)]==[0,0,1]
assert [ip(minus,t) for t in (triv,four,five)]==[2,0,2]
# For each 3-dimensional conjugate, their equal 5-class traces yield
# inner products (1,0), since the golden ratio roots sum to 1.
assert (plus[0]*3+15*plus[1]*-1+12*plus[3])//60==1
assert (minus[0]*3+15*minus[1]*-1+12*minus[3])//60==0
print('VERIFY_OK: 60 A5 rotations, 120 full symmetries, 265 faces including empty')
print('VERIFY_OK: proper classes',sorted(rot.items()))
print('VERIFY_OK: improper classes',sorted(rev.items()))
print('VERIFY_OK: representation (3+3prime+5) even, (2*1+2*5) odd')
