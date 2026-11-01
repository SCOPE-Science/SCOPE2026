#!/usr/bin/env python3
"""Independent checks of finite-n perimeter dispersion for uniform circle vertices.
Requires mpmath; all numerical integrations use explicit probability densities.
"""
import math
import random
from fractions import Fraction
import mpmath as mp

mp.mp.dps = 55
pi = mp.pi

def J(k, a):
    z = mp.mpc(0, a)
    return mp.factorial(k) * (mp.exp(z) - sum(z**j/mp.factorial(j) for j in range(k+1))) / z**(k+1)

def exact_variance(n):
    assert n >= 3
    u=(n-1)*mp.im(J(n-2,pi))
    v=(n-1)*mp.re(J(n-2,2*pi))
    r=(n-1)*(n-2)*mp.re(J(n-3,pi)-J(n-2,pi))
    s=(n-1)*(n-2)/pi*mp.im(J(n-3,pi))
    return 2*n*(1-v)+2*n*(n-1)*(s-r)-4*n*n*u*u, 2*n*u

def quadrature_variance(n):
    u=(n-1)*mp.quad(lambda x:(1-x)**(n-2)*mp.sin(pi*x),[0,1])
    v=(n-1)*mp.quad(lambda x:(1-x)**(n-2)*mp.cos(2*pi*x),[0,1])
    r=(n-1)*(n-2)*mp.quad(lambda x:x*(1-x)**(n-3)*mp.cos(pi*x),[0,1])
    s=(n-1)*(n-2)/pi*mp.quad(lambda x:(1-x)**(n-3)*mp.sin(pi*x),[0,1])
    return 2*n*(1-v)+2*n*(n-1)*(s-r)-4*n*n*u*u

for n in range(3,11):
    a,mean=exact_variance(n)
    b=quadrature_variance(n)
    assert abs(a-b)<mp.mpf('1e-36'), (n,a,b)
    assert a>0 and 0<mean<2*pi
assert abs(exact_variance(3)[0]-(6-48/pi**2))<mp.mpf('1e-40')
assert abs(exact_variance(4)[0]-(8-444/pi**2+4608/pi**4-9216/pi**6))<mp.mpf('1e-40')
print('EXACT_OSCILLATORY_INTEGRALS_AND_FINITE_N_RATIONAL_PI_FORMULAS_PASSED')

# Exact Dirichlet power sums, computed independently from rising factorial moments.
def rising(n, k):
    p=1
    for i in range(k): p*=n+i
    return p

def E_sum_power(n,k): return Fraction(n*math.factorial(k), rising(n,k))
def E_product_sums(n,a,b):
    return Fraction(n*math.factorial(a+b)+n*(n-1)*math.factorial(a)*math.factorial(b),rising(n,a+b))
def var_sum(n,k):return E_product_sums(n,k,k)-E_sum_power(n,k)**2
def cov_sum(n,a,b):return E_product_sums(n,a,b)-E_sum_power(n,a)*E_sum_power(n,b)
for n in [3,4,5,12,31,100]:
    v3=Fraction(72*(n-1)*(5*n+11),(n+1)**2*(n+2)**2*(n+3)*(n+4)*(n+5))
    c35=Fraction(14400*(n-1)*(2*n+5),(n+1)**2*(n+2)**2*(n+3)*(n+4)*(n+5)*(n+6)*(n+7))
    assert var_sum(n,3)==v3 and cov_sum(n,3,5)==c35
print('EXACT_CUBIC_POWER_VARIANCE_AND_CUBIC_QUINTIC_COVARIANCE_PASSED')

# Simulate independently generated iid circle angles rather than Dirichlet samples.
rng=random.Random(20261029)
for n in [3,4,7,12]:
    N=35000
    moments=[0.,0.]
    for _ in range(N):
        angles=sorted(rng.random() for _ in range(n))
        gaps=[angles[j+1]-angles[j] for j in range(n-1)] + [1+angles[0]-angles[-1]]
        perimeter=2*sum(math.sin(math.pi*g) for g in gaps)
        moments[0]+=perimeter
        moments[1]+=perimeter**2
    actual_mean=moments[0]/N
    actual_var=moments[1]/N-actual_mean**2
    target_var,target_mean=exact_variance(n)
    assert abs(actual_mean-float(target_mean))<0.035, (n,'mean',actual_mean,target_mean)
    assert abs(actual_var-float(target_var))<0.060, (n,'variance',actual_var,target_var)
    print('INDEPENDENT_IID_CIRCLE_SAMPLE_PASSED',n,round(actual_var,8),round(float(target_var),8))
print('ALL_CHECKS_PASSED')
