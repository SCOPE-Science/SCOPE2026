#!/usr/bin/env python3
"""Numerical Fourier-coefficient and finite-Gram checks for powered projective exponential kernels.

Requires mpmath >=1.3.0. Runs with: python verify_projective_kernel.py
Numerical examples complement, but cannot replace, the all-parameter analytic proof.
"""
import mpmath as mp
mp.mp.dps = 65


def power_coefficient(n, p):
    """Normalized Fourier coefficient of |cos(t)|**p at harmonic 2*n."""
    return (mp.gamma(p + 1) * mp.rgamma(p / 2 - n + 1) /
            (mp.power(2, p) * mp.gamma(p / 2 + n + 1)))


def exponential_coefficient(n, p, kappa, terms=150):
    return mp.fsum((kappa**j / mp.factorial(j)) * power_coefficient(n, j*p)
                   for j in range(1, terms + 1))


def direct_coefficient(n, p, kappa):
    f = lambda t: mp.exp(kappa * mp.cos(t)**p) * mp.cos(2*n*t)
    return (mp.mpf(2)/mp.pi)*mp.quad(f, [0,mp.pi/8,mp.pi/4,3*mp.pi/8,mp.pi/2])


checks = 0
for p in [mp.mpf('0.75'),mp.mpf('1'),mp.mpf('1.5'),mp.mpf('3'),mp.mpf('4')]:
    for kap in [mp.mpf('.5'),mp.mpf('2')]:
        for n in [3,7,12]:
            a = exponential_coefficient(n,p,kap)
            b = direct_coefficient(n,p,kap)
            assert abs(a-b) < mp.mpf('1e-35'), (p,kap,n,a,b)
            checks += 1
        for n in [8,14,20]:
            a = exponential_coefficient(n,p,kap)
            if p%2:
                # Sign is eventually dictated by the first non-even power.
                limiting = ((-1)**(n+1)*kap*mp.gamma(p+1)*mp.sin(mp.pi*p/2)/
                            (mp.pi*mp.power(2,p)*n**(p+1)))
                assert mp.sign(a)==mp.sign(limiting), (p,kap,n,a,limiting)
            else:
                assert a>0, (p,kap,n,a)
            checks += 1

for p,kap,N,frequency in [(mp.mpf('1'),mp.mpf('1'),64,10),
                            (mp.mpf('1.5'),mp.mpf('2'),64,10),
                            (mp.mpf('3'),mp.mpf('.5'),64,11)]:
    # Unnormalized eigenvalue of equispaced projective-circle Gram matrix.
    eigen = mp.fsum(mp.exp(kap*abs(mp.cos(mp.pi*j/N))**p)*
                    mp.cos(2*mp.pi*frequency*j/N) for j in range(N))
    assert eigen < 0, (p,kap,N,frequency,eigen)
    checks += 1

print('PASS: %d Fourier comparisons, asymptotic-sign checks and finite negative witnesses' % checks)
