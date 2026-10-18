"""Numerical reproducibility checks for quadratic-measurement cubature formulas.

All asserted universal statements in the accompanying manuscript have separate
analytical proofs. Finite checks below are diagnostic, not exhaustive proofs.
Requires Python 3 and NumPy.
"""
import numpy as np


def same_diagonal_basis(b):
    """Construct an orthonormal basis with constant Rayleigh quotients."""
    n = b.shape[0]
    if n == 1:
        return np.eye(1)
    m = np.trace(b) / n
    lam, vec = np.linalg.eigh(b)
    if abs(lam[-1] - lam[0]) < 1e-11:
        return np.eye(n)
    t = np.clip((m-lam[0])/(lam[-1]-lam[0]), 0.0, 1.0)
    v = np.sqrt(1-t)*vec[:,0] + np.sqrt(t)*vec[:,-1]
    vectors = [v]
    for i in range(n):
        w = np.eye(n)[:,i].copy()
        for u in vectors:
            w -= np.dot(u,w)*u
        for u in vectors:
            w -= np.dot(u,w)*u
        if np.linalg.norm(w) > 1e-8:
            vectors.append(w/np.linalg.norm(w))
        if len(vectors) == n:
            break
    q = np.column_stack(vectors)
    rest = q[:,1:]
    return np.column_stack([v, rest @ same_diagonal_basis(rest.T@b@rest)])


def cubature_quantities(b, ell, r, u):
    n = len(ell)
    pts = np.concatenate((np.sqrt(n)*u, -np.sqrt(n)*u), axis=1)
    y = ell @ pts + np.einsum('ik,ij,jk->k', pts, b, pts)
    ybar = np.mean(y)
    s = np.mean((y-ybar)**2)+r
    cross = pts @ (y-ybar)/(2*n)
    s_exact = np.dot(ell,ell)+2*np.sum(b*b)+r
    gain = cross/s
    p_rep = np.eye(n)-np.outer(cross,cross)/s
    p_real = (np.eye(n)-np.outer(gain,ell)-np.outer(ell,gain)
              +s_exact*np.outer(gain,gain))
    return ybar,s,cross,p_rep,p_real,s_exact


def test():
    rng = np.random.default_rng(20261017)
    tests=0
    for n in range(2,9):
        for j in range(35):
            b0=rng.normal(size=(n,n)); b=(b0+b0.T)/2
            ell=rng.normal(size=n); r=float(rng.uniform(.01,4))
            g=rng.normal(size=(n,n)); u=np.linalg.qr(g)[0]
            mu,s,c,p_rep,p_real,s_true=cubature_quantities(b,ell,r,u)
            f=np.sum(b*b); tr=np.trace(b)
            v=n*np.sum(np.diag(u.T@b@u)**2)-tr**2
            target=r+np.dot(ell,ell)+v
            assert np.isclose(mu,tr,rtol=2e-11,atol=2e-11)
            assert np.isclose(s,target,rtol=2e-11,atol=2e-11)
            assert np.allclose(c,ell,atol=2e-11)
            assert np.allclose(p_real-p_rep,(s_true-s)/s**2*np.outer(ell,ell),atol=2e-11)
            assert v>=-1e-9 and v<=n*f-tr**2+1e-9
            tests+=5
            uc=same_diagonal_basis(b)
            assert np.allclose(uc.T@uc,np.eye(n),atol=5e-10)
            assert np.allclose(np.diag(uc.T@b@uc),np.full(n,tr/n),atol=5e-10)
            ucq=n*np.sum(np.diag(uc.T@b@uc)**2)-tr**2
            assert abs(ucq)<5e-8
            ud=np.linalg.eigh(b)[1]
            udq=n*np.sum(np.diag(ud.T@b@ud)**2)-tr**2
            assert np.isclose(udq,n*f-tr**2,atol=2e-8)
            tests+=4
    # Boundary examples, comparing direct sigma-point propagation at extremizers.
    for n,b_diag,cls in [(2,[1,0],'one-sided'),(3,[1,0,0],'boundary'),
                         (4,[1,0,0,0],'two-sided'),(3,[1,-1,0],'two-sided'),
                         (5,[1,1,1,1,1],'one-sided')]:
        b=np.diag(b_diag); ell=np.ones(n)/np.sqrt(n); r=0.75
        ulo=same_diagonal_basis(b); uhi=np.eye(n)
        vals=[cubature_quantities(b,ell,r,u)[1] for u in (ulo,uhi)]
        true=r+1+2*np.sum(b*b)
        if cls=='one-sided': assert vals[-1]<true+1e-8
        if cls=='boundary': assert np.isclose(vals[-1],true)
        if cls=='two-sided': assert vals[0]<true<vals[-1]
        tests+=1
    print(f'PASS: {tests} numerical algebraic identities, extremal constructions and sharp-boundary examples')


if __name__=='__main__':
    test()
