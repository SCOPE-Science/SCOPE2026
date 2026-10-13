#!/usr/bin/env python3
"""Exact-rational certificate for two pH-path support transitions in a four-phenotype game."""
from fractions import Fraction as F
from math import comb


def p(*coeffs):
    return tuple(F(c) for c in coeffs)


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return tuple(a)


def add(a, b):
    return trim(p(*( (a[i] if i < len(a) else 0) +
                     (b[i] if i < len(b) else 0) for i in range(max(len(a), len(b))))))


def scale(a, s):
    return trim(tuple(F(s)*v for v in a))


def sub(a, b):
    return add(a, scale(b, -1))


def mul(a, b):
    c = [F(0)] * (len(a) + len(b) - 1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            c[i+j] += u*v
    return trim(c)


def ev(a, t):
    z = F(0)
    for c in reversed(a):
        z = z*t + c
    return z


def bernstein(a):
    n = len(a)-1
    return tuple(sum(a[j]*F(comb(k, j), comb(n, j)) for j in range(k+1))
                 for k in range(n+1))


def assert_sign(a, sign):
    b = bernstein(trim(a))
    assert all(v * sign > 0 for v in b), (a, b, sign)


def det(a):
    if len(a) == 1:
        return a[0][0]
    return sum((-1)**j * a[0][j] * det([row[:j] + row[j+1:] for row in a[1:]])
               for j in range(len(a)))


base = [[90,90,95,92],[105,85,95,92],[102,100,75,92],[103,104,100,80]]
acid = [[88,85,90,88],[110,88,100,90],[105,105,80,92],[100,102,95,78]]
buff = [[92,90,95,93],[100,85,90,90],[95,95,75,90],[105,105,100,82]]

def interpolated(a1):
    return [[p(F(base[i][j],100),F(a1[i][j]-base[i][j],100))
             for j in range(4)] for i in range(4)]


def matvec(a, n):
    return [sum_poly(*(mul(a[i][j], n[j]) for j in range(4))) for i in range(4)]


def sum_poly(*polys):
    out = p(0)
    for z in polys:
        out=add(out,z)
    return out


def check_PD(a, expected):
    m = [[F(a[i][j]-a[i][3]-a[3][j]+a[3][3],100) for j in range(3)] for i in range(3)]
    h = [[-(m[i][j]+m[j][i])/2 for j in range(3)] for i in range(3)]
    minors = [det([r[:n] for r in h[:n]]) for n in range(1,4)]
    assert minors == expected, (minors,expected)
    assert all(z>0 for z in minors)

check_PD(base, [F(1,4), F(451,10000), F(47263,4000000)])
check_PD(acid, [F(11,50),F(1447,40000),F(32387,4000000)])
check_PD(buff, [F(6,25),F(1167,40000),F(911,160000)])

PA = p(-60,234,-2,1)
PB = p(-2520,3201,-712,41)
assert_sign(p(234,-4,3),1)  # P_A' strictly positive on [0,1]
assert_sign(p(3201,-1424,123),1)  # P_B' strictly positive
assert ev(PA,F(0))<0<ev(PA,F(1))
assert ev(PB,F(0))<0<ev(PB,F(1))
assert ev(PA,F(256901,1000000))<0<ev(PA,F(256902,1000000))
assert ev(PB,F(994745,1000000))<0<ev(PB,F(994746,1000000))

DA=p(-13870,2173,-186,34)
NA=[scale(PA,20),
    scale(mul(p(2,1),p(180,-37,2)),-10),
    scale(p(1260,1196,113,3),-2),
    scale(p(-1310,189,-50,8),5)]
QA=p(-875,188,10)
FA=[p(0),scale(p(24,-1,2),-10),scale(p(-90,-31,5),2),scale(p(-91,48,4),5)]

DB=p(-13870,7871,-1382,31)
NB=[scale(p(240,313,-115,2),-5),
    scale(p(-720,687,-193,9),5), PB,
    scale(p(1310,-560,56,9),-5)]
QB=p(515,-184,3)
FB=[p(60,37,3),p(180,-138,7),p(0),scale(p(-275,83,7),-1)]

for desc,a1,D,N,Q,Nface,excluded,poly,gapfactor in [
 ('acidic', acid, DA, NA, QA, FA, 0, PA, F(1,5)),
 ('buffered', buff, DB, NB, QB, FB, 2, PB, F(-1,100))]:
    aa=interpolated(a1)
    assert sum_poly(*N) == D, desc+' full normalization'
    assert sum_poly(*Nface)==Q, desc+' face normalization'
    products=matvec(aa,N)
    assert all(products[i]==products[0] for i in range(1,4)), desc+' full equal fitness'
    facescores=matvec(aa,Nface)
    active=[i for i in range(4) if i!=excluded]
    assert all(facescores[i]==facescores[active[0]] for i in active), desc+' face equal fitness'
    assert sub(facescores[excluded],facescores[active[0]])==scale(poly,gapfactor), desc+' invasion gap'
    assert_sign(D,-1)
    assert_sign(Q, (-1 if desc=='acidic' else 1))
    for i in active:
        assert_sign(N[i],-1)
        assert_sign(Nface[i],(-1 if desc=='acidic' else 1))
    if desc=='acidic':
        # Numerator of disappearing phenotype changes - to +, denominator negative.
        assert N[excluded]==scale(poly,20)
    else:
        assert N[excluded]==poly
    print(desc, 'exact identities, positive-support certificates and brackets PASS')

# At the two branch contacts, full-support and boundary-support solutions coincide:
# uniqueness of all-active equal-payoff normalized solution on the support follows
# from strictly negative tangent quadratic form; contact condition is gap=0.
print('VERIFY_OK')
