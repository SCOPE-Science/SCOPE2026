"""Independent numerical checks for the two-pulse three-reservoir hydrograph theorem.
Run: python verify.py. Requires Python standard library only.
Checks are finite and do not replace the analytic proof.
"""
import math
import random

def h(t):
    return t*t*math.exp(-t)/2 if t >= 0 else 0.0

def d_h(t):
    return t*(2-t)*math.exp(-t)/2 if t >= 0 else 0.0

def cutoff(d):
    if d <= 2:
        raise ValueError('Requires d>2')
    return math.exp(-d)*(d+math.sqrt(d*d-4))**2/4

def stationary_after(d,m):
    M=m*math.exp(d)
    # F(t) = t(2-t)+M(t-d)(2-t+d).
    a=-(1+M)
    b=2+2*M*(d+1)
    c=-M*d*(d+2)
    disc=b*b-4*a*c
    if disc<=0:
        return []
    r=[(-b-math.sqrt(disc))/(2*a),(-b+math.sqrt(disc))/(2*a)]
    return sorted(x for x in r if x>d+1.e-11)

def deriv_after(d,m,t):
    return d_h(t)+m*d_h(t-d)

rng=random.Random(812857)
checks=0
for _ in range(4000):
    d=rng.uniform(2.001,12)
    mc=cutoff(d)
    m=mc*math.exp(rng.uniform(-1.1,1.1))
    # Avoid numerical cancellation close to fold.
    if abs(m/mc-1)<0.001:
        continue
    roots=stationary_after(d,m)
    expected=2 if m>mc else 0
    assert len(roots)==expected,(d,m,mc,roots)
    if roots:
        left,right=roots
        assert d<left<right
        assert deriv_after(d,m,(d+left)/2)<0
        assert deriv_after(d,m,(left+right)/2)>0
        assert deriv_after(d,m,right+0.1)<0
    checks+=1

m=.3
cases=[(2.1,2),(3.,1),(5.,2)]
for d, expected_peaks in cases:
    n=1+(2 if m>cutoff(d) else 0)//2
    assert n == expected_peaks
    print('delay',d,'load',m,'cutoff',cutoff(d),'maxima',n)

star=2*math.sqrt(2)
ms=(3+2*math.sqrt(2))*math.exp(-star)
assert abs(cutoff(star)-ms)<1e-13
for e in (.00001,.001,.01,.1,.7):
    assert cutoff(star-e)<ms and cutoff(star+e)<ms
assert math.exp(-2)<m<ms
print('randomized cases',checks,'critical separation',star,'maximum cutoff',ms)
print('PASS')
