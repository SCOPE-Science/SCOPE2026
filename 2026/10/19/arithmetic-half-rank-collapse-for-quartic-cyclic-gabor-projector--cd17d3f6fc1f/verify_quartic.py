#!/usr/bin/env python3
"""Exact prime/prime-square cyclotomic checks and independent Fourier-Gram test."""
import math
from collections import Counter


def prime_zero_expected(p, h, w):
    if h == 0:
        return w != 0
    return p % 3 == 2 and w == pow(h, 3, p)


def square_zero_expected(p, h, w):
    if h == 0:
        return w != 0
    if h % p == 0:
        return w % p != 0 or (p % 3 == 2 and w == 0)
    rhs = ((w - h*h*h) * pow(12*h, -1, p)) % p
    return rhs not in {x*x % p for x in range(p)}


def exact_zero(p, k, h, w):
    n = p**k
    counts = [0]*n
    for t in range(n):
        residue = (pow(t+h, 4, n)-pow(t, 4, n)-w*t) % n
        counts[residue] += 1
    if k == 1:
        # Phi_p(T)=1+T+...+T^(p-1)
        return all(a == counts[0] for a in counts)
    if k == 2:
        # Phi_(p^2)(T)=1+T^p+...+T^((p-1)p)
        return all(counts[r+p*j] == counts[r] for r in range(p) for j in range(1, p))
    raise ValueError('Only prime and prime-square dimensions are checked.')


def predicted_rank(p, k):
    if k == 1:
        return p*p - (p-1) * (1 + int(p % 3 == 2))
    return (1 + (p-1)*(p - int(p % 3 == 2))
            + (p*p-p)*p*(p+1)//2)


def exact_census(p, k):
    n = p**k
    nonzero = 0
    for h in range(n):
        for w in range(n):
            expected = (prime_zero_expected(p,h,w) if k == 1
                        else square_zero_expected(p,h,w))
            actual = exact_zero(p,k,h,w)
            assert actual == expected, (p,k,h,w,actual,expected)
            if not actual:
                nonzero += 1
    assert nonzero == predicted_rank(p,k), (p,k,nonzero,predicted_rank(p,k))
    print(f'EXACT p={p} exponent={k}: rank={nonzero}, nullity={n*n-nonzero}, {n*n} cells checked')


def fourier_gram_test(p, k):
    import numpy as np
    n=p**k
    t=np.arange(n, dtype=np.int64)
    g=np.exp(2j*np.pi*np.mod(t**4,n)/n) / np.sqrt(n)
    a=np.empty((n,n),dtype=complex)
    for h in range(n):
        a[h,:]=np.fft.fft(g[np.mod(t+h,n)]*np.conj(g))
    kernel=np.abs(a)**2
    eigen=np.fft.fft2(kernel).ravel()
    target=(n*kernel).ravel()
    err=np.max(np.abs(np.sort(eigen.real)-np.sort(target)))
    imerr=np.max(np.abs(eigen.imag))
    assert err < 1e-9 and imerr < 1e-9, (err,imerr)
    assert abs(kernel[0,0]-1)<1e-10
    # Direct Gram diagonalization in the prime case, not merely FFT agreement.
    if k==1:
        vectors=np.stack([np.roll(g,h)*np.exp(2j*np.pi*w*t/n)
                          for h in range(n) for w in range(n)])
        gram=np.abs(vectors @ np.conjugate(vectors.T))**2
        vals=np.linalg.eigvalsh(gram)
        err2=np.max(np.abs(np.sort(vals)-np.sort(target)))
        assert err2<1e-9,err2
        print(f'DIRECT GRAM p={p}: max eig discrepancy {err2:.3g}')
    print(f'FOURIER GRAM p={p} exponent={k}: max discrepancy {err:.3g}, imaginary {imerr:.3g}')


if __name__ == '__main__':
    for pp in (5,7,11,13):
        exact_census(pp,1)
        exact_census(pp,2)
    for pp,kk in ((5,1),(7,1),(5,2),(7,2)):
        fourier_gram_test(pp,kk)
    print('PASS: all prime and prime-square exact cyclotomic and Gram tests')
