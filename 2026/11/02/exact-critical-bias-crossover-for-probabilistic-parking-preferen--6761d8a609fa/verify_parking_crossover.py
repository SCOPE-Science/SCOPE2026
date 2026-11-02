#!/usr/bin/env python3
"""Reproduce the finite parking-preference law and its critical scaling."""
from fractions import Fraction
from itertools import product
from functools import lru_cache
from math import comb, sqrt, pi, lgamma, log, exp


def exact_a(n,s):
    # All bases are positive, so negative exponents have a rational meaning.
    return Fraction(comb(n-1,s), (n+1)**(n-1)) * Fraction(n-s)**(n-s-2) * Fraction(s+1)**(s-1)


def formula(n,p):
    a=[exact_a(n,s) for s in range(n)]
    return [Fraction(1,n+1)+a[s]/2 + (p-Fraction(1,2))*(sum(a[:s])-sum(a[s+1:]))
            for s in range(n-1,-1,-1)]


def enumeration(n,p):
    # Preference vectors equiprobable. At a collision the first direction is
    # forward with probability p; a blocked direction counts as failure.
    @lru_cache(None)
    def success(preferences,step,mask):
        if step==n:
            return Fraction(1)
        j=preferences[step]-1
        if not ((mask>>j)&1):
            return success(preferences,step+1,mask|(1<<j))
        right=next((k for k in range(j+1,n) if not ((mask>>k)&1)),None)
        left=next((k for k in range(j-1,-1,-1) if not ((mask>>k)&1)),None)
        return ((p*success(preferences,step+1,mask|(1<<right)) if right is not None else 0)
                +((1-p)*success(preferences,step+1,mask|(1<<left))) if left is not None else
                (p*success(preferences,step+1,mask|(1<<right)) if right is not None else 0))
    counts=[Fraction(0) for _ in range(n)]
    for prefs in product(range(1,n+1),repeat=n):
        counts[prefs[-1]-1]+=success(prefs,0,0)
    return [c/sum(counts) for c in counts]


def scaled_tv(n,lam):
    # A log-gamma computation prevents overflow in the large-n sums.
    import numpy as np
    s=np.arange(n,dtype=float)
    k=n-s
    loga=lgamma(n) if False else None
    from scipy.special import gammaln
    loga=gammaln(n)-gammaln(s+1)-gammaln(n-s)+(k-2)*np.log(k)+(s-1)*np.log(s+1)-(n-1)*np.log(n+1)
    a=np.exp(loga)
    d=np.r_[0,np.cumsum(a)[:-1]]-(np.cumsum(a[::-1])[::-1]-a)
    p=.5+lam/sqrt(n)
    q=1/(n+1)+a/2+(p-.5)*d
    assert abs(q.sum()-1)<1.e-8
    return n*.5*float(np.abs(q-1/n).sum())


def main():
    checks=0
    for n in range(2,6):
        for p in (Fraction(0),Fraction(1,4),Fraction(1,2),Fraction(3,4),Fraction(1)):
            assert enumeration(n,p)==formula(n,p), (n,p)
            checks+=1
        a=[exact_a(n,s) for s in range(n)]
        assert sum(a)==Fraction(2,n+1)
        assert a==a[::-1]
        checks+=2
    # Cross-over asymptotics: finite errors decrease with n in representative cases.
    for lam in (0.,.25,.5,1.,2.):
        target=(1+sqrt(1+32*lam*lam/pi))/2
        errs=[abs(scaled_tv(n,lam)-target) for n in (500,2000,10000)]
        assert errs[2]<errs[1]<errs[0],(lam,errs)
        checks+=3
    print(f'PASS: {checks} exact and asymptotic reproducibility checks')

if __name__=='__main__':
    main()
