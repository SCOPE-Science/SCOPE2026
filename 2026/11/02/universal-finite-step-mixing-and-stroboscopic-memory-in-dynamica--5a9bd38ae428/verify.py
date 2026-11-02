"""Direct finite-dimensional diagnostics for stroboscopic Laplacian percolation.
Requires NumPy. The universal convergence proof is analytic, not based on these tests.
"""
import itertools
import numpy as np


def edge_laplacian(n, a, b):
    v = np.zeros(n)
    v[a] = 1.
    v[b] = -1.
    return np.outer(v, v)


def setup_channel(n, edges, probs, tau):
    units = []
    ws = []
    for mask in itertools.product((0, 1), repeat=len(edges)):
        lap = sum((edge_laplacian(n, *e) for e, flag in zip(edges, mask) if flag),
                  np.zeros((n, n)))
        vals, vectors = np.linalg.eigh(lap)
        U = (vectors * np.exp(-1j * tau * vals)) @ vectors.conj().T
        weight = np.prod([p if flag else 1-p for p, flag in zip(probs, mask)])
        units.append(U)
        ws.append(weight)
    channel = sum(w * np.kron(U.conj(), U) for w, U in zip(ws, units))
    return channel, units, ws


def project_limit(rho):
    n = len(rho)
    s = np.ones(n) / np.sqrt(n)
    P = np.outer(s, s)
    Q = np.eye(n)-P
    alpha = np.real(np.trace(P @ rho))
    return alpha * P + (1-alpha)/(n-1) * Q


def vec(x):
    return x.reshape(-1, order='F')


def channel_run(C, rho, steps):
    return (np.linalg.matrix_power(C, steps) @ vec(rho)).reshape(rho.shape, order='F')


def density(n, seed):
    rng = np.random.default_rng(seed)
    A = rng.normal(size=(n,n)) + 1j*rng.normal(size=(n,n))
    X=A @ A.conj().T
    return X / np.trace(X)


def main():
    count=0
    graphs=[(3, [(0,1),(1,2)]), (4, [(0,1),(1,2),(2,3)]),
            (4, [(0,1),(1,2),(2,3),(3,0)]),
            (5, [(0,1),(0,2),(0,3),(0,4)])]
    for j,(n,edges) in enumerate(graphs):
        probs = [0.37 + 0.06 * (i % 2) for i in range(len(edges))]
        for tau in [0.73, 1.24]:
            C, units, ws=setup_channel(n, edges, probs, tau)
            assert abs(sum(ws)-1)<1e-12
            count += 1
            eig=np.linalg.eigvals(C)
            assert sum(abs(eig-1)<1e-7)==2, (j,tau,eig)
            count += 1
            assert all(abs(z)<1-1e-9 for z in eig if abs(z-1)>1e-7)
            count += 1
            for seed in (9,18):
                rho = density(n, seed+3*j)
                pred=project_limit(rho)
                got=channel_run(C,rho,4500)
                assert np.max(abs(got-pred))<5e-8, (j,tau,seed,np.max(abs(got-pred)))
                count += 1
    n=3
    edges=[(0,1),(1,2)]
    s=np.ones(3)/np.sqrt(3)
    P=np.outer(s,s);Q=np.eye(3)-P
    R=P-Q
    for p1,p2 in ((0.2,0.6),(0.4,0.4),(0.8,0.6)):
        z=p1*p2
        for k in (1,3,5):
            C,units,weights=setup_channel(3,edges,[p1,p2],k*np.pi)
            for rho in (density(3,7), np.diag([1,0,0]).astype(complex)):
                diag=P@rho@P+Q@rho@Q
                off=P@rho@Q+Q@rho@P
                for m in (1,5,100):
                    expected=diag + (1-2*z)**m * off
                    got=channel_run(C,rho,m)
                    assert np.max(abs(got-expected)) < 2e-12
                    count += 1
            for j in range(3):
                rho=np.zeros((3,3),complex);rho[j,j]=1
                asym=P@rho@P + Q@rho@Q
                probs=np.real(np.diag(asym))
                assert np.isclose(probs[j],5/9) and np.allclose(np.delete(probs,j),[2/9,2/9])
                count+=1
        for k in (2,4):
            C,_,_=setup_channel(3,edges,[p1,p2],k*np.pi)
            assert np.max(abs(C-np.eye(9)))<2e-13
            count+=1
    for k in (1,3):
        lap=edge_laplacian(3,0,1)+edge_laplacian(3,1,2)
        assert np.allclose(np.linalg.eigvalsh(lap),[0,1,3])
        count+=1
    print('VERIFICATION_OK',count,'assertion groups')

if __name__=='__main__':
    main()
