#!/usr/bin/env python3
"""Independent exact and numerical checks of the star spectral-allocation formulas."""
from fractions import Fraction as F
from itertools import combinations, product
from math import sqrt, isclose
import numpy as np


def determinant(M):
    n = len(M)
    if n == 0:
        return F(1)
    A = [list(row) for row in M]
    sign = 1
    prev = F(1)
    for k in range(n-1):
        if A[k][k] == 0:
            pos = next((j for j in range(k+1,n) if A[j][k]), None)
            if pos is None:
                return F(0)
            A[k], A[pos] = A[pos], A[k]
            sign *= -1
        pivot = A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                A[i][j] = (A[i][j]*pivot - A[i][k]*A[k][j])/prev
        for i in range(k+1,n):
            A[i][k] = F(0)
        prev = pivot
    return sign*A[-1][-1]


def is_psd(A):
    m = len(A)
    return all(determinant([[A[i][j] for j in inds] for i in inds]) >= 0
               for r in range(1,m+1) for inds in combinations(range(m),r))


def optimal_weights_from_integer_sqrt_costs(a, budget=F(1)):
    n=len(a)
    costs=[F(x*x) for x in a]
    S=sum(a)
    j=max(range(n),key=lambda i:a[i])
    delta=max(F(0),F(2*a[j]-S))
    T=sum(costs)-delta*delta/F(n+1)
    lam=budget/T
    rates=[lam*(1 + delta/(F(n+1)*a[i])) for i in range(n)]
    if delta:
        rates[j]=lam*(1-delta/(F(n+1)*a[j]))
    return costs,T,lam,rates,delta


def positive_eigenvalue_star(rates):
    n=len(rates)
    L=np.zeros((n+1,n+1))
    for i,w in enumerate(rates,1):
        L[0,0]+=float(w)
        L[0,i]=L[i,0]=-float(w)
        L[i,i]=float(w)
    return np.linalg.eigvalsh(L)[1:]


def run():
    count=0
    for m in range(2,7):
        for a in product(range(1,5),repeat=m):
            if m>4 and count>3600:
                break
            costs,T,lam,w,delta=optimal_weights_from_integer_sqrt_costs(a)
            assert sum(c*x for c,x in zip(costs,w))==F(1)
            assert all(x>0 for x in w)
            gamma=F(1,m+1)
            A=[[((w[i]/lam-1) if i==j else F(0))+gamma for j in range(m)] for i in range(m)]
            assert is_psd(A)
            assert determinant(A)==0
            eigs=positive_eigenvalue_star(w)
            assert abs(eigs[0]/float(lam)-1)<5e-11, (a,lam,eigs[0])
            if delta:
                assert eigs[1]-eigs[0]>1e-10*float(lam)
            else:
                if m>2:
                    assert abs(eigs[m-2]/float(lam)-1)<5e-11
            count+=1
        if m>4 and count>3600:
            break
    print(f'PASS: {count} exact cost/budget/PSD and independent spectral comparisons')
    rng=np.random.default_rng(20261024)
    ntrial=0
    for m in range(2,13):
        for _ in range(70):
            s=np.exp(rng.normal(0,1.4,size=m))
            c=s*s
            delta=max(0.0,2*max(s)-sum(s))
            T=sum(c)-delta*delta/(m+1)
            lam=1/T
            j=int(np.argmax(s))
            w=np.array([lam*(1+delta/((m+1)*z)) for z in s])
            if delta:w[j]=lam*(1-delta/((m+1)*s[j]))
            assert np.all(w>0)
            assert abs(float(c@w)-1)<3e-12
            eig=positive_eigenvalue_star(w)[0]
            assert abs(eig/lam-1)<1e-9,(m,c,w,eig,lam)
            for _ in range(15):
                v=rng.dirichlet(np.ones(m)) / c
                gap=positive_eigenvalue_star(v)[0]
                assert gap <= lam*(1+1e-10),(m,c,w,v,gap,lam)
                ntrial+=1
    print(f'PASS: {ntrial} asymmetric competing allocations; 770 independent real-price spectral comparisons')
    # The square-root polygon boundary has one price 4 and two prices 1.
    c,T,lam,w,delta=optimal_weights_from_integer_sqrt_costs((2,1,1))
    assert delta==0 and w==[F(1,6)]*3
    c,T,lam,w,delta=optimal_weights_from_integer_sqrt_costs((3,1,1))
    assert delta==1 and w[0]<w[1] and w[1]==w[2]
    print('PASS: equality boundary and strict dominant-price phase transition')

if __name__=='__main__': run()
