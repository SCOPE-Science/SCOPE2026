"""Exact integer and rational verification of conditional cherry laws in uniform plane binary trees.

Run with Python 3.9+; no external dependencies. This supplements the all-size proof.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from math import comb

checks = 0

def expect(flag, message='failed exact identity'):
    global checks
    checks += 1
    if not flag:
        raise AssertionError(message)


def catalan(n):
    return comb(2*n, n)//(n+1)


def cherry_formula(n, j):
    if n == 0:
        return int(j == 0)
    if j < 1 or j > (n+1)//2:
        return 0
    numerator = comb(n, j)*comb(n-j, j-1)*2**(n-2*j+1)
    expect(numerator % n == 0)
    return numerator//n

@lru_cache(None)
def cherry_poly(n):
    if n == 0:
        return (1,)
    res = Counter()
    for a in range(n):
        b = n-1-a
        for i, ai in enumerate(cherry_poly(a)):
            for j, bj in enumerate(cherry_poly(b)):
                if ai and bj:
                    res[i+j+int(n==1)] += ai*bj
    return tuple(res.get(i,0) for i in range(max(res)+1))

@lru_cache(None)
def shapes(n):
    if n == 0:
        return (None,)
    return tuple((left,right) for k in range(n) for left in shapes(k) for right in shapes(n-1-k))


def cherries(t):
    if t is None:
        return 0
    return (int(t[0] is None and t[1] is None)+cherries(t[0])+cherries(t[1]))


def convolve(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=x*y
    return tuple(out)


def tails(poly):
    return tuple(sum(poly[t:]) for t in range(len(poly)+1))


def stoch_leq(poly_a,poly_b):
    ta,tb=tails(poly_a),tails(poly_b)
    dena,denb=sum(poly_a),sum(poly_b)
    return all((ta[t] if t<len(ta) else 0)*denb <= (tb[t] if t<len(tb) else 0)*dena
               for t in range(max(len(ta),len(tb))))

# All-size coefficient and normalization formulas, and independent Catalan recurrence.
for n in range(0,160):
    p=cherry_poly(n)
    expect(sum(p)==catalan(n),f'Catalan normalization n={n}')
    for j in range(max(len(p),(n+1)//2+2)):
        expect((p[j] if j<len(p) else 0)==cherry_formula(n,j),f'coefficient n={n},j={j}')

# Check a second, direct enumeration of actual ordered binary-tree shapes.
for n in range(0,10):
    s=shapes(n)
    expect(len(s)==catalan(n))
    hist=Counter(cherries(t) for t in s)
    for j in range((n+1)//2+2):
        expect(hist[j]==cherry_formula(n,j))
    if n>1:
        for k in range(n):
            # Enumerate every left/right subtree pair independently.
            h=Counter(cherries((a,b)) for a in shapes(k) for b in shapes(n-1-k))
            target=convolve(cherry_poly(k),cherry_poly(n-1-k))
            for j in range(len(target)):
                expect(h[j]==target[j],f'split {n},{k}, cherry {j}')

# Verify the exact stochastic boundary and all split distributions.
for n in range(3,100):
    split=lambda k: convolve(cherry_poly(k),cherry_poly(n-1-k))
    expect(stoch_leq(split(0),split(1)))
    if n>=4:
        expect(stoch_leq(split(2),split(1)))
    if n>=7:
        a,b=split(2),split(3)
        expect(not stoch_leq(a,b),f'mean should prohibit A<=B n={n}')
        expect(not stoch_leq(b,a),f'top tail should prohibit B<=A n={n}')
        m=n-3
        f=lambda j: Fraction(j*(j+1),2*(2*j-1)) if j else Fraction(0)
        expect(f(m)-f(m-1)>f(3)-f(2))
        if n%2==1:
            expect(max(j for j,v in enumerate(b) if v)>max(j for j,v in enumerate(a) if v))
        else:
            top=n//2
            expect(Fraction(b[top],sum(b))/Fraction(a[top],sum(a))==Fraction(2*n-7,5))

# Sharp first crossing (both directions) at n=7; no crossing in an inward step for n<7.
for n in range(3,7):
    for k in range((n-1)//2):
        aa=convolve(cherry_poly(k),cherry_poly(n-1-k))
        bb=convolve(cherry_poly(k+1),cherry_poly(n-2-k))
        expect(stoch_leq(aa,bb) or stoch_leq(bb,aa),f'minimality {n} {k}')

a=convolve(cherry_poly(2),cherry_poly(4))
b=convolve(cherry_poly(3),cherry_poly(3))
expect(a==(0,0,16,12))
expect(b==(0,0,16,8,1))
expect(Fraction(sum(a[3:]),sum(a))==Fraction(3,7))
expect(Fraction(sum(b[3:]),sum(b))==Fraction(9,25))
expect(Fraction(sum(b[4:]),sum(b))==Fraction(1,25))

# Rémy growth numbers count the same number of forward and backward decorated moves.
for m in range(1,160):
    expect(2*(2*m+1)*catalan(m)==(m+2)*catalan(m+1))

print('PASS:',checks,'exact checks; sharp n=7, infinite-family parity/mean certificates and enumerations verified')
