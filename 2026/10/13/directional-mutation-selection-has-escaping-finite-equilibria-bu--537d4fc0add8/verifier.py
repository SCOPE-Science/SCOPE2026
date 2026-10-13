"""Finite computations supporting the analytic trait-escape theorem.
The infinite-dimensional assertions are proved in RESULT.md, not by this test.
"""
from fractions import Fraction
import math
import numpy as np
from scipy.linalg import eigh

r=Fraction(2,5)
c=(1-r)/(1+r)
def p(j):
    return c * r**abs(j)
assert c * (1+2*r/(1-r)) == 1
for k in range(-15,16):
    lhs=(1+r*r)*p(k)-r*(p(k-1)+p(k+1))
    assert lhs == ((1-r)**2 if k==0 else 0)

previous=0.0
samples=[]
for I in [4,8,16,32,64]:
    sites=np.arange(-I,I+1,dtype=float)
    mu=1.0+1.0/(1.0+np.exp(sites))
    P=float(c) * np.power(float(r), np.abs(sites[:,None]-sites[None,:]))
    H=P/np.sqrt(mu[:,None]*mu[None,:])
    rho,v=eigh(H,subset_by_index=(2*I,2*I))
    rho=float(rho[0])
    assert previous < rho < 1.0, (I,rho,previous)
    previous=rho
    phi=(v[:,0]/np.sqrt(mu))
    if sum(phi)<0: phi=-phi
    phi/=sum(phi)
    assert np.min(phi)>-2e-14
    phi=np.maximum(phi,0.0)
    phi/=sum(phi)
    assert np.max(np.abs(P@phi-rho*mu*phi))<2e-12
    mass=1.0-1.0/(3.0*rho)
    assert mass>0
    x=mass*phi
    assert np.max(np.abs(3.0*(1.0-sum(x))*(P@x)-mu*x))<2e-12
    left=float(np.sum(phi[sites<=0]))
    bound=(1.0/rho-1.0)/(mu[sites==0][0]-1.0)
    assert left<=bound+2e-12, (I,left,bound)
    samples.append((I,rho,left,bound,mass))

assert samples[-1][2] < samples[0][2]
print('FINITE_SECTIONS')
for item in samples:
    print('I=%d radius=%.9f left_mass=%.9f upper_bound=%.9f equilibrium_mass=%.9f'%item)
print('VERIFY_OK')
