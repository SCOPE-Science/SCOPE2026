"""Deterministic structural and statistical checks for Gaussian-sketched QR.
No Monte Carlo test is used as a substitute for the moment-integrability proof.
"""
import math
import numpy as np
from scipy.stats import ks_2samp

def run():
    rng=np.random.default_rng(7301)
    checks=0
    for m,ell in ((2,3),(3,4),(3,6),(4,7)):
        n=3*m+2
        for r in range(m+1):
            beta=np.zeros(m)
            beta[:r]=np.linspace(.30,.80,r)
            B=np.diag(beta)
            C=np.zeros((n-m,m))
            C[:m,:]=np.diag(np.sqrt(1-beta**2))
            W=np.vstack((B,C))
            assert np.allclose(W.T@W,np.eye(m),atol=1e-13); checks+=1
            assert np.linalg.matrix_rank(B,tol=1e-12)==r; checks+=1
            for _ in range(45):
                Om=rng.standard_normal((ell,n-m))/math.sqrt(ell)
                Z=np.vstack((B,Om@C))
                _,R=np.linalg.qr(Z,mode='reduced')
                signs=np.where(np.diag(R)<0,-1.,1.)
                R=signs[:,None]*R
                Q=np.linalg.solve(R.T,W.T).T # W @ inv(R): solve R.T X.T = W.T
                assert np.allclose(W,Q@R,rtol=2e-10,atol=2e-10);checks+=1
                assert np.allclose(Z.T@Z,R.T@R,rtol=2e-10,atol=2e-10);checks+=1
                SQ=np.vstack((Q[:m,:],Om@Q[m:,:]))
                assert np.allclose(SQ.T@SQ,np.eye(m),rtol=1e-9,atol=1e-9); checks+=1
                assert abs(np.linalg.norm(Q,2)-1/np.linalg.svd(Z,compute_uv=False)[-1])<5e-9*(1+np.linalg.norm(Q,2));checks+=1
                k=m-r
                if 0<k<m:
                    # in this diagonal-basis witness, the null block is the last k coordinates
                    null=Om@C[:,r:]
                    assert np.linalg.svd(Z,compute_uv=False)[-1] <= np.linalg.svd(null,compute_uv=False)[-1]+1e-9;checks+=1
    # Test arbitrary input-coordinate rotation and nontrivial lower-block geometry.
    for m,ell in ((3,5),(4,6)):
        n=5*m
        for r in range(m+1):
            beta=np.zeros(m); beta[:r]=np.linspace(.22,.73,r)
            T,_=np.linalg.qr(rng.standard_normal((m,m)))
            H,_=np.linalg.qr(rng.standard_normal((n-m,m)))
            W=np.vstack((np.diag(beta)@T.T,H@np.diag(np.sqrt(1-beta**2))@T.T))
            B,C=W[:m,:],W[m:,:]
            assert np.allclose(W.T@W,np.eye(m));checks+=1
            for _ in range(40):
                Om=rng.standard_normal((ell,n-m))/math.sqrt(ell)
                Z=np.vstack((B,Om@C))
                _,R=np.linalg.qr(Z,mode='reduced')
                Q=np.linalg.solve(R.T,W.T).T
                smin=np.linalg.svd(Z,compute_uv=False)[-1]
                assert np.isclose(np.linalg.norm(Q,2)*smin,1.,rtol=5e-11); checks+=1
                if r<m:
                    # Right nullspace of B is the exact Gaussian unanchored block.
                    _, _, Vh=np.linalg.svd(B)
                    Vnull=Vh.T[:,r:]
                    Gn=Om@C@Vnull
                    assert smin<=np.linalg.svd(Gn,compute_uv=False)[-1]+3e-11;checks+=1
    # In the unanchored case the Bartlett distribution generates each column-norm law.
    # Compare independently simulated Gaussian QR against independent chi-square samples.
    for m,ell in ((2,4),(3,5),(4,7)):
        N=4000
        obs=np.empty((N,m)); theory=np.empty((N,m))
        for k in range(N):
            A=rng.standard_normal((ell,m))/math.sqrt(ell)
            _,R=np.linalg.qr(A,mode='reduced')
            R=np.sign(np.diag(R))[:,None]*R
            X=np.linalg.inv(R)
            obs[k,:]=np.sum(X*X,axis=0)
            for j in range(1,m+1):
                df=ell-j+1
                chi=rng.chisquare(df)
                if j>1:
                    z=rng.chisquare(j-1)/rng.chisquare(df+1)
                else:z=0.
                theory[k,j-1]=ell*(1+z)/chi
        for j in range(1,m+1):
            d=ks_2samp(obs[:,j-1],theory[:,j-1]).statistic
            assert d<.05,(m,ell,j,d)
            checks+=1
            mean=ell*(ell-1)/((ell-j)*(ell-j-1))
            if ell-j>=3:
                assert abs(float(np.mean(obs[:,j-1]))-mean) < max(.15,.30*mean), (m,ell,j,mean,np.mean(obs[:,j-1]))
                checks+=1
    print('PASS',checks,'structural, QR, Gram, and independent distribution checks')
if __name__=='__main__':run()
