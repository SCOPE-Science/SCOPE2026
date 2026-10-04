#!/usr/bin/env python3
from itertools import combinations

N=3
DIM=9
ZERO=0
IDENT=(1<<0)|(1<<4)|(1<<8)


def mat(x):
    return [[(x>>(3*i+j))&1 for j in range(3)] for i in range(3)]

def enc(A):
    x=0
    for i in range(3):
        for j in range(3):
            x |= (A[i][j]&1) << (3*i+j)
    return x

def mul(x,y):
    A,B=mat(x),mat(y)
    C=[[0]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            C[i][j]=(A[i][0]*B[0][j]^A[i][1]*B[1][j]^A[i][2]*B[2][j])
    return enc(C)

def cube(x):
    return mul(mul(x,x),x)

def nilpotent(x):
    return cube(x)==0

def dot(x,y):
    return (x & y).bit_count() & 1

def span(rows):
    vals=[0]
    for r in rows:
        vals += [v^r for v in vals]
    return frozenset(vals)

def rref_bases(n,k):
    # Unique RREF basis for every k-subspace of F_2^n.
    for piv in combinations(range(n),k):
        free=[]
        base=[1<<p for p in piv]
        for p in piv:
            free.append([c for c in range(n) if c not in piv and c>p])
        m=sum(map(len,free))
        for mask in range(1<<m):
            rows=base.copy(); z=0
            for i,cols in enumerate(free):
                for c in cols:
                    if (mask>>z)&1:
                        rows[i] |= 1<<c
                    z += 1
            yield tuple(rows)

def kernel(rows):
    return frozenset(x for x in range(1<<DIM) if all(dot(x,r)==0 for r in rows))

def rank3(x):
    rows=[]
    A=mat(x)
    for i in range(3):
        rows.append(A[i][0] | (A[i][1]<<1) | (A[i][2]<<2))
    r=0
    for c in range(3):
        p=next((i for i in range(r,3) if (rows[i]>>c)&1),None)
        if p is None: continue
        rows[r],rows[p]=rows[p],rows[r]
        for i in range(3):
            if i!=r and ((rows[i]>>c)&1): rows[i]^=rows[r]
        r+=1
    return r

def inverse3(x):
    A=mat(x)
    rows=[]
    for i in range(3):
        left=A[i][0] | (A[i][1]<<1) | (A[i][2]<<2)
        rows.append(left | (1<<(3+i)))
    r=0
    for c in range(3):
        p=next((i for i in range(r,3) if (rows[i]>>c)&1),None)
        if p is None: return None
        rows[r],rows[p]=rows[p],rows[r]
        for i in range(3):
            if i!=r and ((rows[i]>>c)&1): rows[i]^=rows[r]
        r+=1
    B=[[ (rows[i]>>(3+j))&1 for j in range(3)] for i in range(3)]
    return enc(B)

def conj(g,x,ginv):
    return mul(mul(g,x),ginv)

# Nilpotent cone in M_3(F_2).
nils=frozenset(x for x in range(1<<DIM) if nilpotent(x))
assert len(nils)==64
nonzero_nils=nils-{0}

# Explicit six-space from the statement.
def in_explicit_W(x):
    A=mat(x)
    return ((A[0][0]^A[0][1]^A[1][0])==0 and
            (A[0][0]^A[0][2]^A[1][2]^A[2][0])==0 and
            (A[0][1]^A[1][1]^A[1][2]^A[2][1])==0)
explicit_W=frozenset(x for x in range(1<<DIM) if in_explicit_W(x))
assert len(explicit_W)==64
assert explicit_W & nonzero_nils == set()

# Method 1: direct census of all 6-spaces by RREF bases.
direct_good=[]
total6=0
for rows in rref_bases(DIM,6):
    total6 += 1
    W=span(rows)
    if W.isdisjoint(nonzero_nils):
        direct_good.append(W)
assert total6==788035
assert len(direct_good)==128
assert len(set(direct_good))==128
assert explicit_W in set(direct_good)

# Method 2: independently enumerate all 3-dimensional orthogonal complements.
# W=U^perp avoids every nonzero nilpotent iff each such N has nonzero pairing
# with at least one row of a basis of U.
hit=[]
for u in range(1<<DIM):
    hit.append(frozenset(n for n in nonzero_nils if dot(u,n)))
dual_good=[]
total3=0
for rows in rref_bases(DIM,3):
    total3 += 1
    covered=hit[rows[0]] | hit[rows[1]] | hit[rows[2]]
    if covered==nonzero_nils:
        dual_good.append(kernel(rows))
assert total3==788035
assert len(dual_good)==128
assert set(dual_good)==set(direct_good)

# Conjugacy under GL_3(F_2).
GL=[]
for g in range(1<<DIM):
    inv=inverse3(g)
    if inv is not None:
        GL.append((g,inv))
assert len(GL)==168
good=set(direct_good)
unseen=set(good)
orbit_sizes=[]
explicit_orbit=None
while unseen:
    W=next(iter(unseen))
    orb=frozenset(frozenset(conj(g,x,gi) for x in W) for g,gi in GL)
    assert orb <= good
    orbit_sizes.append(len(orb))
    if explicit_W in orb:
        explicit_orbit=len(orb)
    unseen -= set(orb)
assert sorted(orbit_sizes)==[8,8,56,56]
assert explicit_orbit==56

print('VERIFY_OK')
print('nilpotent_matrices=64 nonzero_nilpotents=63')
print('grassmannian_count=[9 choose 6]_2=[9 choose 3]_2=788035')
print('nilpotent_free_6spaces=128')
print('GL3F2_conjugacy_orbit_sizes=8,8,56,56')
print('explicit_space_size=64 explicit_orbit_size=56')
