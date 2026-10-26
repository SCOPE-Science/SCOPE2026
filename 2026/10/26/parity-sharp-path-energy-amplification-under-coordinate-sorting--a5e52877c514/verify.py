"""Finite-dimensional checks for path sorting energy amplification.
Requires numpy and scipy. No finite test substitutes for the all-dimensional proof.
"""
import itertools
import math
import numpy as np
from scipy.linalg import eigh


def path_laplacian(n):
    d = np.zeros((n-1,n))
    for j in range(n-1):
        d[j,j] = -1
        d[j,j+1] = 1
    return d.T@d

def perm_modulus(n,perm):
    L=path_laplacian(n)
    P=np.eye(n)[list(perm)]
    basis=np.eye(n)[:,1:]-np.eye(n)[:,[0]]
    a=basis.T@P.T@L@P@basis
    b=basis.T@L@basis
    return math.sqrt(max(eigh(a,b,eigvals_only=True)))

def verify():
    cases=0
    for n in range(2,8):
        theta=math.pi/(2*n)
        u=np.cos((np.arange(n)+0.5)*math.pi/n)
        v=(-1.)**np.arange(n)*np.sin((np.arange(n)+0.5)*math.pi/n)
        L=path_laplacian(n)
        lamlo=4*math.sin(theta)**2
        lamhi=4*math.cos(theta)**2
        assert np.max(np.abs(L@u-lamlo*u))<1e-12
        assert np.max(np.abs(L@v-lamhi*v))<1e-12
        if n%2==0:
            assert np.max(np.abs(np.sort(u)-np.sort(v)))<1e-12
        else:
            assert sum(abs(w)<1e-13 for w in u)==1
            assert min(abs(w) for w in v)>1e-13
            assert np.max(np.abs(np.sort(u)-np.sort(v))) <= theta+1e-12
        vals=[perm_modulus(n,p) for p in itertools.permutations(range(n))]
        largest=max(vals)
        assert largest <= 1/math.tan(theta)+1e-10
        if n%2==0: assert abs(largest-1/math.tan(theta))<1e-9
        else:
            assert largest < 1/math.tan(theta)-1e-7
            lower=1/math.tan(theta)*math.sqrt(1-2*theta*theta)
            assert largest>=lower-1e-9
        print(f'n={n}: exact finite permutation maximum={largest:.14f} spectral ceiling={1/math.tan(theta):.14f}')
        cases+=len(vals)+7
    rng=np.random.default_rng(2861)
    for n in range(2,28):
        L=path_laplacian(n)
        for rep in range(15):
            x=rng.normal(size=n)
            sx=np.sort(x)
            assert sx@L@sx <= x@L@x+1e-10
            cases+=1
    print(f'PASS: {cases} independent finite checks')

if __name__=='__main__': verify()
