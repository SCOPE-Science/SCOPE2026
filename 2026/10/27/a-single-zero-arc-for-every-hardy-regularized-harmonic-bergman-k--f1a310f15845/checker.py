"""Independent finite numerical checks for a harmonic reproducing kernel.

Run with CPython 3.10 or newer. No nonstandard dependencies.
Finite numerical checks supplement, and do not replace, the analytic proof.
"""
import math


def poisson(r, c):
    return (1.0 - r*r)/(1.0-2.0*r*c+r*r)


def simpson(f, count=8192):
    assert count % 2 == 0
    acc = f(0.0)+f(1.0)
    for j in range(1,count):
        acc += (4 if j%2 else 2)*f(j/count)
    return acc/(3.0*count)


def kernel_integral(kappa, r, c):
    return poisson(r,c)/kappa - simpson(
        lambda x:4.0*x**(4.0/kappa+3.0)*poisson(r*x**4,c), 8192)/(kappa*kappa)


def kernel_series(kappa,r,c,nmax=600):
    theta = math.acos(c)
    return 1.0/(1.0+kappa)+2.0*sum(
        (n+1.0)/(1.0+kappa*(n+1.0))*r**n*math.cos(n*theta)
        for n in range(1,nmax+1))


def root(kappa):
    lo=0.0; hi=1.0-1e-13
    assert kernel_integral(kappa,lo,-1)>0
    assert kernel_integral(kappa,hi,-1)<0
    for _ in range(65):
        mid=(lo+hi)/2.0
        if kernel_integral(kappa,mid,-1)>0:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2.0


for kappa in (0.1,1.0,10.0):
    for r in (0.13,0.44,0.7):
        for c in (-0.85,-0.1,0.67):
            lhs=kernel_integral(kappa,r,c)
            rhs=kernel_series(kappa,r,c)
            assert abs(lhs-rhs)<3e-9, (kappa,r,c,lhs,rhs)
print('Integral/series comparisons: 27 passed (absolute error below 3e-9).')
for kappa in (0.1,1.0,10.0,100.0,1000.0):
    rho=root(kappa)
    assert abs(kernel_integral(kappa,rho,-1))<3e-9
    assert kernel_integral(kappa,rho*0.9,-1)>0
    assert kernel_integral(kappa,(1+rho)*0.5,-1)<0
    for r in (rho*0.7,(rho+1)*0.5):
        vals=[kappa*kernel_integral(kappa,r,-1+2*j/10)/poisson(r,-1+2*j/10) for j in range(11)]
        assert all(vals[j+1]>vals[j] for j in range(10))
    print('kappa=%-6g root=%.12f kappa*(1-root)=%.12f' % (kappa,rho,kappa*(1-rho)))
print('Predicted large-kappa slope = %.12f' % (2*(2*math.log(2)-1)))
print('Predicted small-kappa root = %.12f' % (math.sqrt(2)-1))
print('Finite numerical tests passed; all-order result requires the analytic argument.')
