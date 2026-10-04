from decimal import Decimal, getcontext

getcontext().prec = 80
D = Decimal
r = D(17).sqrt()
z = (D(5) - r) / D(12)
A = z.sqrt()
C = (A * (D(1) - A * A)).sqrt()
lam4 = (D(15) + D(3) * r) / D(2)
lam = lam4.sqrt().sqrt()
F = D(1) + (D(6)*A*lam*lam - D(4)*C*lam**3) / (D(1) + lam**4)
target_F = (D(5) - r) / D(2)
target_mu4_fourth = (D(5) + r) / D(4)
poly = D(18)*z*z - D(15)*z + D(1)
crit_A = D(3)*C - lam*(D(1) - D(3)*A*A)
crit_lam = D(3)*A*(D(1)-lam**4) - C*lam*(D(3)-lam**4)
reciprocal = D(1)/F

tol = D('1e-65')
assert abs(poly) < tol
assert abs(crit_A) < tol
assert abs(crit_lam) < tol
assert abs(F-target_F) < tol
assert abs(reciprocal-target_mu4_fourth) < tol
print('VERIFY_OK')
print('z=', z)
print('lambda=', lam)
print('Fmin=', F)
print('mu4=', target_mu4_fourth.sqrt().sqrt())
