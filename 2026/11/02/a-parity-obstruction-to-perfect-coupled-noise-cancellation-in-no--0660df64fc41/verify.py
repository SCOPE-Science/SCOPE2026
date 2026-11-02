"""Reproducible finite-dimensional checks for coupled additive-noise two-call iteration.

This verifies algebraic identities numerically; the all-dimensional optimizer and
parity statement are established analytically in RESULT.md.
"""
import math
import numpy as np


def rotation(a):
    return np.array([[math.cos(a), -math.sin(a)], [math.sin(a), math.cos(a)]])


def blockdiag(*blocks):
    n=sum(b.shape[0] for b in blocks)
    out=np.zeros((n,n)); k=0
    for b in blocks:
        m=b.shape[0];out[k:k+m,k:k+m]=b;k+=m
    return out


def data(M, eta, n, sigma=1.2):
    d=M.shape[0]; eye=np.eye(d)
    T=eye-eta*M+eta*eta*(M@M)
    W=np.zeros_like(M); A=eye.copy()
    for _ in range(n):
        W+=A.T@A
        A=T@A
    U,s,Vt=np.linalg.svd(M)
    Q=U@Vt
    w,v=np.linalg.eigh(W)
    H=(M.T@M)
    Hroot=(Vt.T*s)@Vt
    # All equations in original coordinates, not necessarily ordered spectra.
    predicted=eta*eta*sigma*sigma*sum(wi*(eta*si-1)**2 for wi,si in zip(np.diag(v.T@W@v),np.diag(v.T@Hroot@v)))
    exact=eta*eta*sigma*sigma*np.trace((eta*M-Q).T@W@(eta*M-Q))
    indep=eta*eta*sigma*sigma*(np.trace((eta*M).T@W@(eta*M))+np.trace(W))
    same=eta*eta*sigma*sigma*np.trace((eta*M-eye).T@W@(eta*M-eye))
    return T, W, Q, predicted, exact, indep, same


def main():
    tests=0
    for mats in [
        [1.5*rotation(.2)],
        [1.5*rotation(.7)],
        [2.2*rotation(1.1)],
        [1.5*rotation(.4),2.2*rotation(.9)],
        [1.5*rotation(-.3),2.2*rotation(.8),3.1*rotation(.5)],
        [np.array([[1.4]])],
        [1.7*rotation(.5),np.array([[1.3]])],
        [np.diag([1.1,2.3,3.8])],
    ]:
        M=blockdiag(*mats)
        assert np.linalg.norm(M@M.T-M.T@M)<1e-12
        assert np.linalg.eigvalsh((M+M.T)/2).min()>0
        for eta in [.10,.23,.37,.51]:
            for n in [1,2,5,11]:
                T,W,Q,pred,exact,indep,same=data(M,eta,n)
                assert np.allclose(pred,exact,rtol=1e-10,atol=1e-10)
                assert exact <= indep+1e-9 and exact <=same+1e-9
                assert np.linalg.norm(Q.T@Q-np.eye(M.shape[0]))<1e-11
                assert np.linalg.eigvalsh(W).min()>0
                assert np.linalg.norm(Q@M-M@Q)<1e-10
                tests+=7
    # The cancelling step is contractive exactly on nontrivial right-half-plane rotations.
    for a in [.12,.35,.7,1.0,1.4]:
        r=1.7; M=r*rotation(a); eta=1/r
        T,W,Q,pred,exact,_,_=data(M,eta,7)
        assert abs(exact)<1e-12
        assert np.allclose(T.T@T,(2*math.cos(a)-1)**2*np.eye(2),atol=1e-12)
        assert np.linalg.norm(T,2)<1
        tests+=3
    # An odd-dimensional strictly monotone scalar-orthogonal example retains eigenvalue 1.
    r=1.7; Q=blockdiag(rotation(.6),np.array([[1.0]])); M=r*Q;eta=1/r
    T,W,QQ,pred,exact,_,_=data(M,eta,5)
    assert abs(exact)<1e-12
    assert abs(max(abs(np.linalg.eigvals(T)))-1)<1e-12
    tests+=2
    # Finite-horizon Gaussian Monte Carlo with exact polar coupling and independent coupling.
    rng=np.random.default_rng(6321)
    M=blockdiag(1.5*rotation(.4),2.2*rotation(.9));eta=.35;n=4;sigma=1.2
    T,W,Q,pred,exact,indep,same=data(M,eta,n,sigma)
    Z=rng.normal(size=(150000,4))*sigma
    optnoise=(eta*M@Z.T-Q@Z.T).T
    indepnoise=(eta*M@Z.T-rng.normal(size=(4,150000))*sigma).T
    gotopt=eta*eta*np.einsum('ni,ij,nj->',optnoise,W,optnoise)/len(Z)
    gotind=eta*eta*np.einsum('ni,ij,nj->',indepnoise,W,indepnoise)/len(Z)
    assert abs(gotopt-exact)<.025*max(exact,.01)
    assert abs(gotind-indep)<.025*max(indep,.01)
    tests+=2
    print('PASS',tests,'finite identity, inequality, parity-example and Monte Carlo checks')


if __name__=='__main__': main()
