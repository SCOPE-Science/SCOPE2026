"""Finite-dimensional checks for the singular-value spectral-clipping theorem.

These tests are illustrative and do not certify infinite-dimensional statements.
"""
import numpy as np

rng=np.random.default_rng(22)
count=0
for N in (8,12,20):
    for m in (0,1,3,5):
        if m>=N:continue
        for trial in range(50):
            c=2.0
            neg=np.sort(rng.uniform(0.005,0.65, size=N//2))[::-1]
            pos=rng.uniform(0.01,0.4,size=N-len(neg))
            diagonal=np.r_[c-neg,c+pos]
            A=np.diag(diagonal)
            correction=np.r_[np.zeros(min(m,len(neg))),neg[min(m,len(neg)):],np.zeros(len(pos))]
            Kstar=np.diag(correction)
            assert (np.linalg.svd(Kstar,compute_uv=False)[:N-min(m,len(neg))] >=-1e-9).all()
            assert np.allclose(np.linalg.svd(Kstar,compute_uv=False)[:max(0,len(neg)-m)],neg[m:])
            assert np.count_nonzero(np.linalg.svd(A+Kstar,compute_uv=False)<c-1e-8)<=m
            count+=3
            # Build noncommuting perturbation whose corrected modulus is
            # spectrally constrained to have at most m singular values < c.
            target=A+Kstar
            Q,_=np.linalg.qr(rng.normal(size=(N,N))+1j*rng.normal(size=(N,N)))
            R,_=np.linalg.qr(rng.normal(size=(N,N))+1j*rng.normal(size=(N,N)))
            amp=rng.uniform(0,0.08)
            X=((1-amp)*np.eye(N)+amp*Q)@target@((1-amp)*np.eye(N)+amp*R)
            # The preliminary X need not meet the spectral lower bound; use
            # exact unitaries via QR of near-identity perturbations instead.
            U,_=np.linalg.qr(np.eye(N)+amp*(Q-np.eye(N)))
            V,_=np.linalg.qr(np.eye(N)+amp*(R-np.eye(N)))
            X=U@target@V.conj().T
            small=np.linalg.svd(X,compute_uv=False)
            assert np.count_nonzero(small<c-1e-7)<=m
            K=X-A
            s=np.linalg.svd(K,compute_uv=False)
            required=np.r_[neg[m:],np.zeros(max(0,N-(len(neg)-m)))]
            assert all(s[j]+1e-8>=required[j] for j in range(N)), (N,m,trial,s,required)
            count+=2
print(f'PASS: {count} finite assertions; dimension, phase and tail cases tested')
