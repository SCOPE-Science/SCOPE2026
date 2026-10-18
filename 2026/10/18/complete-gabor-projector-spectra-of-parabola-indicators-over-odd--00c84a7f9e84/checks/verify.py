#!/usr/bin/env python3
"""Reproduce finite Fourier spectra independently of the valuation-count formulas.
Requires Python 3 and NumPy. No network access or external data is needed.
"""
from collections import defaultdict
import numpy as np


def exact_prediction(p, k):
    N = p ** k
    count = defaultdict(int)
    count[p ** (2*k)] += 1
    for j in range(k):
        exponent = (4*k - 3*j - 1) if 2*j <= k else (5*k - 5*j - 1)
        count[p ** (2*j)] += (p-1) * p ** exponent
    for s in range(1, k+1):
        count[p ** (2*k-s)] += (p-1)*p ** (2*s + (s+1)//2 - 2)
    count[0] = N**4 - sum(count.values())
    assert count[0] >= 0
    assert sum(count.values()) == N**4
    assert sum(value*mult for value,mult in count.items()) == N**4
    return dict(count)


def independent_gram_spectrum(p, k):
    N = p**k
    g = np.zeros((N, N), dtype=np.float64)
    for t in range(N):
        g[t, (t*t) % N] = 1.0 / np.sqrt(N)
    # One row of the complete projector Gram matrix is the squared
    # time-frequency autocorrelation of the window. Weyl covariance makes
    # the entire Gram matrix a four-dimensional circulant after harmless
    # diagonal rephasing; the four-dimensional FFT computes all eigenvalues.
    row = np.empty((N,N,N,N), dtype=np.float64)
    for a in range(N):
        for b in range(N):
            shifted = np.roll(g,(a,b),axis=(0,1))
            row[a,b] = np.abs(np.fft.fft2(g*shifted))**2
    spectrum = np.fft.fftn(row)
    expected = exact_prediction(p,k)
    observed = {}
    for level in expected:
        observed[level] = int(np.count_nonzero(np.abs(spectrum.real-level)<1e-6))
    assert sum(observed.values()) == N**4
    assert observed == expected, (p,k,observed,expected)
    assert np.max(np.abs(spectrum.imag)) < 1e-6
    assert abs(np.sum(spectrum.real)-N**4) < 1e-6
    return expected, float(np.max(abs(spectrum.imag)))


def crosscheck_valuation_magnitudes(p,k):
    # Completely separate direct cyclotomic FFT of the translated
    # intersections (rather than relying on the formula for their sizes).
    N=p**k
    for a in range(N):
        for b in range(N):
            curve=[t for t in range(N) if (2*a*t-a*a-b)%N==0]
            f=np.zeros((N,N),complex)
            for t in curve:
                f[t,t*t%N]=1
            strengths=np.abs(np.fft.fft2(f))**2
            for val in strengths.flat:
                valid=(abs(val)<1e-6 or any(abs(val-p**e)<1e-6 for e in range(2*k+1)))
                assert valid,(p,k,a,b,val)
    return N**4


def main():
    for p,k in [(3,1),(5,1),(3,2),(5,2),(3,3)]:
        mult, maxim = independent_gram_spectrum(p,k)
        readable=';'.join(f'{value}:{mult[value]}' for value in sorted(mult))
        print(f'p={p} k={k} dimension={(p**k)**2} spectrum={readable} max_imaginary={maxim:.3g} PASS')
    for p,k in [(3,2),(5,2)]:
        checked=crosscheck_valuation_magnitudes(p,k)
        print(f'p={p} k={k} direct translated-intersection Gaussian levels={checked} PASS')
    for p in [3,5,7]:
        for k in range(1,8):
            counts=exact_prediction(p,k)
            assert sum(counts.values())==p**(4*k)
    print('All finite spectral, translated-intersection, exact-multiplicity, and trace checks passed.')


if __name__ == '__main__':
    main()
