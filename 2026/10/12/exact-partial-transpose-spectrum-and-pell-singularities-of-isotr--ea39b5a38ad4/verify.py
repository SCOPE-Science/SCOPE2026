#!/usr/bin/env python3
import math
import numpy as np


def spin_matrices(j):
    d = int(round(2*j+1))
    ms = np.array([-j + k for k in range(d)], dtype=float)
    jp = np.zeros((d,d), dtype=complex)
    for i,m in enumerate(ms[:-1]):
        jp[i+1,i] = math.sqrt(j*(j+1)-m*(m+1))
    jm = jp.conj().T
    jx = (jp+jm)/2
    jy = (jp-jm)/(2j)
    jz = np.diag(ms)
    return [jx,jy,jz]


def choi_pt(j):
    mats=spin_matrices(j)
    d=mats[0].shape[0]
    ks=[a/math.sqrt(j*(j+1)) for a in mats]
    om=np.zeros(d*d,complex)
    for i in range(d):
        om[i*d+i]=1/math.sqrt(d)
    C=np.zeros((d*d,d*d),complex)
    I=np.eye(d)
    for K in ks:
        v=np.kron(I,K)@om
        C += np.outer(v,v.conj())
    T=C.reshape(d,d,d,d).transpose(0,3,2,1).reshape(d*d,d*d)
    return C,T


def predicted(j):
    d=int(round(2*j+1))
    vals=[]
    for L in range(int(round(2*j))+1):
        q=L*(L+1)-2*j*(j+1)
        lam=((-1)**(int(round(2*j))-L))*q/(2*d*j*(j+1))
        vals += [lam]*(2*L+1)
    return np.array(sorted(vals))


def negativity_closed(j):
    r=(math.sqrt(1+8*j*(j+1))-1)/2
    k=math.ceil(r-1e-12)
    return k*k*(4*j*(j+1)-k*k+1)/(4*(2*j+1)*j*(j+1)) - 0.5

spins=[0.5,1,1.5,2,2.5,3,3.5,4]
for j in spins:
    C,T=choi_pt(j)
    assert np.linalg.norm(C-C.conj().T) < 1e-11
    assert abs(np.trace(C)-1)<1e-11
    obs=np.linalg.eigvalsh(T)
    pred=predicted(j)
    assert np.max(np.abs(obs-pred))<2e-10, (j,np.max(np.abs(obs-pred)))
    neg=float(np.sum(np.maximum(-obs,0)))
    ncl=negativity_closed(j)
    assert abs(neg-ncl)<2e-10, (j,neg,ncl)

# Pell singular spins through j=500: zero eigenvalues iff x^2-2y^2=-1.
zeros=[]
for n in range(1,1001):
    j=n/2
    for L in range(n+1):
        if 2*L*(L+1)==n*(n+2):
            x=2*L+1; y=n+1
            assert x*x-2*y*y==-1
            zeros.append((j,L))
assert zeros[:3]==[(2.0,3),(14.0,20),(84.0,119)], zeros[:3]
print('VERIFY_OK spins=8 max_j=4 pell_first=2,14,84')
