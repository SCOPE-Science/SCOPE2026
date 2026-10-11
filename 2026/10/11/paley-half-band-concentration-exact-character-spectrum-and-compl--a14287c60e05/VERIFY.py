"""Reproduce quadratic-residue Fourier concentration identities for finite prime tests."""
from math import isqrt
import cmath
import numpy as np

def primes(n):
    for p in range(3,n+1,2):
        if all(p%d for d in range(3,isqrt(p)+1,2)):
            yield p

def legendre(n,p):
    n%=p
    if n==0:return 0
    return 1 if pow(n,(p-1)//2,p)==1 else -1

def check(p):
    h=[x for x in range(1,p) if legendre(x,p)==1]
    m=len(h)
    F=np.exp(2j*np.pi*np.outer(h,h)/p)/np.sqrt(p)
    K=F@F.conj().T
    E=np.array([[legendre(x-y,p) for y in h] for x in h], dtype=float)
    J=np.ones((m,m),dtype=float)
    wanted=.5*np.eye(m)-J/(2*p)+1j*E/(2*np.sqrt(p))
    assert np.max(abs(K-wanted))<1e-12
    assert np.allclose(E@np.ones(m),0,atol=1e-12)
    assert np.allclose(E,-E.T)
    assert np.max(abs(np.linalg.eigvalsh(K)-np.linalg.eigvalsh(wanted)))<1e-12
    g=next(x for x in range(2,p) if len({pow(x,j,p) for j in range(1,p)})==p-1)
    a=pow(g,2,p)
    arr=[pow(a,j,p) for j in range(m)]
    C=[legendre(1-t,p) for t in arr]
    mus=[]
    for k in range(m):
        mu=sum(C[j]*cmath.exp(2j*np.pi*j*k/m) for j in range(m))
        mus.append(mu)
        ev=.5+(1j/(2*np.sqrt(p)))*mu if k else (p+1)/(4*p)
        assert abs(ev.imag)<2e-12
        chi=np.array([cmath.exp(2j*np.pi*j*k/m) for j in range(m)])
        Eordered=np.array([[legendre(x-y,p) for y in arr] for x in arr],dtype=float)
        assert np.max(abs(Eordered@chi-mu*chi))<2e-10
    values=[(p+1)/(4*p)]+[float((.5+1j*mus[k]/(2*np.sqrt(p))).real) for k in range(1,m)]
    assert np.max(abs(np.sort(values)-np.linalg.eigvalsh(K)))<1e-10
    assert all(abs(mus[k]+mus[m-k])<2e-9 for k in range(1,m))
    assert abs(sum((v-.5)**2 for v in values[1:])-m*(m-1)/(4*p))<2e-10
    assert min(values)>-1e-11 and max(values)<1+1e-11
    if m>1 and all(m%d for d in range(2,isqrt(m)+1)):
        assert min(abs(v-.5) for v in values[1:])>1e-8
    return p,m,min(values),max(values)

if __name__=='__main__':
    p_list=[p for p in primes(101) if p%4==3]
    for p in p_list:print(check(p))
    print('VERIFY_OK primes='+str(len(p_list))+' eigenvalue_characters='+str(sum((p-1)//2 for p in p_list))+' Gram_identity=PASS complementary_pairs=PASS centered_moment=PASS safe_prime_gap=PASS')
