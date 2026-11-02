"""Exact-rational and numerical spot checks for the beta-threshold cascade theorem.

Run: python checker.py
Only verifies finite instances; the all-parameter conclusions use the analytic proof.
"""
from fractions import Fraction
from math import comb, exp, expm1, log1p


def cumulative(b, k):
    x = Fraction(1, k)
    return 1 - (1 - x)**b * (1 + b*x)


def independent_cumulative(b, k):
    # Direct integration of b(b+1)*t*(1-t)^(b-1), using binomial expansion.
    x = Fraction(1, k)
    return b*(b+1) * sum(
        ((-1)**j * comb(b-1,j) * x**(j+2) / (j+2))
        for j in range(b)
    )


def branch(b,k):
    return (k-1)*cumulative(b,k)


def branch_float(b,k):
    x = 1.0/k
    return (k-1)*(-expm1(b*log1p(-x)) - b*x*exp(b*log1p(-x)))


checks=0
for b in range(1,37):
    ks = list(range(2, min(3000, 10*b*b+100)))
    vals=[branch(b,k) for k in ks]
    for k in range(2, min(60,ks[-1])+1):
        assert cumulative(b,k)==independent_cumulative(b,k), (b,k)
        checks+=1
    # Unimodality means no later increase after a strict decrease.
    phase=0
    for left,right in zip(vals,vals[1:]):
        if right<left:
            phase=1
        if phase==1:
            assert right<=left, (b,ks[vals.index(left)])
        checks+=1
    # The supercritical integers form a contiguous set.
    sup=[k for k,v in zip(ks,vals) if v>1]
    assert not sup or sup==list(range(sup[0],sup[-1]+1)),b
    if b>=4:
        assert branch(b,2)<1<branch(b,3)
        assert not sup or sup[0]==3
    checks+=1

# Stable numerical quadratures and high-b quantitative scaling.
from scipy.integrate import quad
from scipy.optimize import brentq
for b in (3,4,10,50,100,1000):
    for k in (3,5,max(3,b//2),max(3,b*b//2)):
        reference=quad(lambda t:b*(b+1)*t*(1-t)**(b-1),0,1/k,epsabs=1e-13)[0]
        assert abs(reference-(-expm1(b*log1p(-1/k))-b/k*exp(b*log1p(-1/k))))<1e-11,(b,k)
        checks+=1

y0=brentq(lambda y:exp(y)-1-y-y*y,1.2,3.5)
assert 1.79<y0<1.80
for b in (100,500,1000):
    f=lambda k:branch_float(b,k)-1
    root=brentq(f,b*b/4,b*b)
    estimate=b*b/2-b/6-Fraction(13,18)
    assert abs(root-float(estimate))<0.03, (b,root,estimate)
    from scipy.optimize import minimize_scalar
    peak=minimize_scalar(lambda k:-branch_float(b,k),bounds=(b/3,b),method='bounded').x
    assert abs(peak/b -1/y0)<0.02,(b,peak)
    checks+=1
print(f'PASS: {checks} exact-rational comparisons and supplementary numerical checks')
print('limiting optimal degree / b:',1/y0)
print('limiting max branching / b:',(1-exp(-y0)*(1+y0))/y0)
