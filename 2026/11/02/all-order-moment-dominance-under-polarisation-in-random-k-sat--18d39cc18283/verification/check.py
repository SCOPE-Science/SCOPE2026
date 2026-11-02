"""Exact small-model checks for all-order moment monotonicity in polarised k-SAT.
Uses only the Python standard library. Independent clause enumeration and XOR noise checks.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import comb


def clauses(n, k, p):
    out = []
    for K in combinations(range(n), k):
        for signs in product(range(2), repeat=k):
            s = sum(signs)
            prob = (p**s*(1-p)**(k-s) + p**(k-s)*(1-p)**s)/(2*comb(n,k))
            out.append((K, signs, prob))
    assert sum((w for _,_,w in out),F(0))==1
    return out


def tables(n,k,p):
    D=clauses(n,k,p)
    universe=list(product(range(2),repeat=n))
    tab=[]
    for x in universe:
        tab.append([all(x[i]==sign for i,sign in zip(K,sgn))==False for K,sgn,_ in D])
    return universe,D,tab


def moment(n,k,p,m,r,distinct=False):
    universe,D,tab=tables(n,k,p)
    T=F(0)
    for ids in product(range(2**n),repeat=r):
        if distinct and len(set(ids))<r: continue
        a=sum((w for c,(_,_,w) in enumerate(D) if all(tab[i][c] for i in ids)),F(0))
        T+=a**m
    return T


def verify():
    ct=0
    for n,k in [(2,2),(3,2),(3,3)]:
      for m in (1,2,3):
        for r in (1,2,3):
          vals=[moment(n,k,p,m,r) for p in (F(0),F(1,4),F(1,2))]
          assert vals[0]>=vals[1]>=vals[2]; ct+=1
          if m>=2: assert vals[0]>vals[1]>vals[2];ct+=1
          if m==1: assert vals[0]==vals[1]==vals[2];ct+=1
          fact=[moment(n,k,p,m,r,True) for p in (F(0),F(1,4),F(1,2))]
          assert fact[0]>=fact[1]>=fact[2];ct+=1
          if m==1: assert fact[0]==fact[1]==fact[2];ct+=1
    # Check one-clause BSC convolution exactly on all tuples of two assignments.
    n,k=3,2
    for p,q in [(F(0),F(1,4)),(F(1,4),F(1,2))]:
      eps=(q-p)/(1-2*p)
      universe,Dp,tabp=tables(n,k,p)
      _,Dq,tabq=tables(n,k,q)
      for i,j in product(range(2**n),repeat=2):
        lhs=sum((w for c,(_,_,w) in enumerate(Dq) if tabq[i][c] and tabq[j][c]),F(0))
        rhs=F(0)
        for bits in universe:
          u=sum(bits); pr=eps**u*(1-eps)**(n-u)
          x=tuple(a^b for a,b in zip(universe[i],bits))
          y=tuple(a^b for a,b in zip(universe[j],bits))
          ix=universe.index(x);iy=universe.index(y)
          a=sum((w for c,(_,_,w) in enumerate(Dp) if tabp[ix][c] and tabp[iy][c]),F(0))
          rhs+=pr*a
        assert lhs==rhs;(ct:=ct+1)
    print(f'PASS: {ct} exact rational assertions; full tuple/BSC identities verified for n=3,k=2')

if __name__=='__main__': verify()
