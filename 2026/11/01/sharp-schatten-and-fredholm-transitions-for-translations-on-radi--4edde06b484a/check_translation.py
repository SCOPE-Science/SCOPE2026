"""Finite reproducibility checks for translation operators on radial power Fock Hilbert spaces.
This program tests finite identities and asymptotic trends, not infinite-dimensional theorems.
"""
from math import lgamma, exp, sqrt, isclose
import numpy as np
from scipy.linalg import expm, svdvals


def weights(m, alpha, n):
    j = np.arange(1, n, dtype=float)
    out = np.zeros(n)
    out[1:] = j * np.exp((np.log(alpha) / m) + 0.5 *
        np.array([lgamma(2*k/m)-lgamma((2*k+2)/m) for k in j]))
    return out

checks = 0
for m, alpha in [(0.4,1.0), (0.5,1.0),(0.75,1.2),(0.9,2.0)]:
    beta = 1/m-1
    c = (alpha*m/2)**(1/m)
    w = weights(m,alpha,1200)
    for n in [30,100,300,900]:
        val = w[n] * n**beta / c
        # asymptotic check with graded tolerance from gamma-ratio expansion
        assert abs(val-1) < 12.0/n, (m,n,val)
        checks += 1
    # exact shift powers in a finite model, first-order translation matrix coefficients
    n=76
    D=np.zeros((n,n))
    w=weights(m,alpha,n)
    D[np.arange(n-1),np.arange(1,n)]=w[1:]
    b=0.65
    T=expm(b*D)-np.eye(n)
    assert np.max(np.abs(T[np.tril_indices(n,-1)]))<1e-12
    assert np.max(np.abs(np.diag(T,1)-b*w[1:]))<1e-12
    assert np.max(np.abs(np.diag(T,2)-(b*b/2)*w[1:-1]*w[2:]))<1e-12
    checks+=3
    # nonzero singular values are ordered asymptotically like those of bD
    singular=svdvals(T)
    assert singular[0]>0 and singular[-1]<1e-10
    checks+=1

m=1.0
for alpha in [0.8,1.0,2.2]:
    w=weights(m,alpha,501)
    R=alpha/2
    for n in [1,2,10,100,499]:
        assert isclose(w[n], R*sqrt(2*n/(2*n+1)), rel_tol=3e-11)
        assert w[n]<R
        checks+=2
    assert all(w[i]<w[i+1] for i in range(1,400))
    checks+=1

# spectral-folding algebra: count roots of exp(bz)=1 strictly inside |z|<alpha/2
for alpha in [1.0, 2.0]:
    for b in [0.3,4.0, 4*np.pi/alpha, (4*np.pi+0.1)/alpha,12*np.pi/alpha]:
        radius=alpha/2
        count=sum(abs(2*np.pi*k/b)<radius-1e-12 for k in range(-30,31))
        predicted=2*int(np.ceil(alpha*b/(4*np.pi)-1e-12))-1
        assert count==predicted,(alpha,b,count,predicted)
        checks+=1

print(f'PASS finite checks={checks}; exact finite matrix coefficients, gamma asymptotics, critical shift weights, resonance counts')
