from fractions import Fraction as F

# Source baseline economic parameters.
a = F(10)
a1 = F(5)
b = F(-1, 2)
b1 = F(1, 2)
c = F(1)

lam = (b - b1) / c
delta = (a - a1) / c
assert lam == F(-1)
assert delta == F(5)

pstar = -delta / lam
assert pstar == F(5)

# The model right-hand side at the source candidate is exactly zero.
model_rhs = lam * pstar + delta
assert model_rhs == 0

# Admissible positive nonconstant weight on [0,1]: omega(t)=1+t.
def omega(t):
    return F(1) + t

assert omega(F(0)) == F(1)
assert omega(F(1)) == F(2)

# Proposition 1 says I(D p)(t)=((omega p)(t)-(omega p)(0))/omega(t).
# For the claimed constant p*=5, evaluate at t=1.
t = F(1)
weighted_increment = (omega(t) * pstar - omega(F(0)) * pstar) / omega(t)
assert weighted_increment == F(5, 2)
assert weighted_increment != 0

# If p* were the claimed equilibrium then D p*=0, hence I(D p*)=0,
# contradicting the exact weighted increment above.
print("VERIFY_OK")
print("lambda=", lam)
print("delta=", delta)
print("pstar=", pstar)
print("model_rhs=", model_rhs)
print("weighted_increment_at_t1=", weighted_increment)
