"""Exact rational checks for a scalar randomized delay Runge--Kutta stability result.

Run with Python 3: python3 verify.py. The universal result is proved in RESULT.md;
finite checks here are supplementary and cannot establish universal stability.
"""
from fractions import Fraction as F
from itertools import permutations

checks = 0

def check(test, label):
    global checks
    if not test:
        raise AssertionError(label)
    checks += 1

def mm(A, B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),F(0)) for j in range(len(B[0]))] for i in range(len(A))]

def trans(A):
    return [list(row) for row in zip(*A)]

def solve(M,b):
    n=len(b); C=[list(map(F,row))+[F(b[i])] for i,row in enumerate(M)]
    for col in range(n):
        idx=next(i for i in range(col,n) if C[i][col]!=0)
        C[col],C[idx]=C[idx],C[col]
        d=C[col][col]; C[col]=[x/d for x in C[col]]
        for i in range(n):
            if i!=col:
                m=C[i][col]; C[i]=[x-m*y for x,y in zip(C[i],C[col])]
    return [r[-1] for r in C]

pairs=[(0,0),(0,1),(0,2),(1,1),(1,2),(2,2)]

def symmat(v):
    X=[[F(0) for j in range(3)] for i in range(3)]
    for n,(i,j) in enumerate(pairs): X[i][j]=X[j][i]=F(v[n])
    return X

def vec(X): return [X[i][j] for i,j in pairs]

def B(z,u): return [[F(1),-z,z*z*u],[F(1),F(0),F(0)],[F(0),F(1),F(0)]]

def operator(z,u):
    T=[[F(0) for j in range(6)] for i in range(6)]
    for j in range(6):
        e=[F(i==j) for i in range(6)]
        C=mm(mm(B(z,u),symmat(e)),trans(B(z,u)))
        for i,q in enumerate(vec(C)): T[i][j]=q
    return T

def moment(z):
    T0=operator(z,F(0)); T1=operator(z,F(1)); Th=operator(z,F(1,2))
    # Quadratic in the random-stage parameter, hence E[f(U)] =
    # (f(0) + 4 f(1/2) + f(1))/6, exact Simpson quadrature.
    return [[(T0[i][j]+4*Th[i][j]+T1[i][j])/6 for j in range(6)] for i in range(6)]

def f(z): return 4-4*z+2*z*z-z**4

def q(z): return z**7-z**5-4*z**4-4*z**3+12*z*z-24*z+24

def H(z): return F(4)*(4+4*z-2*z*z-z**4)/(z*(2-z)*(z*z+2*z+4)*f(z))

# The moment operator, direct from the source stage construction.
for z in [F(1,10),F(1,3),F(1,2),F(1),F(7,6),F(6,5)]:
    M=moment(z)
    expected=[[1,-2*z,z*z,z*z,-z**3,z**4/F(3)],
              [1,-z,z*z/2,0,0,0],
              [0,1,0,-z,z*z/2,0],
              [1,0,0,0,0,0],
              [0,1,0,0,0,0],
              [0,0,0,1,0,0]]
    for i in range(6):
        for j in range(6): check(M[i][j]==expected[i][j], 'six-moment operator')
    A=operator(z,F(1,2))
    # Independent solution of X-A0 X A0^T = e1 e1^T (A0 a 3x3 matrix).
    G=[[F(i==j)-A[i][j] for j in range(6)] for i in range(6)]
    V=solve(G,[1,0,0,0,0,0])
    check(V[5]==H(z),'discrete Lyapunov transfer')
    # Algebraic relation between the gain crossing and degree-seven polynomial.
    rhs=F(4)*q(z)/(3*(2-z)*(z*z+2*z+4)*f(z))
    check(1-z**4*H(z)/12==rhs,'gain crossing factorization')

# Exact gap witness: A0 Schur by the cubic Jury inequalities, but gain > 1.
z=F(7,6)
check(z*z/F(2)<1,'Jury constant')
check(z-z*z/F(2)>0,'Jury first endpoint')
check(2+z+z*z/F(2)>0,'Jury other endpoint')
check(f(z)>0,'Jury determinant')
check(q(z)<0,'mean-square unstable exact witness')
check(q(F(1))>0 and q(F(6,5))<0,'root bracket')
check(f(F(6,5))>0 and f(F(5,4))<0,'midpoint root bracket')

# Source method, one-stage grid per delay: constant history gives this startup
# and then the three-term recurrence from (2.3)--(2.4).
c=F(2); z=F(7,6); Y={-1:c, 0:c, 1:c*(1-z)}
for j,u in enumerate([F(1,4),F(3,4),F(1,3),F(2,3)],start=1):
    # Direct stage reconstruction for pure lag feedback f(t,x,lag)=-a*lag.
    old_delay=Y[j-1]; prior_delay=Y[j-2]
    stage_delay=old_delay-u*z*prior_delay
    direct=Y[j]-z*stage_delay
    recurrent=Y[j]-z*Y[j-1]+z*z*u*Y[j-2]
    check(direct==recurrent,'source-stage recurrence')
    Y[j+1]=direct

print('PASS:', checks,'exact-rational identities and independently reconstructed matrices')
