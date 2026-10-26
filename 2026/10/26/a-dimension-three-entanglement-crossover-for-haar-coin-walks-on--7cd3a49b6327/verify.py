#!/usr/bin/env python3
"""Reproducibility for Haar-coin quantum-walk short-time coin purity.
Only mathematical definitions and checks; no external resources.
"""
import math
import numpy as np


def haar_unitary(rng, d):
    z = (rng.normal(size=(d,d)) + 1j*rng.normal(size=(d,d)))/math.sqrt(2)
    q,r = np.linalg.qr(z)
    phases = np.diag(r)
    return q*(phases/np.abs(phases))[None,:]


def exact_means(d):
    return 2/(d+1), (d+5)/(d+1)**2


def coin_purity(u, U):
    d=len(u)
    rho1=np.diag(abs(u)**2)
    # vertex is XOR of two coordinate flips, and after two steps
    # final coin b amplitudes indexed by vertex bitmask.
    amp=np.zeros((d,1<<d),dtype=complex)
    for a in range(d):
        for b in range(d):
            amp[b,(1<<a)^(1<<b)] += U[b,a]*u[a]
    rho2=amp@amp.conj().T
    return float(np.real(np.trace(rho1@rho1))),float(np.real(np.trace(rho2@rho2)))


def independent_finite_wick(d):
    # Exact two-copy integration: conditional 4th moment of a Haar row
    # and distinct-row/column contractions of a Haar unitary.
    E_sum_u4=2/(d+1)
    diag=(1+E_sum_u4)/(d+1)
    off=d*(d-1)*2/(d*(d+1)*(d*d-1))
    return 2/(d+1),diag+off


def main():
    rng=np.random.default_rng(20261019)
    check=0
    for d in range(2,10):
        p1,p2=exact_means(d)
        assert abs(p1-independent_finite_wick(d)[0])<1e-13
        assert abs(p2-independent_finite_wick(d)[1])<1e-13
        assert abs((p2-p1)-(3-d)/(d+1)**2)<1e-14
        assert p2>=1/d
        check+=4
        sims=np.zeros((4500,2),float)
        for m in range(len(sims)):
            U1=haar_unitary(rng,d)
            U2=haar_unitary(rng,d)
            u=U1[:,0]
            sims[m]=coin_purity(u,U2)
        avg=sims.mean(axis=0)
        err=sims.std(axis=0,ddof=1)/np.sqrt(len(sims))
        assert np.max(abs(avg-np.array([p1,p2]))/(err+1e-15))<5.0, (d,avg,[p1,p2],err)
        check+=1
        print('d',d,'exact',round(p1,8),round(p2,8),'simulated',np.round(avg,8),'stderr',np.round(err,8))
    print(f'{check} analytical/computational checks passed; 36,000 independent samples')

if __name__=='__main__': main()
