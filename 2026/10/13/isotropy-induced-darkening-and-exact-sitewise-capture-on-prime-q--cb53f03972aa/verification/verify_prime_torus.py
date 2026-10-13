"""Numerical and exact-coefficient checks for absorption on prime square tori.

Dependencies: numpy, scipy. Run: python verification/verify_prime_torus.py
The analytic theorem is proved separately; finite cases do not prove it.
"""
from fractions import Fraction
from itertools import product
from math import cos, pi
import numpy as np
from scipy.linalg import expm


def cyclosign_vector(p, r):
    v = [0]*p
    for j in (r, (-r) % p):
        v[j] += 1
    return v


def key_for_pair(p, r, s, a, b):
    x, y = cyclosign_vector(p, r), cyclosign_vector(p, s)
    coeffs = [a*x[k]+b*y[k] for k in range(p)]
    return tuple(z-coeffs[-1] for z in coeffs[:-1])


def classes(p, a, b):
    h=(p-1)//2
    out={}
    for r,s in product(range(h+1), repeat=2):
        key=key_for_pair(p,r,s,a,b)
        out.setdefault(key, []).append((r,s))
    return list(out.values())


def mode_list(p, pairs):
    modes=[]
    for r,s in pairs:
        rs=(0,) if r==0 else (r,p-r)
        ss=(0,) if s==0 else (s,p-s)
        modes.extend(product(rs,ss))
    assert len(set(modes))==len(modes)
    return modes


def Fourier_capture(p, a, b, x, y):
    total=0.0
    for pairs in classes(p,a,b):
        modes=mode_list(p,pairs)
        val=sum(np.exp(2j*pi*(k*x+ell*y)/p) for k,ell in modes)
        total+=abs(val)**2/(p*p*len(modes))
    return total


def closed_form(p,a,b,x,y):
    if a==b:
        diagonal=(int(x==y)+int(x==(-y)%p))**2
        return ((1+int(x==0))*(1+int(y==0))+diagonal)/8
    return (1+int(x==0))*(1+int(y==0))/4


def matrix_hamiltonian(p,a,b):
    ring=np.zeros((p,p))
    for i in range(p):
        ring[i,(i+1)%p]=ring[i,(i-1)%p]=1.0
    return a*np.kron(ring,np.eye(p))+b*np.kron(np.eye(p),ring)


def run():
    cases=0
    sites=0
    for p in (3,5,7,11,13):
        for a,b in ((1,1),(2,1),(3,2),(4,7)):
            ranks=len(classes(p,a,b));h=(p-1)//2
            want=(h+1)*(h+2)//2 if a==b else (h+1)**2
            assert ranks==want,(p,a,b,ranks,want)
            # The coefficient keys use equality modulo Phi_p; this is exact,
            # independent of any floating-point eigenvalue tolerance.
            for x,y in product(range(p),repeat=2):
                actual=Fourier_capture(p,a,b,x,y)
                expected=closed_form(p,a,b,x,y)
                assert abs(actual-expected)<3e-12,(p,a,b,x,y,actual,expected)
                sites+=1
            cases+=1
    for p in (3,5):
        for a,b in ((1,1),(3,2)):
            mat=matrix_hamiltonian(p,a,b).astype(complex)
            mat[0,0]-=0.8j
            # Direct non-Hermitian propagation, not using spectral projector sums.
            prop=expm(-1j*mat*500.)
            for x,y in product(range(p),repeat=2):
                survival=float(np.linalg.norm(prop[:,p*x+y])**2)
                assert abs(1-survival-closed_form(p,a,b,x,y))<2e-7
    print('VERIFY_OK prime_sizes=5 rational_coupling_pairs=4 exact_spectrum_groups=20'
          f' Fourier_site_checks={sites} direct_loss_models=4')

if __name__=='__main__':run()
