#!/usr/bin/env python3
"""Independent numeric checks for position-only reset of Brownian-squared diffusivity.
Run: python verify.py (requires numpy and scipy).
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import erfcx

LAM=1.2
RATE=1.7

def conditional_characteristic(k, t, a):
    w=2*LAM*abs(k)/math.sqrt(t)
    return 1/math.sqrt(math.cosh(w*a)+w*(t-a)*math.sinh(w*a))

def characteristic_finite(k, t):
    return math.exp(-RATE*t)*conditional_characteristic(k,t,t)+RATE*quad(
        lambda a: math.exp(-RATE*a)*conditional_characteristic(k,t,a),0,t,
        epsabs=1.e-12, epsrel=1.e-12)[0]

def characteristic_limit(k):
    if k==0:return 1.
    z=math.sqrt(RATE)/(2*LAM*abs(k))
    return math.sqrt(math.pi)*z*erfcx(z)

def limit_density_scaled(x):
    # density in y/c units, evaluated in log z for numerical stability
    f=lambda logz: math.exp(-math.exp(2*logz)/2-x*math.exp(-logz))
    return quad(f, math.log(x)/3-12, math.log(x)/3+12, epsabs=1.e-17, epsrel=5.e-12, limit=400, points=[math.log(x)/3])[0]/math.sqrt(2*math.pi)

def limit_density_tail(x):
    return x**(-1/3)*math.exp(-1.5*x**(2/3))/math.sqrt(3)

checks=0

def test(msg,v,expect,tol):
    global checks
    checks+=1
    assert abs(v-expect)<=tol, (msg,v,expect,tol)

# Independence check 1: determinant of discretized Brownian covariance
# from Gaussian integration E[exp(-q sum B(t_j)^2 dt)]
for a in [0.4,1.3,2.1]:
  for t in [3.0,5.0]:
    for k in [0.25,0.73]:
      n=250
      h=a/n
      ss=(t-a)+h*np.arange(1,n+1)
      covariance=np.minimum.outer(ss,ss)
      q=2*LAM*LAM*k*k/t
      # product eigenvalues of I +2 q h covariance
      e=np.linalg.eigvalsh(covariance)
      approximate=math.exp(-.5*np.log1p(2*q*h*e).sum())
      exact=conditional_characteristic(k,t,a)
      test('Gaussian covariance determinant',approximate,exact,0.012)

# Independence check 2: finite-time characteristic approaches mixture law
for k in [0.13,0.4,0.9,1.5]:
  for t in [250.0,2000.0]:
    test('finite characteristic limit',characteristic_finite(k,t),
         characteristic_limit(k),0.003)

# Independence check 3: exact finite-time variance from renewal age integral
for t in [0.3,1,5,20]:
  moment=RATE*quad(lambda a:math.exp(-RATE*a)*4*LAM**2*(a*t-a*a/2),
                    0,t,epsabs=1.e-11)[0]+math.exp(-RATE*t)*4*LAM**2*t*t/2
  target=4*LAM**2*(RATE*t-1+math.exp(-RATE*t))/RATE**2
  test('finite-time variance',moment,target,1.e-9)

# Time-dependent deterministic comparison and its Laplace limit
for k in [0.1, 0.4, 0.9]:
  t=300.
  finite=math.exp(-RATE*t)*math.exp(-2*LAM**2*k*k*(t-t/2))
  finite+=RATE*quad(lambda a:math.exp(-RATE*a)*math.exp(-2*LAM**2*k*k*(a-a*a/(2*t))),0,t,epsabs=1.e-12)[0]
  limit=RATE/(RATE+2*LAM**2*k*k)
  test('deterministic comparison limit',finite,limit,0.003)

# Explicit W2 coupling error bound: calculate Brownian approximation exact L2
for t in [1.,3.,10.]:
  ae2=2/RATE**2*(1-math.exp(-RATE*t)*(1+RATE*t))
  local_l2=math.sqrt(2*LAM**2/t*ae2)
  stated=2*LAM/(RATE*math.sqrt(t))+2*LAM/math.sqrt(RATE)*math.exp(-RATE*t/2)
  assert local_l2<stated
  checks+=1

# Gaussian*Laplace mixture: conditioning on Gaussian, integrate rational transform
from numpy.polynomial.hermite import hermgauss
nodes,weights=hermgauss(120)
for k in [0.1,0.3,0.7,1.2]:
   mixture=float(np.dot(weights,1/(1+4*LAM**2*k*k*nodes**2/RATE))/math.sqrt(math.pi))
   test('independent Gaussian mixture',mixture,characteristic_limit(k),1.e-5)

# Sharp density: log cusp, stretched exponential 2/3 tail
for x in [10.,30.,100.]:
    d=limit_density_scaled(x)
    test('asymptotic tail',d/limit_density_tail(x),1.,0.012)
for x in [1.e-3,1.e-5,1.e-7]:
    lhs=limit_density_scaled(x)
    assert abs(lhs-math.log(1/x)/math.sqrt(2*math.pi))<1.0
    checks+=1

# Independent elementary moment calculation for product Gaussian * Laplace
c=math.sqrt(2)*LAM/math.sqrt(RATE)
variance=(c*c)*1*2
fourth=(c**4)*3*24
test('exact variance',variance,4*LAM*LAM/RATE,1.e-12)
test('raw kurtosis',fourth/variance**2,18.,1.e-12)
test('matched deterministic raw kurtosis',24/2**2,6.,1.e-12)

print('PASS:',checks,'independent numerical/algebraic checks')
