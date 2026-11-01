#!/usr/bin/env python3
"""Exact cyclotomic verification of the prime-square quadratic-cone Fourier law.

No floating-point arithmetic or nonstandard packages are used.  This is a
finite check for p=3,5, not a substitute for the all-prime proof.
"""
from itertools import product


def legendre(t,p):
    t%=p
    if t==0:return 0
    return 1 if pow(t,(p-1)//2,p)==1 else -1


def predicted(p,u,v,w):
    n=p*p
    Delta=(u*u+4*v*w)%n
    if u==v==w==0:return p**4+p**3-p*p
    if u%p==v%p==w%p==0:
        D1=((u//p)**2+4*(v//p)*(w//p))%p
        return p*p*(p-1)+p**3*legendre(D1,p)
    if Delta%p:return 0
    if Delta:return -p*p
    return p*p*(p-1)


def check(p):
    n=p*p
    C=[(a,b,c) for a,b,c in product(range(n),repeat=3) if (a*a+b*c)%n==0]
    assert len(C)==p**4+p**3-p*p
    hist={}
    for u,v,w in product(range(n),repeat=3):
        value=predicted(p,u,v,w)
        hist[value]=hist.get(value,0)+1
        coefficients=[0]*n
        for a,b,c in C:
            coefficients[(u*a+v*b+w*c)%n]+=1
        # P(z)-value is a multiple of Phi_{p^2}(z)=1+z^p+...+z^{(p-1)p}
        # iff all p coefficients in each congruence class mod p agree.
        coefficients[0]-=value
        for residue in range(p):
            t=coefficients[residue]
            assert all(coefficients[residue+j*p]==t for j in range(1,p)),(p,u,v,w,value)
    predicted_counts={
        p**4+p**3-p*p:1,
        p*p*(p-1):p**4-1,
        p*p*(2*p-1):p*(p*p-1)//2,
        -p*p: p*(p-1)**2//2 + p*p*(p-1)*(p*p-1),
        0:p**6-p**5,
    }
    assert hist==predicted_counts, (hist,predicted_counts)
    assert sum(hist.values())==p**6
    assert sum(k*v for k,v in hist.items())==p**6
    print('EXACT_QUADRATIC_CONE_P2_OK', 'p='+str(p), 'vertices='+str(p**6),
          'cone='+str(len(C)), 'rank='+str(sum(v for k,v in hist.items() if k)),
          'spectrum='+repr(sorted(hist.items())))


if __name__=='__main__':
    for p in (3,5):check(p)
