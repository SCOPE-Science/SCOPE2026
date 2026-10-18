"""Finite-dimensional matrix checks for the flux-moment law."""
import numpy as np
import math

def generator(n, coupling, rates, flux):
    h = np.zeros((n, n), dtype=complex)
    for x in range(n):
        y = (x + 1) % n
        h[x, y] = coupling*np.exp(1j*flux/n)
        h[y, x] = coupling*np.exp(-1j*flux/n)
    m = -1j*(np.kron(np.eye(n),h)-np.kron(h.T,np.eye(n)))
    for x in range(n):
        for y in range(n):
            if x != y:
                m[x+n*y,x+n*y] -= (rates[x]+rates[y])/2
    return m

def predicted(n,j,flux):
    if n%2==0:
        return 4*n*n*(-1)**(n//2)*j**n*(np.cos(flux)-1)
    return -4*n*n*j**(2*n)*(math.comb(2*n,n)-2)*np.sin(flux)**2

checks=0
worst=0.
for n in range(3,9):
    for variant in range(3):
        j = [0.7,1.,1.1][variant]
        rates = [0.15 + 0.04*x*x if variant==1 else 0.8 if variant==0 else (0.3 if x%2 else 1.3) for x in range(n)]
        for flux in [0.47, 1.10, 2.22]:
            z0=generator(n,j,rates,0)
            z1=generator(n,j,rates,flux)
            p0=np.eye(n*n,dtype=complex)
            p1=np.eye(n*n,dtype=complex)
            onset = n if n%2==0 else 2*n
            for k in range(1,onset+1):
                p0=p0@z0; p1=p1@z1
                diff=np.trace(p1-p0)
                expected = 0 if k<onset else predicted(n,j,flux)
                scale=max(1.,abs(expected),np.linalg.norm(p0,'fro'),np.linalg.norm(p1,'fro'))
                rel=abs(diff-expected)/scale
                assert rel<2e-10,(n,variant,flux,k,diff,expected,rel)
                worst=max(worst,rel)
                checks+=1
print('PASS',checks,'moment comparisons, relative error <=',worst)
