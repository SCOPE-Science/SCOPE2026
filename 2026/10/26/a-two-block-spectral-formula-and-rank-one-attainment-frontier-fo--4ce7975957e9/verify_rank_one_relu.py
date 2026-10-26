"""Reproduce sign-partition spectral certificates for rectified rank-one approximation."""
import itertools
import numpy as np


def one_block(A):
    """Nonnegative leading rank-one SVD block, with empty cases handled."""
    if A.size == 0 or min(A.shape) == 0 or not np.any(A):
        return np.zeros_like(A), 0.0, np.zeros(A.shape[0]), np.zeros(A.shape[1])
    left, sv, right = np.linalg.svd(A, full_matrices=False)
    p = np.abs(left[:, 0]); q = np.abs(right[0, :])
    # Perron SVD: absolute vectors attain the spectral norm for A>=0.
    score = float(p @ A @ q)
    assert np.isclose(score, sv[0], rtol=1e-10, atol=1e-10)
    up = np.sqrt(score) * p
    vp = np.sqrt(score) * q
    return np.outer(up, vp), score * score, up, vp


def certificate(X):
    m, n = X.shape
    best = None
    for rows in itertools.product((False, True), repeat=m):
        for cols in itertools.product((False, True), repeat=n):
            I = np.flatnonzero(rows); Ic = np.flatnonzero(np.logical_not(rows))
            J = np.flatnonzero(cols); Jc = np.flatnonzero(np.logical_not(cols))
            P, a, u1, v1 = one_block(X[np.ix_(I, J)])
            Q, b, u2, v2 = one_block(X[np.ix_(Ic, Jc)])
            if best is None or a+b > best[0]:
                U=np.zeros(m); V=np.zeros(n)
                U[I]=u1; U[Ic]=-u2
                V[J]=v1; V[Jc]=-v2
                Y=np.maximum(0.0, np.outer(U, V))
                intended=np.zeros((m, n))
                intended[np.ix_(I, J)]=P
                intended[np.ix_(Ic, Jc)]=Q
                assert np.allclose(Y, intended, rtol=1e-10, atol=1e-10)
                best=(a+b, U,V,Y)
    gain,U,V,Y=best
    residual=float(np.linalg.norm(X-Y, 'fro')**2)
    exact=float(np.linalg.norm(X,'fro')**2-gain)
    assert np.isclose(residual, exact, atol=1e-8, rtol=1e-9), (residual, exact)
    return residual, U,V,Y


def run():
    count=0
    # Complete census of 0/1 matrices through 2x3 and a representative 3x3 family.
    for m,n in ((1,1),(1,4),(2,2),(2,3)):
        for bits in itertools.product((0.0,1.0), repeat=m*n):
            X=np.array(bits).reshape(m,n)
            loss,U,V,Y=certificate(X)
            assert np.allclose(Y,np.maximum(0,np.outer(U,V)))
            assert loss >= -1e-8
            count+=1
    for n in range(1,9):
        loss,*_=certificate(np.eye(n))
        assert np.isclose(loss,max(n-2,0),atol=1e-9)
        count+=1
    rng=np.random.default_rng(20261020)
    for m,n in ((2,5),(3,3),(3,4),(4,4)):
        for _ in range(9):
            X=rng.uniform(0,2,size=(m,n))*(rng.random((m,n))>.35)
            loss,*_=certificate(X)
            assert loss>=-1e-8
            count+=1
    for e in (.15,.3,.5,.7):
        X=np.array([[1,0],[e,1.]])
        loss,*_=certificate(X)
        assert np.isclose(loss,e*e,atol=1e-8)
        count+=1
    print(f'PASS {count} certificate cases; enumeration, reconstruction, identity family and prior 2x2 example')

if __name__=='__main__':
    run()
