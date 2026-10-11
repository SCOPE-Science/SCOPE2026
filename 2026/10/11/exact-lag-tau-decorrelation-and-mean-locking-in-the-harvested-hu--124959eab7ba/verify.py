from fractions import Fraction as F

r = F(2)
K = F(3)
delta = F(1, 2)
Kdelta = K * (1 - delta/r)
assert Kdelta == F(9, 4)
assert delta < r

# Pointwise logarithmic-growth identity at an arbitrary exact delayed state.
q = F(7, 5)
left = r * (1 - q/K) - delta
right = (r/K) * (Kdelta - q)
assert left == right

# Abstract stationary moment consequences of E[X_lag | X_now] = Kdelta
EX = Kdelta
EXlag = Kdelta
EXXlag = Kdelta * EX
cov = EXXlag - EX * EXlag
assert cov == 0

# Exact variance/activity conversion.
VarX = F(11, 20)
Eloggrowth2 = (r*r/(K*K)) * VarX
assert VarX == (K*K/(r*r)) * Eloggrowth2

# Harvesting raises lower pressure monotonically on the exact stationary mean.
delta2 = F(3, 4)
Kdelta2 = K * (1 - delta2/r)
assert Kdelta - Kdelta2 == (K/r) * (delta2 - delta)
assert Kdelta2 < Kdelta

print("VERIFY_OK")
