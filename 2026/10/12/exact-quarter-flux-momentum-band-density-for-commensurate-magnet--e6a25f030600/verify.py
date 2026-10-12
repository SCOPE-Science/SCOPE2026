#!/usr/bin/env python3
from fractions import Fraction
from math import gcd

def fl(x: Fraction) -> int:
    return x.numerator // x.denominator

def formula(p, q):
    s = p + q
    corr = Fraction(0, 1)
    if p % 2:
        corr += Fraction(1, p)
    if q % 2:
        corr += Fraction(1, q)
    return Fraction(3, 4) - corr / (4 * s)

def direct(p, q):
    s = p + q
    roots = {Fraction(0), Fraction(1)}
    roots.update(Fraction(m, p) for m in range(p + 1))
    roots.update(Fraction(m, q) for m in range(q + 1))
    for m in range(s):
        r = Fraction(2*m + 1, 2*s)
        if 0 < r < 1:
            roots.add(r)
    roots = sorted(roots)
    good = Fraction(0)
    for a, b in zip(roots, roots[1:]):
        if a == b:
            continue
        u = (a + b) / 2
        exponent = 1 + fl(s*u + Fraction(1,2)) + fl(p*u) + fl(q*u)
        if exponent % 2 == 0:
            good += b - a
    return good

def D_direct(n):
    cuts = sorted({Fraction(0), Fraction(1,2), Fraction(1)} | {Fraction(m,n) for m in range(n+1)})
    left = right = Fraction(0)
    for a,b in zip(cuts,cuts[1:]):
        if a==b: continue
        mid=(a+b)/2
        val=fl(n*mid)
        piece=(b-a)*val
        if mid < Fraction(1,2): left += piece
        else: right += piece
    return left-right

def D_formula(n):
    return -Fraction(n,4) + (Fraction(1,4*n) if n%2 else 0)

for n in range(1,101):
    assert D_direct(n) == D_formula(n), (n,D_direct(n),D_formula(n))
count=0
for p in range(1,41):
    for q in range(1,41):
        if gcd(p,q) != 1:
            continue
        a=direct(p,q); b=formula(p,q)
        assert a == b, (p,q,a,b)
        count += 1
examples={(1,1):Fraction(1,2),(1,2):Fraction(2,3),(2,3):Fraction(11,15),(4,5):Fraction(67,90)}
for pq,want in examples.items():
    assert direct(*pq)==want
print('VERIFY_OK', 'pairs='+str(count), 'P11='+str(direct(1,1)), 'P45='+str(direct(4,5)))
