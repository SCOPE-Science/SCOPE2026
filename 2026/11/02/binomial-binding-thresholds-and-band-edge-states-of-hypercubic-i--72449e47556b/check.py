"""Numerical checks for a finite hypercubic impurity array (non-certifying)."""
from itertools import product
from math import comb
import numpy as np
from scipy.integrate import quad
from scipy.special import ive
from scipy.optimize import brentq
from scipy.sparse import diags, eye, kron
from scipy.sparse.linalg import eigsh


def threshold_eigenvalue(d, ell, k, E=None):
    """Independent Bessel-heat-kernel representation of the sector eigenvalue."""
    delta=0.0 if E is None else E-2*d
    assert d>=3 and ell>=1 and 0<=k<=d and delta>=0
    def f(t):
        a=ive(0,2*t)
        b=ive(ell,2*t)
        return np.exp(-delta*t)*(a+b)**(d-k)*(a-b)**k
    return quad(f,0,np.inf,epsabs=1.5e-11,epsrel=1.5e-11,limit=350)[0]


def torus_sector(d, ell, k, E, n=56):
    """Brillouin-zone trapezoid quadrature, independent of modified Bessel functions."""
    x=2*np.pi*np.arange(n)/n
    freq=2*np.cos(x)
    shape=(n,)*d
    den=np.full(shape,E)
    numerator=np.ones(shape)
    for j in range(d):
        sl=[None]*d;sl[j]=slice(None)
        den=den-freq[tuple(sl)]
        numerator=numerator*(1+(-1 if j<k else 1)*np.cos(ell*x))[tuple(sl)]
    return float(np.mean(numerator/den))


def periodic_adjacency(L,d=3):
    # tensor-product torus. These are *not* used in the mathematical proof.
    from scipy.sparse import csr_matrix
    I=eye(L,format='csr')
    A=diags([np.ones(L-1),np.ones(L-1)],[1,-1],shape=(L,L),format='lil')
    A[0,L-1]=1; A[L-1,0]=1; A=A.tocsr()
    result=None
    for j in range(d):
        M=None
        for i in range(d):M=(I if i!=j else A) if M is None else kron(M,I if i!=j else A,format='csr')
        result=M if result is None else result+M
    return result


def run():
    checks=0
    for d in (3,4,5):
        for ell in (1,2,3):
            vals=[threshold_eigenvalue(d,ell,k) for k in range(d+1)]
            assert all(vals[k]>vals[k+1]>0 for k in range(d))
            checks+=d
            if ell==1:
                assert abs(vals[1]-(d-2)*vals[0]/d)<2e-10
                checks+=1
    for ell in (1,2,3):
        for k in range(4):
            for E in (6.5,7.0,8.0):
                s=threshold_eigenvalue(3,ell,k,E)
                t=torus_sector(3,ell,k,E,n=56)
                assert abs(s-t)<1e-10,(ell,k,E,s,t)
                checks+=1
    L=14; A=periodic_adjacency(L,3).tolil()
    positions=list(product(range(2),repeat=3))
    def flat(pos):return (pos[0]*L+pos[1])*L+pos[2]
    for coupling,expected in ((3,1),(5,4),(7,7),(10,8)):
        H=A.copy()
        for pos in positions:H[flat(pos),flat(pos)]+=coupling
        eigs=np.sort(eigsh(H.tocsr(),k=18,which='LA',ncv=80,return_eigenvectors=False,tol=3e-10))
        observed=int(np.count_nonzero(eigs>6.12))
        assert observed==expected,(coupling,expected,observed,eigs)
        checks+=1
    print('PASS',checks,'checks: Bessel-sector monotonicity, exact adjacent-corner ratio, independent torus quadrature, finite periodic Hamiltonian comparisons')
    for k in range(4):
        v=threshold_eigenvalue(3,1,k)
        print('3D unit cube sector',k,'multiplicity',comb(3,k),'threshold',format(1/v,'.12f'))

if __name__=='__main__':run()
