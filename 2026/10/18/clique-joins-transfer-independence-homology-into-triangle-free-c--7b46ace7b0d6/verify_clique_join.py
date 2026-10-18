#!/usr/bin/env python3
"""Finite reproducibility tests for clique-join triangle-free homotopy splitting.
Enumerates faces directly from graph triangles (without using the decomposition),
computes exact F2 boundary ranks, and checks signed Lefschetz characters.
"""
from itertools import combinations
from collections import Counter
from math import comb

def build(m,n,kind):
    V=list(range(m+n)); E=set()
    def edge(i,j): E.add((min(i,j),max(i,j)))
    for i,j in combinations(range(m),2):edge(i,j)
    for i in range(m):
        for j in range(m,m+n):edge(i,j)
    if kind=='cycle':
        for j in range(n):edge(m+j,m+(j+1)%n)
    elif kind=='path':
        for j in range(n-1):edge(m+j,m+j+1)
    elif kind=='empty':pass
    else:raise ValueError(kind)
    T=[sum(1<<x for x in abc) for abc in combinations(V,3) if all((min(i,j),max(i,j)) in E for i,j in combinations(abc,2))]
    faces_by_size=[[] for _ in range(m+n+1)]
    for mask in range(1<<(m+n)):
        if not any(mask&t==t for t in T):faces_by_size[mask.bit_count()].append(mask)
    return faces_by_size,T

def rank_F2(columns):
    pivots={}
    for col in columns:
        while col:
            bit=col.bit_length()-1
            if bit in pivots:col^=pivots[bit]
            else:
                pivots[bit]=col
                break
    return len(pivots)

def reduced_betti(faces):
    # include empty face as C_-1, so 0-th differential has rank 1.
    ranks={0:1}
    for k in range(1,len(faces)):
        low={a:i for i,a in enumerate(faces[k-1])}
        cols=[]
        for mask in faces[k]:
            j=mask; col=0
            while j:
                b=j&-j; j-=b
                col^=1<<low[mask^b]
            cols.append(col)
        ranks[k]=rank_F2(cols)
    out={}
    for k in range(1,len(faces)):
        b=len(faces[k])-ranks[k]-ranks.get(k+1,0)
        if b:out[k-1]=b
    return out


def independent_sets(n,kind):
    E=[]
    if kind=='cycle':E=[(j,(j+1)%n) for j in range(n)]
    if kind=='path':E=[(j,j+1) for j in range(n-1)]
    return [x for x in range(1<<n) if not any(x>>i&1 and x>>j&1 for i,j in E)]

def signature(ordered):
    return (-1)**sum(ordered[i]>ordered[j] for i in range(len(ordered)) for j in range(i+1,len(ordered)))

def fixed_trace(faces,perm):
    # Reduced Lefschetz number computed using full augmented simplicial chain.
    total=0
    for k,group in enumerate(faces):
        for mask in group:
            ss=[v for v in range(len(perm)) if mask>>v&1]
            image=[perm[v] for v in ss]
            if sum(1<<w for w in image)==mask:
                total+=(-1)**(k-1)*signature(image)
    return int(total)

def check(m,n,kind):
    faces,T=build(m,n,kind)
    assert all(len(f)>0 for f in faces[:1])
    I=independent_sets(n,kind)
    expected_count=(1<<n)+m*len(I)+comb(m,2)
    actual_count=sum(map(len,faces))
    assert actual_count==expected_count, (actual_count,expected_count)
    beta=reduced_betti(faces)
    # Directly compute homology of the base independent-set complex.
    basefaces=[[] for _ in range(n+1)]
    for mask in I:basefaces[mask.bit_count()].append(mask)
    basebeta=reduced_betti(basefaces)
    expected={1:comb(m,2)}
    for d,b in basebeta.items():expected[d+1]=expected.get(d+1,0)+m*b
    expected={d:b for d,b in expected.items() if b}
    assert beta==expected,(m,n,kind,beta,expected)
    print('cases',m,n,kind,'triangles',len(T),'faces',actual_count,'Betti',beta)
    # For cycles with connected independence complex, check product symmetry.
    if kind=='cycle' and n>=5:
        hubperms=[tuple(range(m)),tuple(([1,0]+list(range(2,m))) if m>=2 else [0])]
        rimperms=[tuple(range(n)),tuple((i+1)%n for i in range(n)),tuple((-i)%n for i in range(n))]
        for hp in hubperms:
            for rp in rimperms:
                p=[*hp]+[m+rp[i] for i in range(n)]
                actual_L=fixed_trace(faces,p)
                # H_1 = wedge^2 permutation representation, hence character via exterior square.
                fix=sum(hp[i]==i for i in range(m))
                fix2=sum(hp[hp[i]]==i for i in range(m))
                ch1=(fix*fix-fix2)//2
                # top H_{d+1} = hub permutation tensor base reduced H_d.
                base_L=fixed_trace(basefaces,rp)
                base_hom_char=sum((-1)**d*b for d,b in basebeta.items())
                # base homology is concentrated in one degree, so trace = sign * base_L.
                assert len(basebeta)==1
                d=next(iter(basebeta))
                ch_top=fix*((-1)**d)*base_L
                pred_L=-ch1+((-1)**(d+1))*ch_top
                assert pred_L==actual_L,(m,n,hp,rp,pred_L,actual_L)
        print('  signed dihedral and hub-transposition Lefschetz checks: PASS')

if __name__=='__main__':
    for m,n,kind in [(2,5,'cycle'),(3,5,'cycle'),(2,6,'cycle'),(3,6,'cycle'),(3,5,'path'),(4,3,'empty')]:check(m,n,kind)
    print('ALL FINITE CHECKS PASSED')
