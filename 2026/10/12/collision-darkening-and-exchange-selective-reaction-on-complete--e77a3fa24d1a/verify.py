"""Independent finite-dimensional checks for two-walker collision absorption on complete graphs.

Requires numpy >=1.24 and scipy >=1.10. Run with: python verify.py
All sizes are tested exhaustively over ordered initial site pairs. Tests do not
replace the general projection proof.
"""
import numpy as np
from scipy.linalg import expm


def formula(n, equal, x, y):
    return 1.0 if x == y else (1.0/(n-1) if equal else (2*n-1)/(n*(n-1)))


def spectral_projection(n, a, b):
    A = np.ones((n, n)) - np.eye(n)
    H = a*np.kron(A, np.eye(n)) + b*np.kron(np.eye(n), A)
    w, V = np.linalg.eigh(H)
    detector = np.zeros((n*n, n))
    for x in range(n):
        detector[n*x+x, x] = 1
    P = np.zeros((n*n, n*n))
    ranks = []
    start = 0
    while start < n*n:
        end = start+1
        while end < n*n and abs(w[end]-w[start]) < 2e-8:
            end += 1
        X = V[:, start:end]
        measured = detector.T @ X
        U, singular, _ = np.linalg.svd(measured, full_matrices=False)
        rank = int(np.count_nonzero(singular > 1e-8))
        # Range(X X* detector) = observable subspace for this eigenspace.
        if rank:
            B = X @ (np.linalg.svd(measured, full_matrices=False)[2][:rank, :].conj().T)
            P += B @ B.conj().T
        ranks.append(rank)
        start = end
    assert np.linalg.norm(P@P-P) < 2e-9
    return H, P, sorted(ranks), detector


def run():
    sitewise = 0
    ranks_checked = 0
    loss_checked = 0
    convergence_checked = 0
    exchange_checked = 0
    rng = np.random.default_rng(140275)
    for n in range(4, 10):
        for a,b in [(1.,1.), (1., 1.5), (0.75, 1.25), (2.3, 2.3)]:
            same = a == b
            H,P,ranks,D = spectral_projection(n,a,b)
            target_rank = 2*n if same else 3*n-1
            assert sum(ranks) == target_rank, (n,a,b,ranks)
            ranks_checked += 1
            for x in range(n):
                for y in range(n):
                    observed = P[x*n+y,x*n+y]
                    assert abs(observed-formula(n,same,x,y)) < 3e-9, (n,a,b,x,y,observed)
                    sitewise += 1
            for x in range(n):
                for y in range(x+1, n):
                    ketplus=np.zeros(n*n); ketplus[n*x+y]=1/np.sqrt(2);ketplus[n*y+x]=1/np.sqrt(2)
                    ketminus=np.zeros(n*n);ketminus[n*x+y]=1/np.sqrt(2);ketminus[n*y+x]=-1/np.sqrt(2)
                    plus=ketplus@P@ketplus
                    minus=ketminus@P@ketminus
                    assert abs(plus-2/(n-1))<3e-9,(n,a,b,'plus',plus)
                    assert abs(minus-(0 if same else 2/n))<3e-9,(n,a,b,'minus',minus)
                    exchange_checked += 2
            if n<=6:
                kappa=rng.uniform(0.5,2.5,n)
                loss=np.zeros(n*n)
                for x in range(n):
                    loss[n*x+x]=kappa[x]
                H_eff=H-0.5j*np.diag(loss)
                ev=np.linalg.eigvals(H_eff)
                assert np.max(ev.imag) < 1e-8
                damped=np.count_nonzero(ev.imag < -2e-8)
                assert damped==target_rank,(n,a,b,damped,target_rank)
                loss_checked+=1
            if n<=4:
                loss=np.zeros(n*n)
                for x in range(n):
                    loss[n*x+x]=1.5 + x/n
                U=expm((-1j*H-0.5*np.diag(loss))*2000.0)
                i=1
                c=1-np.sum(np.abs(U[:,i])**2)
                assert abs(c-formula(n,same,0,1))<3e-6,(n,a,b,c)
                convergence_checked+=1
    print('VERIFY_OK spectral_ranks=%d sitewise=%d exchange=%d lossy_spectrum=%d long_time=%d' % (ranks_checked,sitewise,exchange_checked,loss_checked,convergence_checked))

if __name__ == '__main__':
    run()
