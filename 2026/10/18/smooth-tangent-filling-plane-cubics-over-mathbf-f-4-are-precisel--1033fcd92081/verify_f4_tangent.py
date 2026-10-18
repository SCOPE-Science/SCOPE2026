#!/usr/bin/env python3
"""Exact self-contained census of tangent-filling ternary cubics over GF(4).
GF(4) = GF(2)[a]/(a*a+a+1), represented by integers 0,1,2,3.
Cubic forms are counted up to GF(4)-scalar; monomials are ordered lexicographically.
"""
from collections import Counter
from itertools import product

# Fully explicit field table, to avoid any dependence on symbolic algebra packages.
MUL=((0,0,0,0),(0,1,2,3),(0,2,3,1),(0,3,1,2))
INV=(0,1,3,2)
FULL=(1<<21)-1
POINTS=tuple([(1,y,z) for y in range(4) for z in range(4)] + [(0,1,z) for z in range(4)] + [(0,0,1)])
assert len(POINTS)==21
LINE_INDEX={p:i for i,p in enumerate(POINTS)}
MONS=tuple((a,b,3-a-b) for a in range(3,-1,-1) for b in range(3-a,-1,-1))
assert len(MONS)==10

def power(x,n):
    return (1,x,MUL[x][x],MUL[MUL[x][x]][x])[n]

def product3(p,e):
    out=1
    for x,n in zip(p,e):out=MUL[out][power(x,n)]
    return out

def dot3(a,b):
    return MUL[a[0]][b[0]]^MUL[a[1]][b[1]]^MUL[a[2]][b[2]]

LINE_MASKS=tuple(sum(1<<i for i,p in enumerate(POINTS) if dot3(line,p)==0) for line in POINTS)
assert all(v.bit_count()==5 for v in LINE_MASKS)
# Eight packed GF(2)-coordinate bitplanes, each 21 bits:
# E0,E1, dx0,dx1, dy0,dy1, dz0,dz1.
TERMS=[]
for m in MONS:
    term=[]
    for coeff in range(4):
        bits=0
        for i,p in enumerate(POINTS):
            out=MUL[coeff][product3(p,m)]
            bits |= (out&1)<<i | ((out>>1)&1)<<(21+i)
            for k in range(3):
                if m[k]%2:
                    deriv=tuple(t-(j==k) for j,t in enumerate(m))
                    d=MUL[coeff][product3(p,deriv)]
                    bits|=(d&1)<<(42+42*k+i) | ((d>>1)&1)<<(63+42*k+i)
        term.append(bits)
    TERMS.append(tuple(term))

def tangent_data(packed):
    b0=packed&FULL;b1=(packed>>21)&FULL
    zeros=FULL & ~(b0|b1)
    cover=0;nonsingular_count=0
    while zeros:
        bit=zeros&(-zeros);zeros-=bit
        i=bit.bit_length()-1
        g=tuple(((packed>>(42+42*k+i))&1) | 2*((packed>>(63+42*k+i))&1) for k in range(3))
        if g==(0,0,0):continue
        nonsingular_count+=1
        pivot=next(x for x in g if x)
        line=tuple(MUL[INV[pivot]][x] for x in g)
        cover|=LINE_MASKS[LINE_INDEX[line]]
    return nonsingular_count,cover

def is_hermitian(c):
    return (c[0] in (0,1) and c[6] in (0,1) and c[9] in (0,1)
      and c[3]==MUL[c[1]][c[1]] and c[5]==MUL[c[2]][c[2]]
      and c[8]==MUL[c[7]][c[7]] and c[4]==0)

def hermitian_det(c):
    a=((c[0],c[1],c[2]),(c[3],c[6],c[7]),(c[5],c[8],c[9]))
    # determinant (signs equal in characteristic 2)
    return (MUL[a[0][0]][MUL[a[1][1]][a[2][2]]]^
      MUL[a[0][1]][MUL[a[1][2]][a[2][0]]]^
      MUL[a[0][2]][MUL[a[1][0]][a[2][1]]]^
      MUL[a[0][2]][MUL[a[1][1]][a[2][0]]]^
      MUL[a[0][0]][MUL[a[1][2]][a[2][1]]]^
      MUL[a[0][1]][MUL[a[1][0]][a[2][2]]])

def enumerate_forms():
    for leading in range(10):
        for tail in product(range(4),repeat=9-leading):
            yield (0,)*leading+(1,)+tail

if __name__=='__main__':
    all_count=0
    filling=Counter()
    smooth_candidates=[]
    invalid_hermitian=0
    for c in enumerate_forms():
        all_count+=1
        packed=0
        for j,x in enumerate(c): packed^=TERMS[j][x]
        z=((~((packed&FULL)|((packed>>21)&FULL)))&FULL).bit_count()
        if z<5:continue
        smooth_count,cover=tangent_data(packed)
        if cover!=FULL:continue
        filling[(z,smooth_count)]+=1
        if z==smooth_count and z<=9:
            smooth_candidates.append(c)
            if not any(is_hermitian(tuple(MUL[z][a] for a in c)) and hermitian_det(tuple(MUL[z][a] for a in c)) for z in (1,2,3)):
                invalid_hermitian+=1
    print('total projective cubic equations:',all_count)
    print('tangent filling (all cubics) by (points,smooth rational points):',sorted(filling.items()))
    print('smooth cubic candidates:',len(smooth_candidates))
    print('non-Hermitian or singular Hermitian candidates:',invalid_hermitian)
    # Independently enumerate all nonsingular Hermitian matrices up to scalar:
    # Hermitian forms are fixed by field Frobenius so nonzero scalar normalization is unique.
    full_hermitian=0
    for diag in product((0,1),repeat=3):
      for ab,ac,bc in product(range(4),repeat=3):
        c=(diag[0],ab,ac,MUL[ab][ab],0,MUL[ac][ac],diag[1],bc,MUL[bc][bc],diag[2])
        if hermitian_det(c):full_hermitian+=1
    print('nonsingular Hermitian matrices:',full_hermitian)
    # A smooth maximally populated cubic need not be tangent-filling.
    # X^3+Y^3+YZ^2+Z^3 has only the zero-vector as gradient zero.
    counterexample=(1,0,0,0,0,0,1,0,1,1)
    counter_packed=0
    for j,v in enumerate(counterexample):counter_packed^=TERMS[j][v]
    counter_points=(FULL & ~((counter_packed&FULL)|((counter_packed>>21)&FULL))).bit_count()
    counter_smooth,counter_cover=tangent_data(counter_packed)
    print('smooth non-filling nine-point cubic:',counter_points,counter_smooth,counter_cover.bit_count())
    assert (counter_points,counter_smooth,counter_cover.bit_count())==(9,9,18)
    assert all_count==349525
    assert filling=={(9,8):5040,(9,9):280,(10,10):6048}
    assert len(smooth_candidates)==280 and invalid_hermitian==0
    assert full_hermitian==280
    print('PASS')
