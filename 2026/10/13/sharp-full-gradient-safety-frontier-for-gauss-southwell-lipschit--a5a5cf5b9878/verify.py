from fractions import Fraction as F
from decimal import Decimal, getcontext

getcontext().prec = 80
D = Decimal

# Exact rational witness.
a=F(1)
c=F(1,2)
g1=F(1)
g2=F(-9,10)

# Equal coordinate Lipschitz constants and unique GSL choice.
assert abs(g1) > abs(g2)

# Exact coordinate-1 minimization.
gp1 = F(0)
gp2 = g2 - c/a*g1
assert gp2 == F(-7,5)

before = g1*g1 + g2*g2
after = gp2*gp2
assert before == F(181,100)
assert after == F(49,25)
assert after/before == F(196,181)
assert after > before

# Exact objective decrease for a quadratic coordinate minimization.
decrease = g1*g1/(2*a)
assert decrease == F(1,2)

# Eigenvalues of [[1,1/2],[1/2,1]] are 1/2 and 3/2.
assert F(3,2)/F(1,2) == 3

# High-precision algebraic threshold.
sqrt13 = D(13).sqrt()
u = (D(4)-sqrt13)/D(3)
assert abs(D(3)*u*u-D(8)*u+D(1)) < D("1e-70")

delta2 = (D(97)-D(26)*sqrt13)/D(27)
delta = delta2.sqrt()
kappa = (D(1)+delta)/(D(1)-delta)

poly = D(9)*kappa**4 + kappa**3 - D(43)*kappa**2 + kappa + D(9)
assert abs(poly) < D("1e-65")
assert abs(kappa-D("2.06394456101195877071988248747")) < D("1e-28")

# Reconstruct the boundary matrix from u=q^2.
q = u.sqrt()
s = (D(1)-u)/(D(2)*q)
assert abs(u + D(2)*q*s - D(1)) < D("1e-70")
d2_reconstructed = ((D(1)-s*s)**2 + D(4)*u)/(D(1)+s*s)**2
assert abs(d2_reconstructed-delta2) < D("1e-65")

# Representative fixed-matrix safety checks.
def safe_value(q,s):
    return q*q + D(2)*q*s

q2=D(1)/D(3)
s2=D(1)
assert safe_value(q2,s2) < D(1)

q3=D(1)/D(2)
s3=D(1)
assert safe_value(q3,s3) > D(1)

print("VERIFY_OK")
print("kappa_star", kappa)
print("witness_squared_gradient_ratio", F(196,181))
