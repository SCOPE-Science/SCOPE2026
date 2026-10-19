"""Independent finite-matrix and exact-moment checks for the flux-reset parity theorem.
Run with Python 3, NumPy, SymPy. No network is needed.
"""
from math import comb
import numpy as np
import sympy as sp


def hamiltonian(n, coupling, flux):
    h = np.zeros((n,n),dtype=complex)
    z = np.exp(1j*flux/n)
    for k in range(n):
        h[(k+1)%n,k] = coupling*z
        h[k,(k+1)%n] = coupling/z
    return h


def stationary_site_distribution(n, coupling, rate, flux):
    h=hamiltonian(n,coupling,flux)
    energies, v=np.linalg.eigh(h)
    # Restart to the basis vector 0 after exponential waiting times.
    amplitudes=v*np.conj(v[0,:])[None,:]
    denom=rate+1j*(energies[:,None]-energies[None,:])
    rho=np.zeros((n,n),dtype=complex)
    for a in range(n):
        for b in range(n):
            rho += (rate/denom[a,b])*np.outer(amplitudes[:,a],np.conj(amplitudes[:,b]))
    assert np.max(np.abs(rho-rho.conj().T))<1e-11
    assert abs(np.trace(rho)-1)<1e-11
    return rho.diagonal().real


def exact_powers(n, sign, upto):
    h=sp.zeros(n)
    for k in range(n-1):
        h[k+1,k]=h[k,k+1]=1
    h[0,n-1]=sign*sp.I
    h[n-1,0]=-sign*sp.I
    powers=[sp.eye(n)]
    for _ in range(upto):
        powers.append(powers[-1]*h)
    return powers


def moment(powers, j, order):
    return sp.simplify(sum((-sp.I)**a*sp.I**(order-a)*comb(order,a)*
        powers[a][j,0]*sp.conjugate(powers[order-a][j,0])
        for a in range(order+1)))


def verify_exact_moments():
    tested=0
    for n in range(3,10):
        # The physical flux of this gauge is +pi/2 when sign=+1.
        plus=exact_powers(n,1,n+1)
        minus=exact_powers(n,-1,n+1)
        for j in range(n):
            for k in range(n):
                assert moment(plus,j,k)==moment(minus,j,k),(n,j,k)
                tested+=1
            measured=moment(plus,j,n)-moment(minus,j,n)
            if n%2==0:
                expected=0
            elif j==0:
                expected=0
            else:
                expected=4*(-1)**((n+1)//2+j)*comb(n,j)
            assert measured==expected,(n,j,measured,expected)
            assert moment(plus,j,n+1)==moment(minus,j,n+1),(n,j,'next')
            tested+=2
    return tested


def verify_numerics():
    results=[]
    for n in range(3,10):
        for phi in (0.4,1.1,2.4):
            p=stationary_site_distribution(n,1,9,phi)
            q=stationary_site_distribution(n,1,9,-phi)
            if n%2==0:
                assert np.max(np.abs(p-q))<2e-12
            results.append((n,phi,np.max(np.abs(p-q))))
    for n in (3,5,7):
        for r in (35.,70.):
            phi=0.8
            p=stationary_site_distribution(n,1,r,phi)
            q=stationary_site_distribution(n,1,r,-phi)
            tv=sum(abs(p-q))/2
            leading=2*(2**n-2)*abs(np.sin(phi))/r**n
            assert abs(tv-leading)/leading < 0.08,(n,r,tv,leading)
    return results

if __name__=='__main__':
    print('Exact finite-moment checks:',verify_exact_moments())
    ans=verify_numerics()
    print('Numerical stationary state checks:',len(ans))
    print('Even-ring max reversal discrepancy:',max(x[2] for x in ans if x[0]%2==0))
    print('All checks passed.')
