"""Reproduce the star-Gram optimal pair-sampling identities; requires numpy and scipy."""
import math
import numpy as np
from scipy.optimize import minimize_scalar


def analytic(n, u):
    d = 1-u*u
    eta = 1-n*u*u
    t = (n-1)*(1-2*u*u)/(n*d)
    k = eta/(n*d)
    s = 2/n+t
    discriminant = (2*u*(n-1)/(n*math.sqrt(d)))**2
    lam = 2*k/(s+math.sqrt(discriminant)) if False else (s-math.sqrt(discriminant))/(2*(1+t*t/(4*k)))
    theta = 1-t*lam/(2*k)
    return theta, lam


def matrices(n,u,theta):
    d=1-u*u
    G=np.eye(n+1)
    G[0,1:]=u;G[1:,0]=u
    B=np.zeros_like(G)
    for i in range(1,n+1):
        J=[0,i]
        sub=np.linalg.inv(G[np.ix_(J,J)])
        B[np.ix_(J,J)]+=(theta/n)*sub
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            J=[i,j]
            sub=np.linalg.inv(G[np.ix_(J,J)])
            B[np.ix_(J,J)]+=(1-theta)/(n*(n-1)/2)*sub
    return G,B

rng=np.random.default_rng(2026)
checks=0
for n in range(3,12):
    for q in range(12):
        u=float(rng.uniform(.0001,.99/math.sqrt(n)))
        th,lam=analytic(n,u)
        assert 0<th<1
        for theta in (0.,1.,float(rng.uniform()),th):
            G,B=matrices(n,u,theta)
            eig=np.linalg.eigvalsh(np.linalg.cholesky(G).T@B@np.linalg.cholesky(G))
            d=1-u*u;k=(1-n*u*u)/(n*d)
            t=(n-1)*(1-2*u*u)/(n*d)
            T=2/n+t*theta
            P=k*theta*(2-theta)
            lo=(T-math.sqrt(max(0,T*T-4*P)))/2
            L=theta/(n*d)+2*(1-theta)/n
            assert abs(eig[0]-min(lo,L))<2e-11,(n,u,theta,eig[0],lo,L)
            assert abs(eig[-1]-max((T+math.sqrt(max(0,T*T-4*P)))/2,L))<2e-11
            checks+=1
        result=minimize_scalar(lambda A:-np.linalg.eigvalsh(np.linalg.cholesky(matrices(n,u,A)[0]).T @matrices(n,u,A)[1]@np.linalg.cholesky(matrices(n,u,A)[0]))[0],bounds=(0,1),method='bounded',options={'xatol':1e-11})
        assert abs(result.x-th)<2e-5,(n,u,result.x,th)
        assert abs(-result.fun-lam)<2e-8
        checks+=1
print('passed',checks,'analytic eigenvalue and optimality checks')
for n in (3,4,10,100):
    th,lam=analytic(n,.999/math.sqrt(n))
    print('n',n,'nearcritical optimal hub mass',round(th,9),'critical-limit',round(2/(1+math.sqrt(n-1)),9),'min eigen',round(lam,9))
