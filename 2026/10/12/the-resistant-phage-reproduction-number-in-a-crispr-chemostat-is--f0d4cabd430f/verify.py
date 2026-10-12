#!/usr/bin/env python3
from fractions import Fraction as F

D = F(1)
delta = F(1)
b = F(10)
k = F(1, 100)
kappa = F(1, 2)
mu = F(1, 2)
m = F(4)
a = F(1)
R0 = F(11)
epsilon = F(1, 2)

assert all(x > 0 for x in [D, delta, b, k, kappa, mu, m, a, R0, epsilon])
assert 0 < kappa <= 1
assert 0 < mu < 1
assert 0 < epsilon < 1

lambda1 = D*a/(m-D)
lambda2 = D*a/(mu*m-D)
M2 = R0-lambda2

assert lambda1 == F(1,3)
assert lambda2 == 1
assert M2 == 10

def f(R):
    return m*R/(a+R)

assert mu*m > D
assert mu*f(R0) == F(11,6) > D

printed_sq = b*delta*kappa*M2 / ((D+delta)*(D+k*M2))
correct_sq = b*delta*kappa*k*M2 / ((D+delta)*(D+k*M2))

assert printed_sq == F(250,11)
assert printed_sq > 1
assert correct_sq == F(5,22)
assert correct_sq < 1

# Direct resistant-phage invasion block.
j11 = -(D+delta)
j12 = kappa*k*M2
j21 = b*delta
j22 = -(D+k*M2)
trace = j11+j22
det = j11*j22-j12*j21

assert j11 == -2
assert j12 == F(1,20)
assert j21 == 10
assert j22 == F(-11,10)
assert trace == F(-31,10) < 0
assert det == F(17,10) > 0

# The source's downstream G(lambda2) identity.
A2 = b*delta*kappa/(D+delta)-1
assert A2 == F(3,2)
G = -D + k*A2*M2
rhs_correct = (D+k*M2)*(correct_sq-1)
rhs_printed = (D+k*M2)*(printed_sq-1)

assert G == F(-17,20)
assert rhs_correct == G
assert rhs_printed == F(239,10)
assert rhs_printed != G

# Positive resistant-phage equilibrium contradiction.
M3_forced = D/(k*A2)
assert M3_forced == F(200,3)
# Positivity requires mu*f(R3)>D, so R3>lambda2=1.
# Then D/(mu*f(R3))<1 and R0-R3 < R0-lambda2 = 10.
upper_bound_M3 = R0-lambda2
assert upper_bound_M3 == 10
assert M3_forced > upper_bound_M3

print("VERIFY_OK")
print("lambda2", lambda2)
print("M2", M2)
print("printed_sq", printed_sq)
print("correct_sq", correct_sq)
print("trace", trace)
print("det", det)
print("G", G)
print("rhs_printed", rhs_printed)
print("M3_forced", M3_forced)
print("M3_upper_bound", upper_bound_M3)
