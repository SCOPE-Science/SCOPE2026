"""Reproducibility checks for the directed inhibitory clipped logistic ring theorem.

Only standard-library Python is required. Finite checks support, but do not
replace, the proof for arbitrary ring size and parameters.
"""
from fractions import Fraction as Q
from math import cos, pi, sqrt
from cmath import exp
from itertools import product


def lucas(n):
    a, b = 2, 1
    for _ in range(n):
        a, b = b, a+b
    return a


def fixed_candidates(n, r, gamma):
    h = 1-Q(1, 1)/r
    ans = []
    for bits in product((0, 1), repeat=n):
        if any(bits[i] and bits[(i+1)%n] for i in range(n)):
            continue
        ans.append(tuple(h if b else Q(0) for b in bits))
    ans.append(tuple(h/(1+gamma) for _ in range(n)))
    return ans


def clipped_map(x,r,gamma):
    n=len(x)
    return tuple(max(Q(0), min(Q(1),r*x[i]*(1-x[i]-gamma*x[(i+1)%n]))) for i in range(n))


def spectrum(n,r,gamma):
    t=(r-1)/(1+gamma)
    return [1-t*(1+gamma*exp(2j*pi*k/n)) for k in range(n)]


def r_crit(n,gamma):
    c=cos(pi/n)
    return 1 + 2*(1+gamma)*(1-gamma*c)/(1+gamma**2-2*gamma*c)


for n in range(3, 13):
    for r, gamma in ((Q(5,2),Q(3,2)), (Q(7,5),Q(13,10)),(Q(11,4),Q(5,4))):
        cs=fixed_candidates(n,r,gamma)
        assert len(cs)==lucas(n)+1, (n,len(cs),lucas(n))
        assert len(set(cs)) == len(cs)
        assert all(clipped_map(x,r,gamma)==x for x in cs)

for n in range(3, 22):
    if n%2 == 0:
        assert max(abs(z) for z in spectrum(n,2.1,1.01)) > 1
        assert max(abs(z) for z in spectrum(n,1.3,6.0)) > 1
    else:
        sec=1/cos(pi/n)
        for gamma in (1+0.2*(sec-1), 1+0.5*(sec-1),1+0.9*(sec-1)):
            rc=r_crit(n,gamma)
            assert 1<rc<3
            assert max(abs(z) for z in spectrum(n,(1+rc)/2,gamma))<1-1e-8
            assert abs(max(abs(z) for z in spectrum(n,rc,gamma))-1)<1e-8
            assert max(abs(z) for z in spectrum(n,(rc+3)/2,gamma))>1+1e-8
        assert max(abs(z) for z in spectrum(n,1.2,sec+0.02))>1

for n in (4,6,8,10):
    r=Q(12,5); gamma=Q(7,4); h=1-1/r
    for parity in (0,1):
        x=tuple(h if i%2==parity else Q(0) for i in range(n))
        assert clipped_map(x,r,gamma)==x
        # At the zero sites the one-sided diagonal multiplier is <1;
        # at positive sites the scalar multiplier has modulus <1.
        beta=max(0,float(r*(1-gamma*h)))
        assert beta<1
        assert abs(2-float(r))<1

print('PASS: exact fixed-candidate census and fixed equations, N=3..12')
print('PASS: odd-ring sharp spectral thresholds and even-ring instabilities, N=3..21')
print('PASS: checkerboard local multipliers and support, even N=4..10')
print('These are finite checks only; the all-N statements follow from the proof.')
