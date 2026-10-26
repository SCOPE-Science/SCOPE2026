#!/usr/bin/env python3
"""Finite algebraic checks for a rational dissipative source update."""
from fractions import Fraction as F
import numpy as np


def exact_physical_witness():
    a = -F(11, 40000)
    b = F(11, 40)
    numerator = (1-a)**2+b*b
    den_real = 1-2*a+2*(a*a-b*b)
    den_imag = -2*b+4*a*b
    denominator = den_real**2+den_imag**2
    ratio = numerator/denominator
    assert ratio == F(688752048400000000, 655451896588494641)
    assert ratio > 1
    return str(ratio)


def check_sos(rng, n):
    I=np.eye(n, dtype=complex)
    X=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
    Y=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
    B=-X.conj().T@X+(Y-Y.conj().T)
    B *= 1.5/max(1.,np.linalg.norm(B,2))
    D=B@B-2*B+2*I
    N=B@B-B
    lhs=D.conj().T@D-N.conj().T@N
    rhs=4*I-B.conj().T@B+(B-2*I).conj().T@(-B-B.conj().T)@(B-2*I)
    assert np.linalg.norm(lhs-rhs) < 1e-9
    singular = np.linalg.svd(np.linalg.solve(D,N), compute_uv=False)
    assert singular[0] <= 1 + 1e-11


def check_physical(rng, dust_count):
    masses=np.exp(rng.uniform(-2,2,size=dust_count))
    alpha=np.exp(rng.uniform(-3,2,size=dust_count))
    omega=rng.normal(size=dust_count)*np.exp(rng.uniform(-2,3,size=dust_count))
    h=.5/min(np.hypot(alpha,omega)) * (1 + float(rng.uniform(0,4)))
    n=dust_count+1
    J=np.array([[0.,-1.,0.],[1.,0.,0.],[0.,0.,0.]])
    M=np.zeros((3*n,3*n))
    for i in range(dust_count):
        v=np.zeros(n)
        v[0]=np.sqrt(masses[i])
        v[i+1]=-1
        M+=np.kron(np.outer(v,v), -alpha[i]*np.eye(3)+omega[i]*J)
    A=h*M
    I=np.eye(3*n)
    T=np.linalg.solve(I-2*A+2*A@A,I-A)
    smax=np.linalg.svd(T,compute_uv=False)[0]
    assert smax<1+2e-8, (dust_count,h,smax)
    x=rng.normal(size=3*n)
    assert np.linalg.norm(T@x)**2 <= np.linalg.norm(x)**2 + 1e-7*np.linalg.norm(x)**2
    return smax


def main():
    witness=exact_physical_witness()
    rng=np.random.default_rng(261018)
    count=0
    for n in (1,2,3,4,5):
        for _ in range(40):
            check_sos(rng,n)
            count+=1
    for n in (1,2,3,4,6):
        for _ in range(80):
            check_physical(rng,n)
            count+=1
    print('PASS',count,'matrix checks; positive-drag rational witness',witness)

if __name__ == '__main__':
    main()
