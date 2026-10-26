#!/usr/bin/env python3
"""Independent numeric and algebraic checks for the complete-core corona mixing theorem.

The infinite-family assertion is proved in RESULT.md. This program verifies its
finite-dimensional spectral identities and several finite optimization tests.
"""
import math
import numpy as np
from scipy.optimize import minimize


def closed(m):
    c = m / (2*(m-1))
    d = 1-c
    s = math.sqrt(2*c)
    b = (c+d*s)/(2+d*s)
    a = (1-b)/(m-1)
    mu = (d+c*s)/(1+c*c)
    return a,b,mu


def transition(m,a,b):
    P=np.zeros((2*m,2*m),dtype=float)
    for i in range(m):
        for j in range(m):
            if i!=j:
                P[i,j]=a
        P[i,m+i]=P[m+i,i]=b
        P[i,i]=1-(m-1)*a-b
        P[m+i,m+i]=1-b
    return P


def slem(P):
    n=P.shape[0]
    return np.max(np.abs(np.linalg.eigvalsh(P-np.ones((n,n))/n)))


def roots_eigen_formula(m,a,b):
    v=m*a/2
    r=math.hypot(v,b)
    return np.array([1,1-2*b]+[1-b-v+r]*(m-1)+[1-b-v-r]*(m-1))


def unrestricted_random_checks(m,seed,amount=250):
    rng=np.random.default_rng(seed)
    edges=[(i,j) for i in range(m) for j in range(i+1,m)] + [(i,m+i) for i in range(m)]
    _,_,mu=closed(m)
    for k in range(amount):
        P=np.eye(2*m)
        coeff=rng.uniform(0,1,size=len(edges))
        degree=np.zeros(2*m)
        for (i,j),u in zip(edges,coeff):
            degree[i]+=u;degree[j]+=u
        coeff*=rng.uniform(.1,.999)/max(degree)
        for (i,j),u in zip(edges,coeff):
            P[i,j]=P[j,i]=u
            P[i,i]-=u;P[j,j]-=u
        assert np.min(P)>-1e-12
        assert np.max(np.abs(P.sum(axis=1)-1))<1e-12
        assert slem(P)>=mu-1e-11
    return amount


def main():
    spectral=0
    asymmetric=0
    samples=0
    for m in range(2,17):
        a,b,mu=closed(m)
        assert 0<a<1 and 0<b<=.5+1e-14
        assert abs((m-1)*a+b-1)<1e-14
        P=transition(m,a,b)
        assert np.min(P)>-1e-14 and np.max(np.abs(P.sum(axis=1)-1))<1e-14
        actual=np.linalg.eigvalsh(P)
        predicted=np.sort(roots_eigen_formula(m,a,b))
        assert np.max(np.abs(actual-predicted))<1e-12,(m,actual,predicted)
        assert abs(slem(P)-mu)<1e-12
        spectral+=2*m
        rng=np.random.default_rng(m+203)
        for _ in range(220):
            trial_b=rng.uniform(0,1)
            trial_a=rng.uniform(0,(1-trial_b)/(m-1))
            trial_P=transition(m,trial_a,trial_b)
            assert slem(trial_P)>=mu-1e-12
            samples+=1
        pm=transition(m,1/m,1/m)
        md=0.5-1/m+math.sqrt(.25+1/m**2)
        assert abs(slem(pm)-md)<1e-12
    for m in [3,4]:
        asymmetric+=unrestricted_random_checks(m, 101+m)
    a2,b2,mu2=closed(2)
    assert abs(mu2-math.sqrt(.5))<1e-14
    m=100000
    a,b,mu=closed(m)
    assert abs(mu-.8)<1e-5 and abs(b-.4)<1e-5
    md=.5-1/m+math.sqrt(.25+1/m**2)
    assert abs((1-mu)/(1-md)/m-.2)<1e-4
    print(f'VERIFY_OK: {spectral} closed-form eigenvalues; {samples} symmetric feasible competitors; '
          f'{asymmetric} unrestricted feasible random chains for m=3,4; stochasticity, P4 endpoint, '
          f'exact max-degree spectral formula, limit 4/5, spectral-gap ratio 1/5')


if __name__=='__main__':main()
