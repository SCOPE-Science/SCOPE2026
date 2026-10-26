#!/usr/bin/env python3
"""Reproduce rank-one and rank-two collective-spin dephasing spectra.

Dimensionless generator: -i ad(Jx) - eta ad(Jz)^2, eta >= 0.
Uses only NumPy and SymPy. All tests are finite checks supplementing
an analytic SU(2) decomposition, not an infinite-size certification.
"""
import itertools
import numpy as np
import sympy as sp

z, eta, s = sp.symbols('z eta s', real=True)
I = sp.I
odd = sp.Matrix([[-eta, -I],[-I, -4*eta]])
even = sp.Matrix([[0, -I*sp.sqrt(3), 0],
                  [-I*sp.sqrt(3), -eta, -I],
                  [0, -I, -4*eta]])
dipole = sp.Matrix([[0, -I],[-I, -eta]])
odd_poly = sp.factor((z*sp.eye(2)-odd).det())
even_poly = sp.factor((z*sp.eye(3)-even).det())
dipole_poly = sp.factor((z*sp.eye(2)-dipole).det())
assert odd_poly == z**2 + 5*eta*z + 4*eta**2 + 1
assert sp.expand(even_poly-(z**3+5*eta*z**2+(4*eta**2+4)*z+12*eta)) == 0
assert dipole_poly == z**2 + eta*z + 1
assert sp.expand(sp.discriminant(odd_poly,z) - (9*eta**2-4)) == 0
Q = 9*s**3 - 103*s**2 + 4*s - 16
assert sp.expand(sp.discriminant(even_poly,z)-16*Q.subs(s,eta**2)) == 0
num = (z+eta)*(z+4*eta)+1
assert sp.expand((z*sp.eye(3)-even).adjugate()[0,0]-num)==0
assert sp.expand(even_poly-(z*num+3*(z+4*eta)))==0
assert sp.gcd(even_poly,num, z) == 1
q_roots = sp.nroots(Q)
positive = [float(sp.re(a)) for a in q_roots if abs(float(sp.im(a)))<1e-12 and float(sp.re(a))>0]
assert len(positive)==1 and 10<positive[0]<12
eta_star = np.sqrt(positive[0])
assert abs(eta_star-3.37922432778456)<1e-11

def spin_matrices(two_j):
    j=two_j/2
    ms=np.arange(j,-j-0.1,-1)
    dim=len(ms)
    zp=np.diag(ms.astype(float))
    raising=np.zeros((dim,dim),complex)
    for col,m in enumerate(ms):
        if col>=1:
            raising[col-1,col]=np.sqrt((j-m)*(j+m+1))
    x=(raising+raising.conj().T)/2
    y=(raising-raising.conj().T)/(2j)
    return x,y,zp

def ad(A):
    d=A.shape[0]
    eye=np.eye(d,dtype=complex)
    return np.kron(eye,A)-np.kron(A.T,eye)

def minimal_pairing_error(a,b):
    return min(max(abs(a[i]-b[k]) for i,k in enumerate(p))
               for p in itertools.permutations(range(len(b))))

worst = 0.0
count=0
for two_j in (2,3,4,5,6):
    jx,jy,jz=spin_matrices(two_j)
    kx,ky,kz=ad(jx),ad(jy),ad(jz)
    cas=kx@kx+ky@ky+kz@kz
    vals,vectors=np.linalg.eigh(cas)
    select=np.where(abs(vals-6)<1e-8)[0]
    assert len(select)==5
    basis=vectors[:,select]
    for par in (.12,.5,2/3,.9,1.9,2.,2.5,3.1,eta_star,3.6,5.):
        L=-1j*kx-par*kz@kz
        compressed=basis.conj().T@L@basis
        spec=np.linalg.eigvals(compressed)
        expected=np.concatenate((np.linalg.eigvals(np.array(odd.subs(eta,par),complex)),
                                 np.linalg.eigvals(np.array(even.subs(eta,par),complex))))
        err=minimal_pairing_error(spec,expected)
        worst=max(worst,err)
        assert err < 2e-6, (two_j,par,err)
        count+=1

# The remaining complex pair at eta=5/2 belongs to the parity-even
# quadrupole block, although the dipole eigenvalues are all real.
probe=2.5
spec_even=np.linalg.eigvals(np.array(even.subs(eta,probe),complex))
spec_dipole=np.concatenate(([-probe], np.linalg.eigvals(np.array(dipole.subs(eta,probe),complex))))
assert np.max(abs(spec_dipole.imag)) < 1e-12
assert sum(abs(a.imag)>1e-8 for a in spec_even)==2
print('symbolic polynomials and discriminants: verified')
print('unique even-quadrupole threshold eta_* = %.15f'%eta_star)
print('spin-j finite cross-checks:',count,', max spectral error: %.3g'%worst)
print('at eta=2.5 dipole eigenvalues:',spec_dipole)
print('at eta=2.5 even quadrupole eigenvalues:',spec_even)
