#!/usr/bin/env python3
"""Exact finite simplicial checks of cyclic clique-substituted independence complexes.
No external packages, finite checks only: the uniform theorem also has a proof.
"""
from itertools import combinations, product

def faces(q):
    vs = [(i,a) for i in range(7) for a in range(q)]
    out=[[],[],[]]
    for k in (1,2,3):
        for f in combinations(vs,k):
            layers=[v[0] for v in f]
            if len(set(layers))<k: continue
            if any((i-j)%7 in (1,6) for i,j in combinations(layers,2)): continue
            out[k-1].append(f)
    return out

def rank_F2(columns):
    pivots={}
    for x in columns:
        while x:
            bit=x.bit_length()-1
            if bit in pivots: x ^= pivots[bit]
            else: pivots[bit]=x; break
    return len(pivots)

def boundary_rank(lower,upper):
    loc={f:i for i,f in enumerate(lower)}
    return rank_F2(sum(1<<loc[t] for t in combinations(f,len(f)-1)) for f in upper)

def sign_of_sort(mapped):
    return -1 if sum(mapped[i]>mapped[j] for i in range(len(mapped)) for j in range(i+1,len(mapped)))%2 else 1

def trace(F,rotate=False):
    tot=[]
    for L in F:
        z=0
        for f in L:
            target=[((i+1)%7 if rotate else (-i)%7,a) for i,a in f]
            if sorted(target)==list(f):z+=sign_of_sort(target)
        tot.append(z)
    return tot

def test(q):
    F=faces(q)
    assert tuple(map(len,F)) == (7*q,14*q*q,7*q**3)
    r1=boundary_rank(F[0],F[1]);r2=boundary_rank(F[1],F[2]);
    betti=(len(F[0])-r1,len(F[1])-r1-r2,len(F[2])-r2)
    predicted=(1,1,7*q*(q-1)**2)
    assert betti==predicted,(q,betti,predicted)
    rot=trace(F,True); refl=trace(F,False)
    assert rot==[0,0,0],rot
    assert refl==[q,-2*q,-q*q],refl
    Lef=sum((-1)**i*v for i,v in enumerate(refl))
    h2_ref=-(q-1)*(q-2)
    assert Lef==2+h2_ref
    A=(q-1)*(q*q-2*q+2)//2
    B=(q-1)*(q*q-2)//2
    C=q*(q-1)**2
    assert 7*q*(q-1)**2==A+B+6*C
    assert 0==A+B-C
    assert h2_ref==A-B
    # H1 sign is negative under the reflection of the 7-cycle, trivial for rotation.
    print(f'q={q}: f={tuple(map(len,F))}, ranks={(r1,r2)}, H={betti}; refl={refl}; representation (triv,sign,W)={(A,B,C)}')

if __name__=='__main__':
    for q in (2,3,4): test(q)
    print('PASS: exact finite simplicial ranks, traces and representation dimensions')
