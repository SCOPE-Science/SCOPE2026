from fractions import Fraction
from collections import defaultdict
from math import comb, sqrt
from decimal import Decimal, getcontext


def hit_dp(r, p):
    live={0: Fraction(1)}
    hit=Fraction(0)
    for _ in range(p):
        nxt=defaultdict(Fraction)
        for s,prob in live.items():
            up=s+1
            if up>=r:
                hit += prob/2
            else:
                nxt[up] += prob/2
            nxt[s-r] += prob/2
        live=dict(nxt)
    return hit


def first_passage_term(r,d):
    n=(r+1)*d+r
    return Fraction(r*comb(n,d), n*(2**n))


def closed_finite(r,p):
    if p<r:
        return Fraction(0)
    return sum((first_passage_term(r,d) for d in range((p-r)//(r+1)+1)), Fraction(0))


def brute_event(r, bits):
    pos=neg=0
    s=0
    threshold=False
    hit=False
    for b in bits:
        if b:
            pos += 1
            s += 1
        else:
            neg += 1
            s -= r
        if pos>0 and pos >= r*(neg+1):
            threshold=True
        if s>=r:
            hit=True
    return threshold,hit

# Exact finite-horizon identity, many horizons and reciprocal levels.
for r in range(2,13):
    for p in range(0,151):
        assert hit_dp(r,p)==closed_finite(r,p)

# Direct threshold/random-walk equivalence for every short sign pattern.
for r in range(2,5):
    for p in range(0,10):
        for mask in range(1<<p):
            bits=[(mask>>i)&1 for i in range(p)]
            assert brute_event(r,bits)[0]==brute_event(r,bits)[1]

# Exact special cases.
assert closed_finite(2,2)==Fraction(1,4)
assert closed_finite(2,5)==Fraction(5,16)
assert closed_finite(10,10)==Fraction(1,1024)
assert closed_finite(10,20)==Fraction(1,1024)

# High-precision smallest root of 2 f = 1 + f^(r+1).
getcontext().prec=80
def root_f(r):
    lo=Decimal('0.5'); hi=Decimal('0.999999999999999999999999999999999999')
    def h(x): return Decimal(2)*x-Decimal(1)-x**(r+1)
    # h(lo)<0 in this sign convention, h is positive after the small root.
    for _ in range(300):
        mid=(lo+hi)/2
        if h(mid)<=0:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2

f2=root_f(2)
f10=root_f(10)
lim2=f2**2
lim10=f10**10
assert abs(float(lim2)-(3-sqrt(5))/2) < 1e-14
assert abs(float(lim10)-0.0009813672898988613365907608708471381) < 1e-18
# Finite probabilities increase toward the root formula.
for r in [2,3,4,5,10]:
    f=root_f(r); lim=f**r
    vals=[Decimal(closed_finite(r,p).numerator)/Decimal(closed_finite(r,p).denominator) for p in [r,2*r,5*r,20*r,100*r]]
    assert all(vals[i] <= vals[i+1] for i in range(len(vals)-1))
    assert vals[-1] <= lim

print('VERIFY_OK')
print('r=2 limit', lim2)
print('r=10 limit', lim10)
