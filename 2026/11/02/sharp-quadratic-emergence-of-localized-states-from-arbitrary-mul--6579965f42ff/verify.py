"""Independent checks of multi-impurity tight-binding thresholds.

Usage: python verify.py
Requires numpy and scipy.
"""
import numpy as np
from scipy.linalg import eigh_tridiagonal
from scipy.optimize import brentq


def path_laplacian(sites, J):
    m = len(sites)
    out = np.zeros((m,m),float)
    for i, gap in enumerate(np.diff(sites)):
        w = J / float(gap)
        out[i,i] += w
        out[i+1,i+1] += w
        out[i,i+1] -= w
        out[i+1,i] -= w
    return out


def inverse_green(sites, J, k):
    """Exact precision form of compressed free resolvent at E=2J cosh(k)."""
    m=len(sites)
    out=np.zeros((m,m),float)
    h=2*J*np.sinh(k)
    out[0,0]=h
    for i,d in enumerate(np.diff(sites)):
        r=np.exp(-float(d)*k)
        alpha=h/(-np.expm1(-2*float(d)*k))
        out[i,i]+=alpha*r*r
        out[i+1,i+1]+=alpha
        out[i,i+1]-=alpha*r
        out[i+1,i]-=alpha*r
    return out


def green_direct(sites,J,k):
    d=np.abs(np.subtract.outer(sites,sites))
    return np.exp(-k*d)/(2*J*np.sinh(k))


def roots_above_band(sites,J,V):
    nu=np.linalg.eigvalsh(path_laplacian(sites,J))
    roots=[]
    for j,c in enumerate(nu):
        if V <= c + 1e-11: continue
        def f(k): return np.linalg.eigvalsh(inverse_green(sites,J,k))[j]-V
        hi=1.0
        while f(hi)<0: hi*=2
        k=brentq(f,1e-9,hi,xtol=4e-14)
        roots.append((j,2*J*np.cosh(k)))
    return roots


def finite_chain_eigs(sites,J,V,R=230):
    x=np.arange(sites[0]-R,sites[-1]+R+1)
    d=np.zeros(len(x))
    for s in sites:
        d[s-x[0]]=V
    eig=eigh_tridiagonal(d,np.full(len(x)-1,J),eigvals_only=True)
    return eig[eig>2*J+1e-8]


def run():
    rng=np.random.default_rng(126751)
    max_inversion=0
    max_theory=0
    checked=0
    random_cases=0
    min_gap=1e9
    birth_checks=0
    # Tests of precision inverse, Laplacian limit, birth constants,
    # and finite-chain eigenvalues for randomly placed impurities.
    for m in range(4,9):
        for rep in range(9):
            gaps=rng.integers(1,7,size=m-1)
            sites=np.r_[0,np.cumsum(gaps)]
            J=float(rng.choice([0.75,1,1.6]))
            L=path_laplacian(sites,J)
            nu,U=np.linalg.eigh(L)
            min_gap=min(min_gap,float(np.min(np.diff(nu))))
            for k in [0.02,0.17,0.81,1.67]:
                Q=inverse_green(sites,J,k)
                err=np.max(np.abs(Q@green_direct(sites,J,k)-np.eye(m)))
                max_inversion=max(max_inversion,float(err))
                assert err<1.5e-11,(sites,err)
                checked+=1
            # First-order coefficient of Q(k) at k=0.
            k=3e-5
            B=np.zeros((m,m));B[0,0]=J;B[-1,-1]=J
            err=np.max(np.abs((inverse_green(sites,J,k)-L)/k-B))
            assert err < 0.002,(sites,err)
            # Birth energy limits from exact finite m secular matrix.
            for j in range(1,m):
                b=float(U[0,j]**2+U[-1,j]**2)
                theoretical=1/(J*b*b)
                if b < 0.1: continue
                delta=0.000002*min(1.,float(np.min(np.diff(nu))))*b
                V=float(nu[j]+delta)
                f=lambda kap: np.linalg.eigvalsh(inverse_green(sites,J,kap))[j]-V
                kroot=brentq(f,1e-11,1.0,xtol=1e-14)
                observed=(4*J*np.sinh(kroot/2)**2)/(delta*delta)
                relerr=abs(observed/theoretical-1)
                max_theory=max(max_theory,float(relerr))
                assert relerr < 0.015,(sites,j,theoretical,observed,relerr)
                birth_checks+=1
            for j in [0,m//2,m-1]:
                # V midpoint between adjacent thresholds, or above largest.
                V=nu[-1]+0.9*J if j==m-1 else (nu[j]+nu[j+1])/2
                roots=roots_above_band(sites,J,V)
                expected=int(np.count_nonzero(nu<V))
                assert len(roots)==expected
                eigs=finite_chain_eigs(sites,J,V,R=180)
                assert len(eigs)==expected, (sites,V,expected,len(eigs))
                diff=float(np.max(np.abs(np.sort([z[1] for z in roots])-eigs)))
                assert diff < 2e-6,(sites,V,diff)
                random_cases+=1
    # Equal-spacing formula for all m=4..16 and d=1..8.
    equal_cases=0
    for m in range(4,17):
        for d in range(1,9):
            sites=np.arange(m)*d
            nu,U=np.linalg.eigh(path_laplacian(sites,1.3))
            exact=np.array([2*1.3/d*(1-np.cos(j*np.pi/m)) for j in range(m)])
            assert np.max(np.abs(nu-exact))<2e-14
            for j in range(1,m):
                expected=4/m*np.cos(j*np.pi/(2*m))**2
                assert abs((U[0,j]**2+U[-1,j]**2)-expected)<1e-13
            equal_cases+=1
    print('PASS inverse-Green identity:',checked,'matrix instances; maximum residual',f'{max_inversion:.3e}')
    print('PASS random geometries:',random_cases,'independent finite-chain spectral comparisons')
    print('PASS threshold birth:',birth_checks,'local tests; maximum relative asymptotic discrepancy at finite delta',f'{max_theory:.3e}')
    print('PASS equally spaced thresholds and coefficients:',equal_cases,'geometry instances')
    print('Minimum encountered nonzero threshold spacing:',f'{min_gap:.5e}')
    sample=[0,2,5,9]
    J=1
    nu,U=np.linalg.eigh(path_laplacian(sample,J))
    print('Example s=(0,2,5,9), J=1: thresholds',','.join(f'{x:.10f}' for x in nu[1:]))
    print('Example quadratic coefficients',','.join(f'{1/(J*(U[0,j]**2+U[-1,j]**2)**2):.8f}' for j in range(1,len(sample))))

if __name__=='__main__': run()
