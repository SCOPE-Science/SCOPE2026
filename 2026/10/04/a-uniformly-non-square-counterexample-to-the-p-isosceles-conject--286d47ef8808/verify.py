#!/usr/bin/env python3
from decimal import Decimal, getcontext
getcontext().prec = 80
R17 = Decimal(17).sqrt()
u = R17 - Decimal(4)
c = u.sqrt()
d = (Decimal(2) + c + u) / Decimal(4)
lam = (Decimal(1) - c) / (Decimal(1) + c)

def close(a,b,tol=Decimal('1e-60')):
    return abs(a-b) <= tol

assert Decimal(0) < c < Decimal(1)
assert d < Decimal(1)
assert Decimal(2)*d <= Decimal(1)+c
assert Decimal(2)*d > Decimal(1)+u
assert close(u*u + Decimal(8)*u - Decimal(1), Decimal(0))
F0 = (Decimal(1)+u)/(Decimal(1)+c)
assert Decimal(2)*c*d <= Decimal(1)+u
assert close(Decimal(1)-c*lam, F0)
assert close(c+lam, F0)
third = d*(Decimal(1)-lam)
assert third <= F0
U4_4 = Decimal(2)*(Decimal(1)+Decimal(6)*u+u*u)/(Decimal(1)+u)**4
closed = (Decimal(71)+Decimal(17)*R17)/Decimal(64)
assert close(U4_4, closed)
ratio4 = (Decimal(1)+lam**4)/(F0**4)
assert close(ratio4, U4_4)
# Derivative numerator for v in [0,1] is -4(v^2+8v-1); its unique zero is u.
assert close(u*u + Decimal(8)*u - Decimal(1), Decimal(0))
print('VERIFY_OK')
print('c=', c)
print('d=', d)
print('lambda0=', lam)
print('H4=', U4_4.sqrt().sqrt())
