#!/usr/bin/env python3
"""Exact rational checks and finite-horizon diagnostics for phase-dependent survival exponents."""
from fractions import Fraction as F
from math import log, sqrt

D = F(1,4)
P = [
    [F(0),F(0),F(3,4),F(1,4)],
    [F(0),F(0),F(1,4),F(3,4)],
    [F(2,3),F(1,3),F(0),F(0)],
    [F(1,3),F(2,3),F(0),F(0)],
]
f = ((1,-1,1,-1),(2,-2,-1,1))

n_checks = 0
def ck(c, title):
    global n_checks
    assert c, title
    n_checks += 1

def mul(X,Y):
    return [[sum(X[i][k]*Y[k][j] for k in range(len(Y))) for j in range(len(Y[0]))] for i in range(len(X))]

def plus(X,Y):
    return [[X[i][j]+Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]

def scal(a,X):
    return [[a*xx for xx in row] for row in X]

def block(X,r):
    ids=(2*r,2*r+1)
    return [[X[i][j] for j in ids] for i in ids]

A=[[[D*F(f[h][i])*v for v in P[i]] for i in range(4)] for h in (0,1)]
for i in range(4):
    ck(sum(P[i])==1, "P stochastic")
    ck(all(sum(F(1,3)*P[i][j]*(1+D*F(f[h][i])) for j in range(4))<1 for h in (0,1)), "K_n substochastic")
    ck(all(1 + D*F(f[h][i])>0 for h in (0,1)), "K_n positive")

for h in (0,1):
    for r in (0,1):
        W=block(mul(P,P),r)
        C=block(plus(mul(A[h],P),mul(P,A[1-h])),r)
        E=block(mul(A[h],A[1-h]),r)
        pi=[F(1,2),F(1,2)]
        ck([sum(pi[i]*W[i][j] for i in range(2)) for j in range(2)]==pi,"stationary")
        cbar=sum(pi[i]*sum(C[i]) for i in range(2))
        ck(cbar==0,"first-order balanced")
        g=[sum(pi[i]*C[i][j] for i in range(2)) for j in range(2)]
        ck(g[0]+g[1]==0,"Poisson compatibility")
        # w=(z,-z), first coordinate of w(I-W) is z*(1-W00+W10)
        z=g[0]/(1-W[0][0]+W[1][0])
        w=[z,-z]
        ck(sum(w)==0,"zero-mass response")
        for j in range(2):
            ck(w[j]-sum(w[i]*W[i][j] for i in range(2))==g[j],"Poisson equation")
        direct=sum(pi[i]*sum(E[i]) for i in range(2))
        reaction=sum(w[i]*sum(C[i]) for i in range(2))
        beta=direct+reaction
        expect=F(-3,80) if (h,r) in [(0,0),(1,1)] else F(3,16)
        # Note: beta divided by d=2 yields -3/160 or 3/32.
        ck(beta==expect,"second-order scalar beta")
        ck(beta/2==(F(-3,160) if (h,r) in [(0,0),(1,1)] else F(3,32)),"time exponent")
        eps=F(1,101)
        lhs=mul(plus(P,scal(eps,A[h])),plus(P,scal(eps,A[1-h])))
        rhs=plus(plus(mul(P,P),scal(eps,plus(mul(A[h],P),mul(P,A[1-h])))),scal(eps*eps,mul(A[h],A[1-h])))
        ck(lhs==rhs,"formal block product")
        print('phase',h,'class',r,'balance',cbar,'w',w,'direct',direct,'response',reaction,'beta',beta,'exponent',beta/2)

# The infinite-time law is NOT proved by the following finite-horizon checks.
def slopes(start, initial, nmax=160000):
    v=[float(j==initial) for j in range(4)]
    delta=float(D)
    marks={2000,10000,80000,160000}
    obs={}
    logmass=0.0
    for n in range(start,nmax):
        vals=[v[i]*(1+delta*f[n%2][i]/sqrt(n)) for i in range(4)]
        w=[sum(vals[i]*float(P[i][j]) for i in range(4)) for j in range(4)]
        tot=sum(w)
        ck(tot>0,"positive conditional mass") if n in marks else None
        v=[z/tot for z in w]
        logmass+=log(tot)
        if n+1 in marks:obs[n+1]=logmass
    return (obs[160000]-obs[80000])/(log(160000)-log(80000)),obs

for init,expect in ((0,-3/160),(2,3/32)):
    estimate,obs=slopes(2,init)
    ck(abs(estimate-expect)<1e-4,"numerical log-slope agrees with analytic exponent")
    print('initial',init,'finite slope',f'{estimate:.11f}','predicted',f'{expect:.11f}','error',f'{estimate-expect:+.3g}')
print('PASSED',n_checks,'exact/diagnostic assertions')
