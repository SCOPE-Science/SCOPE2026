"""Numerical checks for a finite free mass-spring chain spectral design."""
import numpy as np
from scipy.linalg import eigh
from math import fsum

def design(mass, total_stiffness):
    m = np.asarray(mass,dtype=float)
    n=len(m); pos=np.arange(1,n+1)
    mu=np.dot(m,pos)/sum(m)
    V=np.dot(m,(pos-mu)**2)
    S=np.array([np.dot(m[:i],(mu-pos[:i])) for i in range(1,n)])
    return total_stiffness*S/V,total_stiffness/V,mu,V

def freqs(mass,k):
    n=len(mass);L=np.zeros((n,n))
    for i,v in enumerate(k):
        L[i,i]+=v;L[i+1,i+1]+=v;L[i,i+1]-=v;L[i+1,i]-=v
    return eigh(L, np.diag(mass),eigvals_only=True),L

def run():
    rng=np.random.default_rng(73005); tests=0
    for n in range(2,32):
        for _ in range(80):
            m=np.exp(rng.uniform(-3,3,n));K=np.exp(rng.uniform(-2,2));k,expected,mu,V=design(m,K)
            assert np.all(k>0) and abs(sum(k)-K)<1e-10*K
            ev,L=freqs(m,k)
            assert abs(ev[1]-expected)<(3e-9*expected)
            if n<10:
                for _ in range(4):
                    p=rng.dirichlet(np.ones(n-1))*K
                    ep,_=freqs(m,p)
                    assert ep[1] <= expected*(1+1e-8)
                    tests+=1
            y=np.arange(1,n+1)-mu
            assert np.linalg.norm(L@y-expected*m*y)<1e-8*(1+expected)*np.linalg.norm(m*y)
            tests+=5
    for n in range(2,100):
        m=np.ones(n);K=1.0;k,lam,_,V=design(m,K)
        assert abs(lam -12*K/(n*(n*n-1)))<1e-12
        assert max(abs(k-6*K*np.arange(1,n)*(n-np.arange(1,n))/(n*(n*n-1))))<1e-12
        actual=sum(1/k); expected=(n*n-1)*sum(1/i for i in range(1,n))/(3*K)
        assert abs(actual-expected)<1e-10*expected
        tests+=3
    print('PASS numerical assertion groups',tests)
if __name__=='__main__': run()
