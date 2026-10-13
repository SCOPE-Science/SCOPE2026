"""Reproducible checks for the one-pivot RPCholesky convex-order envelope.

Python 3 with numpy and scipy; the claimed all-dimension result is proved
analytically in RESULT.md, not by the finite checks here.
"""
from fractions import Fraction as F
import math
import numpy as np
from scipy.linalg import null_space


def matmul(A, B):
    return [[sum(a * b for a, b in zip(row, col)) for col in zip(*B)] for row in A]


def transpose(A):
    return [list(row) for row in zip(*A)]


def trace(A):
    return sum(A[i][i] for i in range(len(A)))


def exact_check(evals, v):
    n = len(evals)
    ss = sum(x*x for x in v)
    Q = [[(F(int(i==j)) - 2*v[i]*v[j]/ss) for j in range(n)] for i in range(n)]
    K = matmul(matmul(Q, [[evals[i] if i==j else F(0) for j in range(n)] for i in range(n)]), transpose(Q))
    K2 = matmul(K, K)
    S = sum(evals)
    M2 = sum(l*l for l in evals)
    M3 = sum(l*l*l for l in evals)
    mu = S-M2/S
    a = [K[j][j]/S for j in range(n)]
    t = [S-K2[j][j]/K[j][j] for j in range(n)]
    assert sum(a) == 1
    assert sum(p*x for p,x in zip(a,t)) == mu
    for j in range(n):
        q = [evals[i]*Q[j][i]*Q[j][i]/S for i in range(n)]
        assert sum(q) == a[j]
        assert sum(q[i]*(S-evals[i]) for i in range(n)) == a[j]*t[j]
    vmax = M3/S-(M2/S)**2
    vnow = sum(p*(x-mu)**2 for p,x in zip(a,t))
    assert 0 <= vnow <= vmax
    for exponent in [2,3,4,5]:
        low = mu**exponent
        value = sum(p*x**exponent for p,x in zip(a,t))
        high = sum(evals[i]/S*(S-evals[i])**exponent for i in range(n))
        assert low <= value <= high
    return 1


def hollowize(H):
    """Orthogonal basis with zero diagonal quadratic form for traceless symmetric H."""
    n = H.shape[0]
    H = (H+H.T)/2
    if n == 1 or np.linalg.norm(H, ord='fro') < 1e-12:
        return np.eye(n)
    w,U = np.linalg.eigh(H)
    assert w[0] < -1e-12 and w[-1] > 1e-12, (w, np.trace(H))
    t = math.sqrt(-w[0]/(w[-1]-w[0]))
    z = math.sqrt(w[-1]/(w[-1]-w[0]))
    v = t*U[:,-1]+z*U[:,0]
    N = null_space(v.reshape(1, -1))
    C = N.T @ H @ N
    W = hollowize(C)
    return np.column_stack((v,N@W))


def distribution(K):
    S = float(np.trace(K))
    K2 = K@K
    p = np.diag(K)/S
    t = S-np.diag(K2)/np.diag(K)
    return p,t


def approx(a, b, atol=2e-9):
    assert abs(a-b) <= atol*max(1,abs(a),abs(b)), (a,b)


def numerical_check():
    rng=np.random.default_rng(20261009)
    ntests=0
    for n in range(2,9):
        for _ in range(70):
            eigs=np.exp(rng.uniform(-3,3,size=n))
            S=float(eigs.sum()); M2=float((eigs**2).sum()); M3=float((eigs**3).sum())
            Vmax=M3/S-(M2/S)**2
            mu=S-M2/S
            X=rng.normal(size=(n,n)); U,_=np.linalg.qr(X)
            K=(U*eigs)@U.T
            p,t=distribution(K)
            approx(float(p@t),mu)
            var=float(p@((t-mu)**2))
            assert -1e-9<=var<=Vmax+1e-8*max(1,Vmax)
            eprob=eigs/S; et=S-eigs
            for f in (lambda x:x*x, lambda x:x**3, lambda x:x**4,
                      lambda x:np.exp(x/S),
                      lambda x:np.abs(x-S/2),
                      lambda x:np.maximum(x-S/3,0)**3):
                middle=float(p@f(t)); high=float(eprob@f(et)); low=float(f(mu))
                assert low-1e-9*max(1,high)<=middle<=high+1e-9*max(1,high), (n,low,middle,high)
            H=np.diag(eigs*eigs-(M2/S)*eigs)
            W=hollowize(H)
            approx(float(np.linalg.norm(W.T@W-np.eye(n))),0,1e-9)
            K0=(W.T*eigs)@W
            p0,t0=distribution(K0)
            approx(float(p0@t0),mu)
            approx(float(np.max(np.abs(t0-mu))),0,2e-8)
            for f in (lambda x:x*x,lambda x:np.exp(x/S)):
                approx(float(p0@f(t0)),float(f(mu)),1e-8)
            ntests+=1
    return ntests


def main():
    cases=0
    for n in (2,3,4,5):
        for q in range(1,8):
            eigs=[F(k+q+1) for k in range(n)]
            vs=[F((k+1)*q+1) for k in range(n)]
            cases+=exact_check(eigs,vs)
    # Full exact two-eigenvalue equality example: same spectrum, zero and maximal variance.
    L=F(9);m=F(1);S=L+m; mu=S-(L*L+m*m)/S
    assert mu==F(9,5)
    K=[[F(5),F(4)],[F(4),F(5)]]
    K2=matmul(K,K)
    assert all(S-K2[i][i]/K[i][i]==mu for i in range(2))
    vmax=(L**3+m**3)/S-((L*L+m*m)/S)**2
    assert vmax==F(144,25)
    approx(float(sum([L/S*(m-mu)**2,m/S*(L-mu)**2])),float(vmax))
    ntests=numerical_check()
    print(f'VERIFY_OK exact_householder={cases} numerical_spd={ntests} plus exact two-mode extremizers')

if __name__=='__main__':
    main()
