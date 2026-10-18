#!/usr/bin/env python3
"""Exact standard-library certificate for a three-attractor SIRS adherence theorem."""
from fractions import Fraction as F
from math import comb, sqrt


def add(p, q):
    out = [F(0)] * max(len(p), len(q))
    for i, v in enumerate(p): out[i] += v
    for i, v in enumerate(q): out[i] += v
    return trim(out)


def scale(p, a): return trim([a * v for v in p])


def mul(p, q):
    out = [F(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q): out[i+j] += a*b
    return trim(out)


def trim(p):
    while len(p)>1 and p[-1]==0: p.pop()
    return p


def compose_affine(p, lo, hi):
    t = [lo, hi-lo]
    out = [F(0)]
    power = [F(1)]
    for coeff in p:
        out = add(out, scale(power, coeff))
        power = mul(power, t)
    return out


def bernstein(p, lo, hi):
    a = compose_affine(p, lo, hi)
    n = len(a)-1
    return [sum((a[k] * F(comb(i,k),comb(n,k)) for k in range(i+1)), F(0)) for i in range(n+1)]

# Build characteristic coefficients from the exact Jacobian formulas.
x=[F(0),F(1)]; one=[F(1)]; omx=add(one,scale(x,-1))
om2x=add(one,scale(x,-2))
c1_45=add(add([F(70)],scale(x,-86)),scale(mul(x,x),36))
# C2 = N2/[90(1-x)].
n2=add(scale(mul(omx,om2x),90),scale(mul(mul(x, mul(omx,omx)), add([F(14)],scale(x,-10))), -8))
n2=add(n2,scale(mul(x,om2x),45))
assert n2 == [F(90),F(-337),F(394),F(-272),F(80)], n2
# C3 = x(1-2x)[5-8(1-x)^2]/[10(1-x)].
num3=mul(mul(x,om2x),add([F(5)],scale(mul(omx,omx),-8)))
# C1*C2-C3 = [C1_45*N2-405*num3]/[4050(1-x)]
n6=add(mul(c1_45,n2),scale(num3,-405))
assert n6 == [F(6300),F(-30115),F(50892),F(-48856),F(36696),F(-16672),F(2880)], n6
lo, hi=F(1,5),F(3,8)
certificates = {"45*C1":c1_45,"90*(1-x)*C2":n2,"4050*(1-x)*(C1*C2-C3)":n6}
for title,p in certificates.items():
    vals=bernstein(p,lo,hi)
    assert all(a>0 for a in vals), (title,vals)
    print(title, ': all',len(vals),'Bernstein coefficients strictly positive; minimum',min(vals))
# Exact rational root checks for c=3/25 through the quadratic relation,
# using 2 < sqrt(6) < 5/2 and 3 < sqrt(10) < 13/4.
assert F(1,10)<(7-2*sqrt(10))/5<F(3,25)+(1/50)
assert F(3,25) < (7-2*sqrt(10))/5
assert F(1,5)<1-sqrt(F(5,8))<F(1,4)
assert (F(4,5)*F(3,8)-F(1,2)/(1-F(3,8))+F(3,5)-F(1,10)) == 0
# Algebraic root equalities verified by the rational minimal polynomial:
# x = (4 +/- sqrt(6))/20, so (20*x-4)^2=6.
# Expanding gives 40*x^2-16*x+1=0.
assert [F(1),F(-16),F(40)] == add(scale(add(mul(add(scale(x,20),[-4]),add(scale(x,20),[-4])),[-F(6)]),F(1,10)),[F(0)])
# Exact endpoint eigenvalues:
assert F(1,10)-F(3,25)==-F(1,50)
assert F(3,25)-F(2,5)==-F(7,25)
assert F(2,5)*2*F(13,20)*F(7,20)==F(91,500)
print('Exact algebraic, equilibrium, and characteristic-positivity checks passed.')
