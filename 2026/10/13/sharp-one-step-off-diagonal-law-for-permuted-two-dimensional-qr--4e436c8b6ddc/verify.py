from fractions import Fraction as F

def factor(a,b,d):
    det=a*d-b*b
    den=a*a+b*b
    return det/den

# Condition-four rational witness from rotation cos=12/13, sin=5/13.
a=F(244,169)
b=F(180,169)
d=F(601,169)
det=a*d-b*b
tr=a+d
assert det==4
assert tr==5
g1=factor(a,b,d)
g2=factor(d,b,a)
assert g1==F(169,136)
assert g1>1
assert g2==F(676,2329)
assert g2<1

# Equal-column-norm sharp case, eigenvalues 1 and 4.
a=F(5,2)
b=F(3,2)
d=F(5,2)
assert a*d-b*b==4
assert factor(a,b,d)==F(8,17)
assert factor(d,b,a)==F(8,17)

# Verify the QR off-diagonal formula after clearing r=sqrt(a^2+b^2).
# q1=(a,b)/r, q2=(-b,a)/r, so numerator is
# (a,b) A (-b,a)^T = b det(A).
samples=[
    (F(2),F(1),F(3)),
    (F(5,2),F(3,2),F(5,2)),
    (F(244,169),F(180,169),F(601,169)),
]
for a,b,d in samples:
    det=a*d-b*b
    assert a>0 and det>0
    # Direct cleared numerator.
    Aq2_0 = -a*b + b*a
    Aq2_1 = -b*b + d*a
    num = a*Aq2_0 + b*Aq2_1
    assert num == b*det
    assert num/(a*a+b*b) == b*factor(a,b,d)

# Best-order condition-number equality law for a few kappa values.
for k in [F(2),F(3),F(4),F(7)]:
    a=(1+k)/2
    b=(k-1)/2
    d=a
    assert factor(a,b,d)==2*k/(k*k+1)

print("VERIFY_OK")
print("growth_witness", g1)
print("swapped_factor", g2)
print("sharp_best_factor_kappa4", F(8,17))
