#!/usr/bin/env python3
"""Exact finite-dimensional certificates for a monitored quantum path (L=1,...,4).
Public scientific reproduction code; requires sympy."""
from fractions import Fraction
from sympy import Matrix, Rational, zeros

def quantum_exact(L):
    # Transient lattice positions -L+1,...,L-1; coin 0 is +, coin 1 is -.
    states=[(x,c) for x in range(1-L,L) for c in range(2)]
    idx={v:i for i,v in enumerate(states)}; dim=len(states)
    B=zeros(dim,dim)
    for j,(x,c) in enumerate(states):
        for d in range(2):
            y=x+(1 if d==0 else -1)
            if abs(y)<L: B[idx[(y,d)],j]= (1 if c==0 else (-1 if d==0 else 1))
    # First-step evolution: K=B/sqrt(2); on density matrices K rho K^T=(B rho B^T)/2.
    # Invariant real symmetric, fixed spatial parity block; basis i<=j.
    pairs=[(i,j) for i in range(dim) for j in range(i,dim)
           if (states[i][0]-states[j][0])%2==0]
    pidx={p:i for i,p in enumerate(pairs)};N=len(pairs)
    A=zeros(N,N)
    for k,(i,j) in enumerate(pairs):
        cols_i=[(a,B[a,i]) for a in range(dim) if B[a,i]]
        cols_j=[(a,B[a,j]) for a in range(dim) if B[a,j]]
        for a,vi in cols_i:
            for b,vj in cols_j:
                if a<=b and (a,b) in pidx: A[pidx[(a,b)],k]+=vi*vj/2
                
        if i!=j:
            for a,vj in cols_j:
                for b,vi in cols_i:
                    if a<=b and (a,b) in pidx:A[pidx[(a,b)],k]+=vj*vi/2
                    
    # Matrix column k is the coefficient of B E_k B^T/2.
    eye=Matrix.eye(N)
    e=zeros(N,1);j0=idx[(0,0)];e[pidx[(j0,j0)],0]=1
    F=eye-A
    v=F.inv()*e
    y=F.inv()*v
    mu=sum(v[k,0] for k,(i,j) in enumerate(pairs) if i==j)
    weighted=sum(y[k,0] for k,(i,j) in enumerate(pairs) if i==j)
    second=2*weighted-mu
    var=second-mu**2
    weak=(mu**2-var-mu)/2
    # Exhaustive residual identities prove all moments exactly.
    assert F*v==e and F*y==v
    return int(N),mu,second,var,weak

def classical_exact(L):
    # Absorbing simple random walk on the same centered interval.
    pos=list(range(1-L,L)); idx={x:i for i,x in enumerate(pos)}
    Q=zeros(len(pos),len(pos))
    for j,x in enumerate(pos):
        for y in (x-1,x+1):
            if y in idx: Q[idx[y],j]+=Rational(1,2)
    e=zeros(len(pos),1);e[idx[0],0]=1
    F=Matrix.eye(len(pos))-Q
    v=F.inv()*e;w=F.inv()*v
    mean=sum(v);second=2*sum(w)-mean
    var=second-mean**2
    weak=(mean**2-mean-var)/2
    assert F*v==e and F*w==v
    return mean,second,var,weak

if __name__=='__main__':
    expected={1:(1,1,0,0),2:(4,24,8,2),3:(9,145,64,4),4:(16,560,304,-32)}
    for L in range(1,5):
        n,mu,second,var,weak=quantum_exact(L)
        assert (mu,second,var,weak)==expected[L],(L,n,mu,second,var,weak)
        classical=classical_exact(L)
        assert classical==(L**2,Rational(5*L**4-2*L**2,3),Rational(2*L**2*(L**2-1),3),Rational(L**2*(L**2-1),6))
        print(f'L={L}: invariant-dim={n}, quantum mean={mu}, second={second}, variance={var}, weak-reset slope={weak}; classical weak-reset slope={classical[3]}; all exact residuals PASS')
