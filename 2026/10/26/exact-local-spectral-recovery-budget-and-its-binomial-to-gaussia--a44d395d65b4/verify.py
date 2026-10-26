"""Standalone finite-index checks for sorted Lindblad spectral-budget theorem.
Python standard library only; all rates use exact rational arithmetic.
"""
from fractions import Fraction
from itertools import product
from math import comb

def q(r):
    return Fraction(1, 2)+2*r

def analytic_k(n,r):
    v=q(r)
    assert v.denominator!=1 or not (1<=v<=n), 'tie plane excluded'
    if r<Fraction(1,4):
        return 2*n+1
    return 1+sum(comb(n,j) for j in range(1,n+1) if j<v)

def spectral_slopes(n,r):
    # Each entry (decay eigenvalue, d/da, d/db) with gamma1 normalized to 1.
    D=1<<n
    ns=[i.bit_count() for i in range(D)]
    ans=[]
    for i in range(D):
        for j in range(D):
            if i==j==0: continue
            s=ns[i]+ns[j]
            d=(i^j).bit_count()
            ans.append((Fraction(s,2)+2*r*d,Fraction(s,2),2*d))
    ans.sort()
    return ans

def algebraic_rank(prefix):
    a,b=prefix[0][1:]
    return 2 if any(a*y-b*x for _,x,y in prefix[1:]) else 1

number=0
ratios=[Fraction(1,10),Fraction(1,5),Fraction(3,10),Fraction(2,5),Fraction(2,3),Fraction(4,5),Fraction(5,4),Fraction(7,4),Fraction(11,5),Fraction(37,10)]
for n in range(1,9):
    for r in ratios:
        if q(r).denominator==1 and 1<=q(r)<=n: continue
        spec=spectral_slopes(n,r)
        k=analytic_k(n,r)
        assert k<=len(spec)
        assert algebraic_rank(spec[:k])==2,(n,r,k)
        assert algebraic_rank(spec[:k-1])==1,(n,r,k)
        if r>Fraction(1,4):
            assert spec[k-1][0]==q(r),(n,r,k)
            assert all(y==0 for _,_,y in spec[:k-1]),(n,r,k)
        else:
            assert all(z[0]==q(r) for z in spec[:2*n]),(n,r)
            assert spec[2*n][0]==1,(n,r)
        number+=1
print('PASS',number,'exact-rational first-rank checks n=1..8, multiple ratios')
for n in range(3,70):
    worst=max(analytic_k(n, r) for r in (Fraction(1,10),Fraction(1,5),Fraction(3,10),Fraction(3,5),Fraction(5,1),Fraction(10,1)))
    expected=1+sum(comb(n,j) for j in range(1,min(n,20)+1))
    assert worst==expected
    if n<=20: assert worst==2**n
print('PASS 67 exact interval-maximum formulas n=3..69')
for n in (25,100,400,1600):
    from statistics import NormalDist
    z=1
    v=Fraction(n,2)+Fraction(z,2)*int(n**0.5) # exact only for square n
    K=1+sum(comb(n,j) for j in range(1,n+1) if j<v)
    f=K/2**n
    print('Gaussian window',n,'K/2^n=',float(f),'Phi(1)=',NormalDist().cdf(1))

try:
    import numpy as np
except ImportError:
    print('NumPy unavailable: direct superoperator eigenvalue tests skipped')
else:
    for n in (1,2,3):
        D=1<<n
        I=np.eye(D,dtype=complex)
        omega=0.73
        J=0.19
        gamma=0.91
        phi=0.37
        diag=[]
        for i in range(D):
            z=np.array([1-2*((i>>k)&1) for k in range(n)],dtype=float)
            diag.append(omega*z.sum()/2+J*((z.sum()**2-n)/2))
        H=np.diag(diag)
        A=-1j*(np.kron(I,H)-np.kron(H.T,I))
        for k in range(n):
            Z=np.diag([1-2*((i>>k)&1) for i in range(D)]).astype(complex)
            L=np.sqrt(phi)*Z
            LL=L.conj().T@L
            A+=np.kron(L.conj(),L)-0.5*(np.kron(I,LL)+np.kron(LL.T,I))
            L=np.zeros((D,D),dtype=complex)
            for i in range(D):
                if (i>>k)&1: L[i & ~(1<<k),i]=np.sqrt(gamma)
            LL=L.conj().T@L
            A+=np.kron(L.conj(),L)-0.5*(np.kron(I,LL)+np.kron(LL.T,I))
        observed=sorted(np.linalg.eigvals(A).tolist(),key=lambda z:(round(z.real,9),round(z.imag,9)))
        expected=[]
        for i in range(D):
            for j in range(D):
                s=i.bit_count()+j.bit_count()
                h=(i^j).bit_count()
                expected.append(-1j*(diag[i]-diag[j])-gamma*s/2-2*phi*h)
        expected=sorted(expected,key=lambda z:(round(z.real,9),round(z.imag,9)))
        maxerr=max(abs(a-b) for a,b in zip(observed,expected))
        assert maxerr < 1e-8,(n,maxerr)
        print('PASS direct Lindblad superoperator n=',n,'max absolute eigenvalue error',maxerr)
