"""Standalone checks for the two-scale Gaussian curvature classification.

Usage: python3 verify.py
Only Python's standard library is required. Finite tests check formulas and
examples; the theorem for all parameters is established in RESULT.md.
"""
import math
from fractions import Fraction as Q

checks = 0

def check(p, note):
    global checks
    checks += 1
    if not p:
        raise AssertionError(note)

# Exact rational algebra for the derivative of F_q(t).
for qi in range(1, 14):
    q = Q(qi, 7)
    for ti in range(1, 31):
        t = Q(ti, 13)
        direct = 1/t - q/(2*t*t) + (q+1)/2
        factored = ((q+1)*t*t + 2*t - q)/(2*t*t)
        check(direct == factored, 'derivative identity')

# An exact-series certificate for 7 < exp(2) < 15/2.
S = sum(Q(2**n, math.factorial(n)) for n in range(7))
tail = Q(2**7, math.factorial(7)) / (1-Q(2,8))
check(Q(7) < S, 'exp(2) lower bound')
check(S+tail < Q(15,2), 'exp(2) upper bound')
# For 0<x<1, exp(x)<1/(1-x) by termwise comparison.
# This and the exact rational square comparisons yield 1<R(1/3)<15/11.
check(Q(6,5)**2 < Q(13,9) < Q(5,4)**2, 'sqrt(13)/3 bracket')
check(Q(28,27) > 1 and Q(15,11) < Q(16,9), 'four-dimensional bracket')

# Independent finite numerical curvature tests at many radii and parameters.
def constants(q):
    h = math.sqrt(1+q*(q+1))
    tstar = q/(1+h)
    R = tstar*math.exp(q+h+0.5)
    return tstar,R

def radial_curvature(rad, d, small, large, w):
    alpha=1/(large*large)
    beta=1/(small*small)
    delta=beta-alpha
    r=(w/(1-w))*(large/small)**d
    t=r*math.exp(-delta*rad*rad/2)
    u=(alpha+beta*t)/(1+t)
    return -u+delta**2 * rad**2 * t/(1+t)**2

def direct_second(rad,d,small,large,w):
    # Analytically independent quotient differentiation of a two-term sum.
    alpha=1/(large*large)
    beta=1/(small*small)
    A=(1-w)*large**(-d)
    B=w*small**(-d)
    a=A*math.exp(-alpha*rad*rad/2)
    b=B*math.exp(-beta*rad*rad/2)
    f=a+b
    fp=-rad*(alpha*a+beta*b)
    fpp=(alpha**2*rad*rad-alpha)*a+(beta**2*rad*rad-beta)*b
    return fpp/f-(fp/f)**2

for d in (1,2,3,4,7,11):
    for small,large in ((1.,1.25),(1.,2.),(1.,3.)):
        q=small**2/(large**2-small**2)
        tstar,R=constants(q)
        check(tstar>0 and R>tstar, 'positive critical ratio')
        wc=R/(R+(large/small)**d)
        for w in (wc*0.8, wc, (wc+1)/2):
            for rad in [0.0,0.3,1.0,2.0,3.0,4.0,6.0,10.0]:
                h1=radial_curvature(rad,d,small,large,w)
                h2=direct_second(rad,d,small,large,w)
                check(abs(h1-h2) < 2e-11*max(1,abs(h1)), 'direct curvature comparison')
            r=(w/(1-w))*(large/small)**d
            if w>wc:
                delta=small**(-2)-large**(-2)
                radius=math.sqrt(2*math.log(r/tstar)/delta)
                check(radial_curvature(radius,d,small,large,w)>1e-12,'strict failure witness')
            elif w<wc:
                for j in range(121):
                    rad=12*j/120
                    check(radial_curvature(rad,d,small,large,w)<0, 'below-cutoff curvature')

# Exact consequence of the analytic bound above: in dimension 3 the narrow
# component weight 1/10 lies below cutoff, whereas in dimension 4 it lies above.
q=1/3
_,R=constants(q)
check(Q(8,9)<1<R<Q(15,11)<Q(16,9), 'projection counterexample')
check(8/9<R<16/9,'dimension threshold example')
print('PASS: %d checks; exact rational Taylor bound; direct curvature comparisons; dimension counterexample.'%checks)
