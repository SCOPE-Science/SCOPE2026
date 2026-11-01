"""Exact colour-equality moments and independent Fourier Gram checks.

Usage: python3 verify.py. Requires numpy for the finite spectral cross-check.
"""
from fractions import Fraction
from itertools import product
from math import factorial, pi
import cmath
import numpy as np


def stirling(n, k):
    if n == k == 0:
        return 1
    if n <= 0 or k <= 0 or k > n:
        return 0
    return k * stirling(n - 1, k) + stirling(n - 1, k - 1)


def count(r, s, q):
    ans = 0
    for k in range(1, min(q - 1, r) + 1):
        falling = factorial(q) // factorial(q - k)
        ans += falling * stirling(r, k) * (q-k)**s
    return ans


def spectrum(r,s,q):
    Z=count(r,s,q)
    rho_a=Fraction(q * count(r-1,s,q)-Z, (q-1)*Z) if r>1 else Fraction(0)
    rho_b=Fraction(q * count(r,s-1,q)-Z, (q-1)*Z) if s>1 else Fraction(0)
    # rho for singleton sides is unused. The normalized constant-mode entries remain 1.
    a=1+(r-1)*rho_a
    b=1+(s-1)*rho_b
    c_sq=Fraction(r*s, (q-1)**2)
    return rho_a,rho_b, a,b,c_sq


def enumerate_valid(r,s,q):
    return [w for w in product(range(q),repeat=r+s)
            if set(w[:r]).isdisjoint(w[r:])]


def check_one(r,s,q):
    ws=enumerate_valid(r,s,q)
    Z=count(r,s,q)
    assert len(ws)==Z, (r,s,q,Z,len(ws))
    ra,rb,a,b,c2=spectrum(r,s,q)
    checks=0
    for i in range(r+s):
        for j in range(i+1,r+s):
            same=sum(w[i]==w[j] for w in ws)
            if i<r and j<r:
                predicted=Fraction(count(r-1,s,q),Z)
            elif i>=r and j>=r:
                predicted=Fraction(count(r,s-1,q),Z)
            else:
                predicted=Fraction(0)
            assert Fraction(same,Z)==predicted,(r,s,q,i,j,same,predicted)
            checks+=1
    chi=np.array([[cmath.exp(2j*pi*k*w[i]/q) for i in range(r+s) for k in range(1,q)]
                  for w in ws], dtype=np.complex128)
    mat=(chi.conj().T@chi)/Z
    vals=np.linalg.eigvalsh(mat)
    block=[]
    if r>1: block.extend([float(1-ra)]*(r-1))
    if s>1: block.extend([float(1-rb)]*(s-1))
    discr=float((a-b)**2+4*c2)**0.5
    block.extend([(float(a+b)-discr)/2,(float(a+b)+discr)/2])
    expected=np.sort(block*(q-1))
    assert np.max(np.abs(vals-expected))<2e-10,(r,s,q,vals,expected)
    assert vals[0]>1e-10,(r,s,q,vals[0])
    assert np.max(np.abs(chi.mean(axis=0)))<2e-10
    return checks,len(vals),len(ws)


def check():
    comps=0; vals=0; cases=0; words=0
    for q in (3,4,5):
        for r in range(1,4):
            for s in range(1,4):
                if q**(r+s)>30000: continue
                c,v,w=check_one(r,s,q)
                comps+=c;vals+=v; words+=w;cases+=1
    for q in (3,4,5,6,7):
        for r in range(2,8):
            t=Fraction(q-2,q-1)
            for s in (30,60,120):
                ra,rb,a,b,c2=spectrum(r,s,q)
                alpha=1-ra
                approximated=q*2**(r-2)*t**s
                ratio=float(alpha/approximated)
                if s==120:
                    assert 0.99<ratio<1.01,(q,r,s,ratio)
    print('VERIFY_OK cases=%d colour_pairs=%d eigenvalues=%d words=%d asymptotic_cases=%d' % (cases,comps,vals,words,5*6*3))

if __name__=='__main__':check()
