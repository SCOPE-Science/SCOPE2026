#!/usr/bin/env python3
"""Reproducible checks of the four-cycle spectral-gap allocation formulas.
Uses only the Python standard library. Computations do not replace the proof.
"""
from fractions import Fraction as Q
from math import sqrt
from random import Random

EDGES=((0,1),(1,2),(2,3),(0,3))

def lap(weights):
    M=[[0.0]*4 for _ in range(4)]
    for (i,j),x in zip(EDGES,weights):
        x=float(x)
        M[i][i]+=x;M[j][j]+=x;M[i][j]-=x;M[j][i]-=x
    return M

def evals_symmetric(A):
    # Standard Jacobi diagonalization for real symmetric 4-by-4 matrices.
    A=[list(map(float,row)) for row in A]
    for _ in range(110):
        p,q=max(((i,j) for i in range(4) for j in range(i+1,4)),key=lambda ij:abs(A[ij[0]][ij[1]]))
        if abs(A[p][q])<1.e-13:break
        tau=(A[q][q]-A[p][p])/(2*A[p][q])
        t=(1 if tau>=0 else -1)/(abs(tau)+sqrt(1+tau*tau))
        c=1/sqrt(1+t*t);s=t*c
        app,aqq,apq=A[p][p],A[q][q],A[p][q]
        A[p][p]=app-t*apq;A[q][q]=aqq+t*apq
        A[p][q]=A[q][p]=0.
        for k in range(4):
            if k!=p and k!=q:
                akp,akq=A[k][p],A[k][q]
                A[k][p]=A[p][k]=c*akp-s*akq
                A[k][q]=A[q][k]=s*akp+c*akq
    return sorted(A[i][i] for i in range(4))

def gap(weights):return evals_symmetric(lap(weights))[1]

def optimal(tau,B=1.0):
    if tau < 9:
        t=sqrt(tau)
        lam=4*B/(5+tau+2*t)
        return (lam/2,lam*(1+t)/4,lam/2,lam*(1+1/t)/4),lam
    lam=B/5
    return (1.5*lam,2*lam,1.5*lam,0.),lam

def exact_rational_squared_cost_check(k):
    # Tau=k^2, k positive rational and tau<=9.
    k=Q(k);tau=k*k;B=Q(1)
    D=Q(5)+tau+2*k;lam=Q(4)/D
    a=lam/2;b=lam*(1+k)/4;c=lam*(1+1/k)/4
    assert 2*a+b+tau*c==B
    # Reflection-even eigenvalue: 2a; odd block eigenvalue: lambda.
    assert 2*a==lam
    assert (a+2*c-lam)*(a+2*b-lam)==a*a
    assert a+2*c>=lam and a+2*b>=lam
    # The remaining odd eigenvalue exceeds lambda.
    assert (2*a+2*b+2*c-lam)>lam
    # AM-GM/KKT equality encoded using exact rational arithmetic.
    U=a+2*b-lam;V=a+2*c-lam
    assert U==a*k and V==a/k
    return 1

def boundary_family_check(a):
    a=Q(a);b=a+Q(1,2);c=Q(1,2)-a/3
    assert Q(1,2)<=a<=Q(3,2) and c>=0
    assert 2*a+b+9*c==5
    assert 2*a>=1
    assert (a+2*c-1)*(a+2*b-1)==a*a
    return 1

if __name__=='__main__':
    exact=0
    for den in range(1,10):
        for num in range(1,3*den+1):
            exact+=exact_rational_squared_cost_check(Q(num,den))
    boundary=sum(boundary_family_check(Q(k,10)) for k in range(5,16))
    rng=Random(20261025)
    analytic=0;sample=0
    for j in range(120):
        tau=10**rng.uniform(-2,3)
        B=10**rng.uniform(-2,2)
        w,lam=optimal(tau,B)
        assert abs(sum(x*p for x,p in zip(w,(1,1,1,tau)))-B)<1e-8*B
        assert abs(gap(w)-lam)<2e-8*max(1,B)
        analytic+=1
        # Arbitrary asymmetric random feasible allocations, including boundary weights.
        for _ in range(35):
            vs=[rng.random() if rng.random()>.1 else 0. for _ in range(4)]
            den=sum(x*p for x,p in zip(vs,(1,1,1,tau)))
            if not den:continue
            wtest=[B*x/den for x in vs]
            assert gap(wtest)<=lam+3e-8*max(1,B)
            sample+=1
    for tau in (0.4,1.,4.,8.,9.,10.,20.,81.):
        B=5.
        _,lam=optimal(tau,B)
        if tau<9:assert lam>B/5
        if tau>=9:assert abs(lam-B/5)<1e-10
    assert boundary_family_check(Q(1))
    print('VERIFY_OK exact_rational_sqrt_cost_cases=%d boundary_family_cases=%d independent_spectra=%d arbitrary_feasible_comparisons=%d'%(exact,boundary,analytic,sample))
    print('Scope: numerical comparisons are finite; global optimality follows from the two-block proof and AM-GM or Rayleigh bounds.')
