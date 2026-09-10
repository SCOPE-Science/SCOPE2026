"""Rigorous rational interval arithmetic (stdlib only)."""
from fractions import Fraction
import math
S = 10**12  # sqrt resolution
def sqrt_bounds(a, b):
    """a<=b Fractions, >=0. Return (lo,hi) Fractions with lo<=sqrt(x)<=hi for all x in [a,b]."""
    assert a >= 0
    # lo from a
    klo = math.isqrt((a.numerator * S * S) // a.denominator)
    # hi from b: need ceil(sqrt(b)*S)/S
    q = (b.numerator * S * S) // b.denominator
    khi = math.isqrt(q)
    if khi * khi < q or (khi*S)  == 0 and False:
        pass
    # check exact: if khi^2 * b.denominator < b.numerator*S^2 then +1
    if khi * khi * b.denominator < b.numerator * S * S:
        khi += 1
    # safety: ensure hi covers: bump by 1 ulp
    khi += 1
    return Fraction(klo, S), Fraction(khi, S)
def addi(x, y): return (x[0]+y[0], x[1]+y[1])
def subi(x, y): return (x[0]-y[1], x[1]-y[0])
def muli(x, y):
    vs = [x[0]*y[0], x[0]*y[1], x[1]*y[0], x[1]*y[1]]
    return (min(vs), max(vs))
def recipi(x):
    assert x[0] > 0
    return (Fraction(1,1)/x[1], Fraction(1,1)/x[0])
def divi(x, y): return muli(x, recipi(y))
def powi(x, n):
    assert x[0] >= 0 and n >= 0
    return (x[0]**n, x[1]**n)
def width(x): return x[1]-x[0]
