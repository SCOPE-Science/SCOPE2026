#!/usr/bin/env python3
"""Reproducible numerical diagnostics for a geometric spectral crossover.

The mathematical theorem uses uniform Gamma-ratio asymptotics; these checks
are finite diagnostics, not a proof of the infinite-dimensional statement.
"""
import math


def log_ratio(n, p, j):
    if not (isinstance(n, int) and n >= 2 and isinstance(j, int) and j >= 1
            and 1.0 < p < n):
        raise ValueError('outside stated domain')
    delta = p - 1.0
    k = n - p
    lam = 2.0 * j * (2 * j + n - 2)
    loga = (math.lgamma(j - p/2) + math.lgamma((n+p)/2)
            - math.lgamma(-p/2) - math.lgamma(j + (n+p)/2))
    logD = math.log((k+math.hypot(k,2*math.sqrt(delta*lam)))/2)
    return (math.log(n+p) - 2*math.log(p) - math.log(delta)
            + 2*math.log1p(-k/lam) + 2*logD + 2*loga)


def constant_T(n):
    c = math.exp(math.lgamma((n+1)/2)-math.log(2)-0.5*math.log(math.pi))
    return (n+1)*(n-1)**2*c*c


def B(n, p, j):
    d=p-1.0
    k=n-p
    lam=2.0*j*(2*j+n-2)
    D=2*lam/(k+math.hypot(k,2*math.sqrt(d*lam)))
    loga=(math.lgamma(j-p/2)+math.lgamma((n+p)/2)
          - math.lgamma(-p/2)-math.lgamma(j+(n+p)/2))
    return p*d/2*D*D-(n+p)/(2*p)*(lam-k)**2*math.exp(2*loga)


def check():
    count=0
    # Independent finite-product eigenvalue computation; different formula.
    for n in (2,3,4,7):
        for p in (1.1, 1.4):
            if p>=n: continue
            for j in range(1,9):
                a=1.0
                for r in range(j):
                    a*=abs((p-2*r)/(n+p+2*r))
                loga=(math.lgamma(j-p/2)+math.lgamma((n+p)/2)
                      - math.lgamma(-p/2)-math.lgamma(j+(n+p)/2))
                assert abs(math.exp(loga)-a) <= 3e-13*max(a,1)
                assert (B(n,p,j)>0) == (log_ratio(n,p,j)<0)
                count += 2
    # Quantitative limiting threshold for the first strictly positive mode.
    for n in (2,3,4,5):
        for delta in (1e-5,1e-7,1e-9):
            p=1+delta
            j=1
            while log_ratio(n,p,j) >= 0:
                j+=1
            J=(constant_T(n)/delta)**(1/(n+2))
            assert abs(j/J-1)<0.36, (n,delta,j,J)
            assert log_ratio(n,p,j)<0
            if j>1: assert log_ratio(n,p,j-1)>=0
            count+=3
    # Fixed scaling variable, normalized B convergence; avoid cancellation at tau=T.
    for n in (2,3,4):
        T=constant_T(n)
        c=math.exp(math.lgamma((n+1)/2)-math.log(2)-0.5*math.log(math.pi))
        for fac in (0.5,2.0):
            for j in (50,100):
                delta=fac*T/j**(n+2)
                p=1+delta
                if p==1: continue  # floating-point resolution, not a mathematical limit
                normalized=B(n,p,j)*j**(n-2)/8
                expected=(fac*T-T)/(n-1)**2
                assert abs(normalized-expected)<0.1*max(1,abs(expected)), (n,j,fac,normalized,expected)
                count+=1
    return count

if __name__=='__main__':
    print('PASS',check(),'finite exact-formula and asymptotic diagnostics')
