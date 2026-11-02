#!/usr/bin/env python3
"""Direct non-Hermitian time propagation test, independent of spectral-projector implementation."""
import numpy as np
from scipy.linalg import expm
from fractions import Fraction
from check_resonances import theoretical

def execute():
    count=0;mx=0.
    for a,b in [(1,2),(2,2),(2,3)]:
      n=a+b;N=1<<n
      for rho in [1.,2.,np.sqrt(2.)]:
        ratio=Fraction(int(rho)) if rho in (1.,2.) else None
        H=np.zeros((N,N),complex)
        for x in range(N):
          for j in range(n):H[x,x^(1<<j)]=(1 if j<a else rho)
        H[0,0]-=0.75j
        U=expm(-1j*H*600)
        _,expected=theoretical(a,b,ratio)
        for x in range(N):
          r=(x&((1<<a)-1)).bit_count();s=(x>>a).bit_count()
          abs_prob=1-sum(abs(z)**2 for z in U[:,x])
          err=abs(abs_prob-float(expected[r,s]));mx=max(mx,err)
          assert err<3e-8,(a,b,rho,x,abs_prob,float(expected[r,s]),err)
          count+=1
    print('PASS finite-time non-Hermitian propagation:',count,'initial states, max asymptotic discrepancy',format(mx,'.3g'))
if __name__=='__main__': execute()
