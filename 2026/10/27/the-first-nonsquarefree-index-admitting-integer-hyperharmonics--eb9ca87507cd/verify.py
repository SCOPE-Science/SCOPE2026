"""Reproducible exact arithmetic for integral hyperharmonics at index 45.

No floating point, symbolic packages, or external data needed.
"""
from fractions import Fraction
from math import comb, factorial, gcd

INDEX = 45
PERIOD = factorial(INDEX)
RESIDUE = 68700053771933018729983527085685223542008840099658203156
LOCAL = [(2,41,20),(3,21,19),(5,10,31),(7,6,1),
         (11,4,11),(13,3,8),(17,2,7),(19,2,13),
         (23,1,2),(29,1,14),(31,1,18),(37,1,30),
         (41,1,38),(43,1,42)]

def derivative_rising(r, n, mod=None):
    """Derivative of product (x+j), 0<=j<n, evaluated at integer x=r."""
    prefix = [1]
    for j in range(n):
        a = prefix[-1] * (r+j)
        prefix.append(a if mod is None else a % mod)
    suffix = 1
    total = 0
    for j in range(n-1,-1,-1):
        v = prefix[j] * suffix
        total += v
        if mod is not None:
            total %= mod
        suffix *= r+j
        if mod is not None:
            suffix %= mod
    return total if mod is None else total % mod

def primes_upto(n):
    out=[]
    for p in range(2,n+1):
        if all(p%q for q in out if q*q<=p):
            out.append(p)
    return out

def valuation_factorial(n,p):
    result=0
    while n:
        n//=p
        result+=n
    return result

def independent_exact_h(r, n=INDEX):
    return comb(r+n-1,n)*sum((Fraction(1,k) for k in range(r,r+n)),Fraction(0))

def run():
    assert primes_upto(INDEX) == [p for p,_,_ in LOCAL]
    modprod=1
    for p,e,t in LOCAL:
        modulus=p**e
        assert valuation_factorial(INDEX,p)==e
        assert derivative_rising(t, INDEX, modulus)==0, (p,e,t)
        assert RESIDUE % modulus == t % modulus, (p,e,t)
        assert gcd(modprod,modulus)==1
        modprod*=modulus
    assert modprod == PERIOD
    assert 0 < RESIDUE < PERIOD
    assert derivative_rising(RESIDUE,INDEX,PERIOD)==0
    # Independent exact rational binomial/harmonic evaluation at 3 distant orders.
    for k in (0,1,2):
        r=RESIDUE+k*PERIOD
        h=independent_exact_h(r)
        assert h.denominator==1,(k,h.denominator)
        # An independently calculated exact derivative must recover h*n!.
        assert derivative_rising(r,INDEX)==h.numerator*PERIOD
    # Classify all nonsquarefree indices below the exhibited 45.
    squareful_below=[]
    for n in range(2,INDEX):
        if any(n%(d*d)==0 for d in range(2,n+1) if d*d<=n):
            squareful_below.append(n)
            if n%2:
                assert any(n==p**k for p in primes_upto(n) for k in range(2,8))
    assert 45%9==0 and 45%5==0
    print('VERIFY_OK: 14 exact prime-power derivative zeros; CRT modulus=45!; three independent direct hyperharmonic integers; every nonsquarefree n<45 is even or an odd prime power.')

if __name__=='__main__': run()
