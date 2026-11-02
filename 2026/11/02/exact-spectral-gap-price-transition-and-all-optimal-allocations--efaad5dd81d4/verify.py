"""Reproduce the exact block spectrum and independent optimization bounds.

Requires Python 3, sympy and numpy. This is supplementary verification;
the all-order proof is given separately.
"""
from fractions import Fraction as F
import random
import numpy as np
import sympy as sp


def laplacian(W):
    m = len(W)
    A = sp.Matrix(W)
    left = sp.diag(*[sum(W[i][j] for j in range(m)) for i in range(m)])
    right = sp.diag(*[sum(W[i][j] for i in range(m)) for j in range(m)])
    return left.row_join(-A).col_join((-A.T).row_join(right))


def bound(m, P, Q, B):
    t = F(2*(m-1),m-2)*Q
    if P <= t:
        return B/(P+(m-1)*Q)
    return F(m-2,m*(m-1))*B/Q


def opt(m, P, Q, B):
    t = F(2*(m-1),m-2)*Q
    if P<=t:
        a=b=B/(m*(P+(m-1)*Q))
    else:
        a=F(0)
        b=B/(m*(m-1)*Q)
    return [[a if i==j else b for j in range(m)] for i in range(m)]

checks=0
# Exact characteristic polynomial of the two-orbit Laplacian.
x=sp.symbols('x')
for m in range(3,7):
    for a,b in [(sp.Rational(2,3),sp.Rational(5,7)),(sp.Rational(0),sp.Rational(3,7)),(sp.Rational(5,7),sp.Rational(5,7))]:
        L=laplacian([[a if i==j else b for j in range(m)] for i in range(m)])
        assert sp.factor(L.charpoly(x).as_expr()) == sp.factor(x*(x-m*b)**(m-1)*(x-(2*a+(m-2)*b))**(m-1)*(x-2*(a+(m-1)*b)))
        checks+=1

# Exact linear upper-bound and optimality checks in both regimes and on the boundary.
for m in range(3,9):
    for P,Q,B in [(F(1),F(1),F(10)),(F(20),F(1),F(11)),(F(2*(m-1),m-2),F(1),F(13)),(F(1,7),F(5,9),F(7,5)),(F(81,7),F(3,11),F(13,3))]:
        W=opt(m,P,Q,B)
        A=sum(W[i][i] for i in range(m))
        N=sum(W[i][j] for i in range(m) for j in range(m) if i!=j)
        assert P*A+Q*N==B
        # Exact symbolic positive eigenvalues of all four block types.
        a,b=W[0][0],W[0][1]
        predicted=min(m*b,2*a+(m-2)*b,2*(a+(m-1)*b))
        assert predicted==bound(m,P,Q,B)
        assert F(2,m)*A + F(m-2,m*(m-1))*N>=predicted
        assert N/F(m-1)>=predicted
        checks+=5

# Exact boundary family: every a between zero and b works.
for m in range(3,9):
    Q=F(3,7);P=F(2*(m-1),m-2)*Q;B=F(100,3)
    for ratio in [F(0),F(1,7),F(1,2),F(1)]:
        b=B/(m*(P*ratio+(m-1)*Q)); a=ratio*b
        assert min(m*b,2*a+(m-2)*b)==bound(m,P,Q,B)
        checks+=1

# Free nonnegative edge selections (no class symmetry assumed), checked against
# the exact universal trace bound using independent numerical eigensolvers.
rng = random.Random(20261031)
for m in range(3,9):
    for j in range(360):
        P = 10**rng.uniform(-1.7,1.7)
        Q = 10**rng.uniform(-1.7,1.7)
        B = 10**rng.uniform(-1,1)
        z=np.array([[rng.random()**2 for _ in range(m)] for _ in range(m)])
        z=z*B/(P*np.trace(z)+Q*(np.sum(z)-np.trace(z)))
        degrees_left=z.sum(axis=1);degrees_right=z.sum(axis=0)
        L=np.block([[np.diag(degrees_left),-z],[-z.T,np.diag(degrees_right)]])
        vals=np.linalg.eigvalsh(L)
        A=np.trace(z);N=np.sum(z)-A
        U=N/(m-1)
        V=2*A/m+(m-2)*N/(m*(m-1))
        target=float(bound(m,F(str(P)),F(str(Q)),F(str(B))))
        assert -1e-7<vals[1] <= min(U,V)+2e-8
        assert vals[1] <= target+3e-8
        checks+=2
print(f"PASS: {checks} exact symbolic/rational and independent numerical checks")
