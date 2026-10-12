#!/usr/bin/env python3
"""Exact Kirchhoff-index checks and numerical optimization probes for weighted clique bouquets."""
from fractions import Fraction as F
from itertools import product
from math import sqrt, isclose
import random

def invert(A):
    n=len(A)
    B=[list(map(F,row))+[F(int(i==j)) for j in range(n)] for i,row in enumerate(A)]
    for j in range(n):
        k=next((i for i in range(j,n) if B[i][j]),None)
        if k is None: raise ValueError('singular')
        B[j],B[k]=B[k],B[j]
        piv=B[j][j]
        B[j]=[x/piv for x in B[j]]
        for i in range(n):
            if i!=j:
                fac=B[i][j]
                if fac:
                    B[i]=[x-fac*y for x,y in zip(B[i],B[j])]
    return [row[n:] for row in B]

def edges(qs,aa,bb):
    e=[]; start=1
    for q,a,b in zip(qs,aa,bb):
        vv=list(range(start,start+q))
        for i in vv: e.append((0,i,F(a)))
        for ii in range(q):
            for jj in range(ii+1,q):e.append((vv[ii],vv[jj],F(b)))
        start+=q
    return e

def invert_float(A):
    n=len(A)
    B=[[float(x) for x in row]+[float(i==j) for j in range(n)] for i,row in enumerate(A)]
    for j in range(n):
        k=max(range(j,n),key=lambda i:abs(B[i][j]))
        assert abs(B[k][j])>1e-13
        B[j],B[k]=B[k],B[j]
        div=B[j][j]
        B[j]=[x/div for x in B[j]]
        for i in range(n):
            if i!=j:
                f=B[i][j]
                if f:
                    B[i]=[x-f*y for x,y in zip(B[i],B[j])]
    return [row[n:] for row in B]

def k_exact(qs,aa,bb):
    N=1+sum(qs)
    L=[[F(0) for j in range(N)] for i in range(N)]
    for i,j,w in edges(qs,aa,bb):
        L[i][i]+=w; L[j][j]+=w; L[i][j]-=w; L[j][i]-=w
    Q=invert([row[1:] for row in L[1:]])
    return N*sum(Q[i][i] for i in range(N-1))-sum(map(sum,Q))

def k_formula(qs,aa,bb):
    N=1+sum(qs)
    return sum(F(N-q,a)+F(N*(q-1),a+q*b) for q,a,b in zip(qs,aa,bb))

def local(q,N,c,d):
    t=d/c; beta=(q-1)*t/(2*q)
    if t>=2*N/(N-1): return float(q*q*c*(N-1)),1.0,False
    A=N-q; B=N*(q-1)
    y=sqrt(B*(1-beta)/(A*beta))
    C=q*c*(sqrt(A*(1-beta))+sqrt(B*beta))**2
    return C,y,True

def allocation(qs,cs,ds):
    N=1+sum(qs)
    lo=[local(q,N,c,d) for q,c,d in zip(qs,cs,ds)]
    S=sum(sqrt(C) for C,y,used in lo)
    ps=[sqrt(C)/S for C,y,used in lo]
    aa=[];bb=[]
    for q,c,d,p,(C,y,used) in zip(qs,cs,ds,ps,lo):
        x=(y-1)/q
        a=p/(q*c*(1+(q-1)*d*x/(2*c)))
        aa.append(a);bb.append(x*a)
    return S*S,aa,bb,ps,lo

def k_float(qs,aa,bb):
    N=1+sum(qs)
    return sum((N-q)/a + N*(q-1)/(a+q*b) for q,a,b in zip(qs,aa,bb))

def main():
    ct=0
    for qs in [(2,),(2,2),(2,3),(3,2),(2,2,2),(4,2),(3,3)]:
        m=len(qs)
        for j in range(31):
            aa=[F((3*i+2*j)%7+1,(j+i)%4+1) for i in range(m)]
            bb=[F((i+5*j)%8, (2+j)%5+1) for i in range(m)]
            k1=k_exact(qs,aa,bb)
            k2=k_formula(qs,aa,bb)
            assert k1==k2,(qs,aa,bb,k1,k2)
            ct+=1
    random.seed(7301991)
    opt=0; clipped=0; interior=0
    for _ in range(700):
        qs=[random.choice([2,3,4]) for i in range(random.randint(1,4))]
        N=1+sum(qs)
        cs=[random.uniform(0.25,5.0) for q in qs]
        ds=[c*random.uniform(.02,5.0) for c in cs]
        K,aa,bb,ps,lo=allocation(qs,cs,ds)
        assert abs(sum(q*c*a+q*(q-1)/2*d*b for q,c,d,a,b in zip(qs,cs,ds,aa,bb))-1)<2e-14
        assert abs(k_float(qs,aa,bb)-K)<2e-9*max(1,K)
        # Exact first-order condition at boundary and interior via normalized derivative.
        for q,c,d,a,b,(C,y,used) in zip(qs,cs,ds,aa,bb,lo):
            t=d/c; beta=(q-1)*t/(2*q)
            A=N-q;B=N*(q-1)
            dFy=A*beta - B*(1-beta)/(y*y)
            if used:
                assert y>1 and abs(dFy)<1e-10*max(1,abs(A*beta))
                interior+=1
            else:
                assert y==1 and dFy >= -1e-10
                clipped+=1
        # Random feasible asymmetric full edge conductances: test via grounded inverse numeric matrix.
        for j in range(3):
            e=edges(qs,aa,bb)
            # Change every individual edge independently, then normalize to unit cost.
            un=[];base=0
            start=1
            for q,c,d in zip(qs,cs,ds):
                for x in range(q):
                    un.append((0,start+x,c))
                for x in range(q):
                    for y in range(x+1,q):un.append((start+x,start+y,d))
                start+=q
            rates=[random.uniform(.05,2.0) for i in un]
            denom=sum(w*cost for w,(_,_,cost) in zip(rates,un))
            rates=[w/denom for w in rates]
            M=[[0.0]*N for i in range(N)]
            for (u,v,cost),w in zip(un,rates):
                M[u][u]+=w; M[v][v]+=w;M[u][v]-=w;M[v][u]-=w
            Q=invert_float([row[1:] for row in M[1:]])
            k_rand=N*sum(Q[i][i] for i in range(N-1))-sum(map(sum,Q))
            assert k_rand > K-3e-7*max(K,1),(qs,K,k_rand)
        opt+=1
    print(f'VERIFY_OK {ct} exact Laplacian-inverse Kirchhoff identities; {opt} heterogeneous optimal allocation/budget/stationarity checks; {interior} retained and {clipped} deleted internal-edge cases; {3*opt} feasible nonsymmetric numerical comparisons')
if __name__=='__main__':main()
