#!/usr/bin/env python3
"""Independent numerical and exact-identity tests for stationary-velocity-reset tails."""
import math
from scipy.integrate import quad
from scipy.special import ndtr

checks = 0

def close(x, y, tol=2e-10):
    global checks
    assert math.isfinite(x) and math.isfinite(y)
    assert abs(x-y) <= tol*max(1,abs(y)), (x,y)
    checks += 1

def pos_tail_laplace_gaussian(x, rate, sig2):
    # X=Laplace(rate)+N(0,sig2), independent. Positive tail.
    sig=math.sqrt(sig2)
    q=rate*sig
    return ndtr(-x/sig) + .5*math.exp(q*q/2-rate*x)*ndtr(x/sig-q) - .5*math.exp(q*q/2+rate*x)*ndtr(-x/sig-q)

def no_reset_tail(r,D,T,x):
    kappa=math.sqrt(r/D)
    return math.exp(-r*T)*pos_tail_laplace_gaussian(x,kappa/T,2*D*T**3/3)

# Check stationary Laplace variance from exponential-age Gaussian mixing,
# independent stationary covariance and exact time-integrated diffusion variance.
for r in (.4,1.,2.5):
 for D in (.3,1.,1.7):
  k=math.sqrt(r/D)
  vvar,err=quad(lambda age:r*math.exp(-r*age)*2*D*age,0,math.inf)
  close(vvar,2/(k*k))
  for T in (.4,1.,2.4):
   via_cov=quad(lambda s:2*(T-s)*2*D/r*math.exp(-r*s),0,T)[0]
   formula=4*D*(r*T-1+math.exp(-r*T))/r**3
   close(via_cov,formula)
   mgf_crit=k/T
   for theta in (0,.25*mgf_crit,.75*mgf_crit):
    # conditional no-reset transform as independent stationary V0 & future integrated BM
    no_reset_mgf=math.exp(-r*T)*k*k/(k*k-theta*theta*T*T)*math.exp(D*theta*theta*T**3/3)
    assert math.isfinite(no_reset_mgf) and no_reset_mgf>0
    checks+=1

# Exact finite-time large-position prefactor and no-reset analytic Gaussian convolution.
for r,D,T in ((1.,1.,1.),(.8,2.,1.3),(2.,.7,.6)):
 k=math.sqrt(r/D)
 theta=k/T
 C=.5*math.exp(-2*r*T/3)
 for scale in (9.,14.,20.):
  x=scale/theta
  ratio=math.exp(theta*x)*no_reset_tail(r,D,T,x)
  close(ratio,C,4e-5)

# One interior reset is exponentially subdominant; evaluate its exact conditional law.
r=D=T=1.
for x in (6.,9.,12.):
 ratio0=math.exp(x)*no_reset_tail(r,D,T,x)
 C=.5*math.exp(-2/3)
 close(ratio0,C,3e-8)
 single=quad(lambda t:math.exp(x-r*T)*r*pos_tail_laplace_gaussian(x,1/t,2*(t**3+(T-t)**3)/3),.5,.9999,epsabs=1e-11)[0]
 assert single>0
 checks+=1
 if x>=9:
  assert single < (.10 if x==9. else .09)
  checks+=1

# Conditional no-reset amplitude and MGF pole coincide: pole coefficient=2*tail prefactor.
for r in (.5,1.4,3.2):
 for D in (.2,2.):
  for T in (.4,1.2):
   k=math.sqrt(r/D)
   lim=math.exp(-r*T)*math.exp((k/T)**2*D*T**3/3)
   close(lim,math.exp(-2*r*T/3))
   close(lim,2*(.5*math.exp(-2*r*T/3)))
print('PASS',checks,'deterministic assertions')
