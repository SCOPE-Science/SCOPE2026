#!/usr/bin/env python3
"""Exact checks for the Euclidean inradius of bistar symmetric-edge polytopes.
Only Python standard library is needed for all-rational enumeration and rank.
"""
from itertools import product
from math import comb
from fractions import Fraction

def v_from_edges(a,b,s):
    # raw vertex potentials: A leaves, hub A, hub B, B leaves
    return [s[i] for i in range(a)] + [0,s[a]] + [s[a]+s[a+1+j] for j in range(b)]

def sqnorm_centered(v):
    n=len(v)
    return Fraction(n*sum(x*x for x in v)-sum(v)**2,n)

def centered_integer(v):
    n=len(v);su=sum(v)
    return tuple(n*x-su for x in v)

def rank_integer(rows):
    if not rows:return 0
    mat=[[Fraction(x) for x in row] for row in rows]
    rr=0; c=0; M=len(mat); N=len(mat[0]);
    while c<N and rr<M:
        piv=next((i for i in range(rr,M) if mat[i][c]),None)
        if piv is None:c+=1;continue
        mat[rr],mat[piv]=mat[piv],mat[rr]
        div=mat[rr][c]
        mat[rr]=[x/div for x in mat[rr]]
        for i in range(rr+1,M):
            fac=mat[i][c]
            if fac:
                mat[i]=[x-fac*y for x,y in zip(mat[i],mat[rr])]
        rr+=1;c+=1
    return rr

def formula(a,b):
    N=a+b+2;L=max(a,b);U=min(a,b)
    if L<=2*U+1:
        return Fraction(9*a*b+5*(a+b)+1,N),2,1
    if L%2:
        k=(L-2*U-1)//2
        return Fraction(L+1+4*U),2*comb(L,k),L
    k=(L-2*U-2)//2
    return Fraction(L+1+4*U)-Fraction(1,N),2*(comb(L,k)+comb(L,k+1)),L+1

def exact(a,b):
    M=Fraction(-1);stars=[]
    for bits in product((-1,1),repeat=a+b+1):
        v=v_from_edges(a,b,bits)
        F=sqnorm_centered(v)
        if F>M:M=F;stars=[centered_integer(v)]
        elif F==M:stars.append(centered_integer(v))
    return M,len(stars),rank_integer(stars)

def main():
    pairs=[(a,b) for a in range(2,7) for b in range(2,8)] + [(2,8),(2,9),(2,10),(3,10),(3,11),(4,12)]
    for a,b in pairs:
        pred=formula(a,b);calc=exact(a,b)
        assert pred==calc,(a,b,pred,calc)
    print('PASS exact: %d bistar instances, checked radius, tangency count, rank'%len(pairs))
    for a,b in [(2,2),(2,5),(2,6),(2,7),(2,8),(3,9),(4,12)]:
        print(a,b,formula(a,b))
if __name__=='__main__':main()
