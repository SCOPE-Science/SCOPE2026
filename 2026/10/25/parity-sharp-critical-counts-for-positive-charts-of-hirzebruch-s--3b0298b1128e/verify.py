"""Independent finite exact-rational sanity checks for the stated complex surface family.
The universal result rests on the accompanying mathematical proof, not this sample.
"""
from fractions import Fraction
from math import comb


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def divide(a, b):
    a, b = trim(a), trim(b)
    q = [Fraction(0)] * max(1, len(a) - len(b) + 1)
    while len(a) >= len(b) and a != [0]:
        d = len(a) - len(b)
        c = Fraction(a[-1], b[-1])
        q[d] += c
        for j, z in enumerate(b):
            a[j + d] -= c*z
        a = trim(a)
    return trim(q), trim(a)


def gcd(a, b):
    a, b = trim(a), trim(b)
    while b != [0]:
        _, r = divide(a, b)
        a, b = b, r
    return trim([z/a[-1] for z in a])


def evaluate(p, x):
    out = 0
    for c in reversed(p):
        out = out*x+c
    return out


def derivative(p):
    return trim([i*p[i] for i in range(1, len(p))] or [0])


def hcoeff(m):
    out = [Fraction(((-1)**j)*comb(m,j)) for j in range(m+1)]
    out[m] += 1
    return trim(out)


def qcoeff(m, a=2, b=3, g=11):
    out = [Fraction(0)] * (m+2)
    for k,v in [(0,a),(1,a+g),(m,a-m*b),(m+1,a+g-m*b)]:
        out[k] += v
    return trim(out)


def main():
    for m in range(0,13):
        h = hcoeff(m)
        assert len(h)-1 == (m if m % 2 == 0 else m-1)
        assert gcd(h, derivative(h)) == [1]
        assert evaluate(h, 0) == (2 if m == 0 else 1)
        assert evaluate(h, 1) == (2 if m == 0 else 1)
        q = qcoeff(m)
        assert gcd(q, derivative(q)) == [1]
        assert evaluate(q, -1) == (0 if m % 2 else -22)
        assert len(q)-1 == m+1
        assert (len(q)-1-(m%2)) == (m+1 if m%2==0 else m)
        if m > 0:
            roots_unavailable = [Fraction(1)] + [Fraction(0)]*(m-1)+[Fraction(1)]
            assert gcd(q, roots_unavailable) == ([1,1] if m%2 else [1])
        assert (len(h)-1+4) == (m+4 if m % 2 == 0 else m+3)
        print(f'm={m:2d} degree(h)={len(h)-1:2d} beta2={len(h)+3:2d} chi={len(h):2d} critical={len(q)-1-(m%2):2d}')
    print('FINITE_EXACT_CHECKS_PASS (m=0..12); not an infinite certificate')

if __name__ == '__main__':
    main()
