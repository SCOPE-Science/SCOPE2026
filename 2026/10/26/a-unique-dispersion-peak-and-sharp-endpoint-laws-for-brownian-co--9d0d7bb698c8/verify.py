#!/usr/bin/env python3
"""Independent numerical quadrature checks for the Brownian occupation-variance theorem.

Requires Python 3 standard library only. These computations do not replace proofs
of global uniqueness or the two limiting asymptotics.
"""
import math

N = 16384

def simpson(func, n=N):
    if n % 2:
        raise ValueError('Simpson subdivisions must be even')
    h = 1.0 / n
    total = func(0.0) + func(1.0)
    for i in range(1, n):
        total += (4 if i % 2 else 2) * func(i * h)
    return total * h / 3

def A(k, n=N):
    return simpson(lambda t: t*t / (1+t*t)**2 * math.exp(-k*(1+t*t)), n)

def B(k, n=N):
    return simpson(lambda t: (1.0 if k==0 else 0.0) if t == 0 else
                   math.exp(-k*(1+1/(t*t))) / (1+t*t)**2, n)

def variance_transformed(z, n=N):
    k = z*z/2
    return 8/math.pi * simpson(
        lambda t: 0.0 if t == 0 else
        t*t / (1+t*t)**3 *
        (math.exp(-k*(1+t*t))-math.exp(-k*(1+1/(t*t)))),n)

def variance_plackett(z, n=N):
    a=z*z
    # r=sin(theta) removes the square-root endpoint singularity
    return simpson(lambda t: (math.pi/2) * math.cos(t*math.pi/2)**2 *
        (math.exp(-a/(1+math.sin(t*math.pi/2))) -
         (0.0 if t==1 else math.exp(-a/(1-math.sin(t*math.pi/2))))),n)/math.pi

def sign(k):return B(k)-A(k)

assert abs(A(0)-(math.pi/8-.25))<2e-12
assert abs(B(0)-(math.pi/8+.25))<2e-12
assert sign(0)>0 and sign(1)<0
lo,hi=.3,.4
for _ in range(54):
    mid=(lo+hi)/2
    if sign(mid)>0:lo=mid
    else:hi=mid
k=(lo+hi)/2
z=math.sqrt(2*k)
coverage=math.erf(z/math.sqrt(2))
variance=variance_transformed(z)
assert abs(k-.3440548516017336)<1e-9
assert abs(z-.8295237809752456)<1e-9
assert abs(coverage-.5931919141540194)<1e-9
assert abs(variance-.08135656185520381)<1e-9
checks=5
for z_test in [0.005,0.01,0.03,0.1,0.2,0.4,0.8,1.0,1.5,2,3,4]:
    v1=variance_transformed(z_test)
    v2=variance_plackett(z_test)
    assert v1>0 and abs(v1-v2)<2e-9, (z_test,v1,v2)
    checks+=2
for k_test in [0.01,0.07,0.2,0.3,0.5,1,3]:
    assert sign(k_test)*(1 if k_test<k else -1)>0
    checks+=1
for z_test in [0.02,0.01,0.005]:
    value=variance_transformed(z_test)
    small=(2/math.pi)*z_test**2-(4/3)*math.sqrt(2/math.pi)*z_test**3
    assert abs(value-small)/z_test**3<.03
    checks+=1
for z_test in [5,6,8]:
    value=variance_transformed(z_test)
    asym=8*math.exp(-z_test*z_test/2)/math.sqrt(2*math.pi)/z_test**3
    assert .70<value/asym<.91
    checks+=1
print('PASS',checks,'numerical assertions')
print('k_star',format(k,'.15g'))
print('z_star',format(z,'.15g'))
print('coverage_star',format(coverage,'.15g'))
print('max_variance',format(variance,'.15g'))
