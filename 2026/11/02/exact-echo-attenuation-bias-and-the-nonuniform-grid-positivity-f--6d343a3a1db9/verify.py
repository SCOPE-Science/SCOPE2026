#!/usr/bin/env python3
"""Exact-rational checks for a finite-grid Bloch--Torrey echo-splitting theorem.

This file supplements, but does not replace, the algebraic proof.
Requires only the Python standard library.
"""
from fractions import Fraction as F
from random import Random


def error_data(h, q):
    n = len(h)
    assert len(q) == n + 1 and all(x > 0 for x in h)
    I = sum((h[j] * (q[j]**2 + q[j]*q[j+1] + q[j+1]**2) / 3
             for j in range(n)), F(0))
    L = sum((h[j] * q[j]**2 for j in range(n)), F(0))
    R = sum((h[j] * q[j+1]**2 for j in range(n)), F(0))
    E = sum((h[j] * (q[j+1] - q[j])**2 / 6
             for j in range(n)), F(0))
    J = sum((h[j]*(q[j+1]**2-q[j]**2)/2
             for j in range(n)), F(0))
    return I, L, R, E, J


def form(h, q, right):
    m = len(h) - 1
    a = [2*h[i] - h[i+1] if right else 2*h[i+1] - h[i]
         for i in range(m)]
    # Endpoints are zero, and matrices represent three times the error.
    value = sum((a[i] * q[i+1]**2 for i in range(m)), F(0))
    value -= sum((h[i+1]*q[i+1]*q[i+2] for i in range(m-1)), F(0))
    return value


def leading_minors(h, right):
    m = len(h) - 1
    delta0, delta1 = F(1), F(1)
    out = []
    for i in range(m):
        a = 2*h[i] - h[i+1] if right else 2*h[i+1] - h[i]
        d = a*delta1-(h[i]**2/F(4))*delta0 if i > 0 else a
        out.append(d)
        delta0, delta1 = delta1, d
    return out


def safe(h, right):
    ds = leading_minors(h, right)
    return all(x > 0 for x in ds[:-1]) and ds[-1] >= 0


def run():
    rng = Random(1409017)
    checks = 0
    for n in range(2, 11):
        for _ in range(300):
            h = [F(rng.randint(1, 13), rng.randint(1, 8)) for j in range(n)]
            q = [F(0)] + [F(rng.randint(-8, 8), rng.randint(1, 7))
                          for j in range(n-1)] + [F(0)]
            I,L,R,E,J = error_data(h,q)
            assert R-I == E+J and L-I == E-J
            assert 3*(R-I) == form(h,q,True)
            assert 3*(L-I) == form(h,q,False)
            assert 2*J == sum(((h[i-1]-h[i])*q[i]**2
                               for i in range(1,n)), F(0))
            checks += 5
    for n in range(2, 20):
        for _ in range(100):
            hval = F(rng.randint(1,20),rng.randint(1,10))
            h=[hval]*n
            q=[F(0)]+[F(rng.randint(-8,8)) for _ in range(n-1)]+[F(0)]
            I,L,R,E,J=error_data(h,q)
            assert J == 0 and R == L and R-I == E
            assert safe(h, True) and safe(h,False)
            checks+=2
    for a in range(1, 20):
        for b in range(1, 20):
            h=[F(a),F(b)]
            expected=F(1,2)<=F(a,b)<=F(2)
            assert safe(h,True) and safe(h,False) if expected else not(safe(h,True) and safe(h,False))
            checks+=1
    h=[F(1),F(2),F(1)]
    I,L,R,E,J=error_data(h,[F(0),F(2),F(1),F(0)])
    assert I==F(19,3) and R==F(6) and L==F(9) and R<I
    I,L,R,E,J=error_data(h,[F(0),F(1),F(2),F(0)])
    assert I==F(19,3) and L==F(6) and R==F(9) and L<I
    assert not safe(h,True) and not safe(h,False)
    checks += 3
    print(f'PASS: {checks} exact-rational consistency checks')

if __name__ == '__main__':
    run()
