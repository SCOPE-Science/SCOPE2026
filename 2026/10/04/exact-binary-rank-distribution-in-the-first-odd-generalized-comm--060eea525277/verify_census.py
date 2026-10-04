#!/usr/bin/env python3
from itertools import combinations, permutations, islice
from collections import Counter

N=3
DIM=9
I3=(1<<0)|(1<<4)|(1<<8)
E=[1<<(3*i+j) for i in range(3) for j in range(3)]

# 3x3 matrices over F_2 are encoded row-major in nine bits.
def mat(x):
    return [[(x>>(3*i+j))&1 for j in range(3)] for i in range(3)]
MATS=[mat(x) for x in range(512)]
MULT=[[0]*512 for _ in range(512)]
for a,A in enumerate(MATS):
    for b,B in enumerate(MATS):
        C=[[sum(A[i][k]*B[k][j] for k in range(3))&1 for j in range(3)] for i in range(3)]
        MULT[a][b]=sum(C[i][j]<<(3*i+j) for i in range(3) for j in range(3))

def rank_vecs(vs):
    piv={}
    for v in vs:
        while v:
            p=v.bit_length()-1
            if p in piv: v ^= piv[p]
            else:
                piv[p]=v
                break
    return len(piv)

def rref_spaces():
    # Every 3-space in F_2^9 has one reduced-row-echelon 3x9 basis matrix.
    for piv in combinations(range(9),3):
        free=[]
        base=[1<<p for p in piv]
        for i,p in enumerate(piv):
            for j in range(9):
                if j not in piv and j>p:
                    free.append((i,j))
        for mask in range(1<<len(free)):
            rows=base[:]
            for t,(i,j) in enumerate(free):
                if (mask>>t)&1: rows[i] |= 1<<j
            yield tuple(rows)

PERMS=list(permutations(range(4)))
def op_direct(a,b,c):
    vals=[a,b,c,0]
    out=[]
    for x in E:
        vals[3]=x
        y=0
        for p in PERMS: # signs are all +1 in F_2
            z=vals[p[0]]
            z=MULT[z][vals[p[1]]]
            z=MULT[z][vals[p[2]]]
            z=MULT[z][vals[p[3]]]
            y ^= z
        out.append(y)
    return out

def s3(a,b,c):
    m=MULT
    return (m[m[a][b]][c]^m[m[a][c]][b]^m[m[b][a]][c]^
            m[m[b][c]][a]^m[m[c][a]][b]^m[m[c][b]][a])

def op_grouped(a,b,c):
    # Independently grouped expansion of s_4(a,b,c,X) in characteristic two.
    m=MULT
    s=s3(a,b,c)
    bc=m[b][c]^m[c][b]
    ac=m[a][c]^m[c][a]
    ab=m[a][b]^m[b][a]
    out=[]
    for x in E:
        y=m[s][x]^m[x][s]
        y ^= m[m[a][x]][bc]^m[m[b][x]][ac]^m[m[c][x]][ab]
        y ^= m[m[ab][x]][c]^m[m[ac][x]][b]^m[m[bc][x]][a]
        out.append(y)
    return out

def contains_identity(rows):
    return rank_vecs(rows)==rank_vecs(rows+(I3,))

def gaussian(n,k,q=2):
    a=b=1
    for i in range(k):
        a*=q**(n-i)-1
        b*=q**(k-i)-1
    return a//b

# Full census, with both operator constructions compared on every space.
direct=Counter(); grouped=Counter(); zero_with_I=0
count=0
for rows in rref_spaces():
    d=op_direct(*rows)
    g=op_grouped(*rows)
    if d!=g:
        raise AssertionError("direct/grouped operator mismatch")
    rd=rank_vecs(d); rg=rank_vecs(g)
    direct[rd]+=1; grouped[rg]+=1; count+=1
    if rd==0 and contains_identity(rows):
        zero_with_I+=1

expected={0:11635,2:122320,4:654080}
assert count==gaussian(9,3)==788035
assert direct==grouped==Counter(expected)
assert zero_with_I==gaussian(8,2)==10795
assert direct[0]-zero_with_I==840
print("VERIFY_OK")
print("total",count)
print("rank_counts",dict(sorted(direct.items())))
print("nullity_counts",{9-r:c for r,c in sorted(direct.items())})
print("rank0_containing_identity",zero_with_I)
print("rank0_not_containing_identity",direct[0]-zero_with_I)
print("maximal_rank_fraction",f"{direct[4]}/{count}=1792/2159")
