#!/usr/bin/env python3
"""Finite-dimensional computational checks for a dephased driven two-qubit battery.

Analytic convergence, algebra dimension, and the entanglement-breaking
property are proved separately; finite tests here are diagnostic, not proofs.
"""
import numpy as np
from scipy.linalg import expm

I2=np.eye(2,dtype=complex)
X=np.array([[0,1],[1,0]],dtype=complex)
Y=np.array([[0,-1j],[1j,0]],dtype=complex)
Z=np.diag([1,-1]).astype(complex)
I4=np.eye(4,dtype=complex)
kron=np.kron


def generator(F,g,gamma):
    h=F*kron(X,I2)+g/2*(kron(X,X)+kron(Y,Y))
    z=kron(Z,I2)
    k=(2*F*kron(I2,X)-g*kron(Z,Z))/np.hypot(2*F,g)
    d=-1j*(kron(I4,h)-kron(h.T,I4))
    d+=(gamma/4)*(kron(z.conj(),z)-np.eye(16))
    return h,z,k,d


def vec(m): return m.reshape(-1,order='F')

def mat(v): return v.reshape((4,4),order='F')

def rand_density(rng):
    a=rng.normal(size=(4,4))+1j*rng.normal(size=(4,4))
    v=a@a.conj().T
    return v/np.trace(v)


def test():
    rng=np.random.default_rng(736451)
    max_comm=max_gen=max_stat=max_asym=max_erg=0.
    for j in range(80):
        F=float(np.exp(rng.uniform(-1.4,1.2)))
        g=float(np.exp(rng.uniform(-1.0,1.2)))
        gamma=float(np.exp(rng.uniform(-1.2,1.1)))
        h,z,q,L=generator(F,g,gamma)
        max_comm=max(max_comm,np.linalg.norm(h@q-q@h),np.linalg.norm(z@q-q@z),np.linalg.norm(q@q-I4))
        eig=np.linalg.eigvals(L)
        assert len(eig)==16
        assert sum(abs(eig)<1.e-9)==2
        assert max(ev.real for ev in eig if abs(ev)>1.e-9)<-1.e-10
        rho=rand_density(rng)
        c=np.trace(q@rho).real
        out=(I4+c*q)/4
        max_gen=max(max_gen,np.linalg.norm(L@vec(out)))
        max_stat=max(max_stat,abs(np.trace(out)-1),abs(np.trace(q@out)-c),
                     abs(np.min(np.linalg.eigvalsh(out))-(1-abs(c))/4))
        # Check the analytic asymptotic channel against a genuine evolution.
        scale=max(1.,19/(-max(ev.real for ev in eig if abs(ev)>1e-9)))
        num=mat(expm(L*scale)@vec(rho))
        max_asym=max(max_asym,np.linalg.norm(num-out))
        rX=np.trace(kron(I2,X)@out).real
        exact=2*F*c/np.hypot(2*F,g)
        max_erg=max(max_erg,abs(rX-exact),abs(rX)/2-abs(F*c)/np.hypot(2*F,g))
        # Characteristic: two rank-two dephasing-compatible stationary projections.
        plus=(I4+q)/2; minus=(I4-q)/2
        assert np.linalg.norm(plus@plus-plus)<1.e-11
        assert np.linalg.norm(minus@minus-minus)<1.e-11
        assert abs(np.trace(plus)-2)<1.e-11
        assert abs(np.trace(minus)-2)<1.e-11
        mix=np.trace(plus@rho)*plus/2+np.trace(minus@rho)*minus/2
        assert np.linalg.norm(mix-out)<1.e-11
    assert max_comm<3.e-14
    assert max_gen<3.e-14
    assert max_stat<3.e-14
    assert max_asym<2.e-7
    assert max_erg<3.e-14
    print('80 random positive-parameter, random full-rank-state tests passed')
    print('max commutation/Q² error',format(max_comm,'.3e'))
    print('max stationary residual',format(max_gen,'.3e'))
    print('max stationary scalar error',format(max_stat,'.3e'))
    print('max asymptotic numerical density-matrix error',format(max_asym,'.3e'))
    print('max battery ergotropy/Bloch error',format(max_erg,'.3e'))
    # Ground-state source specialization (ground has Z=-1).
    F=0.5;g=1.;gamma=1.15
    _,_,q,L=generator(F,g,gamma)
    rho=np.zeros((4,4),complex);rho[3,3]=1
    c=np.trace(q@rho).real
    expected=F*g/(g*g+4*F*F)
    ergotropy=(abs(2*F*c/np.hypot(2*F,g)))/2
    assert abs(ergotropy-expected)<1.e-14
    assert abs(ergotropy-.25)<1.e-14
    print('ground-state source ergotropy 0.25 exactly reproduced')


if __name__=='__main__': test()
