"""Independent deterministic grid checks for uniform random circular spacings.

Run: python circle_coverage_verification.py
The rigorous all-n argument is in RESULT.md; these lattice checks are finite tests.
"""
from fractions import Fraction
from math import comb, exp


def covariance_formula(n, s):
    a = 1 - s
    b = max(1 - 2*s, 0)
    return a**n - n*a**(2*n-1) + (n-1)*b**n


def variance_formula(n, s):
    a = 1-s
    b = max(1-2*s, 0)
    return (2*a**(n+1)+(n-1)*b**(n+1))/(n+1)-a**(2*n)


def compositions(total, count):
    if count == 1:
        yield (total,)
    else:
        for first in range(total+1):
            for rest in compositions(total-first, count-1):
                yield (first,)+rest


def lattice_covariance(n, denominator, s):
    # All uniform grid points of the simplex, equally weighted.
    # Their averages converge to Dirichlet(1,...,1) integrals.
    acc_count = Fraction(0)
    acc_uncovered = Fraction(0)
    acc_product = Fraction(0)
    N = comb(denominator+n-1, n-1)
    for k in compositions(denominator, n):
        positive = [Fraction(x, denominator)-s for x in k]
        count = sum(x>0 for x in positive)
        uncovered = sum((x for x in positive if x>0), Fraction(0))
        acc_count += count
        acc_uncovered += uncovered
        acc_product += count*uncovered
    return acc_product/N - (acc_count/N)*(acc_uncovered/N)


def one_dimensional_integral(n, s):
    assert n == 2
    # Exact direct integration on x in [0,1] by polynomial antiderivatives.
    cuts = sorted(set([Fraction(0), min(s,1-s), max(s,1-s), Fraction(1)]))
    eb = eu = ebu = Fraction(0)
    for lo, hi in zip(cuts,cuts[1:]):
        mid = (lo+hi)/2
        # U(x)=A*x+B, B(x) constant on each open interval.
        terms = []
        if mid > s: terms.append((Fraction(1),-s))
        if 1-mid > s: terms.append((Fraction(-1),1-s))
        count=len(terms)
        A=sum((x for x,y in terms),Fraction(0)); B=sum((y for x,y in terms),Fraction(0))
        integral=A*(hi*hi-lo*lo)/2+B*(hi-lo)
        eb += count*(hi-lo)
        eu += integral
        ebu += count*integral
    return ebu-eb*eu


def verify():
    for n in range(2,8):
        for s in (Fraction(1,10),Fraction(1,4),Fraction(2,5),Fraction(1,2),Fraction(3,5)):
            assert variance_formula(n,s)>=0
            delta=Fraction(1,100000)
            if 0<s-delta and s+delta<1:
                numerical=(variance_formula(n,s+delta)-variance_formula(n,s-delta))/(2*delta)
                assert abs(numerical+2*covariance_formula(n,s))<Fraction(1,100000)
    for s in (Fraction(1,10),Fraction(2,5),Fraction(1,2),Fraction(3,5)):
        assert one_dimensional_integral(2,s)==covariance_formula(2,s)
    checks=[(2,600,Fraction(2,5)),(2,600,Fraction(3,5)),
            (3,160,Fraction(1,5)),(3,160,Fraction(9,20)),
            (4,60,Fraction(1,5)),(4,60,Fraction(2,5))]
    for n,M,s in checks:
        observed=lattice_covariance(n,M,s)
        expected=covariance_formula(n,s)
        print('n',n,'mesh',M,'s',str(s),'grid',float(observed),'exact',float(expected))
        assert abs(observed-expected)<Fraction(1,25)
        assert observed*expected>0
    # Finite analytic sign tests across a mesh, not a uniqueness proof.
    for n in range(2,31):
        svals=[Fraction(i,2000) for i in range(1,2000)]
        signs=[-1 if covariance_formula(n,s)<0 else (1 if covariance_formula(n,s)>0 else 0) for s in svals]
        assert signs[0]<0 and signs[-1]>0
        assert all(signs[i]<=signs[i+1] for i in range(len(signs)-1))
    from math import log
    def root_of_cov(n):
        low, high = 1e-12/n, 0.5
        for _ in range(100):
            mid = (low+high)/2
            if covariance_formula(n,mid)>0:
                high=mid
            else:
                low=mid
        return (low+high)/2
    c_low,c_high=1.5,2.0
    for _ in range(100):
        mid=(c_low+c_high)/2
        if exp(mid)>1+mid+mid**2:c_high=mid
        else:c_low=mid
    c=(c_low+c_high)/2
    alpha=c*(2*c-1)/2
    print('limiting critical density',format(c,'.14f'),'first correction',format(alpha,'.12f'))
    for n in [2,3,4,5,10,20,50,100,200,500]:
        x=n*root_of_cov(n)
        print('n',n,'critical density',format(x,'.12f'))
        assert 0<x<c+1e-9
        if n>=100:
            assert abs(x-(c-alpha/n))<3/n**2
    print('All deterministic consistency checks passed.')

if __name__=='__main__':
    verify()
