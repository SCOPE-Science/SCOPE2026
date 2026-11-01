"""Reproducible exact finite-horizon and spectral tests for iid complementary-cylinder holes."""
from fractions import Fraction
from itertools import product
from math import log

import numpy as np


def brute_survival(k, p, n):
    """Average survival over the source digits and iid holes via independent word summation."""
    q = 1-p
    total = Fraction(0)
    for bits in product((0, 1), repeat=n+k-1):
        wt = Fraction(1)
        for i in range(n):
            b = bits[i:i+k]
            if all(t==0 for t in b):
                wt *= q
            elif all(t==1 for t in b):
                wt *= p
        total += wt
    return total/Fraction(2**(n+k-1))


def state_survival(k, p, n):
    """Different calculation using the 2(k-1)-state truncated-run transfer."""
    states = [(c,j) for c in (0,1) for j in range(1,k)]
    counts = {s:Fraction(0) for s in states}
    for bits in product((0,1), repeat=k-1):
        c=bits[-1]; j=1
        for v in bits[-2::-1]:
            if v!=c: break
            j+=1
        counts[(c,j)]+=1
    for _ in range(n):
        new={s:Fraction(0) for s in states}
        for (c,j),v in counts.items():
            new[(1-c,1)]+=v
            new[(c,min(k-1,j+1))]+=v*(1 if j<k-1 else (1-p if c==0 else p))
        counts=new
    return sum(counts.values(),Fraction(0))/Fraction(2**(n+k-1))


def A(k, w, lam):
    return sum(lam**(-j) for j in range(1,k)) + w*lam**(-(k-1))/(lam-w)


def root(k,p):
    lo,hi=1.000000000001,2.
    for _ in range(95):
        mid=(lo+hi)/2
        if A(k,p,mid)*A(k,1-p,mid)>1: lo=mid
        else: hi=mid
    return (lo+hi)/2


def independent_perron(k,p):
    states=[(c,j) for c in (0,1) for j in range(1,k)]
    ix={s:i for i,s in enumerate(states)}
    mat=np.zeros((len(states),len(states)))
    for c,j in states:
        mat[ix[c,j],ix[1-c,1]]+=1
        mat[ix[c,j],ix[c,min(k-1,j+1)]]+=(1 if j<k-1 else (1-p if c==0 else p))
    return max(abs(z) for z in np.linalg.eigvals(mat))

def test():
    cases=0
    for k in (3,4,5,6):
        for p in (Fraction(0),Fraction(1,5),Fraction(1,2),Fraction(4,5),Fraction(1)):
            for n in range(0,8):
                z=brute_survival(k,p,n)
                assert z==state_survival(k,p,n),(k,p,n,z)
                cases+=1
    for k in (3,4,5,6,8,12):
        rr=[root(k,p) for p in (0.,.1,.25,.5)]
        for p in (0.,.1,.25,.5,.75,1.):
            assert abs(root(k,p)-independent_perron(k,p))<1e-12,(k,p)
        assert rr[0]>rr[1]>rr[2]>rr[3],(k,rr)
        l=rr[-1]
        assert abs((2-l)*(2*l-1)*l**(k-2)-1)<1e-11
    for k in (8,12,16,20,24):
        e=2**(-k)
        for p in (0.,.1,.5,.9,1.):
            B=p/(1+p)+(1-p)/(2-p)
            gamma=log(2/root(k,p))
            assert abs(gamma/e-B)<4*k*e, (k,p,gamma/e,B)
    print(f'PASS: {cases} independent exact-rational finite-horizon comparisons; 36 transfer-eigenvalue tests; monotonicity, fair-root and small-hole spectral checks passed')

if __name__=='__main__':
    test()
