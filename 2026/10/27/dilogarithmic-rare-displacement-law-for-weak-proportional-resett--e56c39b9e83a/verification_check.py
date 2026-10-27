#!/usr/bin/env python3
"""Numerical cross-checks for the stated weak-rescaling stationary rate law.
Requires only the Python standard library. Numerical checks do not replace proof.
"""
import math

COUNT = 0

def check(test, context):
    global COUNT
    COUNT += 1
    if not test:
        raise AssertionError(context)

def li2_series(z):
    assert 0 <= z < 1
    if z > 0.5:
        return math.pi**2/6 - math.log(z)*math.log1p(-z) - li2_series(1-z)
    ans = 0.0
    for n in range(1, 10000):
        term = z**n / (n*n)
        ans += term
        if term < 2e-16:
            break
    return ans

def li2_quad(z, n=12000):
    assert n % 2 == 0
    def f(u):
        return z if u == 0 else -math.log1p(-z*u)/u
    acc = f(0.0) + f(1.0)
    for k in range(1,n):
        acc += (4 if k%2 else 2) * f(k/n)
    return acc/(3*n)

def scaled_cgf(eps, theta):
    assert 0 < eps and abs(theta) < 1
    z=theta*theta
    total=0.0
    for k in range(100000):
        term=-math.log1p(-z*math.exp(-eps*k))
        total+=term
        if k>1 and term<2e-16:
            break
    return eps*total

def slope(theta):
    return 0.0 if theta == 0 else -2*math.log1p(-theta*theta)/theta

def rate(y):
    if y<0:
        return rate(-y)
    if y==0:
        return 0.0,0.0
    lo, hi = 0.0, 1.0-1e-15
    for _ in range(160):
        mid=(lo+hi)/2
        if slope(mid)<y:
            lo=mid
        else:
            hi=mid
    theta=(lo+hi)/2
    return theta*y - li2_series(theta*theta),theta

for z in (0.01,0.0625,0.25,0.49,0.81,0.9025):
    lhs=li2_series(z)
    rhs=li2_quad(z)
    check(abs(lhs-rhs)<2e-10, ('quadrature vs series',z,lhs,rhs))

for eps in (0.5,0.2,0.1,0.05):
    for theta in (0.2,0.5,0.8):
        exact=li2_series(theta**2)
        finite=scaled_cgf(eps,theta)
        upper=eps*(-math.log1p(-theta**2))
        check(-1e-12<=finite-exact<=upper+1e-12, ('rigorous Riemann bracket',eps,theta,finite,exact))
        check(finite>exact, ('positive Riemann surplus',eps,theta))

for y in (0.1,0.2,0.5,1,2,4,8,12,16,20):
    val, theta=rate(y)
    check(0<theta<1, ('optimizer interior',y))
    check(abs(slope(theta)-y)<2e-8, ('stationary derivative',y,theta))
    check(0<val<y*y/4, ('strictly sub-Gaussian large-deviation rate',y,val))
    neg,t_neg=rate(-y)
    check(abs(neg-val)<1e-12, ('symmetry',y))

for y in (0.1,0.2,0.3):
    val,_=rate(y)
    approx=y*y/4-y**4/64
    check(abs(val-approx)<y**6/30, ('small amplitude expansion',y,val,approx))

for y in (12,16,20):
    val,_=rate(y)
    approx=y-math.pi**2/6+math.exp(-y/2)
    check(abs(val-approx)<8*y*math.exp(-y), ('large amplitude expansion',y,val,approx))

# The exact static variance is 2D/[r(1-a^2)] and agrees with
# the second derivative of the finite epsilon CGF at the origin.
for eps in (0.5,0.2,0.05):
    c2=math.exp(-eps)
    scaled_var=2*eps*eps/(1-c2)
    check(abs(scaled_var-2*eps)<3*eps*eps, ('variance scaling',eps,scaled_var))

print(f'PASS: {COUNT} independent deterministic comparisons')
for y in (1,2,4,8,12):
    v,t=rate(y)
    print(f'y={y}: rate={v:.12f}, optimum_theta={t:.12f}, Gaussian_rate={y*y/4:.12f}')
print('limiting scaled CGF: Li_2(theta^2), theta in (-1,1)')
print('large-displacement rate: |y| - pi^2/6 + exp(-|y|/2) + O(|y| exp(-|y|))')
