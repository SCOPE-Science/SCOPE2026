#!/usr/bin/env python3
"""Numerical checks for a regular polygon's central spherical depth.

Requirements: Python 3, NumPy, SciPy. This file checks only finite instances.
Run: python verify.py
"""
import math
import numpy as np
from scipy.integrate import quad


def coefficients(n, max_odd=79):
    a = math.pi / n
    out = []
    for k in range(1, max_odd + 1, 2):
        integral = quad(lambda t: 1 / math.cos(t)**2, -a, a,
                        weight='cos', wvar=k*n, epsabs=2e-13,
                        epsrel=2e-13, limit=250)[0]
        out.append(integral / (2 * math.tan(a)))
    return out


def fourier_depth(n, max_odd=79):
    if n % 2 == 0:
        return 0.5
    coeff = coefficients(n, max_odd)
    series = sum(((-1)**j) * b*b / (2*j+1) for j,b in enumerate(coeff))
    return 0.5 - 2 * ((-1)**((n-1)//2)) * series / (math.pi*n)


def angular_fft_depth(n, size=131072):
    angles = 2*np.pi*np.arange(size)/size
    spacing = ((angles+np.pi/n) % (2*np.pi/n))-np.pi/n
    raw = 1/np.cos(spacing)**2
    probability = raw/raw.sum()
    spectrum = np.fft.fft(probability)
    # autocorrelation of the normalized discrete angular distribution
    delta_prob = np.fft.ifft(np.conjugate(spectrum)*spectrum).real
    return float(delta_prob[size//4:3*size//4].sum())


def main():
    b = 5*math.pi**4/192
    c = 7*math.pi**6/720
    for n in (3,5,7,9,11,15,21):
        p = fourier_depth(n)
        independent = angular_fft_depth(n)
        assert abs(p-independent) < 2e-7, (n,p,independent)
        assert ((p-0.5)*((-1)**((n-1)//2))) < 0
        if n == 3:
            assert abs(p-(1/3+math.log(3)/6)) < 3e-9
        signed = -(p-0.5)*((-1)**((n-1)//2))
        scaled = signed*n**5
        print(f'n={n:2d} depth={p:.12f} scaled={scaled:.9f} '
              f'two_term={b+c/n**2:.9f}')
        assert scaled>b
    for n in (4,6,8,10):
        assert abs(angular_fft_depth(n)-0.5)<3e-7
    print('Fourier/FFT agreement, parity, equilateral benchmark, and scaled checks passed.')

if __name__=='__main__':
    main()
