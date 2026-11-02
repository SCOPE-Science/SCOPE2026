"""Exact symbolic checks for the normal conic of the Baily--Danelon quartic.

Run: python3 verify_normal_conic.py
This verifies polynomial identities, not irreducibility or nonsquareness;
those are proved separately in RESULT.md.
"""
from fractions import Fraction

NAMES = ('x', 'y', 'p', 'u', 'v', 'q', 'w')
Z = (0,) * len(NAMES)

def const(a):
    a = Fraction(a)
    return {Z: a} if a else {}

def var(i):
    v = list(Z)
    v[i] = 1
    return {tuple(v): Fraction(1)}

def add(a, b):
    c = dict(a)
    for key, val in b.items():
        c[key] = c.get(key, Fraction(0)) + val
        if c[key] == 0:
            del c[key]
    return c

def neg(a):
    return {k: -v for k, v in a.items()}

def sub(a, b):
    return add(a, neg(b))

def mul(a, b):
    c = {}
    for ka, va in a.items():
        for kb, vb in b.items():
            k = tuple(x + y for x, y in zip(ka, kb))
            c[k] = c.get(k, Fraction(0)) + va * vb
    return {k: v for k, v in c.items() if v}

def sq(a):
    return mul(a, a)

x, y, p, u, v, q, w = (var(i) for i in range(7))
zero, one, two, four = (const(i) for i in (0,1,2,4))
H = add(add(mul(sq(x), u), mul(mul(x,y),v)),
        add(mul(sq(y),q), sub(sq(p),mul(mul(y,w),p))))
D = sub(sub(mul(mul(four,u),q),mul(u,sq(w))),sq(v))
# 4uH=(2ux+vy)^2+u(2p-wy)^2+Dy^2
rhs = add(add(sq(add(mul(mul(two,u),x),mul(v,y))),
              mul(u,sq(sub(mul(two,p),mul(w,y))))),mul(D,sq(y)))
assert not sub(mul(mul(four,u),H),rhs)
# For Q(x,y,p), 4det(M)=4uq-uw^2-v^2 (compute by cofactor).
# M=((u,v/2,0),(v/2,q,-w/2),(0,-w/2,1)).
det = sub(mul(u,sub(q,mul(const(Fraction(1,4)),sq(w)))),
          mul(const(Fraction(1,4)),sq(v)))
assert not sub(mul(four,det),D)
# H is a quartic if deg(x,y,w)=1, deg(p,q,u,v)=2.
weights = (1,1,2,2,2,2,1)
assert all(sum(k[i]*weights[i] for i in range(7))==4 for k in H)
assert all(sum(k[i]*weights[i] for i in range(7))==4 for k in D)
print('VERIFY_OK: exact rational polynomial identities and homogeneous degrees')
