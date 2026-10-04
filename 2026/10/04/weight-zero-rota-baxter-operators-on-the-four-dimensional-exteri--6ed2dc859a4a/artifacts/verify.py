#!/usr/bin/env python3
from itertools import product
from collections import Counter

# A = Lambda_2(F_2), basis (1,e1,e2,z=e1e2), vectors encoded as 4-bit ints.
# Method A: bit-level multiplication and exhaustive linear maps.

def mul_bit(a,b):
    aa=[(a>>i)&1 for i in range(4)]
    bb=[(b>>i)&1 for i in range(4)]
    c=[0,0,0,0]
    c[0]=aa[0]&bb[0]
    c[1]=(aa[0]&bb[1])^(aa[1]&bb[0])
    c[2]=(aa[0]&bb[2])^(aa[2]&bb[0])
    c[3]=(aa[0]&bb[3])^(aa[3]&bb[0])^(aa[1]&bb[2])^(aa[2]&bb[1])
    return sum(c[i]<<i for i in range(4))

BASIS=(1,2,4,8)

def lin_map(cols, v):
    out=0
    for i in range(4):
        if (v>>i)&1: out ^= cols[i]
    return out

def rb_basis_ok(cols):
    for x in BASIS:
        Rx=lin_map(cols,x)
        for y in BASIS:
            Ry=lin_map(cols,y)
            lhs=mul_bit(Rx,Ry)
            rhs=lin_map(cols, mul_bit(Rx,y)^mul_bit(x,Ry))
            if lhs != rhs:
                return False
    return True

ops=[]
for cols in product(range(16), repeat=4):
    if rb_basis_ok(cols):
        ops.append(cols)
assert len(ops)==80

# Method B: tuple-coordinate implementation, different multiplication/evaluation path;
# recheck each candidate on all 16x16 algebra-element pairs and all noncandidates on basis pairs.
def bits(v): return ((v>>0)&1,(v>>1)&1,(v>>2)&1,(v>>3)&1)
def enc(t): return t[0] | (t[1]<<1) | (t[2]<<2) | (t[3]<<3)
def add_t(a,b): return tuple(x^y for x,y in zip(a,b))
def mul_t(a,b):
    a0,a1,a2,a3=a; b0,b1,b2,b3=b
    return (a0*b0,
            (a0*b1)^(a1*b0),
            (a0*b2)^(a2*b0),
            (a0*b3)^(a3*b0)^(a1*b2)^(a2*b1))
def apply_t(cols, a):
    out=(0,0,0,0)
    for i,bit in enumerate(a):
        if bit: out=add_t(out,bits(cols[i]))
    return out

def rb_all_elements_ok(cols):
    for xv in range(16):
        x=bits(xv); Rx=apply_t(cols,x)
        for yv in range(16):
            y=bits(yv); Ry=apply_t(cols,y)
            lhs=mul_t(Rx,Ry)
            rhs=apply_t(cols, add_t(mul_t(Rx,y),mul_t(x,Ry)))
            if lhs != rhs: return False
    return True
assert all(rb_all_elements_ok(c) for c in ops)

# Linear rank over F2.
def rank_cols(cols):
    rows=[]
    for r in range(4):
        row=sum(((cols[c]>>r)&1)<<c for c in range(4))
        rows.append(row)
    rank=0; col=0
    for col in range(4):
        p=next((i for i in range(rank,4) if (rows[i]>>col)&1),None)
        if p is None: continue
        rows[rank],rows[p]=rows[p],rows[rank]
        for i in range(4):
            if i!=rank and ((rows[i]>>col)&1): rows[i]^=rows[rank]
        rank+=1
    return rank
rankdist=Counter(rank_cols(c) for c in ops)
assert rankdist==Counter({2:30,1:25,3:24,0:1})
assert all(c[3]==0 for c in ops)  # R(z)=0.

# Brute-force every unital multiplicative bijective F2-linear map to recover Aut(A).
def is_bijective(cols): return rank_cols(cols)==4
def alg_hom(cols):
    if cols[0] != 1: return False
    for x in BASIS:
        for y in BASIS:
            if lin_map(cols,mul_bit(x,y)) != mul_bit(lin_map(cols,x),lin_map(cols,y)):
                return False
    return True
autos=[c for c in product(range(16),repeat=4) if is_bijective(c) and alg_hom(c)]
assert len(autos)==24
assert all(c[0]==1 and c[3]==8 for c in autos)

# Composition/inverse/conjugation.
def compose(f,g): # f o g
    return tuple(lin_map(f,g[i]) for i in range(4))
ID=(1,2,4,8)
def inv(f):
    return next(g for g in autos if compose(f,g)==ID and compose(g,f)==ID)
invauto={f:inv(f) for f in autos}
def conj(phi,R): return compose(compose(phi,R),invauto[phi])
S=set(ops); unseen=set(ops); orbits=[]
while unseen:
    r=min(unseen)
    orb={conj(phi,r) for phi in autos}
    assert orb <= S
    # full closure automatically because autos is group; assert stability
    for phi in autos: assert {conj(phi,x) for x in orb}==orb
    orbits.append(orb); unseen-=orb
assert len(orbits)==12
sizes=sorted(len(o) for o in orbits)
assert sizes==[1,1,3,3,6,6,6,6,6,6,12,24]
assert sum(sizes)==80

# Canonical reps ordered by rank, orbit size, tuple.
def matrix_rows(cols):
    return [[(cols[c]>>r)&1 for c in range(4)] for r in range(4)]
reps=[]
for o in orbits:
    r=min(o)
    reps.append((rank_cols(r),len(o),r,matrix_rows(r)))
reps.sort(key=lambda x:(x[0],x[1],x[2]))

print('CHECK_OK')
print('operator_count',len(ops))
print('rank_distribution',dict(sorted(rankdist.items())))
print('all_R_z_zero',all(c[3]==0 for c in ops))
print('automorphism_group_order',len(autos))
print('orbit_count',len(orbits))
print('orbit_sizes',sizes)
print('representatives: columns are R(1),R(e1),R(e2),R(z); matrices printed by rows')
for i,(rk,sz,r,mat) in enumerate(reps,1):
    print(i,'rank',rk,'orbit_size',sz,'cols',r,'matrix',mat)
