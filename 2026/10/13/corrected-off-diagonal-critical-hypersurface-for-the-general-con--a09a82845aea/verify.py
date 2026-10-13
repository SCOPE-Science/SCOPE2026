from decimal import Decimal, getcontext
getcontext().prec = 70
D=Decimal
rt2=D(2).sqrt()

def delta(a,b,g):
    return ((a*b+g-D(4))**2+D(16)*g).sqrt()

def mu1(a,b,g):
    return D(2)*rt2*b/(D(4)+a*b+g-delta(a,b,g))

def mu2(a,b,g):
    return D(2)*rt2*b/(D(4)+a*b+g+delta(a,b,g))

def alpha_c(b,g):
    return (D(2)*b-rt2*(g+D(4)))/(rt2*b-D(4))

def alpha_printed(b,g):
    return (g/(D(2)*rt2*(D(2)*rt2-b))-(g-D(4))-rt2*(D(2)*rt2-b))/b

def diff_formula(b,g):
    return D(7)*g/(D(2)*b*(rt2*b-D(4)))

def slope(b,g):
    t=b-D(2)*rt2
    return (D(1)/rt2)*t*t/(t*t+D(2)*g)

cases=[(D(1),D(1)),(D(2),D('0.6')),(D(4),D(1)),(D(5),D('1.75'))]
for b,g in cases:
    ac=alpha_c(b,g)
    selected=mu1(ac,b,g) if b < D(2)*rt2 else mu2(ac,b,g)
    assert abs(selected-D(1)) < D('1e-60')
    ap=alpha_printed(b,g)
    assert abs((ap-ac)-diff_formula(b,g)) < D('1e-60')
    assert abs(ap-ac) > D('1e-20')
    eps=D('1e-18')
    ml=mu1(ac-eps,b,g) if b < D(2)*rt2 else mu2(ac-eps,b,g)
    assert ml > D(1)
    numerical=((D(1)/(mu1(ac+eps,b,g) if b < D(2)*rt2 else mu2(ac+eps,b,g)))-
               (D(1)/(mu1(ac-eps,b,g) if b < D(2)*rt2 else mu2(ac-eps,b,g))))/(D(2)*eps)
    assert abs((numerical-slope(b,g))/slope(b,g)) < D('1e-16')

# Diagonal consistency: the corrected crossing is sqrt(2) away from the singular beta.
for b in (D(1),D(4),D(7)):
    assert abs(alpha_c(b,D(0))-rt2) < D('1e-60')

# Concrete countercheck from the review.
b=D(1); g=D(1)
ap=alpha_printed(b,g); ac=alpha_c(b,g)
assert abs(mu1(ap,b,g)-D('2.987634251180783')) < D('1e-15')
assert abs(mu1(ac,b,g)-D(1)) < D('1e-60')

print('VERIFY_OK cases=4 diagonal=3 concrete_countercheck=1')
