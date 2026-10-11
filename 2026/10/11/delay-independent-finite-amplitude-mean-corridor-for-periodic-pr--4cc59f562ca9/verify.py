from fractions import Fraction as F
from decimal import Decimal, getcontext

s = F(1, 5)
m = F(1, 10)
a = F(1, 1)
beta = F(3, 5)
n = F(2, 5)
p = a * beta
q = m + p

# Lower bound.
L = 1 - s * (n + 1/a)
assert L == F(18, 25)

# Expand (1-x)(p+x) - (s p/q)(n(p+x)+beta).
# Coefficients are constant, x, x^2.
c0 = p - (s*p/q) * (n*p + beta)
c1 = 1 - p - (s*p/q) * n
c2 = F(-1, 1)
assert (c0, c1, c2) == (F(399,875), F(290,875), F(-1,1))

# Source Case 2 equilibrium coefficients.
A = m + a*beta + s*n - 1
B = s*n*a*beta + s*beta - m - a*beta
assert A == F(-11, 50)
assert B == F(-133, 250)

# Exact mean-defect algebra at rational synthetic moments.
ubar = F(4, 5)
var = F(1, 100)
Wbar = (1-ubar)/s
uWbar = (ubar*(1-ubar)-var)/s
vbar_left = q*Wbar + uWbar
vbar_right = ((q+ubar)*(1-ubar)-var)/s
assert vbar_left == vbar_right

# High-precision evaluations of the exact radicals.
getcontext().prec = 50
D = Decimal
U = (D(29) + D(14806).sqrt()) / D(175)
ustar = (D(11) + D(5441).sqrt()) / D(100)
assert abs(U - D('0.8610280454586158')) < D('1e-15')
assert abs(ustar - D('0.8476313442364011')) < D('1e-15')
assert U > ustar
assert U - ustar < D('0.013398')

print('VERIFY_OK')
