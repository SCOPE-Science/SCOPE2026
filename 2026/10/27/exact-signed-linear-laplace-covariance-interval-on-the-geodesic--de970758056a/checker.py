#!/usr/bin/env python3
"""Independent numerical checks for the affine-geodesic Laplace circle covariance.
Standard library only. Proof is in RESULT.md; finite tests do not prove universal positivity.
"""
import math

PI = math.pi

def limits(a):
    e = math.exp(-PI * a)
    return (-a*(1-e)/(1-e-PI*a*e), a*(1-e)/(1-e+PI*a*e))

def exact_coeff(a,b,n):
    e = math.exp(-PI*a)
    s = (-1)**n
    f = a * (1-s*e)/(a*a+n*n)
    log_derivative = 1/a + s*PI*e/(1-s*e) - 2*a/(a*a+n*n)
    return f*(1-b*log_derivative)/PI

def independent_integral(a,b,n,steps=32768):
    # Composite Simpson rule on [0,pi].
    h=PI/steps
    total=0.0
    for k in range(steps+1):
        x=k*h
        w=1 if k==0 or k==steps else (4 if k%2 else 2)
        total += w * math.exp(-a*x) * (1+b*x) * math.cos(n*x)
    return total*h/(3*PI)

def circular_dft_eigenvalue(a,b,M,n):
    return sum(math.exp(-a*x)*(1+b*x)*math.cos(2*PI*n*j/M)
               for j in range(M)
               for x in (2*PI*min(j,M-j)/M,))

def run():
    count=0
    maxerr=0.0
    for a in (0.2, 1.0, 3.0):
        lo,hi=limits(a)
        assert lo < 0 < hi < a
        for b in (lo, 0.0, hi, (lo+hi)/2):
            for n in (0,1,2,3,4,5,8,11,20,31):
                lhs=exact_coeff(a,b,n)
                rhs=independent_integral(a,b,n)
                err=abs(lhs-rhs)
                maxerr=max(maxerr,err)
                assert err<3e-11,(a,b,n,lhs,rhs,err)
                assert lhs>-1e-12,(a,b,n,lhs)
                count+=1
        assert abs(exact_coeff(a,lo,0))<1e-12
        for n in range(1,100):
            assert exact_coeff(a,lo,n)>0
        for n in range(100):
            assert exact_coeff(a,hi,n)>0
        assert exact_coeff(a,lo-0.05,0)<0
        assert exact_coeff(a,hi*1.10,200)<0
    # Independent finite Gram witnesses, using circulant matrices sampled on 1024 sites.
    a=1.0
    lo,hi=limits(a)
    finite_lo=circular_dft_eigenvalue(a,lo-0.1,1024,0)
    finite_hi=circular_dft_eigenvalue(a,hi*1.20,1024,32)
    assert finite_lo<0,(finite_lo,lo)
    assert finite_hi<0,(finite_hi,hi)
    print('PASS: %d independently integrated Fourier coefficients; max absolute discrepancy %.3g' % (count,maxerr))
    print('PASS: low-mode and high-even-mode negative finite-circulant witnesses:',finite_lo,finite_hi)
    print('EXAMPLE a=1: b_min=%.15f b_max=%.15f; a-b_max=%.15f' % (lo,hi,a-hi))

if __name__=='__main__':
    run()
