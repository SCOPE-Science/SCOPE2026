#!/usr/bin/env python3
"""Direct finite checks for two-sink Hamming network capture theorem.
Requires Python 3, NumPy and SymPy. Uses direct Hamiltonian diagonalization rather
than the analytic Hamming-scheme projectors when testing capture probabilities.
"""
import itertools, math
from collections import defaultdict
import numpy as np


def K(q,d,k,r):
    return sum((-1)**j*(q-1)**(k-j)*math.comb(r,j)*math.comb(d-r,k-j)
               for j in range(max(0,k-(d-r)),min(k,r)+1))


def analytic(q,d,a,b,x):
    t=sum(u!=v for u,v in zip(a,b))
    r=sum(u!=v for u,v in zip(a,x))
    s=sum(u!=v for u,v in zip(b,x))
    out=1.0/q**d
    for k in range(1,d+1):
        m=math.comb(d,k)*(q-1)**k
        h=K(q,d,k,t)
        u,v=K(q,d,k,r),K(q,d,k,s)
        assert m*m>h*h,(q,d,k,t,m,h)
        out+=(m*(u*u+v*v)-2*h*u*v)/(q**d*(m*m-h*h))
    return out


def verify_graph(q,d):
    verts=list(itertools.product(range(q),repeat=d)); n=len(verts)
    A=np.zeros((n,n),dtype=float)
    for i,x in enumerate(verts):
        for j in range(i):
            if sum(u!=v for u,v in zip(x,verts[j]))==1:
                A[i,j]=A[j,i]=1
    vals,U=np.linalg.eigh(A)
    spectral={}
    for k in range(d+1):
        lam=d*(q-1)-q*k
        B=U[:,np.abs(vals-lam)<1e-7]
        assert B.shape[1]==math.comb(d,k)*(q-1)**k
        spectral[k]=B@B.T
    combos=0;sites=0;worst=0.
    a=(0,)*d; ai=verts.index(a)
    for t in range(1,d+1):
        b=(1,)*t+(0,)*(d-t); bi=verts.index(b)
        P=np.zeros((n,n)); rk=0
        for k,E in spectral.items():
            Q=E[:,[ai,bi]]
            rank=np.linalg.matrix_rank(Q,tol=1e-8)
            assert rank==(1 if k==0 else 2),(q,d,t,k,rank)
            rk+=rank
            P+=Q@np.linalg.pinv(Q,rcond=1e-10)
        assert rk==2*d+1
        diagonal=np.diag(P)
        assert abs(np.trace(P)-2*d-1)<1e-8
        assert np.linalg.norm(P@P-P,ord='fro')<1e-7
        for i,x in enumerate(verts):
            expect=analytic(q,d,a,b,x)
            err=abs(diagonal[i]-expect)
            worst=max(worst,err)
            assert err<2e-8,(q,d,t,x,expect,diagonal[i])
            assert (expect>1-1e-8)==(x==a or x==b),(q,d,t,x,expect)
            sites+=1
        combos+=1
    return combos,sites,worst


def exact_projector_check():
    import sympy as sp
    q,d=3,3
    verts=list(itertools.product(range(q),repeat=d)); n=len(verts)
    A=sp.zeros(n,n)
    for i,x in enumerate(verts):
        for j in range(i):
            if sum(u!=v for u,v in zip(x,verts[j]))==1:
                A[i,j]=A[j,i]=1
    I=sp.eye(n); Es=[]
    for k in range(d+1):
        E=I
        lam=d*(q-1)-q*k
        for h in range(d+1):
            if h!=k:
                mu=d*(q-1)-q*h
                E=E*(A-mu*I)/(lam-mu)
        assert E*E==E
        Es.append(E)
    comparison=0
    a=(0,)*d; ai=verts.index(a)
    for t in [1,2,3]:
        b=(1,)*t+(0,)*(d-t);bi=verts.index(b)
        P=sp.zeros(n,n)
        for E in Es:
            Q=E[:,[ai,bi]]
            G=Q.T*Q
            if G.det()==0:
                assert E==Es[0]
                P+=Q[:,0]*Q[:,0].T/G[0,0]
            else: P+=Q*G.inv()*Q.T
        assert P*P==P
        assert sp.trace(P)==2*d+1
        for i,x in enumerate(verts):
            t0=sum(u!=v for u,v in zip(a,b))
            r=sum(u!=v for u,v in zip(a,x));s=sum(u!=v for u,v in zip(b,x))
            formula=sp.Rational(1,q**d)
            for k in range(1,d+1):
                m=math.comb(d,k)*(q-1)**k;h=K(q,d,k,t0)
                u,v=K(q,d,k,r),K(q,d,k,s)
                formula+=sp.Rational(m*(u*u+v*v)-2*h*u*v,q**d*(m*m-h*h))
            assert P[i,i]==formula,(t,x,P[i,i],formula)
            comparison+=1
    return comparison


def main():
    cases=[(3,3),(3,4),(4,3),(5,3)]
    checks=sites=0;worst=0.
    for q,d in cases:
        a,b,c=verify_graph(q,d)
        checks+=a; sites+=b;worst=max(worst,c)
        print(f'NUMERICAL q={q} d={d} pairs={a} sites={b} max_error={c:.3g}')
    n=exact_projector_check()
    print(f'EXACT sympy rational projector comparisons={n}')
    print(f'PASS graph_pair_cases={checks} vertex_checks={sites} exact_checks={n} max_error={worst:.3g}')
if __name__=='__main__': main()
