"""Independent finite-matrix consistency checks for a Schatten commutator factorization identity."""
import numpy as np

def snorm(a, p):
    return np.linalg.norm(np.linalg.svd(a,compute_uv=False),ord=p)

def check():
    count=0
    rng=np.random.default_rng(84762)
    for k in range(1,7):
        for p in (1,1.2,1.5,2,3,5,8):
            q=2*p
            values=0.15+rng.random(k)*2
            d=np.diag(values)
            t=np.zeros((2*k,2*k),dtype=complex);t[:k,k:]=d
            x=np.zeros_like(t);x[:k,k:]=np.diag(np.sqrt(values))
            y=np.zeros_like(t);y[:k,:k]=-np.diag(np.sqrt(values))/2;y[k:,k:]=np.diag(np.sqrt(values))/2
            assert np.linalg.norm(x@y-y@x-t)<1e-12
            claimed=2**(1/q-1)*snorm(t,p)
            assert abs(snorm(x,q)*snorm(y,q)-claimed)<1e-10
            for _ in range(12):
                a=rng.normal(size=t.shape)+1j*rng.normal(size=t.shape)
                b=rng.normal(size=t.shape)+1j*rng.normal(size=t.shape)
                u=(a@b-b@a)[:k,k:]
                lhs=snorm(u,p)
                rhs=2**(1-1/q)*snorm(a,q)*snorm(b,q)
                assert lhs<=rhs+1e-8
                count+=1
    print('PASS',count,'random cross-block commutator inequalities; 42 exact constructive identities')
if __name__=='__main__': check()
