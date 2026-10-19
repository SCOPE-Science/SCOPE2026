"""Exact-rational certificate for first-arrival mean/variance sensitivities.
Run: python certify_sensitivity.py. No external dependencies.
"""
from fractions import Fraction as F
from math import factorial
import json
import sys
import time


def atan_brackets(q, k):
    # arctan(1/q): even truncation upper, odd truncation lower
    term=F(1,q)
    s=term
    for n in range(1,2*k+2):
        term=F(1,(2*n+1)*q**(2*n+1))
        s += (-1 if n%2 else 1)*term
        if n==2*k:
            hi=s
    return s,hi

# Archimedean constant certified by Machin's arctangent identity.
a_lo,a_hi=atan_brackets(5,33)
b_lo,b_hi=atan_brackets(239,7)
pi_lo=16*a_lo-4*b_hi
pi_hi=16*a_hi-4*b_lo
c_lo=F(112837916709,10**11)
c_hi=F(112837916710,10**11)
assert c_lo*c_lo*pi_hi<4 and c_hi*c_hi*pi_lo>4

# The alternating Taylor-polynomial envelopes for exp(-z), z>=0,
# remain globally valid via the integral-form Taylor remainder.
K=35

def erf_over_u_bounds(u):
    term=F(1)
    v=u*u
    s=term
    for k in range(2*K+1):
        term=term*v*(2*k+1)/((k+1)*(2*k+3))
        s += (-term if k%2==0 else term)
        if k==2*K-1: upper=s
    lower=s
    assert 0 < lower <= upper
    return c_lo*lower,c_hi*upper


def interval(n, divisions):
    # Integral m_j=2 integral_0^infty u^(n-2j-3) (erf(u)/u)^n du.
    # Use u in [0,4] partitioned uniformly. Monotonicity of erf(u)/u
    # gives lower/upper Darboux sums, with tail bounded by erf(4)^n,1.
    assert n>=7
    L=[F(0) for _ in range(3)]
    U=[F(0) for _ in range(3)]
    h=F(4,divisions)
    e_l,e_u=erf_over_u_bounds(F(0))
    for i in range(divisions):
        a=i*h; b=(i+1)*h
        f_l,f_u=erf_over_u_bounds(b)
        for j in range(3):
            d=n-2*j-2
            w=2*(b**d-a**d)/d
            L[j]+=w*f_l**n
            U[j]+=w*e_u**n
        e_l,e_u=f_l,f_u
    # For u>=4 the whole erf(u) lies in [erf(4),1].
    erf4_l=4*e_l
    assert 0<erf4_l<1
    for j in range(3):
        tail=F(1,(j+1)*4**(2*j+2))
        L[j]+=tail*erf4_l**n
        U[j]+=tail
    a,b,c=zip(L,U)
    ml=a[0]**2-b[1]
    mu=a[1]**2-b[0]
    vl=-2*c[1]+6*a[0]*b[0]-2*a[1]**3
    vu=-2*c[0]+6*a[1]*b[1]-2*a[0]**3
    # cv^2 derivative is positive multiple of 2m1^2-m0*m2.
    cl=2*b[0]**2-a[1]*c[1]
    cu=2*b[1]**2-a[0]*c[0]
    def decimal_string(q):
        return f'{float(q):.12f}'
    return {'N':n,'divisions':divisions,'m0':[decimal_string(x) for x in a],
            'm1':[decimal_string(x) for x in b],
            'm2':[decimal_string(x) for x in c],
            'mean_derivative_bounds':[decimal_string(ml),decimal_string(mu)],
            'variance_derivative_bounds':[decimal_string(vl),decimal_string(vu)],
            'cv_derivative_sign_bounds':[decimal_string(cl),decimal_string(cu)],
            '_signs':[int(ml>0),int(vu<0),int(vl>0),int(cu<0),int(cl>0)]}


def main():
    # Run one exactly certified team size per invocation for bounded memory.
    assert len(sys.argv)==2 and sys.argv[1] in ['7','8','9','10']
    n=int(sys.argv[1]); t=time.monotonic()
    r=interval(n,2000)
    print('N',n,'seconds',round(time.monotonic()-t,2),'mean',r['mean_derivative_bounds'],'variance',r['variance_derivative_bounds'],'cv_sign',r['cv_derivative_sign_bounds'],flush=True)
    assert r['_signs'][0]==1
    assert r['_signs'][1 if n<=9 else 2]==1
    assert r['_signs'][3]==1
    with open(f'certified_intervals_{n}.json','w',encoding='utf-8') as f:
        json.dump({k:v for k,v in r.items() if k!='_signs'},f,indent=2)
    print('EXACT-RATIONAL SIGN CERTIFICATE PASS',flush=True)

if __name__=='__main__': main()
