"""Reproducible finite-dimensional checks for a dephased rhombic chain.

Requires NumPy and SciPy. These calculations check small instances only;
the arbitrary-size statements are proved algebraically in RESULT.md.
"""
import numpy as np
from scipy.linalg import expm, eigvals


def blocks(n, phase):
    assert n >= 3
    q = np.zeros((n, 2*n), dtype=complex)
    for j in range(n):
        q[j, j] = 1
        q[(j+1)%n, j] = 1
        q[j, n+j] = 1
        q[(j+1)%n, n+j] = np.exp(1j*phase)
    h = np.zeros((3*n, 3*n), dtype=complex)
    h[:n, n:] = q
    h[n:, :n] = q.conj().T
    return q, h


def candidates(n, phase, initial):
    q, h = blocks(n, phase)
    inverse = np.linalg.inv(q @ q.conj().T)
    bright = np.zeros((3*n, 3*n), dtype=complex)
    bright[:n, :n] = np.eye(n)
    bright[n:, n:] = q.conj().T @ inverse @ q
    dark = np.eye(3*n) - bright
    rho = np.zeros_like(bright)
    rho[initial, initial] = 1
    output = dark @ rho @ dark
    if abs(phase - np.pi) < 1e-12:
        sectors = []
        for j in range(n):
            r = np.zeros(3*n, dtype=complex)
            r[n:] = q[j, :].conj() / 2
            a = np.zeros(3*n, dtype=complex)
            a[j] = 1
            s = np.outer(a, a.conj()) + np.outer(r, r.conj())
            sectors.append(s)
            output += np.trace(s @ rho).real * s / 2
        assert np.linalg.norm(sum(sectors)-bright)<1e-11
    else:
        output += np.trace(bright @ rho).real * bright / (2*n)
    return q, h, dark, bright, output


def generator(n, phase, rates):
    q, h = blocks(n, phase)
    d = 3*n
    ident = np.eye(d)
    l = -1j*(np.kron(ident, h)-np.kron(h.T, ident))
    for j, rate in enumerate(rates):
        p = np.zeros((d,d)); p[j,j] = 1
        l += rate*(np.kron(p,p)-0.5*np.kron(ident,p)-0.5*np.kron(p,ident))
    return l


def finite_checks():
    count = 0
    for n in (3,4,5,6):
        for phi in (0.4,1.35,np.pi,4.8):
            q,h,dark,bright,out = candidates(n,phi,0)
            assert np.linalg.norm(q@q.conj().T-np.conj(q@q.conj().T).T)<1e-11
            assert np.linalg.norm(dark@dark-dark)<1e-10
            assert np.linalg.norm(h@dark)<1e-10
            assert np.linalg.norm(bright@dark)<1e-10
            assert abs(np.trace(out).real-1)<1e-10
            assert np.linalg.norm(out-out.conj().T)<1e-10
            assert np.linalg.eigvalsh(out).min()>-1e-10
            expected = 0.5 if phi==np.pi else 1/(2*n)
            assert abs(out[0,0].real-expected)<1e-10
            _,_,_,_,outb = candidates(n,phi,n)
            # The generic return of a bridge-site input is determined by dark weight.
            p = dark[n,n].real
            if phi==np.pi:
                assert abs(outb[n,n].real-5/16)<1e-10
            else:
                assert abs(outb[n,n].real-(p*p+(1-p)**2/(2*n)))<1e-10
            if phi != np.pi:
                k = 2*np.pi*np.arange(n)/n
                den=4+2*np.cos(k)+2*np.cos(k-phi)
                p_fourier = 1-np.mean((2+2*np.cos(k))/den)
                assert abs(p_fourier-p)<1e-10
            count+=1
    # Match the matrix semigroup to the algebraic limit, with unequal rates.
    for n in (3,4):
        for phi in (0.6,np.pi):
            l=generator(n,phi,[0.7+0.11*j for j in range(n)])
            target_dim=n*n+(n if phi==np.pi else 1)
            eig=eigvals(l)
            assert sum(abs(eig)<1e-8)==target_dim, (n,phi,target_dim)
            rho=np.zeros((3*n,3*n));rho[0,0]=1
            approx=expm(400*l)@rho.flatten(order='F')
            approx=approx.reshape((3*n,3*n),order='F')
            _,_,_,_,expected=candidates(n,phi,0)
            assert np.linalg.norm(approx-expected)<1e-8, (n,phi)
            count+=1
    # The thermodynamic bridge-site weight approaches one half for fixed nonzero flux.
    for phi in (0.3,1.0,2.2,3.8,5.7):
        n=256
        k=2*np.pi*np.arange(n)/n
        p=1-np.mean((2+2*np.cos(k))/(4+2*np.cos(k)+2*np.cos(k-phi)))
        assert abs(p-.5)<3e-6, (phi,p)
        count+=1
    print('PASS:', count, 'families of finite matrix and semigroup checks')


if __name__=='__main__':
    finite_checks()
