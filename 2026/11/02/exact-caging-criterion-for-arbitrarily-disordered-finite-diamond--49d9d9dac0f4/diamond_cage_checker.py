"""Reproducibility checks for exact caging on finite weighted diamond paths.

Requires numpy and scipy. Run: python diamond_cage_checker.py
These numerical experiments corroborate but do not replace the local-moment proof.
"""
import numpy as np
from numpy.linalg import norm, eigvalsh
from scipy.linalg import expm


def sample(N, seed):
    rng = np.random.default_rng(seed)
    h = rng.normal(size=N)
    eps = rng.normal(size=N - 1)
    v, w = [], []
    for _ in range(N - 1):
        a = rng.normal(size=2) + 1j * rng.normal(size=2)
        z = rng.normal() + 1j * rng.normal()
        b = z * np.array([-np.conj(a[1]), np.conj(a[0])])
        v.append(a)
        w.append(b)
    return h, eps, np.array(v), np.array(w)


def matrix(h, upper, lower, v, w):
    N = len(h)
    H = np.zeros((3*N-2, 3*N-2), complex)
    H[np.arange(N), np.arange(N)] = h
    for j in range(N-1):
        for a, e in enumerate((upper[j], lower[j])):
            k = N+2*j+a
            H[k,k] = e
            H[k,j] = v[j,a]
            H[j,k] = np.conj(v[j,a])
            H[k,j+1] = w[j,a]
            H[j+1,k] = np.conj(w[j,a])
    return H


def cage_basis(N, v, w):
    blocks = []
    for j in range(N):
        B = np.zeros((3*N-2, 1+(j>0)+(j<N-1)),complex)
        B[j,0] = 1.0
        k = 1
        if j > 0:
            B[N+2*(j-1):N+2*j,k] = w[j-1]/norm(w[j-1]);k+=1
        if j < N-1:
            B[N+2*j:N+2*(j+1),k] = v[j]/norm(v[j])
        blocks.append(B)
    return blocks


def run():
    tests = 0
    max_error = 0.0
    for N in range(2,13):
        for seed in range(9):
            h,eps,v,w = sample(N, seed+111*N)
            H = matrix(h,eps,eps,v,w)
            Bs = cage_basis(N,v,w)
            U = np.column_stack(Bs)
            checks = [norm(H-H.conj().T),norm(U.conj().T@U-np.eye(len(H)))]
            transformed = U.conj().T@H@U
            start = 0
            eigen_parts = []
            for B in Bs:
                A = B.conj().T@H@B
                eigen_parts.extend(eigvalsh(A))
                start += B.shape[1]
            blockH = np.zeros_like(H)
            k=0
            for B in Bs:
                d=B.shape[1]
                blockH[k:k+d,k:k+d] = B.conj().T@H@B
                k+=d
            checks.extend((norm(transformed-blockH),norm(eigvalsh(H)-np.sort(eigen_parts))))
            for t in (0.2,1.0,2.7):
                V = expm(-1j*t*H)[:N,:N]
                checks.append(norm(V-np.diag(np.diag(V))))
            for j in range(N-1):
                checks.extend((abs(np.vdot(w[j],v[j])),
                               abs((H@H)[j+1,j]),
                               abs((H@H@H)[j+1,j])))
            for c in checks:
                max_error=max(max_error,float(c))
                assert c<2e-10,(N,seed,c)
                tests+=1
            # Perturb exactly one arm energy: second moment remains zero,
            # and the third moment is its predicted nonzero term.
            j=(N-1)//2
            upper=eps.copy();upper[j]+=0.37
            Hdet=matrix(h,upper,eps,v,w)
            m2=(Hdet@Hdet)[j+1,j]
            m3=np.linalg.matrix_power(Hdet,3)[j+1,j]
            expected=0.37*np.vdot(w[j,:1],v[j,:1])
            assert abs(m2)<2e-10
            assert abs(m3-expected)<2e-10
            assert abs(expected)>1e-9
            tests+=3
            # Perturb one bond and verify its immediate quadratic leakage.
            ww=w.copy();ww[j,0]*=1.08
            Hb=matrix(h,eps,eps,v,ww)
            amp2=(Hb@Hb)[j+1,j]
            expected2=np.vdot(ww[j],v[j])
            assert abs(amp2-expected2)<2e-10
            assert abs(amp2)>1e-9
            tests+=2
    print(f"PASS: {tests} checks, N=2..12, 9 disorder realizations each; maximum structural/spectral discrepancy {max_error:.3g}")

if __name__=='__main__':
    run()
