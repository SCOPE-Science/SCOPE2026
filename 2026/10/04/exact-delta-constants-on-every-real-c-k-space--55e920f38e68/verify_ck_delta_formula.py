from fractions import Fraction
from itertools import product


def phi(a, r):
    return sum((1-x)/(r+1-x) for x in a)


def canonical_separator(a, r):
    b=[1/(r+1-x) for x in a]
    s=sum(b)
    lam=[x/s for x in b]
    value=sum(l*x for l,x in zip(lam,a))
    bad=max(1-l*(r+1-x) for l,x in zip(lam,a))
    return value,bad


def brute_bad_support(a, r, w):
    # Bad set is a union of cube faces u_j <= a_j-r.
    best=None
    n=len(a)
    for j in range(n):
        lj=a[j]-r
        # Exact linear maximum on that face.
        val=Fraction(0)
        for i,wi in enumerate(w):
            if i==j:
                val += wi*(lj if wi>=0 else Fraction(-1))
            else:
                val += abs(wi)
        best=val if best is None or val>best else best
    return best

count=0
vals=[Fraction(i,5) for i in range(1,5)]
radii=[Fraction(i,10) for i in range(10,21)]
for n in range(1,5):
    for a in product(vals, repeat=n):
        for r in radii:
            if any(x <= r-1 for x in a):
                continue
            P=phi(a,r)
            v,b=canonical_separator(a,r)
            assert (v>b) == (P<1)
            # canonical weights, exact support check
            ww=[Fraction(1,1)/(r+1-x) for x in a]
            sw=sum(ww); ww=[x/sw for x in ww]
            assert b == brute_bad_support(a,r,ww)
            count += 1
print('VERIFY_OK', count)
