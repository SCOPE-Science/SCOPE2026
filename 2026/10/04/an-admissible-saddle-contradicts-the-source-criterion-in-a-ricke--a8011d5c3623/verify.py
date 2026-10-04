#!/usr/bin/env python3
from fractions import Fraction as F
import math

a = F(12)
b = F(8)
c = F(1)
d = F(4)
e = F(1)
f = F(8)
alpha = F(1,10)
beta = F(1)

H = d*e/(f-d)
P = ((a-b*H)*(beta+H)*(e+H)-alpha*(e+H))/(c*(beta+H))

assert H == F(1)
assert P == F(79,10)

# Source sufficient coexistence conditions.
assert alpha < a*beta
assert alpha < (a-b*H)*(beta+H)
assert max(beta,H) < a/b < beta+H

j11 = F(1) - b*H + alpha*H/(beta+H)**2 + c*H*P/(e+H)**2
j12 = -c*H/(e+H)
j21 = e*f*P/(e+H)**2
j22 = F(1)

assert j11 == F(-5)
assert j12 == F(-1,2)
assert j21 == F(79,5)
assert j22 == F(1)

T = j11+j22
D = j11*j22-j12*j21
assert T == F(-4)
assert D == F(29,10)

# Both printed Lemma-3 predicates hold.
printed_source = (D > 1 and abs(T) < D+1) or (abs(T) > D+1)
printed_source_parenthesized = D > 1 and ((abs(T) < D+1) or (abs(T) > D+1))
printed_saddle = F(0) < abs(T)+D+1 < 2*abs(T)
assert printed_source
assert printed_source_parenthesized
assert printed_saddle

root_plus = -2 + math.sqrt(11/10)
root_minus = -2 - math.sqrt(11/10)
assert abs(root_plus) < 1
assert abs(root_minus) > 1

p1 = F(1)-T+D
pm1 = F(1)+T+D
assert p1 == F(79,10)
assert pm1 == F(-1,10)

# Correct classification predicates.
correct_source = abs(D) > 1 and abs(T) < abs(D+1)
correct_saddle = abs(T) > abs(D+1)
assert not correct_source
assert correct_saddle

print("VERIFY_OK")
print("H_star", H)
print("P_star", P)
print("T", T)
print("D", D)
print("lambda_plus", repr(root_plus))
print("lambda_minus", repr(root_minus))
print("p1", p1)
print("pm1", pm1)
