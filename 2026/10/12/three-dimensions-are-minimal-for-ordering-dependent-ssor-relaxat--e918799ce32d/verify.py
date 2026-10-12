from fractions import Fraction as F
from decimal import Decimal, getcontext

# 2x2 normalized polynomial checks.
for rho in [F(1,5), F(1,2), F(3,5)]:
    p = 1-rho*rho
    for w in [F(1,2), F(1), F(6,5), F(3,2)]:
        # det(A-lambda M)=lambda^2-S lambda+p
        S = F(2)-rho*rho*w*(F(2)-w)
        assert S == F(2)-rho*rho + rho*rho*(w-F(1))**2
        assert p > 0
        if w != 1:
            assert S > F(2)-rho*rho

# Natural 3x3 path at r=1/2, omega=1.
r=F(1,2)
# Q(lambda)=lambda^2-23/16 lambda+1/2.
assert r**4 + 2*r**2 - 2 == F(-23,16)
assert 1-2*r**2 == F(1,2)

# dF/domega=-2 lambda r^4(lambda-1).  At the smaller root it is positive.
# Use high precision for the radical and derivative, while all coefficients above are exact.
getcontext().prec=80
D=Decimal
sqrt17=D(17).sqrt()
lm=(D(23)-sqrt17)/D(32)
dlm=-D(1)/D(16)+D(23)*sqrt17/D(272)
dk=-D(1)/D(8)-D(23)*sqrt17/D(136)
assert D(0) < lm < D(1)
assert dlm > 0
assert dk < 0
# kappa derivative equals -lambda'/lambda^2.
assert abs(dk + dlm/(lm*lm)) < D('1e-70')

# Center-first order: product and sum of the nontrivial roots.
for r in [F(1,4),F(1,2),F(2,3)]:
    assert r*r < F(1,2)
    p=1-2*r*r
    S1=2-2*r*r
    assert S1 == 1+p
    for w in [F(4,5),F(1),F(6,5),F(3,2)]:
        S=2-2*r*r*w*(2-w)
        assert S == S1 + 2*r*r*(w-1)**2
        if w != 1:
            assert S>S1

print('VERIFY_OK')
print('r_half_lambda_minus', lm)
print('r_half_kappa_derivative', dk)
