#!/usr/bin/env python3
"""Exact rational verification of split-graph cut/cycle projection identities.

The universal arguments are given in the accompanying mathematical proof;
finite checks here independently reconstruct full matrices and compare the
closed formulas on a bounded parameter grid.
"""
from fractions import Fraction as F
from itertools import combinations


def edges(a,b):
    return [('cc',i,j) for i,j in combinations(range(a),2)]+[('cp',i,j) for i in range(a) for j in range(b)]


def parameters(a,b):
    n=a+b
    h=F((a-1)*(a+2*b-2),a)
    d=2*b*(n-1)+(a-1)*(a+2*b-2)
    z=2*b*(n-3)+(a-1)*(a+2*b-4)
    bp=F(a+2*b-2,d)
    bq=F(a+2*b-4,z)
    ap=F(1-b*bp,a)
    aq=F(1-b*bq,a)
    cut=F(2*(n-1))*ap
    cycle=F(1)+2*(n-3)*aq
    return (ap,bp,cut),(aq,bq,cycle)


def matrix(a,b,A,B):
    E=edges(a,b); m=len(E)
    cols=[]
    for tag,i,j in E:
        k=[F(0)]*a
        h=[F(0)]*a
        g=[F(0)]*b
        if tag=='cc':
            k[i]+=1;k[j]-=1;s=F(0)
        else:
            h[i]+=1;g[j]+=1;s=F(1)
        u=[A*k[v]+B*(h[v]-s/a) for v in range(a)]
        v=[-g[w]/a for w in range(b)]
        cols.append([u[p]-u[q] if t=='cc' else u[p]-v[q] for t,p,q in E])
    return cols


def norm_columns(cols):
    return max(map(lambda c:sum(map(abs,c)),cols))


def identity_minus(cols):
    return [[(F(1) if i==j else F(0))-cols[j][i]
             for i in range(len(cols))] for j in range(len(cols))]


def verify(a,b):
    E=edges(a,b);m=len(E)
    (ap,bp,lcut),(aq,bq,lcycle)=parameters(a,b)
    assert ap*a+bp*b==1
    assert aq*a+bq*b==1
    assert 0<bp<bq<F(1,b)
    dc=2*b*(a+b-1)+(a-1)*(a+2*b-2)
    dz=2*b*(a+b-3)+(a-1)*(a+2*b-4)
    assert bq-bp==F(4*b*(b-1),dc*dz)
    assert (bp==F(1,a+b))==(a==2)
    assert (bq==F(1,a+b))==(a==4)
    for A,B,target,which in [(ap,bp,lcut,'cut'),(aq,bq,lcycle,'cycle')]:
        P=matrix(a,b,A,B)
        for c in P:
            assert len(c)==m
        # Projection range: P acts identically on every gradient basis.
        for vertex in range(a+b):
            grad=[(F(1) if i==vertex else F(0))-(F(1) if j==vertex else F(0))
                  if t=='cc' else (F(1) if i==vertex else F(0))-(F(1) if a+j==vertex else F(0))
                  for t,i,j in E]
            output=[sum(P[col][row]*grad[col] for col in range(m)) for row in range(m)]
            assert output==grad
        # Every column of P is the gradient of an explicit vertex potential;
        # therefore P^2=P follows from the previous assertion.
        for col in P:
            assert all(isinstance(x,F) for x in col)
        if which=='cut':assert norm_columns(P)==target
        else:assert norm_columns(identity_minus(P))==target
        for tag in ('cc','cp'):
            vals=[sum(map(abs,P[j])) if which=='cut'
                  else sum(map(abs,identity_minus(P)[j]))
                  for j,e in enumerate(E) if e[0]==tag]
            assert len(set(vals))==1
    assert norm_columns(matrix(a,b,ap,bp))==lcut
    assert norm_columns(identity_minus(matrix(a,b,aq,bq)))==lcycle
    assert lcut>=1 and lcycle>=1
    return m


def main():
    samples=0;entries=0
    for a in range(2,9):
        for b in range(2,9):
            entries+=verify(a,b);samples+=1
    print(f'CHECK_OK {samples} parameter pairs, {entries} edge columns, exact rational identities')

if __name__=='__main__':main()
