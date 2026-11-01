"""Quasi-Monte Carlo check of the exact local spherical-chart probability integral.
The proof of the expansion does not use this numerical check.
"""
import math
import numpy as np
from scipy.stats import qmc

def constants(d):
 q=d-1
 C=d*2**q*math.gamma(d/2)*q**(1.5*q)/(math.pi**(d/2)*math.factorial(q))
 K=q**1.5*(q*q+2*q+3)/(2*(q+1))
 return C,K

def probability_local_integral(d, eps, points=2**18):
 q=d-1
 top=1/math.sqrt(q)
 m=math.sqrt(d-1/(top-eps)**2)
 delta=1-m
 sampler=qmc.Sobol(d=q+1,scramble=True,seed=20261026)
 t=np.maximum(sampler.random_base2(int(math.log2(points))),1e-15)
 expo=-np.log(t)
 y=expo[:,:q]/expo.sum(axis=1)[:,None]
 u=delta*y
 s2=np.sum(u*u,axis=1)
 survives=(u.sum(axis=1)+1-np.sqrt(1-s2) < delta)
 integrand=survives /np.sqrt(1-s2)
 orthant_volume=delta**q/math.factorial(q)
 sphere_area=2*math.pi**(d/2)/math.gamma(d/2)
 return (2*d)*2**q*orthant_volume*float(integrand.mean())/sphere_area

def run():
 for d in (2,3,4,5):
  c,k=constants(d)
  for e in (.004,.008,.016):
   true=probability_local_integral(d,e)
   a=c*e**(d-1)
   approx=a*(1+k*e)
   print('d',d,'eps',e,'p',format(true,'.10g'),'p/leading',round(true/a,7),'p/two-term',round(true/approx,7))

if __name__=='__main__':run()
