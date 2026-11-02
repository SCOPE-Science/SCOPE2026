#!/usr/bin/env python3
"""Independent finite numerical checks for reset Brownian threshold occupation."""
import math
from scipy.integrate import quad
from scipy.special import erfc

def stationary_corr(z):
    return math.erfc(math.sqrt(z))

def stationary_corr_integral(z):
    # Conditional Gaussian signs integrated over the independent Exp(1) reset age.
    return math.exp(-z)*(2/math.pi)*quad(
        lambda a: math.exp(-a)*math.atan(math.sqrt(a/z)), 0, 50,
        epsabs=2e-13, epsrel=2e-13)[0]

def stationary_var_quadrature(z):
    return 0.5/z**2*quad(lambda u:(z-u)*math.erfc(math.sqrt(u)),0,z,
                          epsabs=2e-13,epsrel=2e-13)[0]

def stationary_var_closed(z):
    root=math.sqrt(z)
    return ((4*z*z-4*z+3)*erfc(root)+(4*z-3)
            +2*root*(3-2*z)*math.exp(-z)/math.sqrt(math.pi))/(16*z*z)

def fresh_var(z):
    return (z+math.expm1(-z))/(4*z*z)

def fresh_var_poisson(z):
    return sum(math.exp(-z)*z**n/math.factorial(n)/(4*(n+2))
               for n in range(0, max(80,int(z)+50)))

def stationary_vs_fresh_cov(z,s):
    # Time is made dimensionless by the resetting rate; fix lag z, past time s.
    f=lambda a: math.exp(-a)*2/math.pi*math.atan(math.sqrt(a/z))
    trunc=math.exp(-s)*2/math.pi*math.atan(math.sqrt(s/z))
    return math.exp(-z)*(quad(f,0,s,epsabs=1e-12)[0]+trunc),stationary_corr(z)

n=0
for z in (0.02,0.1,0.3,0.8,1.0,2.5,7.0,17.0):
    check=stationary_corr_integral(z)
    ref=stationary_corr(z)
    assert abs(check-ref)<1e-10,(z,check,ref)
    n+=1
    v=stationary_var_quadrature(z)
    v2=stationary_var_closed(z)
    assert abs(v-v2)<2e-10,(z,v,v2)
    n+=1
    vf=fresh_var(z)
    vp=fresh_var_poisson(z)
    assert abs(vf-vp)<5e-12,(z,vf,vp)
    n+=1
    assert 0<vf<v<0.25,(z,vf,v)
    n+=1
for z in (0.05,0.5,1.0,3.0):
    for s in (0.1,1.0,4.0):
        fresh,stationary=stationary_vs_fresh_cov(z,s)
        assert 0<fresh<stationary,(z,s,fresh,stationary)
        n+=1
for z in (10,20,40):
    vs=stationary_var_quadrature(z)
    vf=fresh_var(z)
    assert abs(z*z*(vs-vf)-1/16)<0.01,(z,vs,vf)
    n+=1
print('PASS',n,'independent finite comparisons; all-time strict inequality rests on analytic proof.')
