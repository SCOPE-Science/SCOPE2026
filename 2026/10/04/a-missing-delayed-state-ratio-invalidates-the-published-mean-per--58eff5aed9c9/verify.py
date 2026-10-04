from fractions import Fraction as F

A = F(100)
lam = phi = xi = beta = kappa = F(1)
s1sq = s2sq = s3sq = F(1)
exp_delay = F(1, 2)

L1 = lam + s1sq / 2
L2 = lam + phi + s2sq / 2
L3 = lam + xi + s3sq / 2 + 1

a = A * beta * exp_delay / (L1 * L1 * L2)
b = A * beta * exp_delay / (L1 * L2 * L2)
Rtilde = A * beta * exp_delay / (L1 * L2 * L3)

assert a == F(80, 9)
assert b == F(16, 3)
assert Rtilde == F(80, 21) and Rtilde > 1

S = F(1000)
I = F(1, 100)
R = F(1, 101)
Sdel = F(1, 1000)
Idel = F(1, 100)

rho = (Sdel / S) * ((1 + kappa * I) / (1 + kappa * Idel))
assert rho == F(1, 1_000_000)

# Generator printed before the contested bounding step.
LU = (
    a * (-A / S + lam + beta * I / (1 + kappa * I) - xi * R / S + s1sq / 2)
    + b * (-beta * exp_delay * Sdel * Idel / (I * (1 + kappa * Idel)) + (lam + phi) + s2sq / 2)
    + (-phi * I / R + (lam + xi) + s3sq / 2)
)
assert LU == F(2486393, 90900)

# The source's bracket immediately before AM-GM is a genuine upper bound
# for this witness; hence the counterexample isolates the state-independent
# AM-GM replacement rather than relying on an earlier inequality.
pre_amgm = (
    -a * A / S
    - b * beta * exp_delay * Sdel / (1 + kappa * Idel)
    - (1 + kappa * I)
    + a * L1 + b * L2 + L3 + (a * beta + kappa) * I
)
assert LU <= pre_amgm

# The paper replaces the product of the three AM-GM factors by the
# state-independent value a*b*A*beta*exp_delay = (40/3)^3.
assert a * b * A * beta * exp_delay == F(64000, 27)
claimed_post_amgm = -3 * F(40, 3) + a * L1 + b * L2 + L3 + (a * beta + kappa) * I
assert claimed_post_amgm == F(-8761, 900)
assert LU > claimed_post_amgm

print('VERIFY_OK')
