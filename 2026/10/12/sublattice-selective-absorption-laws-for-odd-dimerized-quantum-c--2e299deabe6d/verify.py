"""Finite numerical and exact-arithmetic cross-checks of the SSH absorption theorem.

Run: python verify.py. Finite checks corroborate, but do not replace, the proof.
"""
from math import gcd, sqrt
from functools import reduce
import numpy as np
from scipy.linalg import expm
from sympy import Poly, symbols


def hamiltonian(m, a, b):
    n = m + 1
    H = np.zeros((2*m+1, 2*m+1), float)
    # A sites precede B sites.
    for j in range(m):
        H[j, n+j] = H[n+j, j] = a
        H[j+1, n+j] = H[n+j, j+1] = b
    return H


def dark_indices(H, monitored, eps=5e-9):
    vals, U = np.linalg.eigh(H)
    selected = [q for q in range(H.shape[0])
                if max(abs(U[s, q]) for s in monitored) < eps]
    return selected, U


def test():
    dims = captures = lossy = exact = trajectories = 0
    for m in range(2, 13):
        n=m+1
        for a,b in [(1.,1.), (1.,2.), (1.,sqrt(2)), (1.,sqrt(3)), (2.,1.)]:
            H=hamiltonian(m,a,b)
            # All single-site loss positions on either sublattice.
            for j in range(2*m+1):
                selected,U=dark_indices(H,[j])
                if j>=n:
                    g=gcd(n,j-n+1)
                    desired=2*g-1
                else:
                    theta=np.arange(1,n)*np.pi/n
                    desired=2*int(np.sum(np.abs(a*np.sin((j+1)*theta)+b*np.sin(j*theta)) < 5e-9))
                assert len(selected)==desired, (m,a,b,j,len(selected),desired)
                dims+=1
            # Joint monitoring, including non-singleton gcd examples.
            sets = [tuple(range(1,m+1)), (1,), (m,), tuple(range(1,m+1,2))]
            if m>=4:
                sets.extend([(2,4), (2,m)])
            for S in sets:
                selected,U=dark_indices(H,[n+j-1 for j in S])
                g=reduce(gcd,(n,*S))
                assert len(selected)==2*g-1
                dims+=1
                for x in range(1,n):
                    dark=sum(abs(U[n+x-1,q])**2 for q in selected)
                    expected = (g/n) if x%g else 0.
                    assert abs(dark-expected)<1e-9,(m,a,b,S,x,dark,expected)
                    captures+=1
            # Direct non-Hermitian eigenvalue classification.
            if m<=5 and (a,b) in [(1.,1.),(1.,sqrt(3))]:
                for pos in [0,1,n,n+min(1,m-1)]:
                    K=H.astype(complex)
                    K[pos,pos]-=0.7j
                    imag=np.linalg.eigvals(K).imag
                    count=int(np.sum(np.abs(imag)<2e-8))
                    desired=len(dark_indices(H,[pos])[0])
                    assert count==desired,(m,a,b,pos,count,desired)
                    assert np.max(imag)<1e-8
                    lossy+=1
    # Exact rational characteristic polynomial of the eleven-site SSH chain,
    # where a=1,b=sqrt(3); the Hamiltonian uses only alternating squared hoppings.
    z=symbols('z')
    diag=[1,3]*5
    P0, P1=Poly(1,z), Poly(z,z)
    allpolys=[P0,P1]
    for q in diag:
        P0,P1=P1,Poly(z,z)*P1-Poly(q,z)*P0
        allpolys.append(P1)
    full=allpolys[11]
    # Deleting A_2 separates the left 2-vertex chain (A_1,B_1)
    # from an 8-vertex right chain beginning at B_2.
    def chain_poly(bond_squares):
        p0,p1=Poly(1,z),Poly(z,z)
        for x in bond_squares:
            p0,p1=p1,Poly(z,z)*p1-Poly(x,z)*p0
        return p1
    minorA2=chain_poly([1])*chain_poly([3,1,3,1,3,1,3])
    assert full.gcd(minorA2)==Poly(z**2-1,z)
    exact+=1
    # Exponential survival converges to projected dark weight in a few examples.
    for m,a,b,pos,origin in [(2,1.,1.,3,0),(3,1.,2.,4,4),(4,1.,sqrt(3),2,3),
                             (5,1.,sqrt(3),1,0)]:
        H=hamiltonian(m,a,b)
        ix,U=dark_indices(H,[pos])
        expected=float(np.sum(np.abs(U[origin,ix])**2))
        K=H.astype(complex)
        K[pos,pos]-=1j
        evolved=expm(-1j*K*2000.)[:,origin]
        observed=float(np.linalg.norm(evolved)**2)
        assert abs(observed-expected)<1e-6,(m,pos,origin,observed,expected)
        trajectories+=1
    print(f'VERIFY_OK spectral_rank_cases={dims} sitewise_capture={captures} '
          f'loss_spectrum={lossy} exact_polynomial={exact} '
          f'finite_time_convergence={trajectories}')


if __name__=='__main__':
    test()
