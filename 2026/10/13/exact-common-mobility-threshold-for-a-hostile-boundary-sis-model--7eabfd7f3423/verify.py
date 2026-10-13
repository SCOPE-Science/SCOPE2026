#!/usr/bin/env python3
from fractions import Fraction as F
from math import sqrt

# Rational test triples verify the polynomial threshold comparisons exactly.
triples = [
    (F(1), F(1), F(1)),
    (F(2), F(3), F(5)),
    (F(7,3), F(11,5), F(13,2)),
    (F(9), F(1,4), F(17,3)),
]

for A,B,C in triples:
    # Use floating r only to choose rational d values safely on either side.
    rf = (-float(B) + sqrt(float(B*B + 4*A*C))) / (2*float(A))
    d_lo = F(int(rf*1000)-2, 1000)
    if d_lo <= 0:
        d_lo = F(1,10000)
    d_hi = F(int(rf*1000)+2, 1000)
    while A*d_lo*d_lo + B*d_lo >= C:
        d_lo -= F(1,1000)
    while A*d_hi*d_hi + B*d_hi <= C:
        d_hi += F(1,1000)
    assert C/(d_lo*d_lo*A+d_lo*B) > 1
    assert C/(d_hi*d_hi*A+d_hi*B) < 1

# Monotonicity scaling: denominator at d2 dominates (d2/d1) times denominator at d1.
for A,B,C in triples:
    for d1,d2 in [(F(1,5),F(2,5)), (F(1),F(3,2)), (F(7,4),F(11,3))]:
        q1=C/(d1*d1*A+d1*B)
        q2=C/(d2*d2*A+d2*B)
        assert q2 <= (d1/d2)*q1
        assert q2 < q1

# The global-threshold inequalities are algebraic once r <= dc < d.
for A,B in [(F(1),F(2)), (F(3),F(5)), (F(7,2),F(4,3))]:
    r=F(2,3)
    dc=F(3,4)
    d=F(5,4)
    C=A*r*r+B*r
    q=C/(d*d*A+d*B)
    assert q <= dc/d
    qcrit=C/(dc*dc*A+dc*B)
    assert qcrit >= (r/dc)**2

print('VERIFY_OK')
