"""Independent finite checks for half-line Hermite concentration.

Run: python verify.py. NumPy/SciPy required.
No finite numerical experiment is used as a proof of the all-mask theorem.
"""
import itertools
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import eval_hermite, gammaln
import mpmath as mp


def boundary_even(a):
    return (-1)**a * math.sqrt(math.factorial(2*a))/(2**a*math.factorial(a)*math.pi**0.25)


def boundary_odd(b):
    return (-1)**b * 2**(0.5-b)*math.sqrt(math.factorial(2*b+1))/(math.factorial(b)*math.pi**0.25)


def centered_block(evens, odds):
    return np.array([[boundary_even(a)*boundary_odd(b)/(2*b+1-2*a) for b in odds]
                      for a in evens], dtype=float).reshape(len(evens), len(odds))


def gap_product_from_minors(B):
    e,o=B.shape
    r=min(e,o)
    if r==0: return 1.0
    return sum(float(np.linalg.det(B[np.ix_(I,J)])**2)
               for I in itertools.combinations(range(e),r)
               for J in itertools.combinations(range(o),r))


def psi(n,x):
    return eval_hermite(n,x)*np.exp(-x*x/2.0)/math.sqrt(2.0**n*math.factorial(n)*math.sqrt(math.pi))


def main():
    nmax=12
    gram=np.empty((nmax,nmax),dtype=float)
    for i in range(nmax):
        for j in range(nmax):
            if (i+j)%2==0:
                gram[i,j]=0.5 if i==j else 0.0
            else:
                gram[i,j]=quad(lambda t: psi(i,t)*psi(j,t),0.0,10.0,
                               epsabs=3e-13,epsrel=3e-13,limit=120)[0]
    max_gram_err=0.0
    max_gap_err=0.0
    masks=0
    for n in range(1,11):
        for bits in range(1,1<<n):
            F=[i for i in range(n) if bits>>i&1]
            evens=[i//2 for i in F if i%2==0]
            odds=[i//2 for i in F if i%2==1]
            B=centered_block(evens,odds)
            C=gram[np.ix_(F,F)]
            E=np.zeros_like(C)
            for i,x in enumerate(F):
                for j,y in enumerate(F):
                    if x==y: E[i,j]=0.5
                    elif x%2!=y%2:
                        a=x//2 if x%2==0 else y//2
                        b=y//2 if y%2==1 else x//2
                        E[i,j]=boundary_even(a)*boundary_odd(b)/(2*(2*b+1-2*a))
            err=float(np.max(np.abs(E-C)))
            max_gram_err=max(max_gram_err,err)
            assert err<2e-11,(F,err)
            ev=np.linalg.eigvalsh(C)
            assert np.max(np.abs(ev+ev[::-1]-1))<3e-11,F
            r=min(len(evens),len(odds))
            mid=np.count_nonzero(np.abs(ev-0.5)<1e-9)
            assert mid==abs(len(evens)-len(odds)),(F,mid,ev)
            assert np.min(ev)>-1e-11 and np.max(ev)<1+1e-11,F
            if len(evens)<=4 and len(odds)<=4:
                gap=float(np.prod(np.abs(2*ev[np.abs(ev-0.5)>1e-9]-1)))
                minors=gap_product_from_minors(B)
                ge=abs(gap-minors)
                max_gap_err=max(max_gap_err,ge)
                assert ge<2e-10,(F,gap,minors)
            masks+=1
    assert masks==sum((1<<n)-1 for n in range(1,11))
    for m in range(1,11):
        B=centered_block(list(range(m)),list(range(m)))
        det_sq=float(np.linalg.det(B)**2)
        gamma_product=float(mp.fprod([mp.gamma(j+1)**2 /
                        (mp.gamma(j+mp.mpf('.5'))*mp.gamma(j+mp.mpf('1.5')))
                        for j in range(m)]))
        assert abs(det_sq-gamma_product)<1e-9,(m,det_sq,gamma_product)
    mp.mp.dps=40
    barnes_constant=mp.sqrt(mp.pi)*mp.barnesg(mp.mpf('.5'))**2
    logprod=sum(2*math.lgamma(j+1)-math.lgamma(j+.5)-math.lgamma(j+1.5)
                for j in range(10000))
    asymptotic_ratio=math.exp(logprod)*10000**.25
    assert abs(asymptotic_ratio-float(barnes_constant))<1e-5
    print('VERIFY_OK masks=%s max_gram_err=%.3e max_gap_err=%.3e exact_barnes_cases=10 asymptotic_ratio=%.9f target=%.9f' %
          (masks,max_gram_err,max_gap_err,asymptotic_ratio,float(barnes_constant)))

if __name__=='__main__': main()
