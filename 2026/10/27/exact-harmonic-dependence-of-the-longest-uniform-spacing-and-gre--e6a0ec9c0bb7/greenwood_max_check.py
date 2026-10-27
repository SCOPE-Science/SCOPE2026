"""Reproducible exact checks for maximum-Greenwood mixed moment on a uniform simplex.

No external packages are required. Every rational comparison is exact.
"""
from fractions import Fraction as F
from math import comb


def beta_int(p,q):
    # int_0^1 z^p (1-z)^q dz, nonnegative integer p,q
    from math import factorial as fac
    return F(fac(p)*fac(q),fac(p+q+1))


def compute(m):
    h=sum((F(1,j) for j in range(1,m+1)),F(0))
    h2=sum((F(1,j*j) for j in range(1,m+1)),F(0))
    # independent inclusion-exclusion evaluation of integral over max threshold
    mixed=F(0)
    mean_max=F(0)
    second_max=F(0)
    for k in range(1,m+1):
        weight=(-1)**(k+1)*comb(m,k)
        # P(X_1,...,X_k>t) = (1-kt)^(m-1) for 0<t<1/k
        # conditional Q expectation = k t^2 + 2kt(1-kt)/m + 2(1-kt)^2/(m+1)
        ii=F(1,k*k)*beta_int(2,m-1)   # k*t^2, dt under substitution z=kt
        jj=F(2,m*k)*beta_int(1,m)    # 2k*t*(1-kt)/m
        kk=F(2,(m+1)*k)*beta_int(0,m+1)
        mixed+=weight*(ii+jj+kk)
        mean_max+=weight*F(1,k)*beta_int(0,m-1)
        second_max+=weight*F(2,k*k)*beta_int(1,m-1)
    assert mean_max==h/m
    assert second_max==(h*h+h2)/(m*(m+1))
    expected_mixed=(h*h+h2+2*(m+1)*h)/(m*(m+1)*(m+2))
    assert mixed==expected_mixed,(m,mixed,expected_mixed)
    # separate coordinate moments for Greenwood squared
    eq=F(2,m+1)
    eq2=F(4*(m+5),(m+1)*(m+2)*(m+3))
    vq=eq2-eq*eq
    assert vq==F(4*(m-1),(m+1)**2*(m+2)*(m+3))
    vm=second_max-mean_max**2
    assert vm==F(m*h2-h*h,m*m*(m+1))
    cov=mixed-mean_max*eq
    assert cov==(h*h+h2-2*h)/(m*(m+1)*(m+2))
    assert cov>0 and vm>0 and vq>0
    return cov,vm,vq

if __name__=='__main__':
    for m in range(2,161):
        compute(m)
    print('PASS: 159 exact rational checks, m=2,...,160')
    for m in (2,3,4,10,100,160):
        co,vm,vg=compute(m)
        print('m=',m,'cov=',str(co),'correlation=',round(float(co)/((float(vm)*float(vg))**.5),10))
