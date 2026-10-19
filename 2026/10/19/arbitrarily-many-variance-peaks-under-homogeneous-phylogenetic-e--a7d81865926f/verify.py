"""Reproduce finite checks for a multiple-peak phylogenetic-diversity variance theorem.

This is supplementary arithmetic. The all-orders existence statement is proved
analytically by an induction, not inferred from finite experiments.
"""
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction
from itertools import product

PREC = 48

def dec_floor(num,den=1):
    with localcontext() as ctx:
        ctx.prec=PREC; ctx.rounding=ROUND_FLOOR
        return Decimal(num)/Decimal(den)

def dec_ceil(num,den=1):
    with localcontext() as ctx:
        ctx.prec=PREC; ctx.rounding=ROUND_CEILING
        return Decimal(num)/Decimal(den)

def interval_plus(a,b):
    with localcontext() as c:
        c.prec=PREC; c.rounding=ROUND_FLOOR
        lo=a[0]+b[0]
    with localcontext() as c:
        c.prec=PREC; c.rounding=ROUND_CEILING
        hi=a[1]+b[1]
    return lo,hi

def interval_multiply(a,b):
    with localcontext() as c:
        c.prec=PREC; c.rounding=ROUND_FLOOR
        lo=min(x*y for x in a for y in b)
    with localcontext() as c:
        c.prec=PREC; c.rounding=ROUND_CEILING
        hi=max(x*y for x in a for y in b)
    return lo,hi

def interval_power_positive(a,k):
    assert 0<=a[0]<=a[1] and k>=0
    with localcontext() as c:
        c.prec=PREC; c.rounding=ROUND_FLOOR
        lo=a[0]**k
    with localcontext() as c:
        c.prec=PREC; c.rounding=ROUND_CEILING
        hi=a[1]**k
    return lo,hi

def interval_twice_minus_one(a):
    with localcontext() as c:
        c.prec=PREC; c.rounding=ROUND_FLOOR
        lo=2*a[0]-1
    with localcontext() as c:
        c.prec=PREC; c.rounding=ROUND_CEILING
        hi=2*a[1]-1
    return lo,hi

def derivative_interval(ks, lengths, denominator):
    assert all(k>=2 for k in ks)
    r=(dec_floor(denominator-1,denominator),dec_ceil(denominator-1,denominator))
    total=(Decimal(0),Decimal(0))
    for k,L in zip(ks,lengths):
        power=interval_power_positive(r,k)
        factor=interval_multiply(interval_power_positive(r,k-1),interval_twice_minus_one(power))
        scale=(Decimal(L.numerator**2*k)/Decimal(L.denominator**2),)*2
        total=interval_plus(total,interval_multiply(scale,factor))
    return total

def verify_example():
    ks=[2,512,100000]
    lengths=[Fraction(1),Fraction(1,4),Fraction(1,16)]
    checks=[]
    for k in ks:
        plus=derivative_interval(ks,lengths,4*k)
        minus=derivative_interval(ks,lengths,k)
        assert plus[0]>0 and minus[1]<0,(k,plus,minus)
        print('k=',k,'positive interval at 1/(4k):',plus,'negative interval at 1/k:',minus)
        checks.append((plus,minus))
    n=sum(ks)
    L=sum(lengths)
    eta=Fraction(2*n-2-len(ks),10**18)
    error_bound=6*n*L*eta+3*n*eta**2
    minimum_gap=min(min(plus[0],-minus[1]) for plus,minus in checks)
    assert dec_ceil(error_bound.numerator,error_bound.denominator)<minimum_gap
    print('n=',n,'large-branch lengths=',lengths,'other-branch length=1/10^18')
    print('global derivative error bound=',float(error_bound),'smallest signed-derivative margin>=',minimum_gap)
    print('at least three strict local maxima on disjoint intervals')

def verify_small_exact_variance():
    ks=(2,3)
    lengths=(Fraction(3,2),Fraction(2,3))
    n=sum(ks)
    for p in (Fraction(1,4),Fraction(1,2),Fraction(3,4)):
        mean=Fraction(0)
        second=Fraction(0)
        for bits in product((0,1), repeat=n):
            prob=p**sum(bits)*(1-p)**(n-sum(bits))
            x=(lengths[0] if any(bits[:2]) else 0)+(lengths[1] if any(bits[2:]) else 0)
            mean+=prob*x
            second+=prob*x*x
        v=second-mean*mean
        claimed=sum(L*L*((1-p)**k-(1-p)**(2*k)) for L,k in zip(lengths,ks))
        assert v==claimed,(p,v,claimed)
        print('exact subset check at p=',p,': variance=',v)

if __name__=='__main__':
    verify_small_exact_variance()
    verify_example()
    print('PASS: finite identities, outward-rounded witnesses, positive-edge perturbation bound')
