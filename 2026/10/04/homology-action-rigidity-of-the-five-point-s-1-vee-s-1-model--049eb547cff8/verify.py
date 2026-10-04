#!/usr/bin/env python3
from itertools import product, permutations
from collections import Counter
from math import gcd

# Five-point minimal finite model of S^1 v S^1:
# minima A=0,B=1; maxima X=2,Y=3,Z=4; every minimum is below every maximum.
MIN={0,1}
MAX={2,3,4}
ELS=range(5)
EDGES=[(0,2),(0,3),(0,4),(1,2),(1,3),(1,4)]  # AX,AY,AZ,BX,BY,BZ
EIDX={e:i for i,e in enumerate(EDGES)}

# Cycle basis in C_1(K(P);Z), oriented minimum -> maximum:
# c1 = AX - BX + BY - AY
# c2 = AX - BX + BZ - AZ
C1=(1,-1,0,-1,1,0)
C2=(1,0,-1,-1,0,1)

def leq(a,b):
    return a==b or (a in MIN and b in MAX)

def add(u,v):
    return tuple(a+b for a,b in zip(u,v))

def scale(k,u):
    return tuple(k*a for a in u)

def edge_image(f,e):
    a,b=f[e[0]],f[e[1]]
    out=[0]*6
    if a==b:
        return tuple(out)
    assert (a,b) in EIDX
    out[EIDX[(a,b)]]=1
    return tuple(out)

def chain_image(f,c):
    out=(0,0,0,0,0,0)
    for coeff,e in zip(c,EDGES):
        if coeff:
            out=add(out,scale(coeff,edge_image(f,e)))
    return out

def coords(c):
    # In a 1-cycle, BY and BZ coefficients give coordinates in basis (C1,C2).
    a,b=c[4],c[5]
    rebuilt=add(scale(a,C1),scale(b,C2))
    assert rebuilt==c, (c,rebuilt)
    return (a,b)

def matrix(f):
    a=coords(chain_image(f,C1))
    b=coords(chain_image(f,C2))
    return ((a[0],b[0]),(a[1],b[1]))

def det(M):
    return M[0][0]*M[1][1]-M[0][1]*M[1][0]

def matmul(A,B):
    return (
        (A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]),
        (A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]),
    )

def transpose(A):
    return ((A[0][0],A[1][0]),(A[0][1],A[1][1]))

G=((2,1),(1,2))  # 2*q Gram matrix for q(x,y)=x^2+xy+y^2

def preserves_q(M):
    return matmul(matmul(transpose(M),G),M)==G

def is_homeomorphism(f):
    if len(set(f))<5:
        return False
    inv=[None]*5
    for i,j in enumerate(f):
        inv[j]=i
    # Both f and inverse are order-preserving.
    return all(leq(f[a],f[b]) for a in ELS for b in ELS if leq(a,b)) and \
           all(leq(inv[a],inv[b]) for a in ELS for b in ELS if leq(a,b))

maps=[]
for f in product(ELS, repeat=5):
    if all(leq(f[a],f[b]) for a in MIN for b in MAX):
        maps.append(f)

assert len(maps)==197
counter=Counter(matrix(f) for f in maps)
assert len(counter)==31

zero=((0,0),(0,0))
U=[(1,0),(0,1),(1,-1)]
V=[(1,0),(0,1),(1,1)]
rank1=set()
for u in U:
    for v in V:
        M=((u[0]*v[0],u[0]*v[1]),(u[1]*v[0],u[1]*v[1]))
        rank1.add(M)
        rank1.add(tuple(tuple(-x for x in row) for row in M))
assert len(rank1)==18

# Enumerate all integral q-isometries: because q(M e_i)=1, each column must be
# one of the six primitive q-minimal vectors.
roots=[(1,0),(-1,0),(0,1),(0,-1),(1,-1),(-1,1)]
qiso=set()
for c1 in roots:
    for c2 in roots:
        M=((c1[0],c2[0]),(c1[1],c2[1]))
        if preserves_q(M):
            qiso.add(M)
assert len(qiso)==12

expected={zero} | rank1 | qiso
assert set(counter)==expected

homeos=[f for f in maps if is_homeomorphism(f)]
assert len(homeos)==12
homeo_mats={matrix(f) for f in homeos}
assert homeo_mats==qiso
assert all(counter[M]==1 for M in qiso)

# Exactly the homeomorphisms induce H1-isomorphisms.
invertible=[f for f in maps if det(matrix(f)) in (-1,1)]
assert set(invertible)==set(homeos)

# Rank distribution and multiplicities.
rank0_maps=counter[zero]
rank2_maps=sum(counter[M] for M in qiso)
rank1_maps=sum(counter[M] for M in rank1)
assert (rank0_maps,rank1_maps,rank2_maps)==(149,36,12)
assert all(counter[M]==2 for M in rank1)

print("VERIFY_OK")
print("continuous_self_maps=197")
print("distinct_H1_matrices=31")
print("matrix_types=1_zero+18_rank_one+12_q_isometries")
print("map_rank_distribution=149_zero_action+36_rank_one_action+12_isomorphism_action")
print("homeomorphisms=12")
print("H1_isomorphism_iff_homeomorphism=yes")
print("q=x^2+x*y+y^2")
