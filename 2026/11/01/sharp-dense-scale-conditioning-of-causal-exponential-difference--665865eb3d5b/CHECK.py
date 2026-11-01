#!/usr/bin/env python3
"""Independent numerical and exact-arithmetic checks for causal exponential dilates.

This script checks finite identities and representative spectral values. The
analytical proof of the infinite Riesz bounds and limiting laws is in RESULT.md.
Only Python standard-library modules are required.
"""
from fractions import Fraction as Q
from math import cos, exp, hypot, log, pi, sqrt


def norm_sq(c):
    return (c-1)**2/(2*c*(c+1))


def overlap_unscaled(c, t):
    # <h_ca-h_a,h_cta-h_ta> with a=1.
    return (1+1/c)/(1+t)-1/(c+t)-1/(1+c*t)


def overlap_factored(c, t):
    return t*(c-1)**2*(c+1)/(c*(c+t)*(1+t)*(1+c*t))


def gram(k, c):
    k = abs(k)
    t = c**k
    return 2*(c+1)**2*t**1.5/((c+t)*(1+t)*(1+c*t))


def sech(x):
    y=exp(-abs(x))
    return 2*y/(1+y*y)


def spectral(theta,c,cut=8):
    ell=log(c)
    q=c**(-0.5)
    factor=1+q*q-2*q*cos(theta)
    p=sum(sech(pi*(theta+2*pi*m)/ell) for m in range(-cut,cut+1))
    return pi*factor*p/(ell*norm_sq(c))


def direct_gram_spectral(theta,c,cut=300):
    return 1+2*sum(gram(k,c)*cos(k*theta) for k in range(1,cut+1))


def check_exact_identity():
    tests = 0
    for c in [Q(6,5),Q(3,2),Q(2,1),Q(5,2),Q(3,1),Q(7,1)]:
        assert norm_sq(c)==(c-1)**2/(2*c*(c+1))
        for k in range(0,14):
            t=c**k
            a=overlap_unscaled(c,t)
            b=overlap_factored(c,t)
            assert a==b, (c,k,a,b)
            assert a>0
            tests+=1
    return tests


def check_spectral():
    tests=0
    for c in [2.0,3.0,4.0]:
        for theta in [0,pi/5,pi/2,3*pi/4,pi]:
            x=spectral(theta,c)
            y=direct_gram_spectral(theta,c)
            assert x>0 and abs(x-y) <= 2e-9*max(1,x), (c,theta,x,y)
            tests+=1
        # Positivity and endpoint extrema numerically; not used as proof.
        vals=[spectral(j*pi/1024,c) for j in range(1025)]
        assert min(vals)>0
        assert min(vals)>=spectral(pi,c)*(1-3e-8)
        assert max(vals)<=spectral(0,c)*(1+3e-8)
        tests+=2
    return tests


def check_dense_scale():
    tests=0
    errors=[]
    for ell in [0.30,0.20,0.15,0.10]:
        c=exp(ell)
        lo=spectral(pi,c)
        hi=spectral(0,c)
        lo_asy=64*pi/ell**3*exp(-pi*pi/ell)
        hi_asy=pi/ell
        assert lo>0 and hi>lo
        ea=abs(lo/lo_asy-1)
        eb=abs(hi/hi_asy-1)
        assert ea<0.012 and eb<0.007,(ell,ea,eb)
        errors.append((ell,ea,eb))
        tests+=2
    assert all(errors[i+1][1]<errors[i][1] for i in range(len(errors)-1))
    assert all(errors[i+1][2]<errors[i][2] for i in range(len(errors)-1))
    return tests,errors


if __name__=='__main__':
    a=check_exact_identity()
    b=check_spectral()
    c,err=check_dense_scale()
    print('Exact rational inner-product identities:',a,'passed')
    print('Spectral agreement and sampled endpoint checks:',b,'passed')
    print('Dense-scale asymptotic comparisons:',c,'passed')
    for ell,ea,eb in err:
        print('log scale spacing:',ell,'lower relative error:',f'{ea:.6g}',
              'upper relative error:',f'{eb:.6g}')
    print('Note: finite/sampled checks do not establish an infinite theorem.')
