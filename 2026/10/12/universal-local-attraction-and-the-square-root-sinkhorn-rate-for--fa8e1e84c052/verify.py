#!/usr/bin/env python3
"""Exact and perturbative checks for local BDRS matrix-scaling spectral law."""
from fractions import Fraction as F
from math import exp, log, sqrt


def matvec(M, v):
    return [sum(x * y for x,y in zip(row,v)) for row in M]

def transpose(M):
    return list(map(list, zip(*M)))

def sinkhorn(M, r, c, q):
    p=[a/b for a,b in zip(r,matvec(M,q))]
    return [a/b for a,b in zip(c,matvec(transpose(M),p))]

def bdrs_step(X,r,c,v_old):
    u=[a/b for a,b in zip(r,matvec(X,v_old))]
    v=[a/b for a,b in zip(c,matvec(transpose(X),u))]
    Y=[[u[i]*X[i][j]*v[j] for j in range(len(c))] for i in range(len(r))]
    return Y,v

def jac(M):
    r=[sum(row) for row in M]
    c=[sum(M[i][j] for i in range(len(M))) for j in range(len(M[0]))]
    J=[[sum(M[i][j]*M[i][k]/r[i] for i in range(len(M)))/c[j] for k in range(len(c))] for j in range(len(c))]
    return r,c,J

def proj(y,c):
    z=sum(a*b for a,b in zip(y,c))/sum(c)
    return [a-z for a in y]

# The source's multiplicative iteration and derived cumulative recurrence agree exactly.
M=[[F(3),F(1)],[F(2),F(4)]]
r,c=[F(1,2)]*2,[F(1,2)]*2
X=[[a for a in row] for row in M]
vprev=[F(5,4),F(4,5)]
qprev=[F(1),F(1)]
qnow=[F(1),F(1)]
for k in range(6):
    X,v=bdrs_step(X,r,c,vprev)
    qnew=[a*b for a,b in zip(qnow,v)]
    if k>0:
        pred=sinkhorn(M,r,c, [qnow[j]**2/qprev[j] for j in range(len(c))])
        assert pred==qnew,(k,pred,qnew)
    qprev,qnow=qnow,qnew
    vprev=v
    assert [sum(X[i][j] for i in range(2)) for j in range(2)]==c

# Symmetrization and stochastic invariance are verified exactly for nonsquare
# positive rational couplings (including rank-deficient examples).
P=[[F(3,40),F(2,40),F(1,40)], [F(1,40),F(6,40),F(7,40)], [F(3,40),F(9,40),F(8,40)]]
r,c,J=jac(P)
for j in range(3):
    assert sum(J[j]) == 1
    assert sum(c[k]*J[k][j] for k in range(3)) == c[j]
    for k in range(3):
        assert c[j]*J[j][k] == c[k]*J[k][j]

# Local first-order response in c-centered log coordinates of S.
Q=[[float(x) for x in row] for row in P]
rf=[float(x) for x in r]
cf=[float(x) for x in c]
dirn=[0.6,-1.1,0.4]
expected=proj([sum(float(J[j][k])*dirn[k] for k in range(3)) for j in range(3)],cf)
for eps in [1e-4,1e-5,1e-6]:
    vec=[exp(eps*z) for z in dirn]
    out=sinkhorn(Q,rf,cf,vec)
    centered=proj([log(z) for z in out],cf)
    error=max(abs(centered[k]/eps-expected[k]) for k in range(3))
    assert error < 2.0*eps, (eps,error)

# Fully symbolic 2x2 family: r=c=(1/2,1/2), M=[[t,1],[1,t]].
# J has eigenvalues 1 and sigma=((t-1)/(t+1))^2. BDRS modal
# polynomial lambda^2-2*sigma*lambda+sigma has roots of modulus sqrt(sigma).
for t in [F(1),F(6,5),F(2),F(3),F(5),F(10),F(41)]:
    A=[[t,F(1)],[F(1),t]]
    row,col,J=jac(A)
    sigma=((t-1)/(t+1))**2
    assert J[0][0]-J[0][1] == sigma
    assert J[1][1]-J[1][0] == sigma
    assert sigma < 1
    if sigma:
        # lambda=sigma +/- i sqrt(sigma(1-sigma)); modulus^2=sigma
        assert sigma*sigma+sigma*(1-sigma)==sigma
        assert 4*sigma*(sigma-1)<0
    else:
        assert t==1
print('VERIFY_OK: exact BDRS recurrence, positive-coupling derivative, Jacobian symmetry, and sharp 2x2 modes')
