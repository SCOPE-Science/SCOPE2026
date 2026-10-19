"""Independent moment-generator checks for the symmetric persuasive-opinion model.

Run: python3 verify.py
Only Python's standard library is required.
"""
from fractions import Fraction as F
from itertools import product
from math import exp, log, sqrt, isclose


def coefficients(n, mu):
    d = mu*mu/(n-1)
    e = mu*mu*(n+1)/(2*n*(n-1))
    a = mu*(2-mu)/2 + mu*(1-mu)/(n-1)
    b = mu*(1-mu)*n/(n-1)
    return a, b, d, e


def generator_of_moments(x, mu):
    """Compute the exact conditional generators by enumerating all ordered pairs."""
    n = len(x)
    mean = sum(x, F(0))/n
    second = sum(z*z for z in x)/n
    u = mean*mean
    rate = F(1,2*(n-1))
    gu = F(0); gv = F(0); gm = F(0)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            for eps,prob in [(F(1),(1+x[j])/2),(F(-1),(1-x[j])/2)]:
                updated = (1-mu)*x[i]+mu*eps
                dmean=(updated-x[i])/n
                du=2*mean*dmean+dmean*dmean
                dv=(updated*updated-x[i]*x[i])/n
                gu+=rate*prob*du
                gv+=rate*prob*dv
                gm+=rate*prob*dmean
    return u,second,gm,gu,gv


def eigenvalues(n,mu):
    a,b,d,e=coefficients(n,mu)
    discr = sqrt((a-d)**2+4*e*b)
    return (-(a+d)+discr)/2, (-(a+d)-discr)/2


def expected_sample_variance(n,mu,t):
    slow,fast=eigenvalues(n,mu)
    amp=mu*mu*(n-1)/(2*n*(slow-fast))
    return amp*(exp(slow*t)-exp(fast*t))


def test():
    count=0
    rational_mus=[F(1,5),F(1,2),F(3,4)]
    for n in (2,3,4,5):
        # Deterministic, heterogeneous, partially extreme configurations.
        states=[tuple([F(0)]*n),tuple(F(k,n+1) for k in range(n)),
                tuple(F(1) if i%2 else F(-1) for i in range(n)),
                tuple(F((i*7)%11-5,5) for i in range(n))]
        for mu in rational_mus:
            a,b,d,e=coefficients(n,mu)
            assert d*a-e*b == mu**3/(2*(n-1))
            for x in states:
                u,v,gm,gu,gv=generator_of_moments(x,mu)
                assert gm==0
                assert gu == mu**2/(2*n)+e*v-d*u
                assert gv == -a*v+b*u+mu**2/2
                count+=3
    for n in (2,3,4,9,50,500,10000):
        for mu in (0.2,0.5,0.8):
            slow,fast=eigenvalues(n,mu)
            assert slow<0 and fast<slow
            a,b,d,e=coefficients(n,mu)
            assert isclose(slow*fast,float(d*a-e*b),rel_tol=1e-8,abs_tol=1e-13)
            peak=log(fast/slow)/(slow-fast)
            assert peak>0
            vals=[expected_sample_variance(n,mu,peak*s) for s in (.5,.99,1,1.01,2)]
            assert vals[2]>max(vals[0],vals[1],vals[3],vals[4])
            count+=4
    for mu in (0.25,0.5,0.75):
        n=1000000
        slow,fast=eigenvalues(n,mu)
        kappa=mu*mu/(2-mu)
        assert abs(n*slow+kappa)<4e-5
        peak=log(fast/slow)/(slow-fast)
        asymp=(2/(mu*(2-mu)))*(log(n)+log((2-mu)**2/(2*mu)))
        assert abs(peak-asymp)<0.001
        for s in (.15,.5,1,2):
            expected=mu/(2-mu)*exp(-kappa*s)
            actual=expected_sample_variance(n,mu,n*s)
            assert abs(actual-expected)<5e-6
            count+=1
    print('PASS:',count,'exact/numerical generator, spectral, peak, and crossover assertions')


if __name__ == '__main__':
    test()
