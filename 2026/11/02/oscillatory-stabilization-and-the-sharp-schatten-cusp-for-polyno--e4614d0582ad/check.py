#!/usr/bin/env python3
"""Numerical quadrature consistency checks for radial Gaussian Fock multipliers."""
import math
import mpmath as mp
mp.mp.dps = 50
s=mp.mpf('1.5')
for tau in [mp.mpf('0.6'), mp.mpf('1.0'),mp.mpf('1.7')]:
 for a in [mp.mpf('0.66666666666666666666666666666666666666666666666667'),mp.mpc('0.55','0.38')]:
  for n in (2,6,20,80):
   I1=mp.quad(lambda x: x**n/(1+x)**tau*mp.exp(-a*x),[0,1,4,16,64,256,mp.inf])/mp.factorial(n)/s**(n+mp.mpf('0.5'))
   I2=mp.quad(lambda t: t**(tau-1)*mp.exp(-t)/(a+t)**(n+1),[0,1,4,16,64,mp.inf])/mp.gamma(tau)/s**(n+mp.mpf('0.5'))
   assert abs(I1-I2) < 1e-18*max(abs(I1),abs(I2),mp.mpf('1e-40')),(tau,a,n,I1,I2)
  n=600
  Im=mp.quad(lambda u:u**(tau-1)*mp.exp(-u/n)*(1+u/(n*a))**(-n-1),[0,1,4,16,64,mp.inf])/mp.gamma(tau)
  # n^tau * a^(n+1) * unscaled moment I -> a^tau
  val=Im/n**tau
  ratio= val/(a**tau/n**tau)
  assert abs(ratio-1)<mp.mpf('0.09'), (tau,a,ratio)
print('CHECK_OK: two moment representations agree; complex critical Watson-law ratios converge (finite tests only)')
