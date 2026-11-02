#!/usr/bin/env python3
"""Independent rational and numerical checks for the two-mass complete-bipartite FMMC law.

Dependencies: sympy, numpy, scipy. All tests use a fixed random seed.
"""
from fractions import Fraction as Fr
from itertools import product
import random
import sympy as sp
import numpy as np
from scipy.optimize import minimize

R = random.Random(20261029)
checks = 0

def optimum(alpha):
    a = min(alpha, 1-alpha)
    b = 1-a
    if a <= Fr(1,3):
        S = a
        mu = (b-a)/b
    else:
        S = 2*a*b/(1+a)
        mu = b/(1+a)
    return S,mu

def kernel(p,q,alpha,S):
    beta = 1-alpha
    f = S/Fr(p*q)
    pi = [alpha/p]*p + [beta/q]*q
    P = [[Fr(0) for _ in range(p+q)] for __ in range(p+q)]
    for i in range(p):
        for j in range(q):
            P[i][p+j] = f/pi[i]
            P[p+j][i] = f/pi[p+j]
    for i in range(p+q):
        P[i][i] = 1-sum(P[i])
    return pi,P

def mu_numeric(P,pi):
    A=np.asarray(P,dtype=float)
    sqrtpi=np.sqrt(np.asarray(pi,dtype=float))
    K=(sqrtpi[:,None]*A)/sqrtpi[None,:]
    vals=np.linalg.eigvalsh((K+K.T)/2)
    return max(abs(v) for v in vals[:-1])

# An exact characteristic-polynomial identity for rational stationary masses.
for p,q,alpha in product(range(2,6), range(2,6),
                         [Fr(1,10),Fr(1,5),Fr(1,3),Fr(2,5),Fr(1,2),Fr(3,5),Fr(9,10)]):
    beta=1-alpha
    S,mu=optimum(alpha)
    pi,P=kernel(p,q,alpha,S)
    assert all(sum(row)==1 for row in P)
    assert all(x>=0 for row in P for x in row)
    for i in range(p+q):
        for j in range(p+q):
            assert pi[i]*P[i][j]==pi[j]*P[j][i]
    X=sp.Symbol('X')
    expected=sp.expand((X-1)*(X-(1-S/alpha))**(p-1)
                      *(X-(1-S/beta))**(q-1)*(X-(1-S/(alpha*beta))))
    measured=sp.Matrix(P).charpoly(X).as_expr()
    assert sp.expand(expected-measured)==0,(p,q,alpha)
    assert abs(mu_numeric(P,pi)-float(mu))<1e-10
    checks+=1

# Independently vary all cross-edge stationary flows, including asymmetric matrices.
for p,q,alpha in product(range(2,5),range(2,5),[Fr(1,8),Fr(1,3),Fr(2,5),Fr(1,2),Fr(4,5)]):
    beta=1-alpha
    Sstar,mustar=optimum(alpha)
    pi=[alpha/p]*p+[beta/q]*q
    for _ in range(40):
        F=[[Fr(R.randint(1,100),1000) for j in range(q)] for i in range(p)]
        row=[sum(row) for row in F]
        col=[sum(F[i][j] for i in range(p)) for j in range(q)]
        cap=min([pi[i]/row[i] for i in range(p)]+[pi[p+j]/col[j] for j in range(q)])
        F=[[x*cap*Fr(R.randint(10,100),100) for x in row_] for row_ in F]
        row=[sum(row_) for row_ in F]
        col=[sum(F[i][j] for i in range(p)) for j in range(q)]
        S=sum(row)
        P=[[Fr(0) for i in range(p+q)] for j in range(p+q)]
        for i in range(p):
            for j in range(q):
                P[i][p+j]=F[i][j]/pi[i]
                P[p+j][i]=F[i][j]/pi[p+j]
        for i in range(p+q):
            P[i][i]=1-sum(P[i])
        assert all(x>=0 for row_ in P for x in row_)
        lower=max(1-S/max(alpha,beta),abs(1-S/(alpha*beta)))
        actual=mu_numeric(P,pi)
        assert actual+1e-9>=float(lower),(p,q,alpha,lower,actual)
        assert actual+1e-9>=float(mustar),(p,q,alpha,actual,mustar)
        checks+=1

# Preserve total flow and each row/column total, but break edge symmetry.
# Every such genuinely nonuniform feasible 2-by-2 perturbation is strictly worse.
for p,q,alpha in product(range(2,5),range(2,5),
                         [Fr(1,10),Fr(1,3),Fr(2,5),Fr(1,2),Fr(3,5)]):
    S,mu=optimum(alpha)
    pi=[alpha/p]*p+[(1-alpha)/q]*q
    F=[[S/Fr(p*q) for j in range(q)] for i in range(p)]
    e=S/Fr(2*p*q)
    F[0][0]+=e; F[1][1]+=e; F[0][1]-=e; F[1][0]-=e
    P=[[Fr(0) for _ in range(p+q)] for __ in range(p+q)]
    for i in range(p):
        for j in range(q):
            P[i][p+j]=F[i][j]/pi[i]
            P[p+j][i]=F[i][j]/pi[p+j]
    for i in range(p+q): P[i][i]=1-sum(P[i])
    assert all(z>=0 for row in P for z in row)
    assert mu_numeric(P,pi)>float(mu)+1e-8,(p,q,alpha)
    checks+=1

# The natural Metropolis proposal (uniform neighbor proposal) is optimal iff
# the minority-side stationary mass does not exceed one third.
for alpha in [Fr(1,20),Fr(1,4),Fr(1,3),Fr(7,20),Fr(2,5),Fr(1,2),Fr(3,5),Fr(9,10)]:
    Sopt,muopt=optimum(alpha)
    Smh=min(alpha,1-alpha)
    pi,P=kernel(3,4,alpha,Smh)
    mumh=mu_numeric(P,pi)
    if min(alpha,1-alpha)<=Fr(1,3):
        assert abs(mumh-float(muopt))<1e-10
    else:
        assert mumh>float(muopt)+1e-4
    checks+=1

# Independent constrained optimization of edge flows, without enforcing symmetry.
# SLSQP finds a feasible local solution; the analytic lower bound above certifies
# the global optimum, not SLSQP's numerical convergence.
for p,q,alpha_float in [(2,3,.12),(2,3,.33),(2,3,.4),(3,3,.5),(3,4,.8),(2,4,.25)]:
    alpha=Fr(str(alpha_float)); beta=1-alpha
    pi=np.array([float(alpha/p)]*p+[float(beta/q)]*q)
    Starget,mutarget=optimum(alpha)
    def make_P(z):
        F=np.reshape(z,(p,q))
        P=np.zeros((p+q,p+q))
        for i in range(p):
            for j in range(q):
                P[i,p+j]=F[i,j]/pi[i]
                P[p+j,i]=F[i,j]/pi[p+j]
        for i in range(p+q):P[i,i]=1-P[i].sum()
        return P
    def objective(z): return mu_numeric(make_P(z),pi)
    def ineq(z):
        F=np.reshape(z,(p,q))
        return np.r_[pi[:p]-F.sum(axis=1),pi[p:]-F.sum(axis=0)]
    best=10
    for trial in range(3):
        if trial==0: z0=np.full(p*q,float(Starget)/(p*q))
        else: z0=np.full(p*q,float(Starget)/(p*q))*(1+.03*np.array([R.random()-.5 for _ in range(p*q)]))
        res=minimize(objective,z0,bounds=[(0,None)]*(p*q),
                     constraints=[{'type':'ineq','fun':ineq}],method='SLSQP',
                     options={'maxiter':350,'ftol':1e-11})
        if min(ineq(res.x))>=-1e-8: best=min(best,res.fun)
    assert abs(best-float(mutarget))<1e-4,(p,q,alpha,best,mutarget)
    checks+=1
print('PASS',checks,'independent exact / asymmetric-flow / Metropolis / numerical-optimization cases')
