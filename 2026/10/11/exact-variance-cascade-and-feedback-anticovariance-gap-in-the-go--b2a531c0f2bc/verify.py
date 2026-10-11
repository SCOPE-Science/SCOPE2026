from fractions import Fraction as F

# Source parameter specialization.
k2 = F(1)
k3 = F(1)
k4 = F(1, 5)
k5 = F(1, 5)
k6 = F(1, 10)

sharp = k6*(k4+k6)*(k5+k6)/(k3*k3*(k4+k5+k6))
direct = (k6/k3)**2
assert sharp == F(9, 500)
assert direct == F(1, 100)
assert sharp/direct == F(9, 5)

# General improvement identity, checked at independent exact rational rates.
a = F(7, 5)   # k4
c = F(11, 6)  # k5
e = F(5, 4)   # k6
d = F(9, 7)   # k3

sharp2 = e*(a+e)*(c+e)/(d*d*(a+c+e))
direct2 = (e/d)**2
factor = (a+e)*(c+e)/(e*(a+c+e))
assert sharp2 == direct2 * factor
assert factor == 1 + a*c/(e*(a+c+e))
assert factor > 1

# Covariance elimination at exact test variances.
b = F(8, 5)  # k2
Vy = F(13, 7)
Vz = F(4, 9)
Cxy = c/b * Vy
Cyz = e/d * Vz
Cxz = ((c+e)*Cyz - d*Vy)/b
cov_feedback = (a+e)*Cxz - d*Cxy

rhs = e*(a+e)*(c+e)*Vz - d*d*(a+c+e)*Vy
assert b*d*cov_feedback == rhs

print("VERIFY_OK")
