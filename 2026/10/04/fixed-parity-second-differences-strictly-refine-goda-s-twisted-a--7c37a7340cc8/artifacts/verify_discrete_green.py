#!/usr/bin/env python3
import math

L = 7.25
N = 160

# Exact Green identity regression for a quadratic-plus-linear sequence.
b = [(L/math.pi)*k*k + 3.0*k - 2.0 for k in range(N+1)]
q = [0.0]*(N+1)
for k in range(1, N):
    q[k] = (math.pi/2.0)*(b[k-1] + b[k+1] - 2.0*b[k])

for k in range(2, N):
    reconstructed = b[0] + k*(b[1]-b[0])
    reconstructed += (2.0/math.pi)*sum((k-j)*q[j] for j in range(1, k))
    assert abs(reconstructed-b[k]) < 1e-9
assert max(abs(q[k]-L) for k in range(1,N)) < 1e-10

# Sequence-level converse obstruction.
bc = [(L/math.pi)*k*k + ((-1.0)**k)*(k**1.5) for k in range(N+2)]
target = L/(4.0*math.pi)
ratio = bc[N]/((2*(N+1))**2)
assert abs(ratio-target) < 0.03

tail = []
for k in range(2,N):
    qk = (math.pi/2.0)*(bc[k-2]+bc[k]-2.0*bc[k-1])
    tail.append(abs(qk))
assert max(tail[-10:]) > 1000.0

print(
    "VERIFY_OK "
    f"green_identity_N={N} "
    f"constant_second_difference={L:.2f} "
    f"converse_tail_max={max(tail[-10:]):.6f}"
)
