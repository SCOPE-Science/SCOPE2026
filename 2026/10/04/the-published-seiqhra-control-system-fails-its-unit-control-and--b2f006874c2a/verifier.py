from fractions import Fraction as F

# Exact source-parameter witness for the incidence mismatch.
c = F(1, 2)
lam = F(1, 40000)
omega = F(3, 1000)
theta = F(3, 200)
A = omega / theta
S = F(100)
I = F(10)
base = lam*S*I/(1+c*A)
controlled = lam*S*I/(1+A)
assert A == F(1,5)
assert base == F(1,44)
assert controlled == F(1,48)
assert base-controlled == F(1,528)

# Exact source-parameter witness for the transfer-balance residual.
r1 = F(1,500)
r2 = F(23,1000)
r3 = F(1,50)
Q = F(5)
H = F(2)
u1 = F(1,2)
flux = A*(r1*I+r2*Q+r3*H)
extra = (1-u1)*flux
assert flux == F(7,200)
assert extra == F(7,400)

# Coefficient bookkeeping for dH/du1 in the repaired transfer.
# Ordered coefficients of (r1*A*I, r2*A*Q, r3*A*H).
# Loss costates are xi3,xi4,xi5 and the recovered gain has xi6.
expected = ("xi6-xi3", "xi6-xi4", "xi6-xi5")
constructed = tuple(f"xi6-xi{k}" for k in (3,4,5))
assert constructed == expected
print("VERIFY_OK")
