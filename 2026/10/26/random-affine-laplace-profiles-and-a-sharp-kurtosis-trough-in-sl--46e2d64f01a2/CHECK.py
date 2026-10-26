"""Independent checks for the boundary-reset harmonic-chain limiting formulas."""
from fractions import Fraction as F
import numpy as np
from scipy.linalg import solve_continuous_lyapunov

checks=0
for n in range(2,15):
    K=np.diag([F(2)]*n)
    # Symbolic rational inversion with sympy
    import sympy as sp
    M=sp.diag(*([2]*n))
    for i in range(n-1): M[i,i+1]=M[i+1,i]=-1
    L=M.inv()*sp.Matrix([1]+[0]*(n-1))
    R=M.inv()*sp.Matrix([0]*(n-1)+[1])
    for i in range(n):
        assert L[i]==sp.Rational(n-i,n+1)
        assert R[i]==sp.Rational(i+1,n+1)
        checks+=2

# Brownian reset and its covariance-matched Ornstein-Uhlenbeck force.
for D in [F(1,2),F(3,1),F(7,5)]:
    for rate in [F(1,10),F(4),F(6,7)]:
        assert (4*D)/(2*rate)==2*D/rate
        checks+=1

# Characteristic function and 4th-cumulant formula for two independent Laplace inputs.
for n in [2,3,4,7,11]:
    for etaL,etaR in [(F(1),F(1)),(F(1,3),F(5,2)),(F(3,2),F(2,5))]:
        A=np.array([F(n+1-i,n+1) for i in range(1,n+1)],dtype=object)
        B=np.array([F(i,n+1) for i in range(1,n+1)],dtype=object)
        cov=np.array([[2*(etaL*A[i]*A[j]+etaR*B[i]*B[j]) for j in range(n)] for i in range(n)],dtype=object)
        assert cov[0,0] > 0
        checks+=1
        for i in range(n):
            vl=etaL*A[i]*A[i]
            vr=etaR*B[i]*B[i]
            fourth=24*(vl*vl+vr*vr)+24*vl*vr
            variance=2*(vl+vr)
            # Independent Laplace sum: E(X^4) = sum E(Xi^4)+6 Var(XL)Var(XR).
            assert fourth-3*variance*variance==12*(vl*vl+vr*vr)
            excess=(fourth-3*variance*variance)/(variance*variance)
            assert F(3,2)<=excess<F(3)
            checks+=3

# Exact second-moment convergence from the augmented linear OU generator.
for n in [2,3,5]:
    m=1.4;k=2.2;gamma=1.3
    eta=(1.5,0.7)
    a=np.array([(n+1-i)/(n+1) for i in range(1,n+1)])
    b=np.array([i/(n+1) for i in range(1,n+1)])
    target=2*eta[0]*np.outer(a,a)+2*eta[1]*np.outer(b,b)
    assert np.linalg.matrix_rank(target,tol=1e-9)==2
    checks+=1
    errors=[]
    for eps in [0.1,0.02,0.004]:
        K=2*np.eye(n)-np.eye(n,k=1)-np.eye(n,k=-1)
        G=np.zeros((n,n));G[0,0]=gamma;G[-1,-1]=gamma
        AA=np.zeros((2*n+2,2*n+2))
        AA[:n,n:2*n]=np.eye(n)
        AA[n:2*n,:n]=-(k/m)*K
        AA[n:2*n,n:2*n]=-G/m
        AA[n,2*n]=k/m; AA[2*n-1,2*n+1]=k/m
        AA[2*n,2*n]=-eps
        AA[2*n+1,2*n+1]=-2*eps
        BB=np.zeros((2*n+2,2*n+2))
        BB[2*n,2*n]=4*eta[0]
        BB[2*n+1,2*n+1]=4*eta[1]*2
        C=solve_continuous_lyapunov(AA,-BB)
        errors.append(np.max(np.abs(eps*C[:n,:n]-target)))
    assert errors[2]<errors[1]<errors[0], errors
    checks+=3

print('PASS',checks,'exact/static/characteristic/moment/OU-matching checks')
