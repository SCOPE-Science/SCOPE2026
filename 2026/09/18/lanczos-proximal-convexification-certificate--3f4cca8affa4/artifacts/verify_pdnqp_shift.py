from fractions import Fraction as F


delta = F(1, 100)
m = 4
positive = [delta * F(j, m + 1) for j in range(1, m + 1)]
theta = min(positive)
beta = F(1)
shift = -theta + delta * beta
lam_min = F(-1)
shifted = lam_min + shift

assert theta == F(1, 500)
assert shift == F(1, 125)
assert shifted == F(-124, 125)

# The determinant below is the Vandermonde determinant for the distinct
# positive eigenvalues; multiplying rows by nonzero start coordinates
# preserves nonvanishing.
vandermonde = F(1)
for i in range(m):
    for j in range(i + 1, m):
        vandermonde *= positive[j] - positive[i]
assert vandermonde != 0

print("delta =", delta)
print("m =", m)
print("positive eigenvalues =", positive)
print("smallest Ritz value theta =", theta)
print("gamma^{-1} =", shift)
print("lambda_min(Q + gamma^{-1} I) =", shifted)
print("positive-block Vandermonde determinant (up to nonzero row scaling) =", vandermonde)

# Sharp norm-only threshold witnesses.
for d in [F(1, 2), F(1), F(3, 2), F(2)]:
    if d <= 1:
        witness_theta = F(0)
    else:
        witness_theta = F(1)
    witness_shift = -witness_theta + d
    witness_shifted = F(-1) + witness_shift
    assert witness_shift > 0
    assert witness_shifted <= 0
    print("delta=" + str(d), "shift =", witness_shift, "shifted minimum =", witness_shifted)

d = F(201, 100)
witness_theta = F(1)
witness_shift = -witness_theta + d
witness_shifted = F(-1) + witness_shift
assert witness_shifted > 0
print("delta=" + str(d), "shift =", witness_shift, "shifted minimum =", witness_shifted)

# Certified Gershgorin repair for the explicit diagonal example.
eta = F(1, 1000)
gershgorin_lower = lam_min
cert_shift = max(F(0), -gershgorin_lower) + eta * beta
certified_minimum_lower_bound = lam_min + cert_shift
assert certified_minimum_lower_bound == eta
print("Gershgorin safe shift =", cert_shift)
print("certified shifted minimum lower bound =", certified_minimum_lower_bound)
