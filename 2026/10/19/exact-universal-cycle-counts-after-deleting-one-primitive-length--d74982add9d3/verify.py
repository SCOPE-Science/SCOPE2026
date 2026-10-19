#!/usr/bin/env python3
"""Exact, standalone checks for the two one-necklace deletion formulas."""
from fractions import Fraction
from collections import defaultdict
from itertools import product
from math import factorial


def det3(M):
    a,b,c=M[0]; d,e,f=M[1]; g,h,i=M[2]
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)


def formula_ratio(q, kind):
    if kind == 'aab':
        return Fraction((q-2)*(q*q-q+1),q**3)
    return Fraction(q**4-3*q**3+3*q*q-3*q+3,q**4)


def cycles_formula(q, kind):
    factor = formula_ratio(q,kind)
    trees = q**(q*q-3)*factor
    assert trees.denominator == 1
    return int(trees)*factorial(q-2)**3*factorial(q-1)**(q*q-3)


def orbit(w):
    return {tuple(w[i:]+w[:i]) for i in range(3)}


def allowed_edges(q,w):
    banned=orbit(w)
    return [x for x in product(range(q),repeat=3) if x not in banned]


def laplacian(q,w):
    N=q*q
    L=[[0]*N for _ in range(N)]
    for a,b,c in allowed_edges(q,w):
        i=a*q+b; j=b*q+c
        L[i][i]+=1; L[i][j]-=1
    return L


def bareiss(M):
    A=[list(map(int,row)) for row in M]
    n=len(A); sign=1; denom=1
    if n==0:return 1
    for k in range(n-1):
        if A[k][k]==0:
            swap=next((i for i in range(k+1,n) if A[i][k]),None)
            if swap is None:return 0
            A[k],A[swap]=A[swap],A[k];sign=-sign
        p=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator=A[i][j]*p-A[i][k]*A[k][j]
                assert numerator%denom==0
                A[i][j]=numerator//denom
            A[i][k]=0
        denom=p
    return sign*A[-1][-1]


def perturbation_ratio(q,w):
    v=[(w[i],w[(i+1)%3]) for i in range(3)]
    I=lambda x,y:int(x==y)
    A=lambda x,y:int(x[1]==y[0])
    K=[[Fraction(I(v[i],v[j])-I(v[(i+1)%3],v[j]),q)
       +Fraction(A(v[i],v[j])-A(v[(i+1)%3],v[j]),q*q)
        for j in range(3)] for i in range(3)]
    return det3([[int(i==j)-K[i][j] for j in range(3)] for i in range(3)])


def explicit_euler_tours(q,w):
    E=allowed_edges(q,w); m=len(E)
    origin=E[0][:2]; start=E[0][1:]
    adjacency=defaultdict(list)
    for j,(a,b,c) in enumerate(E): adjacency[a,b].append((j,(b,c)))
    def search(v,visited):
        if visited.bit_count()==m:
            return int(v==origin)
        return sum(search(vnext,visited|(1<<j))
                   for j,vnext in adjacency[v] if not (visited>>j)&1)
    return search(start,1)


def main():
    for q in range(2,7):
        words=[('aab',[0,0,1])]
        if q>=3: words.append(('abc',[0,1,2]))
        for kind,w in words:
            ratio=formula_ratio(q,kind)
            assert perturbation_ratio(q,w)==ratio
            L=laplacian(q,w)
            minor=[row[:-1] for row in L[:-1]]
            tree=bareiss(minor)
            expected=q**(q*q-3)*ratio
            assert expected.denominator==1 and tree==expected, (q,kind,tree,expected)
            assert tree*factorial(q-2)**3*factorial(q-1)**(q*q-3)==cycles_formula(q,kind)
            if q<=3:
                direct=explicit_euler_tours(q,w)
                assert direct==cycles_formula(q,kind), (q,kind,direct,cycles_formula(q,kind))
            print('q=%d kind=%s trees=%d tours=%d' % (q,kind,tree,cycles_formula(q,kind)))
    assert cycles_formula(3,'aab')==cycles_formula(3,'abc')==12096
    assert cycles_formula(4,'aab')==2848587100012412928
    assert cycles_formula(4,'abc')==2821196839435370496
    print('ALL_CHECKS_PASS')

if __name__=='__main__':main()
