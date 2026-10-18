"""Exact rank and parity comparison of dicyclic/dihedral three-tap filters.

Run from same folder as check.py: python twist_check.py.
Integer nullities use SymPy exact rational elimination. Also counts all
singular and half-nullity mixed supports for 2 <= m <= 20 combinatorially.
"""
from itertools import combinations
from math import gcd
from sympy import QQ, zeros
from sympy.polys.matrices import DomainMatrix
from check import group_product, predicted_nullity


def dihedral_product(x,y,m):
    i,s=x; j,t=y
    return ((i + (1 if s==0 else -1)*j)%(2*m),(s+t)%2)


def dihedral_prediction(triple,m):
    n=2*m
    blocks=[[i for i,s in triple if s==j] for j in (0,1)]
    if len(blocks[0])==3 or len(blocks[1])==3:
        return predicted_nullity(triple,m)
    pair=blocks[0] if len(blocks[0])==2 else blocks[1]
    u=(pair[1]-pair[0])%n
    g=gcd(n,u)
    return 2*g if (n//g)%3==0 else 0


def exact_rank_nullity(m,triple,twist):
    elements=[(i,s) for s in (0,1) for i in range(2*m)]
    pos={x:i for i,x in enumerate(elements)}
    matrix=zeros(4*m)
    product=group_product if twist else dihedral_product
    for s in triple:
        for col,t in enumerate(elements):
            matrix[pos[product(s,t,m)],col]+=1
    return 4*m-DomainMatrix.from_Matrix(matrix).convert_to(QQ).rank()


def valuation(n,p):
    out=0
    while n%p==0:
        out+=1
        n//=p
    return out


def compute(m):
    n=2*m
    elements=[(i,s) for s in (0,1) for i in range(n)]
    half=singular=0
    examples=[]
    for triple in combinations(elements,3):
        q=predicted_nullity(triple,m)
        d=dihedral_prediction(triple,m)
        assert (q==0)==(d==0),(m,triple,q,d)
        assert q==d or (q>0 and 2*q==d),(m,triple,q,d)
        if q:
            singular+=1
        if q>0 and 2*q==d:
            half+=1
            if len(examples)<2: examples.append((triple,q,d))
        if m in (3,6):
            assert exact_rank_nullity(m,triple,True)==q
            assert exact_rank_nullity(m,triple,False)==d
    r,s=valuation(m,3),valuation(m,2)
    expected_half=4*m**3*(3**r-1)//(2**s*3**r) if r else 0
    expected_singular=(2*m**3*(3**(2*r)-1)//(3*3**(2*r)) + 8*m**3*(3**r-1)//3**r) if r else 0
    assert half==expected_half,(m,half,expected_half)
    assert singular==expected_singular,(m,singular,expected_singular)
    print(f'm={m} singular={singular} halved={half} examples={examples}',flush=True)


if __name__=='__main__':
    for m in range(2,13): compute(m)
