"""Exact-rational checks for the local order-two real-shift resolvent tradeoff.

Run with Python 3.11+: python check_residue_tradeoff.py
This is supplementary finite testing; the accompanying analytic dual certificate
establishes the result for the full real parameter domain.
"""
from fractions import Fraction as F
from random import Random


def extremizer(a, b, t):
    assert F(0) < a < b and a <= t <= b
    c, h = (a+b)/2, (b-a)/2
    d, delta = t-c, t*t/2
    if delta <= d*d+abs(d)*h:
        D = h+abs(d)
        lam = delta/(D*D-delta)
        v = a if d >= 0 else b
        u = (t+lam*v)/(1+lam)
        return lam, [(u, 1+lam), (v, -lam)], u, abs(u-v), 'outer'
    lam = (delta-d*d)/(h*h)
    return lam, [(c, 1+lam), (a, -(lam+d/h)/2),
                  (b, -(lam-d/h)/2)], c, h, 'inner'


def check(a,b,t):
    lam, atoms, center, radius, regime = extremizer(a,b,t)
    assert lam > 0 and radius > 0
    assert a <= center <= b
    assert radius >= max(center-a,b-center)
    assert all(a <= s <= b for s,w in atoms)
    assert sum((w for _, w in atoms), F(0)) == 1
    assert sum((w*s for s,w in atoms), F(0)) == t
    assert sum((w*s*s for s,w in atoms), F(0)) == t*t/2
    # Nonzero mass signs are equal to the corresponding dual certificate.
    q = lambda s: 1-2*(s-center)**2/radius**2
    assert all(q(s)==(1 if w>0 else -1) for s,w in atoms if w)
    assert q(a)>=-1 and q(b)>=-1 and q(center)==1
    Iq = 1-2*(t*t/2-2*center*t+center*center)/(radius*radius)
    assert Iq == sum((abs(w) for _,w in atoms), F(0)) == 1+2*lam
    return regime


def main():
    rng = Random(20261029)
    counts = {'outer':0,'inner':0}
    # Randomized rational exact arithmetic, including both lopsided regimes.
    for _ in range(2500):
        a=F(rng.randint(1,60),rng.randint(4,55))
        b=a+F(rng.randint(1,80),rng.randint(2,30))
        t=a+(b-a)*F(rng.randint(0,100),100)
        counts[check(a,b,t)]+=1
    for k in range(1,61):
        a,b,t=F(k,20),F(2*k+1,10),F(k,10)
        if a<=t<=b: counts[check(a,b,t)]+=1
    assert check(F(4,5),F(6,5),F(1)) == 'inner'
    lam,atoms,_,_,_ = extremizer(F(4,5),F(6,5),F(1))
    assert lam==F(25,2) and sorted(w for _,w in atoms)==[F(-25,4), F(-25,4),F(27,2)]
    print('EXACT_RATIONAL_CHECKS_PASS',sum(counts.values()),counts,'special_tv',1+2*lam)

if __name__=='__main__': main()
