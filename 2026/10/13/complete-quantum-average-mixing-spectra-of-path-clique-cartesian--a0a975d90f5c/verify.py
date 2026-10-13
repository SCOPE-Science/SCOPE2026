#!/usr/bin/env python3
"""Reproduce the exact path-clique mixing formula by independent adjacency diagonalization.
Requires Python 3, NumPy, SymPy.
"""
from fractions import Fraction
import math
import numpy as np
import sympy as sp


def formula(m,q):
    L=m+1
    Jm=np.ones((m,m),float)
    Fm=np.fliplr(np.eye(m))
    B=(2*Jm+np.eye(m)+Fm)/(2*L)
    if q>=3:
        C=(1-2/q)*np.eye(q)+(2/q**2)*np.ones((q,q))
        return np.kron(B,C)
    plus=np.ones((2,2))/2
    minus=np.array([[1,-1],[-1,1]],float)/2
    output=np.kron(B,plus)
    if L%3==0:
        x=np.arange(1,m+1)
        w=2/L*np.sin(np.pi*x/3)*np.sin(2*np.pi*x/3)
        output+=np.kron(np.outer(w,w),minus)
    return output


def adjacency(m,q):
    P=np.zeros((m,m))
    for i in range(m-1):P[i,i+1]=P[i+1,i]=1
    K=np.ones((q,q))-np.eye(q)
    return np.kron(P,np.eye(q))+np.kron(np.eye(m),K)


def independent_average(m,q):
    A=adjacency(m,q)
    eig, vec=np.linalg.eigh(A)
    out=np.zeros_like(A)
    # exact equal eigenvalues of integral symmetric matrices can be identified
    # to 1e-9 for tested finite cases (minimum separated gaps monitored).
    groups=[]
    for k,ev in enumerate(eig):
        if not groups or abs(ev-eig[groups[-1][0]])>1e-9:groups.append([k])
        else: groups[-1].append(k)
    min_gap=min((eig[g[0]]-eig[groups[i-1][0]] for i,g in enumerate(groups) if i),default=1)
    for g in groups:
        E=vec[:,g]@vec[:,g].T
        out+=E*E
    return out,min_gap


def symbolic_checks():
    # Independently build the spectral projectors for P2 x K2 and P5 x K2
    # using exact eigenvectors of the two factors; no numeric interpolation.
    total=0
    for m in (2,3,5):
        for q in (2,3):
            n=m*q
            if n>15:continue
            Ap=sp.zeros(m)
            for a in range(m-1):Ap[a,a+1]=Ap[a+1,a]=1
            Ak=sp.ones(q)-sp.eye(q)
            A=sp.kronecker_product(Ap,sp.eye(q))+sp.kronecker_product(sp.eye(m),Ak)
            eigs=A.eigenvects()
            if sum(len(vecs) for _,_,vecs in eigs)!=n:
                raise AssertionError('bad projector rank')
            out=sp.zeros(n)
            for _,_,basis in eigs:
                V=sp.Matrix.hstack(*basis)
                E=V*(V.T*V).inv()*V.T
                out+=E.multiply_elementwise(E)
            L=m+1
            R=(2*sp.ones(m)+sp.eye(m)+sp.zeros(m))/(2*L)
            for j in range(m):R[j,m-1-j]+=sp.Rational(1,2*L)
            if q>=3:
                C=(1-sp.Rational(2,q))*sp.eye(q)+sp.Rational(2,q*q)*sp.ones(q)
                target=sp.kronecker_product(R,C)
            else:
                Pplus=sp.ones(2)/2
                Pminus=sp.Matrix([[1,-1],[-1,1]])/2
                target=sp.kronecker_product(R,Pplus)
                if L%3==0:
                    w=sp.Matrix([sp.simplify(sp.Rational(2,L)*sp.sin(sp.pi*x/3)*sp.sin(2*sp.pi*x/3)) for x in range(1,L)])
                    target+=sp.kronecker_product(w*w.T,Pminus)
            assert out==target,(m,q,sp.simplify(out-target))
            total+=n*n
    return total


def main():
    worst=0.0
    trials=0
    min_sep=1.0
    for m in range(2,19):
        for q in (2,3,4,5,6):
            observed,gap=independent_average(m,q)
            proposed=formula(m,q)
            error=np.max(np.abs(observed-proposed))
            worst=max(worst,error)
            assert error<1e-10,(m,q,error)
            assert np.max(np.abs(observed.sum(axis=1)-1))<1e-10
            min_sep=min(min_sep,gap)
            ev=np.linalg.eigvalsh(observed)
            rank=int(np.sum(ev>1e-8))
            want=(math.ceil(m/2)+(int((m+1)%3==0))) if q==2 else q*math.ceil(m/2)
            assert rank==want,(m,q,rank,want)
            trials+=1
    exact=symbolic_checks()
    for m in (2,5,8,11):
        v=np.linalg.eigvalsh(formula(m,2))
        positive=v[v>1e-9]
        L=m+1
        assert np.min(abs(positive-3/(2*L)))<1e-10
    print(f'VERIFY_OK independent_graphs={trials} exact_entries={exact} resonance_tests=4 '
          f'worst_matrix_error={worst:.2e} min_distinct_gap={min_sep:.3e} '
          'P5_K2_rank=4/10 P6_K3_rank=9/18')

if __name__=='__main__':main()
