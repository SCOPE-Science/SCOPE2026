#!/usr/bin/env python3
"""Numerical corroboration of the loopless prism spectral minimax theorem."""
import math

count = 0
for n in range(3, 101):
    if n % 2 == 0:
        for q in (0.0, 0.1, 0.25, 0.4, 0.5):
            lam = [2 - 2 * math.cos(2 * math.pi * k / n) for k in range(n)]
            anti = [-1 + q * (4 - v) for v in lam]
            assert min(abs(v + 1) for v in anti) < 1e-9
            count += 1
        continue
    eps = 2 - 2 * math.cos(math.pi / n)
    q = 2 / (4 + eps)
    p = 1 - 2*q
    mu = (4 - eps)/(4 + eps)
    assert 0 < p < 1 and 0 < q < .5
    count += 1
    lam = [2 - 2 * math.cos(2 * math.pi * k / n) for k in range(n)]
    modes = [1 - q*v for v in lam[1:]] + [-1 + q * (4-v) for v in lam]
    assert abs(max(map(abs, modes)) - mu) < 1e-9
    count += 1
    for trial_q in [i/1000 for i in range(501)]:
        trial_modes = [1-trial_q*v for v in lam[1:]] + [-1+trial_q*(4-v) for v in lam]
        assert max(map(abs, trial_modes)) + 1e-11 >= mu
        count += 1
print(f"VERIFY_OK assertions={count}")
