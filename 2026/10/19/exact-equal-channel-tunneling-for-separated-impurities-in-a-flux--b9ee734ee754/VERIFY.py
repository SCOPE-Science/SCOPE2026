"""Independent finite-section and symbolic checks of two-plaquette diamond-chain splitting.

Requires Python 3, numpy, and sympy. Run: python VERIFY.py
The infinite-volume identity is proved in RESULT.md; finite tests are diagnostic.
"""
import numpy as np
import sympy as sp


def infinite_coefficients(flux, separation):
    assert 0 < flux < np.pi and separation >= 2
    r = np.exp(-np.arccosh(1.0 / np.cos(flux / 2.0)))
    h = (1.0 - r*r) * r**(separation-1) / 4.0
    u = np.sqrt(r*r/4.0 + h*h)
    return r, h, np.sort(np.array([0.5 + sign*h + band*u
                                     for sign in (-1, 1) for band in (-1, 1)]))


def physical_finite_chain(N, flux, epsilon, defect_plaquettes):
    """Hermitian matrix and compact zero modes, independently assembled from links."""
    hubs = N + 2
    total = hubs + 2*(N+1)
    H = np.zeros((total,total), dtype=complex)
    Z = np.zeros((total,N), dtype=complex)
    B = lambda p: hubs + 2*(p-1)
    C = lambda p: hubs + 2*(p-1) + 1
    phase = np.exp(-0.5j*flux)
    def hop(i,j,a):
        H[i,j] += a
        H[j,i] += np.conjugate(a)
    for p in range(1,N+2):
        hop(p-1,B(p),phase)
        hop(p-1,C(p),1)
        hop(p,B(p),1)
        hop(p,C(p),phase)
        if p in defect_plaquettes:
            H[B(p),B(p)] += epsilon
            H[C(p),C(p)] += epsilon
    for j in range(1,N+1):
        Z[B(j),j-1] = 0.5
        Z[C(j),j-1] = -phase/2
        Z[B(j+1),j-1] = phase/2
        Z[C(j+1),j-1] = -0.5
    return H,Z


def symbolic_check():
    r,h,x = sp.symbols('r h x', positive=True, real=True)
    aa=(1+r)/2
    bb=(1-r)/2
    M=sp.Matrix([[aa,0,-h,-h], [0,bb,h,h],
                 [-h,h,aa,0], [-h,h,0,bb]])
    expected=((x-sp.Rational(1,2))**2-r*r/4)**2 - \
             4*h*h*(x-sp.Rational(1,2))**2
    assert sp.simplify((x*sp.eye(4)-M).det()-expected)==0
    # Independent symbolic reconstruction of the whitened blocks from
    # the normalized inverse Toeplitz Gram kernel and defect-site Gram blocks.
    k=sp.symbols('k',real=True)
    C=(1+r*r)/(1-r*r)
    Q=sp.Matrix([[1,1],[1,-1]])/sp.sqrt(2)
    D=sp.diag((1+r)/sp.sqrt(2*(1+r*r)),
              (1-r)/sp.sqrt(2*(1+r*r)))
    K0=C*sp.Matrix([[1,-r],[-r,1]])
    Kx=C*k*sp.Matrix([[-r,r*r],[1,-r]])
    A=sp.simplify(D*Q.T*K0*Q*D)
    T=sp.simplify(D*Q.T*Kx*Q*D)
    assert sp.simplify(A-sp.diag(aa,bb))==sp.zeros(2)
    assert sp.simplify(T-k*(1-r*r)*sp.Matrix([[1,1],[-1,-1]])/4)==sp.zeros(2)
    return str(sp.factor(expected))


def finite_checks():
    total=0
    for flux in (np.pi/3, np.pi/2):
        for d in (2,4,7):
            N=72
            p=25
            H0,Z=physical_finite_chain(N,flux,0,(p,p+d))
            assert np.linalg.norm(H0@Z,ord=np.inf)<2e-12
            r,h,values=infinite_coefficients(flux,d)
            gram=Z.conj().T@Z
            expected_s=np.eye(N)+np.diag(np.full(N-1,np.cos(flux/2)/2),1) \
                                    +np.diag(np.full(N-1,np.cos(flux/2)/2),-1)
            assert np.max(np.abs(gram-expected_s))<1e-12
            physical_indices=[N+2+2*(q-1)+offset for q in (p,p+d) for offset in (0,1)]
            T=Z[physical_indices,:].conj().T@Z[physical_indices,:]
            evals,evecs=np.linalg.eigh(gram)
            Sinvhalf=(evecs*evals**(-0.5))@evecs.conj().T
            mu=np.linalg.eigvalsh(Sinvhalf@T@Sinvhalf)
            mu=mu[-4:]
            assert np.max(np.abs(mu-values))<5e-9, (flux,d,mu,values)
            # Full finite physical spectrum: error is O(epsilon**2), not zero.
            for eps in (0.006, 0.001):
                H,Z=physical_finite_chain(N,flux,eps,(p,p+d))
                w=np.linalg.eigvalsh(H)
                states=w[(w>1e-9)&(w<1.1*eps)]
                assert len(states)==4,(flux,d,eps,states)
                # The true finite-chain first-order slopes agree with mu.
                assert np.max(np.abs(states/eps-mu)) < 0.04*eps, (flux,d,eps,states/eps,mu)
                total+=1
    print('Verified %d full finite-chain spectra and six projected four-level spectra.' % total)
    r=np.sqrt(2)-1
    print('Quarter-flux relative coupling at d=8 versus d=6: %.12f' % (r*r))
    assert abs(r*r-(3-2*np.sqrt(2)))<1e-14


if __name__ == '__main__':
    print('Symbolic characteristic polynomial:',symbolic_check())
    finite_checks()
    print('All diagnostic checks passed.')
