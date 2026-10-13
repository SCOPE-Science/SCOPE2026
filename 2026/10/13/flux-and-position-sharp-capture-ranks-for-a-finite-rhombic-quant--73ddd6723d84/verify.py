"""Numerical checks for the finite rhombic-chain single-site absorption theorem.

This tests specified finite dimensions and is not a proof for unbounded length.
Requires numpy and scipy.
"""
import math
import numpy as np
from scipy.linalg import expm


def hamiltonian(n, flux):
    b = np.zeros((2*n, n+1), dtype=complex)
    for j in range(1, n+1):
        b[2*j-2, j-1] = 1
        b[2*j-2, j] = np.exp(1j*flux)
        b[2*j-1, j-1] = 1
        b[2*j-1, j] = 1
    o = np.zeros((n+1, n+1))
    p = np.zeros((2*n, 2*n))
    return np.block([[o, b.conj().T], [b, p]])


def expected_rank(n, j, phase):
    if phase == 'zero':
        return 2*n-2*math.gcd(j,n+1)+3
    if phase == 'half':
        return 5 if j in (1,n) else 3
    return 2*n+3


def krylov_rank(h, detector):
    e = np.eye(h.shape[0], dtype=complex)[:, detector]
    q = []
    for _ in range(h.shape[0]):
        for v in q:
            e -= v*np.vdot(v,e)
        norm = np.linalg.norm(e)
        if norm < 2e-7:
            return len(q)
        e /= norm
        q.append(e.copy())
        e = h@e
    return len(q)


def spectral_rank(h, detector):
    ev, v = np.linalg.eigh(h)
    groups=[]
    for m,e in enumerate(ev):
        if not groups or abs(e - groups[-1][0]) > 5e-7:
            groups.append((e,[m]))
        else:
            groups[-1][1].append(m)
    return sum(np.linalg.norm(v[detector, indices]) > 3e-7 for _,indices in groups)


def main():
    cases=0
    for n in range(2,9):
        for phase, flux in [('zero',0.),('generic',np.pi/7),('generic',np.pi/2),('half',np.pi)]:
            h=hamiltonian(n,flux)
            for j in range(1,n+1):
                detector=n+1+2*(j-1)
                needed=expected_rank(n,j,phase)
                k=krylov_rank(h, detector)
                s=spectral_rank(h, detector)
                assert k == s == needed, (n,j,phase,k,s,needed)
                cases+=1
    # Independent dynamical check: local loss leaves only dark components.
    dynamics=0
    for n,j,phase,flux in [(2,1,'generic',np.pi/2),(3,2,'half',np.pi),(3,2,'zero',0.)]:
        h=hamiltonian(n,flux)
        idx=n+1+2*(j-1)
        generator=h-0.8j*np.diag(np.eye(h.shape[0])[idx])
        propagator=expm(-1j*generator*360)
        remain=np.linalg.norm(propagator, 'fro')**2/(3*n+1)
        target=1-expected_rank(n,j,phase)/(3*n+1)
        assert abs(remain-target) < 1e-5, (n,j,phase,remain,target)
        dynamics+=1
    print('VERIFY_OK rank_cases=%d independent_spectral_rank=%d loss_dynamics=%d' % (cases,cases,dynamics))


if __name__ == '__main__':
    main()
