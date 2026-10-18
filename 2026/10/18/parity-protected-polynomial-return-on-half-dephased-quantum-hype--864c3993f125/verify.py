"""Direct numerical crosschecks for parity-selective dephasing on hypercubes.
Run: python verify.py  (needs numpy and scipy)."""
import math
import numpy as np
from scipy.linalg import null_space
from scipy.sparse import csr_matrix, kron, identity
from scipy.sparse.linalg import expm_multiply


def construction(d, gamma=0.8):
    n = 1 << d
    even = [i for i in range(n) if i.bit_count() % 2 == 0]
    odd = [i for i in range(n) if i.bit_count() % 2 == 1]
    h = np.zeros((n,n))
    for i in range(n):
        for bit in range(d):
            h[i,i^(1<<bit)] = 1
    t = h[np.ix_(even,odd)]
    nd = null_space(t, rcond=1e-11)
    w = np.zeros((n,nd.shape[1]));w[odd,:] = nd
    dark = w @ w.T
    bright = np.eye(n)-dark
    # Column-major vectorization convention: vec(A rho B)=(B.T ⊗ A)vec(rho)
    ident = identity(n, dtype=complex,format='csr')
    hsp = csr_matrix(h)
    liouv = -1j*(kron(ident,hsp)-kron(hsp,ident))
    for e in even:
        p = csr_matrix(([1.0],([e],[e])),shape=(n,n))
        rate=gamma*(1+0.2*e/(n-1))
        liouv += rate*(kron(p,p)-0.5*(kron(ident,p)+kron(p,ident)))
    return h,liouv,dark,bright,even,odd


def main():
    for d in range(1,7):
        h,L,D,B,even,odd=construction(d)
        n=1<<d
        k=math.comb(d,d//2)//2 if d%2 == 0 else 0
        assert abs(np.trace(D)-k)<1e-8, ('nullity',d,np.trace(D),k)
        assert np.max(abs(h@D))<1e-8
        assert np.max(abs(D@D-D))<1e-8
        if d %2 == 0:
            p=math.comb(d,d//2)/n
            assert abs(D[odd[0],odd[0]]-p)<1e-9
            assert np.max(abs(np.diag(D)[odd]-p))<1e-8
            assert np.max(abs(np.diag(D)[even]))<1e-8
            return_inf=p*p+(1-p)**2/(n-k)
        else:
            p=0.0
            return_inf=1/n
        # Verify proposed limit is truly stationary and trace preserving.
        v=odd[0]; state=np.zeros((n,n),complex);state[v,v]=1
        limit=D@state@D+(1-p)/(n-k)*B
        assert abs(np.trace(limit)-1)<1e-9
        assert np.max(abs(L @ limit.reshape(-1,order='F')))<1e-8
        assert abs(limit[v,v]-return_inf)<1e-8
        if d<=4:
            # Evolve both a basis state and a deliberately coherent random pure state.
            rng=np.random.default_rng(217+d)
            z=rng.normal(size=n)+1j*rng.normal(size=n)
            z=z/np.linalg.norm(z)
            pure=np.outer(z,z.conj())
            for original, expected in [(state,limit),
                 (pure,D@pure@D+np.trace(B@pure)/(n-k)*B)]:
                evolved=expm_multiply(L*500,original.reshape(-1,order='F'))
                deviation=np.linalg.norm(evolved-expected.reshape(-1,order='F'))
                assert deviation < 2e-6,(d,deviation)
        print('PASS dimension',d,'dark',k,'odd survival',round(p,12),'return',round(return_inf,12))
    # Probability law demonstrates polynomial, not exponential, return.
    for d in (20,40,100,200):
        k=math.comb(d,d//2)//2
        p=math.comb(d,d//2)/(1<<d)
        exact=p*p+(1-p)**2/((1<<d)-k)
        asym=2/(math.pi*d)
        print('asymptotic',d,round(exact/asym,8))

if __name__=='__main__':main()
