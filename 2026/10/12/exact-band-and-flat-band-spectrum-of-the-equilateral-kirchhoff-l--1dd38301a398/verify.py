#!/usr/bin/env python3
import math

# Nonresonant algebra: sin(k) tan(k/2) = 1-cos(k), and the
# resulting discriminant is F(k)=2 cos(k)-1.
for k in (0.37, 0.91, 1.73, 2.41, 4.12, 5.53):
    if abs(math.sin(k)) < 1e-12:
        continue
    lhs = math.sin(k) * math.tan(k/2.0)
    rhs = 1.0 - math.cos(k)
    assert abs(lhs-rhs) < 2e-12
    F1 = math.cos(k) - math.sin(k) * math.tan(k/2.0)
    F2 = 2.0*math.cos(k) - 1.0
    assert abs(F1-F2) < 2e-12
    assert (abs(F2) <= 1.0 + 1e-12) == (math.cos(k) >= -1e-12)

# Resonant coefficient balance at k=n*pi:
# a_j - s*a_{j-1} + (1-s)*b_j = 0, s=(-1)^n.
def balance(a_j, a_prev, b_j, parity):
    s = 1 if parity == 0 else -1
    return a_j - s*a_prev + (1-s)*b_j

# Even n: a=0 and one arbitrary loop amplitude.
assert balance(0.0, 0.0, 1.0, 0) == 0.0

# Odd n: one backbone edge with amplitude 1 and endpoint-loop amplitudes -1/2.
# Vertex 0: a_0=1, a_-1=0, b_0=-1/2.
assert balance(1.0, 0.0, -0.5, 1) == 0.0
# Vertex 1: a_1=0, a_0=1, b_1=-1/2.
assert balance(0.0, 1.0, -0.5, 1) == 0.0
# All other vertices vanish.
assert balance(0.0, 0.0, 0.0, 1) == 0.0

print('VERIFY_OK discriminant=2cos(k)-1 even_loop=ok odd_three_edge=ok')
