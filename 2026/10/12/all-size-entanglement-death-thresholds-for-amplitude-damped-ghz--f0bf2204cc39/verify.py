"""Independent matrix-channel verification of the two-stage GHZ concurrence law.
Run: python verify.py  (requires numpy)"""
import math
import numpy as np
from math import comb


def ratio(n, m, p, a, b, r):
    q = 1.0-p
    A = (1-p*r)**m * (1-q*r)**(n-m)
    B = (2**(n-1)-2**m)*math.sqrt(A)
    for k in range(m):
        z = (1-p*r)**k * (1-r)**(m-k)
        B += comb(m,k)*math.sqrt(A+(a*a/(b*b*p**k))*z)
    return (b/a)*(p/q)**(m/2)*B


def formula(n,m,p,a,b,r):
    return 2*a*b*((1-p)*r)**(n/2) * max(0.0,1-ratio(n,m,p,a,b,r))


def propagator(n, p, mat):
    size=2**n
    e0=np.diag([1.0,math.sqrt(1-p)]).astype(complex)
    e1=np.array([[0,math.sqrt(p)],[0,0]],complex)
    ident=np.eye(2,dtype=complex)
    for j in range(n):
        out=np.zeros_like(mat)
        for el in (e0,e1):
            full=np.array([[1.+0.j]])
            for k in range(n):
                full=np.kron(full,el if j==k else ident)
            out+=full@mat@full.conj().T
        mat=out
    return mat


def direct(n,m,p,a,b,r):
    size=2**n
    v=np.zeros(size,complex)
    v[0]=a;v[-1]=b
    rho=np.outer(v,v.conj())
    rho=propagator(n,p,rho)
    mask=sum(2**(n-1-j) for j in range(m))
    perm=np.array([u^mask for u in range(size)])
    rho=rho[np.ix_(perm,perm)]
    rho=propagator(n,1-r,rho)
    rho=rho[np.ix_(perm,perm)]
    diagonal=np.real(np.diag(rho))
    s=sum(math.sqrt(max(0.,diagonal[j])*max(0.,diagonal[size-1-j])) for j in range(1,size//2))
    return 2*max(0.,abs(rho[0,-1])-s),rho


def main():
    checks=0
    for n in range(2,7):
        for m in range(1,n):
            for p in (.03,.1,.24,.49,.8):
                for r in (.07,.4,.82,1.):
                    a=math.sqrt(.37);b=math.sqrt(.63)
                    expected=formula(n,m,p,a,b,r)
                    got,rho=direct(n,m,p,a,b,r)
                    assert abs(expected-got)<3e-11,(n,m,p,r,expected,got)
                    assert abs(np.trace(rho)-1)<2e-11
                    assert np.max(np.abs(rho-rho.conj().T))<2e-11
                    checks+=1
            for p in (.01,.14,.51):
                a=b=2**-.5
                rv=[ratio(n,m,p,a,b,j/100) for j in range(101)]
                assert all(rv[j+1]<rv[j] for j in range(100))
                checks+=1
    # Sample showing a qualitative strategy distinction at 5 qubits.
    a=b=2**-.5
    assert ratio(5,1,.03,a,b,0)>1
    assert ratio(5,2,.03,a,b,0)<1
    assert ratio(5,3,.03,a,b,0)<1
    assert ratio(5,4,.03,a,b,0)<1
    # Zero pre-damping: every proper, nonempty mask has identical exact GMC.
    for n in range(2,7):
        for m in range(1,n):
            for r in (.15,.47,.9):
                got,_=direct(n,m,0.,a,b,r)
                assert abs(got-2*a*b*r**(n/2))<2e-11,(n,m,r,got)
                checks+=1
    print('VERIFY_OK',checks)

if __name__=='__main__':
    main()
