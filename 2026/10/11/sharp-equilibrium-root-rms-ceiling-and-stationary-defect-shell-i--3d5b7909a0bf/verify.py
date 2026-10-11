from fractions import Fraction as F
from decimal import Decimal, getcontext

# Polynomial identity for V = x^2/sigma + y^2 + z^2.
# Evaluate both expanded sides at several exact rational points.
def check_point(x,y,z,sigma,r,c):
    xdot = sigma*(y-x)
    ydot = r*x-x*z-y+c
    zdot = x*y-z
    lhs = 2*x*xdot/sigma + 2*y*ydot + 2*z*zdot
    rhs = 2*(1+r)*x*y - 2*x*x - 2*y*y - 2*z*z + 2*c*y
    assert lhs == rhs

for vals in [
    (F(2,3), F(-5,7), F(11,13), F(3,2), F(17,5), F(7,4)),
    (F(-4,5), F(9,8), F(3,7), F(15), F(2000), F(1500)),
    (F(1,9), F(2,11), F(-3,10), F(7,3), F(-2), F(5,6)),
]:
    check_point(*vals)

# Stationary shell algebra.
h = F(13,7)
m = F(5,6)
r = F(19,4)
c = F(11,5)
s = F(3,8)
Ey2 = h+s
Ez2 = r*h+c*m-Ey2
varz = Ez2-h*h
assert varz+s == h*(r-1-h)+c*m

# Orthogonal residual algebra for y = x + R, E[R]=0, E[xR]=0.
Ex = F(2,5)
Ex2 = F(7,9)
ER = F(0)
ER2 = F(4,13)
ExR = F(0)
Ey = Ex+ER
Ey2 = Ex2+2*ExR+ER2
varx = Ex2-Ex*Ex
vary = Ey2-Ey*Ey
assert vary == varx+ER2

# Orthogonal residual algebra for XY = Z + Q, E[Q]=0, E[ZQ]=0.
EZ = F(3,8)
EZ2 = F(5,7)
EQ = F(0)
EQ2 = F(9,17)
EZQ = F(0)
EXY = EZ+EQ
EXY2 = EZ2+2*EZQ+EQ2
varZ = EZ2-EZ*EZ
varXY = EXY2-EXY*EXY
covZXY = (EZ2+EZQ)-EZ*EXY
assert varXY == varZ+EQ2
assert covZXY == varZ

# Deterministic high-precision bisection for xi^3 - 1999 xi - 1500 = 0.
getcontext().prec = 60
D = Decimal
def f(q):
    return q*q*q - D(1999)*q - D(1500)
lo, hi = D(45), D(46)
assert f(lo) < 0 < f(hi)
for _ in range(240):
    mid = (lo+hi)/2
    if f(mid) <= 0:
        lo = mid
    else:
        hi = mid
root = (lo+hi)/2
root2 = root*root
assert abs(root - D('45.08074565562506')) < D('5e-14')
assert abs(root2 - D('2032.2736288671576')) < D('5e-13')

print('VERIFY_OK')
