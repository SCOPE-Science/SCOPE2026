"""Supplementary arithmetic checks for the monomial singular values and Weyl coefficient.
Uses scipy for gamma arithmetic and numpy for finite arrays. Numerical checks do not establish asymptotic theorems.
"""
import math
import numpy as np
from scipy.special import gammaln


def exact_singular(n, m, k, rho, N, b):
    if N + b == 0:
        return 0.
    if rho == 0 and b:
        return 0.
    log_ratio = (math.log(b + 1) - math.log(b + k + 1)
        + gammaln(1 + (b + k + 1) / m) - gammaln(1 + (b + 1) / m)
        + gammaln(N + n + (b + 1) / m) - gammaln(N + n + (b + k + 1) / m))
    return ((N + b)/(N + b + k)) * rho**b * math.exp(log_ratio/2)


def leading_amplitude(m, k, b):
    return math.exp((math.log(b + 1) - math.log(b + k + 1)
        + gammaln(1 + (b + k + 1)/m)
        - gammaln(1 + (b + 1)/m))/2)


def constant(n, m, k, rho, bcap=2000):
    d = n - 1
    pstar = 2*m*d/k
    if rho == 0:
        return leading_amplitude(m,k,0)**pstar / math.factorial(d)
    summands = [(rho**b*leading_amplitude(m,k,b))**pstar for b in range(bcap)]
    return math.fsum(summands)/math.factorial(d)


def check_simple():
    n,m,k = 2,2,2
    for rho in (0.0,.35,.6,.85):
        L = constant(n,m,k,rho,500)
        expected = 1/(2*(1-rho*rho)**2)
        assert abs(L-expected) < 1e-11 * expected, (rho,L,expected)
        print('closed_coefficient',rho,L,expected)
        for N,b in [(1,0),(2,1),(5,3),(15,12)]:
            s = exact_singular(n,m,k,rho,N,b)
            sq = (rho**(2*b))*((N+b)/(N+b+2))**2 * (b+1)/(2*N+b+5)
            assert abs(s*s-sq) < 5e-13 * max(1e-8,sq)
    print('closed-form singular weights verified on 16 cases')


def check_general():
    for n,m,k,rho in [(3,2,1,.4),(3,3,3,.7),(4,2,2,.45)]:
        for b in [0,1,3,7]:
            N=20000
            s=exact_singular(n,m,k,rho,N,b)
            target=rho**b*leading_amplitude(m,k,b)*N**(-k/(2*m))
            assert abs(s/target-1)<.0015,(n,m,k,rho,b,s,target)
        print('asymptotic-amplitudes',n,m,k,rho,'OK')


def check_counting():
    n,m,k,rho=2,2,2,.6
    L=constant(n,m,k,rho)
    Nmax=6000; bmax=65
    weights=np.array([[exact_singular(n,m,k,rho,N,b) for b in range(bmax)] for N in range(Nmax+1)])
    for eps in (.08,.055,.04,.03):
        val=float((weights>eps).sum()*eps**2)
        print('counting',eps,val,'target',L,'relative_gap',abs(val/L-1))
    assert abs((weights>.03).sum()*.03**2/L-1)<.12
    print('finite counting diagnostic OK')

if __name__=='__main__':
    check_simple(); check_general(); check_counting()
