#!/usr/bin/env python3
"""Exact rational admissibility checks for one explicit delayed quasispecies model.

The global delay comparison theorem is proved mathematically in RESULT.md.
"""
from fractions import Fraction as F

N = 3
q = F(2, 5)
m = F(9, 10)
M = F(7, 5)
f_base = (F(1), F(6, 5), F(13, 10))
f_sine = F(1, 10)
Q = (
    (F(2, 5), F(3, 5), F(0)),
    (F(0), F(1, 2), F(1, 2)),
    (F(0), F(0), F(1)),
)
delays = (F(100), F(100) + F(1, 25), F(100) + F(1, 10))

assert m > 0 and M > 0 and F(0) < q < F(1)
assert all((v - f_sine >= m) and (v + f_sine <= M) for v in f_base)
assert all(f_base[j] >= f_base[0] for j in range(N))
assert all(sum(row, F(0)) == 1 and all(v >= 0 for v in row) for row in Q)
assert all(Q[j][0] == 0 for j in range(1, N))
assert Q[0][0] <= q
assert delays[0] > 0 and len(set(delays)) == N
lo = min(delays)
hi = max(delays)
span = hi - lo
assert lo == F(100) and hi == F(1001, 10) and span == F(1, 10)
exponent = N * M * span
assert exponent == F(21, 50)
assert 1 - exponent == F(29, 50) > q
# The inequality exp(-u) >= 1-u (valid for all real u)
# proves exp(-exponent) > q without approximate transcendental arithmetic.
# Root uniqueness: g(0)>0 follows; derivative g'=-m*q*b*exp(b*z)-1<0.
print('VERIFY_OK')
