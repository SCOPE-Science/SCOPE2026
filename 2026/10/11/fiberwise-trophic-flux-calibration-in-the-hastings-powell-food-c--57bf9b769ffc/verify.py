from fractions import Fraction as F

a1 = F(5)
b1 = F(3)
a2 = F(1,10)
b2 = F(2)
d1 = F(2,5)
d2 = F(1,100)

x = F(2,5)
y = F(3,20)
z = F(7,2)

f1 = a1*x/(1+b1*x)
f2 = a2*y/(1+b2*y)

xdot = x*(1-x)-f1*y
ydot = f1*y-f2*z-d1*y
zdot = (f2-d2)*z

g = (1-x)*(1+b1*x)/a1
Q = f1-a2*z/(1+b2*y)

assert y-g == -(1+b1*x)*xdot/(a1*x)
assert Q-d1 == ydot/y
assert f2-d2 == zdot/z

# Exact Holling-II curvature numerator.
# f''(y) = -2*a2*b2/(1+b2*y)^3.
curvature = -2*a2*b2/(1+b2*y)**3
assert curvature < 0

ystar = d2/(a2-b2*d2)
assert ystar == F(1,8)
assert a2 > b2*d2
assert a2*ystar/(1+b2*ystar) == d2

# Abstract variance decomposition under E[R|X]=0:
# E[R]=0 and E[GR]=0.
EG = F(2,7)
EG2 = F(11,13)
ER = F(0)
ER2 = F(5,17)
EGR = F(0)
EY = EG+ER
EY2 = EG2+2*EGR+ER2
varY = EY2-EY*EY
varG = EG2-EG*EG
assert varY == varG+ER2

print("VERIFY_OK")
