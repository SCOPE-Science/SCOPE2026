"""Numerical cross-check of circular logarithmic-kernel Gram spectra.

The proof of the all-N result is analytic and independent of this script.
Requires Python 3, numpy, mpmath.
"""
import math
import numpy as np
import mpmath as mp

def moment_kernel(u, shift):
    # Integer shift > 0: sum_{n>=0} u^n/(n+shift).
    if abs(u) < mp.mpf('0.01'):
        return mp.fsum(u**n/(n+shift) for n in range(40))
    return (-mp.log(1-u)-sum(u**k/k for k in range(1,shift))) / u**shift

def circular_values(N, shift, c):
    mp.mp.dps = 90
    rho=1-mp.exp(-mp.mpf(c)*N)
    theta=2*mp.pi/N
    first=[moment_kernel(rho*mp.exp(1j*k*theta),shift) for k in range(N)]
    diag=moment_kernel(rho,shift)
    spectrum=[mp.re(mp.fsum(first[k]*mp.exp(-1j*k*j*theta) for k in range(N))/diag) for j in range(N)]
    assert max(abs(mp.im(mp.fsum(first[k]*mp.exp(-1j*k*j*theta) for k in range(N))/diag)) for j in range(N)) < mp.mpf('1e-67')
    return spectrum

checks=0
for N in (4,6,9,13):
  for shift in (1,2,3):
    rho=0.37
    angles=2*np.pi*np.arange(N)/N
    vals=np.array([[sum((rho*np.exp(1j*(angles[k]-angles[m])))**n/(n+shift) for n in range(190)) for m in range(N)] for k in range(N)],complex)
    ev=np.linalg.eigvalsh(vals)/sum(rho**n/(n+shift) for n in range(190))
    diag=sum(rho**n/(n+shift) for n in range(190))
    residues=[N*sum(rho**(j+k*N)/(j+k*N+shift) for k in range(60))/diag for j in range(N)]
    assert max(abs(x-y) for x,y in zip(ev,sorted(residues)))<2e-10
    assert all(residues[i]>residues[i+1] for i in range(N-1))
    checks+=2
for shift in (1,2):
  for c in (0.75,1.5):
    for N in (12,24,48):
      eig=circular_values(N,shift,c)
      assert all(eig[j]>eig[j+1] for j in range(N-1))
      target=[1+1/(c*(j+shift)) for j in range(N)]
      err=max(float(abs(eig[j]-target[j])) for j in range(N))
      # Proven asymptotic rate is O(log N/N), not an exact finite-N bound.
      print(f'shift={shift} c={c:.2f} N={N} top={float(eig[0]):.9f} bottom={float(eig[-1]):.9f} target_top={target[0]:.9f} max_err={err:.9f}')
      assert err<3.5*math.log(N)/N
      checks+=3
print(f'PASS: {checks} verification assertions across exact Fourier residue identities and critical spectral estimates')
