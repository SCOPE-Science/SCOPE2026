#!/usr/bin/env python3
"""Standalone exact-arithmetic checks of resistance metrics on complete multipartite graphs.

Requires Python 3 with sympy and numpy.  No network access or external data.
"""
from fractions import Fraction
from itertools import accumulate
from collections import Counter
import numpy as np
import sympy as sp


def scalar_test(parts):
    N = sum(parts)
    if len(set(parts)) == 1:
        return None
    ds = [N-v for v in parts]
    tau = [Fraction(1, v)-Fraction(2*N-1, N*N) for v in parts]
    S0 = sum(1/t for t in tau)
    S1 = sum(Fraction(d, 1)/t for d,t in zip(ds, tau))
    S2 = sum(Fraction(d*d, 1)/t for d,t in zip(ds, tau))
    assert S0*S2-S1*S1 != 0
    M = S2/(S0*S2-S1*S1)
    delta = M-Fraction((N-1)**2, 2*N*N)
    return M,delta


def verify_case(parts):
    N = sum(parts)
    offsets = [0] + list(accumulate(parts))
    colors = [i for i, size in enumerate(parts) for _ in range(size)]
    L = sp.zeros(N)
    for i in range(N):
        for j in range(i+1,N):
            if colors[i] != colors[j]:
                L[i,i]+=1;L[j,j]+=1;L[i,j]-=1;L[j,i]-=1
    J = sp.ones(N)/N
    Linv = (L+J).inv()-J
    R=sp.zeros(N)
    for i in range(N):
        for j in range(N):
            R[i,j]=Linv[i,i]+Linv[j,j]-2*Linv[i,j]
            if i==j:
                assert R[i,j]==0
            elif colors[i]==colors[j]:
                assert R[i,j]==sp.Rational(2,N-parts[colors[i]])
            else:
                a,b=colors[i],colors[j]
                assert R[i,j]==sp.Rational(N-1,N)*(sp.Rational(1,N-parts[a])+sp.Rational(1,N-parts[b]))
    D=R.multiply_elementwise(R)
    H=sp.eye(N)-J
    B=-(H*D*H)/2
    assert B*sp.ones(N,1)==sp.zeros(N,1)
    p2=scalar_test(parts)
    expected='strict' if p2 is None or p2[1]>0 else ('critical' if p2[1]==0 else 'indefinite')
    lamb=np.linalg.eigvalsh(np.array(B.tolist(),dtype=float))
    eps=1e-8
    pos=sum(lamb>eps); neg=sum(lamb< -eps); zeros=N-pos-neg
    target={'strict':(N-1,0,1),'critical':(N-2,0,2),'indefinite':(N-2,1,1)}[expected]
    assert (pos,neg,zeros)==target,(parts,(pos,neg,zeros),target, lamb)
    rank = B.rank()
    assert rank == N-zeros
    # Exact decomposition tested on several deterministic zero-sum coefficient families.
    C = sp.Rational(N-1,N)
    ds=[N-v for v in parts]
    ts=[sp.Rational(1,v)-sp.Rational(2*N-1,N*N) for v in parts]
    for shift in range(min(N,5)):
        z=[sp.Rational(((i+2*shift+1)%7)-3, 1) for i in range(N)]
        z[0]-=sum(z)
        xs=[sum(z[offsets[i]:offsets[i+1]]) for i in range(len(parts))]
        ys=[xs[i]/ds[i] for i in range(len(parts))]
        normsum=sum((z[j]-xs[i]/parts[i])**2 for i in range(len(parts)) for j in range(offsets[i],offsets[i+1]))
        # Internal energy uses group-specific denominators.
        q_rhs=2*C*C*sum(ys)**2-4*sum(ts[i]*ys[i]**2 for i in range(len(parts)))\
            -sum(sp.Rational(4,ds[i]**2)*sum((z[j]-xs[i]/parts[i])**2 for j in range(offsets[i], offsets[i+1])) for i in range(len(parts)))
        q_actual=(sp.Matrix([z]).multiply(D).multiply(sp.Matrix(z)))[0]
        assert q_actual==sp.expand(q_rhs),(parts,shift,q_actual,q_rhs)
    print('EXACT_CASE_OK',parts,'N',N,'inertia',(pos,neg,zeros),'margin',str(p2[1]) if p2 else 'equal-parts')

if __name__=='__main__':
    profiles=[(1,1),(1,2),(1,1,1),(2,2),(2,3),(2,4),(3,4),(2,2,2),
              (1,1,3),(1,2,2),(1,1,1,4),(2,2,4),(3,3,6),
              (1,1,3,5),(1,2,2,5),(2,3,5)]
    for p in profiles:
        verify_case(p)
    # Every partition of N<=12 cross-checks algebraic compressed inertia with
    # a direct numerical eigenvalue calculation of the exact powered-distance formula.
    for N in range(2,13):
        def partitions(rest, smallest=1):
            if rest==0:
                yield ()
            for n in range(smallest,rest+1):
                for tail in partitions(rest-n,n):
                    yield (n,)+tail
        count=0
        for a in partitions(N):
            if len(a)<2: continue
            colors=[i for i,v in enumerate(a) for _ in range(v)]
            R=np.zeros((N,N))
            for i in range(N):
                for j in range(N):
                    if i!=j:
                        R[i,j]=(2/(N-a[colors[i]]) if colors[i]==colors[j]
                         else (N-1)/N*(1/(N-a[colors[i]])+1/(N-a[colors[j]])))
            H=np.eye(N)-np.ones((N,N))/N
            B=-H@(R*R)@H/2
            eig=np.linalg.eigvalsh(B)
            npos=int(sum(eig>1e-9)); nneg=int(sum(eig< -1e-9)); nzero=N-npos-nneg
            sig=scalar_test(a)
            mode='strict' if sig is None or sig[1]>0 else ('critical' if sig[1]==0 else 'indefinite')
            target={'strict':(N-1,0,1),'critical':(N-2,0,2),'indefinite':(N-2,1,1)}[mode]
            assert (npos,nneg,nzero)==target,(a,target,(npos,nneg,nzero))
            count+=1
        print('PARTITION_CENSUS_OK',N,count)
    print('ALL_MULTIPARTITE_EUCLIDEAN_CHECKS_OK')
