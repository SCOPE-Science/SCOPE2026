"""Finite diagnostics for a regularly varying weighted-shift weak endpoint theorem.

Run: python3 numeric_checker.py
No network or third-party packages are needed. Finite tests are not proofs.
"""
import itertools
import math

checks = 0
for p, alpha in ((1, 0.4), (2, 0.2), (4, 0.15)):
    beta = p * alpha
    assert 0 < beta < 1
    for n in (8, 16, 32, 64):
        for j in range(1, n + 9):
            for m in (1, max(1, n // 4), max(1, n // 2), n):
                m = min(m, n)
                candidates = [tuple(range(m)), tuple(range(n-m, n))]
                for E in candidates:
                    actual = sum((j / (j-k)) ** beta for k in E if k < j)
                    bound = n**beta * m**(1-beta) / (1-beta)
                    assert actual <= bound * (1 + 2e-13)
                    checks += 1
    for gamma in (-1, 0, 1):
        def slow(j):
            return math.log(math.e + j)**gamma
        for j in (16, 32, 64, 128, 256):
            vals = [((j / s)**alpha * slow(j)/slow(s))*(s/j)**alpha
                    for s in range(1, j+1)]
            obs = max(vals)
            assert math.isfinite(obs)
            if gamma <= 0:
                assert abs(obs - 1) < 1e-11
            else:
                assert obs > 1
            checks += 1
print(f"PASS: {checks} finite diagnostic inequalities/examples; no infinite proof claimed")
