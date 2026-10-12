"""Exact small-field check of all prescribed rank-one-idempotent product fibers.

Uses prime-field arithmetic for q=2,3,5 and F_4=F_2[z]/(z^2+z+1).
All matrices and every prescribed target are inspected in the listed cases.
"""
from collections import Counter
from fractions import Fraction
from itertools import product


def plus(a, b, q):
    return a ^ b if q == 4 else (a + b) % q


def times(a, b, q):
    if q != 4:
        return a * b % q
    c = (a & 1) * b ^ ((a >> 1) & 1) * (b << 1)
    if c & 4:
        c ^= 7
    return c


def pairing(u, v, q):
    s = 0
    for a, b in zip(u, v):
        s = plus(s, times(a, b, q), q)
    return s


def outer(u, v, q):
    return tuple(times(a, b, q) for a in u for b in v)


def multiply(a, b, n, q):
    return tuple(pairing(a[i*n:(i+1)*n], b[j::n], q)
                 for i in range(n) for j in range(n))


def trace(a, n, q):
    s = 0
    for i in range(n):
        s = plus(s, a[i*n+i], q)
    return s


def formula(n, q, r, t=None, zero=False):
    h = q ** (n-1)
    m = h * (q**n - 1) // (q - 1)
    k = r - 1
    if zero:
        return m**r - m*q**((2*n-2)*k)
    a = q**((2*n-2)*k)
    b = q**((n-2)*k)
    c = q**((n-1)*k)
    result = Fraction(h, q**n - 1)*(a-b)
    if t != 0:
        result += Fraction(b-c, q-1)
    if t == 1:
        result += c
    assert result.denominator == 1
    return int(result)


def check(n, q, r):
    vs = list(product(range(q), repeat=n))
    nz = [v for v in vs if any(v)]
    rank_one = {outer(u, f, q) for u in nz for f in nz}
    projectors = {outer(u, f, q) for u in nz for f in vs
                  if pairing(f, u, q) == 1}
    expected_projectors = q**(n-1) * (q**n-1)//(q-1)
    assert len(projectors) == expected_projectors
    hist = Counter({a: 1 for a in projectors})
    for _ in range(2, r+1):
        nxt = Counter()
        for a, weight in hist.items():
            for b in projectors:
                nxt[multiply(a,b,n,q)] += weight
        hist = nxt
    for a in product(range(q), repeat=n*n):
        if not any(a):
            expected = formula(n,q,r,zero=True)
        elif a in rank_one:
            expected = formula(n,q,r,t=trace(a,n,q))
        else:
            expected = 0
        actual = hist.get(a,0)
        assert actual == expected, (n,q,r,a,actual,expected)
    assert sum(hist.values()) == expected_projectors**r
    print('PASS', 'n=',n,'q=',q,'r=',r,
          'idempotents=',len(projectors),
          'nonzero_outputs=',sum(v for a,v in hist.items() if any(a)),
          'zero_count=',formula(n,q,r,zero=True))


if __name__ == '__main__':
    for args in [(2,2,1),(2,2,2),(2,2,3),(2,2,4),
                 (2,3,1),(2,3,2),(2,3,3),(2,3,4),
                 (2,4,2),(2,4,3),(2,5,2),
                 (3,2,2),(3,2,3),(3,2,4),
                 (3,3,2),(3,3,3),(4,2,2),(4,2,3)]:
        check(*args)
    print('VERIFY_OK')
