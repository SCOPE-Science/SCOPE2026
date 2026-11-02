"""Independent numerical and exact-rational checks of the priced book-network theorem.

Usage: python verify_book_resistance.py
Dependencies: Python 3, numpy, scipy.
The theorem's proof is analytic; sampled tests are consistency checks only.
"""
from fractions import Fraction as F
from math import sqrt
import numpy as np
from scipy.optimize import minimize


def optimum(m, S, R, B):
    K = m*m*(m+1)/(2*(m+2))
    k = 4*S/R - 1
    if k <= K:
        y = 0.
    else:
        y = (sqrt(k)-sqrt(K))/(k*sqrt(K)+sqrt(k))
    t = B*(1-y)/(2*m*S)
    z = B*y/R
    return t,z


def weighted_laplacian(m, w):
    n=m+2
    L=np.zeros((n,n),dtype=float)
    edges=[(0,1)]+[(0,j) for j in range(2,n)]+[(1,j) for j in range(2,n)]
    for (u,v),val in zip(edges,w):
        L[u,u]+=val;L[v,v]+=val
        L[u,v]-=val;L[v,u]-=val
    return L


def trace_inv_perp(L):
    e=np.linalg.eigvalsh(L)[1:]
    if min(e)<1e-10:return 1e20
    return float(sum(1/e))


def inverse_frac(a):
    n=len(a)
    M=[[a[i][j] for j in range(n)]+[F(int(i==j)) for j in range(n)] for i in range(n)]
    for k in range(n):
        ii=next(i for i in range(k,n) if M[i][k])
        M[k],M[ii]=M[ii],M[k]
        pivot=M[k][k]
        M[k]=[x/pivot for x in M[k]]
        for i in range(n):
            if i==k:continue
            c=M[i][k]
            if c:M[i]=[x-c*y for x,y in zip(M[i],M[k])]
    return [row[n:] for row in M]


def rational_laplacian(m,t,z):
    n=m+2
    L=[[F(0) for _ in range(n)] for _ in range(n)]
    for u,v,val in [(0,1,z)]+[(i,j,t) for i in [0,1] for j in range(2,n)]:
        L[u][u]+=val;L[v][v]+=val
        L[u][v]-=val;L[v][u]-=val
    return L


def run():
    rational_cases=0
    for m in range(2,7):
        for t,z in [(F(1,2),F(0)),(F(3,4),F(2,3)),(F(7,11),F(3,5))]:
            L=rational_laplacian(m,t,z)
            n=m+2
            A=[[L[i][j]+F(1,n) for j in range(n)] for i in range(n)]
            inv=inverse_frac(A)
            tr=sum(inv[i][i] for i in range(n))-1
            theory=F(m*(m+1),2*(m+2))/t+1/(m*t+2*z)
            assert tr==theory,(m,t,z,tr,theory)
            rational_cases+=1
    rng=np.random.default_rng(43174)
    budget_checks=0;domination_checks=0;solver_checks=0;threshold_checks=0
    for m in range(2,9):
        K=m*m*(m+1)/(2*(m+2))
        Rc=4/(1+K)
        for ratio in [Rc*.4,Rc*.9,Rc,Rc*1.1,Rc*2., 1.,10.]:
            S=float(rng.uniform(.4,2.3));R=ratio*S;B=float(rng.uniform(.5,3))
            t,z=optimum(m,S,R,B)
            assert t>0 and z>=-1e-12
            assert abs(2*m*S*t+R*z-B)<1e-10
            assert (z>1e-10)==(ratio<Rc*(1-1e-10)),(m,ratio,Rc,z)
            w=np.array([z]+[t]*(2*m),dtype=float)
            Fstar=trace_inv_perp(weighted_laplacian(m,w))
            Acoef=m*(m+1)/(2*(m+2))
            assert abs(Fstar-(Acoef/t+1/(m*t+2*z)))<1e-8
            threshold_checks+=1
            for _ in range(20):
                r=rng.exponential(size=2*m+1)
                r*=B/(R*r[0]+S*sum(r[1:]))
                Fr=trace_inv_perp(weighted_laplacian(m,r))
                assert Fr+1e-8>=Fstar,(m,ratio,Fr,Fstar)
                domination_checks+=1
            budget_checks+=1
            if m <= 6 and ratio in [Rc*.4,Rc*1.1, 1.]:
                prices=np.array([R]+[S]*(2*m))
                r=np.array([z]+[t]*(2*m))
                # A strictly positive initialization tests the unrestricted edge problem.
                x0=B/prices/(2*m+1)
                sol=minimize(lambda v:trace_inv_perp(weighted_laplacian(m,v)),x0,
                    method='SLSQP',bounds=[(0,None)]*(2*m+1),
                    constraints=[{'type':'eq','fun':lambda v,p=prices:float(np.dot(v,p)-B),
                    'jac':lambda v,p=prices:p}],
                    options={'ftol':1e-11,'maxiter':800})
                if not sol.success:
                    # Numerical stationarity is not used in the analytical theorem.
                    assert sol.fun + 1e-7 >= Fstar
                else:
                    assert abs(sol.fun-Fstar)<1e-6,(m,ratio,sol.fun,Fstar)
                solver_checks+=1
    # Equal-price page count support transition.
    assert optimum(2,1,1,1)[1]>0
    for m in range(3,45):assert optimum(m,1,1,1)[1]==0
    print('PASS exact rational trace identities:',rational_cases)
    print('PASS analytic budget/spectral checks:',budget_checks)
    print('PASS asymmetric feasible comparisons:',domination_checks)
    print('PASS unrestricted numerical attempts:',solver_checks)
    print('PASS support threshold checks:',threshold_checks)
    print('PASS equal-price page-count transition: m=2 keeps shortcut; m>=3 deletes')

if __name__=='__main__':run()
