#!/usr/bin/env python3
"""Reproducible algebraic and numerical checks for a two-pulse Erlang-3 hydrograph.

Standard-library only. These checks supplement, but do not replace, the analytic proof.
"""
from decimal import Decimal, localcontext
from fractions import Fraction as F
from math import exp, sqrt

checks = 0

def require(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)

# All these are exact rational polynomial identities.
for a in range(1, 43):
    d = F(a, 7)
    for b in range(1, 47):
        k = F(b, 11)
        A = -(1+k)
        B = 2*(1+k-d)
        C = d*(2-d)
        disc = B*B - 4*A*C
        require(disc == 4*(k*k+(2-d*d)*k+1), "discriminant expansion")
        for x in (F(0), F(1,3), F(7,5)):
            direct = (x+d)*(2-x-d)+k*x*(2-x)
            factored = A*x*x+B*x+C
            require(direct == factored, "derivative expansion")

# The critical curve and three characteristic reentrant cases.
with localcontext() as ctx:
    ctx.prec = 70
    one = Decimal(1)
    two = Decimal(2)
    ratio = one / Decimal(5)
    R = lambda d: (((d*d-two)+d*(d*d-Decimal(4)).sqrt())/two)*(-d).exp()
    samples = [(Decimal('2.01'), True), (Decimal(3), False), (Decimal(5), True)]
    for d, expected in samples:
        prediction = ratio > R(d)
        require(prediction == expected, "certified reentrance example")
        print("delay",str(d),"critical ratio",str(R(d)),"two peaks",prediction)
    dstar = two * two.sqrt()
    rmax = (Decimal(3)+two*two.sqrt())*(-dstar).exp()
    require(rmax > ratio > (-two).exp(), "reentrant interval nonempty")
    print("maximal critical ratio",str(rmax))

# Verify root geometry against the criterion at representative nonboundary parameters.
for i in range(1,251):
    d = i / 30
    for j in range(1,21):
        r = j/55
        k = r*exp(d)
        A = -(1+k)
        B = 2*(1+k-d)
        C = d*(2-d)
        disc = B*B - 4*A*C
        positive_roots = 0
        if disc > 1e-10:
            positive_roots = sum((-B+s*sqrt(disc))/(2*A) > 1e-10 for s in (-1,1))
        if d > 2:
            kc = (d*d-2+d*sqrt(d*d-4))/2
            expected = k > kc
            # Exclude near-critical numerical roundoff; exact algebra covers boundaries.
            if abs(k-kc) > 1e-8:
                require((positive_roots == 2) == expected, "positive-root criterion")
        else:
            require(positive_roots <= 1, "early second pulse cannot create two peaks")

print("PASS", checks,"algebraic/numerical assertions")
