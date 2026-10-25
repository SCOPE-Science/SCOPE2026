"""Exact-rational standalone certificate for the GD degree of the S(2,3) ruling curve.
Run: python3 verify_gd_scroll.py (Python standard library only).
"""
from fractions import Fraction as F


def trim(p):
    p = [F(a) for a in p]
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(a, b):
    return trim([(a[i] if i < len(a) else 0) +
                 (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])


def neg(a):
    return [-v for v in a]


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    c = [F(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return trim(c)


def scale(a, q):
    return trim([x*F(q) for x in a])


def deriv(a):
    return trim([i*a[i] for i in range(1,len(a))] or [0])


def divrem(a, b):
    a,b=trim(a),trim(b)
    if b == [0]:
        raise ZeroDivisionError
    if len(a)<len(b):
        return [F(0)],a
    q = [F(0)]*(len(a)-len(b)+1)
    while a != [0] and len(a)>=len(b):
        shift = len(a)-len(b)
        c = a[-1]/b[-1]
        q[shift] += c
        a = sub(a, [0]*shift+scale(b,c))
    return trim(q),trim(a)


def monic(a):
    a=trim(a)
    return a if a == [0] else scale(a,F(1)/a[-1])


def gcd(a,b):
    a,b=trim(a),trim(b)
    while b != [0]:
        _,r=divrem(a,b)
        a,b=b,r
    return monic(a)

# v_1=(1,t,t^2) and v_2=(1,t,t^2,t^3). Their squared norms are s_1,s_2.
s1=[1,0,1,0,1]
s2=[1,0,1,0,1,0,1]
p1=[1,2,3]
p2=[1,2,3,4]
c1=sum(v*v for v in p1)
c2=sum(v*v for v in p2)
assert (c1,c2)==(14,30)
assert gcd(s1,s2)==[F(1)]
L=mul(s1,s2)
G=add(scale(mul(mul(p1,p1),s2), F(1,14)),
      scale(mul(mul(p2,p2),s1), F(1,30)))
H=sub(mul(deriv(G),L),mul(G,deriv(L)))
expected_scaled_H=[44,198,524,972,1452,2151,2374,3288,2718,3420,
                   1602,2232,276,969,-422,168,-474,-78,-174]
assert scale(H,105)==[F(v) for v in expected_scaled_H]
assert len(L)-1==10 and len(H)-1==18
assert gcd(L,G)==[F(1)]
assert gcd(L,H)==[F(1)]
assert gcd(H,deriv(H))==[F(1)]
# The cut locus for this block-diagonal data is p_1(t)*p_2(t)=0.
assert gcd(H,mul(p1,p2))==[F(1)]
# The first vector lives in a 3-coordinate block and the second in a
# disjoint 4-coordinate block. Their normalized outer products sum to a
# symmetric rank-two idempotent with trace two.
assert c1!=0 and c2!=0
print('VERIFY_OK GD=18; 18 simple finite critical points, no poles/infinity')
