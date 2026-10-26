"""Finite-dimensional independent numerical checks for weak-dephasing absorption on cycles.

Requires Python 3, NumPy and SciPy. This is a finite-dimensional sanity check,
not a substitute for the exact spectral perturbation proof in RESULT.md.
"""
import numpy as np
from scipy.linalg import solve

def cycle_h(n):
    h=np.zeros((n,n),dtype=complex)
    for x in range(n):
        h[x,(x+1)%n]=1
        h[(x+1)%n,x]=1
    return h

def odd_projector(n):
    r=np.zeros((n,n),dtype=complex)
    for x in range(n):
        r[x,(-x)%n]=1
    return (np.eye(n)-r)/2

def matrices(n,gamma):
    h=cycle_h(n)
    p=np.zeros((n,n),complex);p[0,0]=1
    eye=np.eye(n)
    l0=-1j*(np.kron(eye,h)-np.kron(h.T,eye))-gamma*(np.kron(eye,p)+np.kron(p.T,eye))
    dl=np.zeros((n*n,n*n),complex)
    for a in range(n):
        for b in range(n):
            if a!=b:dl[a+n*b,a+n*b]=-1.
    return l0,dl

def mean_lifetime(l0,dl,kappa,rho):
    n=rho.shape[0]
    integral=solve(-(l0+kappa*dl),rho.reshape(n*n,order='F'),assume_a='gen')
    return np.trace(integral.reshape(n,n,order='F')).real

def check():
    count=0
    rng=np.random.default_rng(20261020)
    for n in range(3,11):
        h=cycle_h(n);q=odd_projector(n)
        assert np.allclose(q@q,q) and np.allclose(h@q,q@h)
        assert np.allclose(q[:,0],0)
        assert np.allclose(q.diagonal().real,[0 if (x==0 or n%2==0 and x==n//2) else 0.5 for x in range(n)])
        count+=4
        # Nonzero dark mode count equals the spectral bright kernel from cyclic Krylov rank.
        p=np.eye(n)[:,0]
        ky=np.column_stack([np.linalg.matrix_power(h,j)@p for j in range(n)])
        assert np.linalg.matrix_rank(ky,tol=1e-7)==n-round(np.trace(q).real)
        count+=1
        for gamma in (0.35,1.3,3.):
            l0,dl=matrices(n,gamma)
            for a in range(n):
                rho=np.zeros((n,n),complex);rho[a,a]=1
                target=2*np.trace(q@rho).real
                vals=[rate*mean_lifetime(l0,dl,rate,rho) for rate in (1e-3,2e-4)]
                # Linear extrapolation in the dephasing strength eliminates the leading O(rate) term.
                extrap=(5*vals[1]-vals[0])/4
                assert abs(extrap-target)<0.003,(n,gamma,a,extrap,target)
                count+=1
            v=rng.normal(size=n)+1j*rng.normal(size=n)
            v/=np.linalg.norm(v)
            rho=np.outer(v,v.conj())
            target=2*np.trace(q@rho).real
            vals=[rate*mean_lifetime(l0,dl,rate,rho) for rate in (1e-3,2e-4)]
            extrap=(5*vals[1]-vals[0])/4
            assert abs(extrap-target)<0.003,(n,gamma,'coherent',extrap,target)
            count+=1
    print('PASS finite cross-checks:',count)

if __name__=='__main__':
    check()
