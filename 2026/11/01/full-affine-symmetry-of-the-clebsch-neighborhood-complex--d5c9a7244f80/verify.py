#!/usr/bin/env python3
"""Independent exact finite checks for the Clebsch neighborhood homology character.
Run: python3 verify.py. No nonstandard packages or external inputs required.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, permutations

S=(1,2,4,8,15)
A=range(16)
P=list(permutations(range(5)))
IDENTITY=tuple(range(5))
star=[frozenset(v^s for s in S) for v in A]
faces={frozenset()}
for F in star:
    for k in range(1,6):
        faces.update(frozenset(t) for t in combinations(F,k))
D=Counter(len(f)-1 for f in faces if f)
assert D == {0:16,1:80,2:160,3:80,4:16}
assert len(faces)==353
assert len(set(star))==16
assert all(sum({x,y}<=f for f in star)==(2 if (x^y) not in S else 0)
           for x,y in combinations(A,2))
assert all(sum(t<=f for f in star)==1 for t in faces if len(t)>=3)

# The 1-skeleton is connected and has rank 15; this also follows from its
# vertex-transitive complement-of-Clebsch description.
E=sorted(tuple(sorted(f)) for f in faces if len(f)==2)
T=sorted(tuple(sorted(f)) for f in faces if len(f)==3)
edge_number={e:i for i,e in enumerate(E)}
parent=list(A)
def root(x):
    while x!=parent[x]:
        x=parent[x]
    return x
for u,v in E:
    a,b=root(u),root(v)
    if a!=b:parent[a]=b
assert len({root(u) for u in A})==1

# Ranks: ∂_3 is the direct sum of 16 copies of the rank-4 simplex
# boundary C_3(Δ^4)->C_2(Δ^4). ∂_4 has rank 16.
# The chain relation bounds rank_Q(∂_2) by 80-15=65.
# Find 65 independent ∂_2 columns modulo two, forcing the rational rank.
basis={}
for a,b,c in T:
    col=0
    for e in ((a,b),(a,c),(b,c)):
        col^=1<<edge_number[e]
    while col:
        k=col.bit_length()-1
        if k in basis:col^=basis[k]
        else:basis[k]=col;break
assert len(basis)==65
assert 160-65-64==31

# Generator permutation action and two independently evaluated Lefschetz
# characters, including orientations on every individually invariant face.
def linear(p,x):
    y=0
    for i in range(4):
        if (x>>i)&1:y^=S[p[i]]
    return y

def permutation_sign(z):
    return -1 if sum(z[i]>z[j] for i in range(len(z)) for j in range(i+1,len(z)))%2 else 1

def direct_trace(g):
    ans=-1  # reduced chain C_-1 contributes -1
    for f in faces:
        if not f:continue
        if {g[x] for x in f} != set(f):continue
        t=sorted(f)
        perm=[t.index(g[x]) for x in t]
        ans+=(-1)**(len(f)-1)*permutation_sign(perm)
    return ans

def orbit_trace(g):
    orb=[];visited=set()
    for x in A:
        if x not in visited:
            C=set();y=x
            while y not in visited:
                visited.add(y);C.add(y);y=g[y]
            orb.append(frozenset(C))
    z=0
    for mask in range(1<<len(orb)):
        f=frozenset().union(*(orb[i] for i in range(len(orb)) if mask&(1<<i)))
        if f in faces:z+=(-1)**mask.bit_count()
    return -z

def fixed(p):return sum(i==p[i] for i in range(5))

def induced_character(a,p):
    # Inflation of wedge^2 of the 4-dimensional standard S5 module.
    p2=tuple(p[p[i]] for i in range(5))
    v=((fixed(p)-1)**2-(fixed(p2)-1))//2
    # Ten Fourier characters supported on the 2-subsets of the 5-star.
    # Their little-group character is the sign on the 3-element complement.
    for K in combinations(range(5),2):
        if {p[i] for i in K}!=set(K):continue
        lam=sum(1<<i for i in K if i<4)
        comp=tuple(i for i in range(5) if i not in K)
        pcomp=[comp.index(p[i]) for i in comp]
        v+=(-1)**((a&lam).bit_count())*permutation_sign(pcomp)
    # Five characters supported on 4-subsets; their multiplicity space
    # is the sign-twisted 3-dimensional standard module of S4.
    for K in combinations(range(5),4):
        if {p[i] for i in K}!=set(K):continue
        lam=sum(1<<i for i in K if i<4)
        q=[K.index(p[i]) for i in K]
        v+=(-1)**((a&lam).bit_count())*permutation_sign(q)*(sum(i==p[i] for i in K)-1)
    return v

chi={}
for p in P:
    for a in A:
        g=[a^linear(p,x) for x in A]
        v=direct_trace(g)
        assert v==orbit_trace(g)==induced_character(a,p),(a,p,v,orbit_trace(g),induced_character(a,p))
        chi[a,p]=v
assert Counter(chi.values())=={1:944,-1:825,-5:80,3:60,7:10,31:1}
assert Counter(chi[a,IDENTITY] for a in A)=={7:10,-1:5,31:1}
assert sum(chi.values())==0
assert sum(chi[a,IDENTITY] for a in A)==16*6
# Check Fourier multiplicity distribution of A explicitly.
mult=[]
for lam in A:
    m=sum((-1)**((a&lam).bit_count())*chi[a,IDENTITY] for a in A)
    assert m%16==0
    mult.append(m//16)
assert Counter(mult)=={1:10,3:5,6:1}
print('faces=(16,80,160,80,16); simplices_with_empty=353')
print('boundary_ranks_Q=(15,65,64,16); reduced_H2_Q=31')
print('affine_aut_group_order=1920; independent_characters=1920/1920')
print('character_distribution={-5:80,-1:825,1:944,3:60,7:10,31:1}')
print('translation_character={31:1,-1:5,7:10}')
print('Fourier_multiplicities_on_A={6:1,1:10,3:5}')
print('invariants_A=6; invariants_G=0')
print('irreducible_blocks_dimensions=(6,10,15)')
print('VERIFY_OK')
