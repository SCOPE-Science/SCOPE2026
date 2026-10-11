#!/usr/bin/env python3
import math

worst = 1.0
for m in range(4, 201):
    N = 2*m + 1
    alpha = math.pi / N
    A = math.cos(alpha/2) / (math.cos(alpha) * math.cos(3*alpha/2))
    B = ((-1)**m) * 2*math.sin(alpha) / math.cos(3*alpha/2)

    vals = []
    for j in range(N):
        v = 1 + A*math.cos(2*math.pi*j/N) + B*math.cos(2*math.pi*m*j/N)
        vals.append(v)
    worst = min(worst, min(vals))

    # The two contact indices are m and m-1 (and their symmetric partners).
    assert abs(vals[m]) < 2e-11
    assert abs(vals[m-1]) < 2e-11
    assert min(vals) > -2e-11

    # Recover A from the two contact equations by eliminating B.
    u = math.sin(alpha/2)
    v = math.sin(3*alpha/2)
    A2 = (u+v) / (math.cos(alpha)*v + math.cos(3*alpha)*u)
    assert abs(A-A2) < 2e-12

print(f"VERIFY_OK m_range=4..200 worst_sample={worst:.3e}")
