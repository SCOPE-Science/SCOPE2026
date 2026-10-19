#!/usr/bin/env python3
"""Exact cyclotomic check of quartic-graph Fourier zeros at three small primes."""
from math import comb

def predicted(a,b,p):
    q=p*p
    return (b%p==0 and a%p!=0) or (b==0 and a!=0)

def exact_zero(a,b,p,power):
    q=p*p
    count=[0]*q
    for x,y in enumerate(power):
        count[(a*x+b*y)%q]+=1
    # Phi_{p^2}(X)=sum_{j=0}^{p-1}X^{jp}.
    # Coefficient test is exact since deg(H)<p^2.
    for r in range(p):
        c=count[r]
        for j in range(1,p):
            if count[r+j*p]!=c:return False
    return True

def run(p):
    q=p*p
    power=[pow(x,4,q) for x in range(q)]
    zero=0
    for a in range(q):
      for b in range(q):
        z=exact_zero(a,b,p,power)
        z0=predicted(a,b,p)
        if z!=z0:
            raise AssertionError((p,a,b,z,z0))
        zero+=int(z)
    countpred=(p-1)*p*p + (p-1) # first term: a unit p*(p-1), b multiple p count p, and a divisible p nonzero p-1,b=0
    assert zero==countpred,(zero,countpred)
    # Construct non-affine spectrum as prescribed, and verify every pair of exponentials is orthogonal.
    beta=lambda r:r*r%p
    lam=[(a,p*beta(a%p)) for a in range(q)]
    assert len(set(lam))==q
    for i in range(q):
      ai,bi=lam[i]
      for j in range(i):
        aj,bj=lam[j]
        a=(ai-aj)%q;b=(bi-bj)%q
        assert predicted(a,b,p)
    # Show non-affine beta for p>=5.
    assert (beta(0)+beta(2)-2*beta(1))%p!=0
    print(f'p={p}, q={q}, tested_Fourier_differences={q*q}, exact_zeros={zero}, nonaffine_basis_verified={q}, predicted_bases={p**(p+1)}')

def moment_witness(p):
    assert p>=5 and p%6==5
    h=(p-5)//6
    r=(h+1)//2
    j=3*r+1
    k=(p-1-j)//3
    assert 0<=k<=j<p-1 and 4*j<2*(p-1)
    assert (j+3*k)==(p-1)
    assert comb(j,k)%p!=0
    for A in range(p):
        for B in range(1,p):
            expected=(-comb(j,k)*pow(B,k,p)*pow(A,j-k,p))%p
            observed=sum(pow((B*pow(x,4,p)+A*x)%p,j,p) for x in range(p))%p
            assert expected==observed,(p,A,B,j,k)
            if A!=0 or j==k:
                assert observed!=0
    return (j,k)

if __name__=='__main__':
 for p in (5,11,17):run(p)
 for p in (5,11,17,23):
    j,k=moment_witness(p)
    print(f'Hermite_moment p={p}, j={j}, k={k}, all_coefficients_checked={p*(p-1)}')
